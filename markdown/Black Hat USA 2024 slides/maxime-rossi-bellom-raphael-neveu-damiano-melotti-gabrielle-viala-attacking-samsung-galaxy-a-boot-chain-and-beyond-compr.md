---
title: "Attacking Samsung Galaxy A Boot Chain, and Beyond"
speakers: ["Maxime Rossi Bellom", "Raphael Neveu", "Damiano Melotti", "Gabrielle Viala"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Maxime Rossi Bellom & Raphael Neveu & Damiano Melotti & Gabrielle Viala_Attacking Samsung Galaxy A Boot Chain, and Beyond_Compressed.pdf"
pages: 87
sha256: "30a728dd30270db7363e6ee08d45174e10e08c98044c94e3638937000596b0a5"
text_chars: 25684
ocr_pages: 24
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:00:10Z"
---
# Attacking Samsung Galaxy A Boot Chain, and Beyond

**Speakers:** Maxime Rossi Bellom, Raphael Neveu, Damiano Melotti, Gabrielle Viala  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Maxime Rossi Bellom & Raphael Neveu & Damiano Melotti & Gabrielle Viala_Attacking Samsung Galaxy A Boot Chain, and Beyond_Compressed.pdf` (87 pages)

## Slide 1

# **Attacking Samsung Galaxy A* Boot Chain, and Beyond**

Maxime Rossi Bellom Damiano Melotti Raphaël Neveu Gabrielle Viala

## Slide 2

#### **Who we are**

- Maxime Rossi Bellom <u>@max_r_b</u>

- Security researcher and R&D leader @ Quarkslab

- ■ Working on mobile and embedded software security

- Damiano Melotti <u>@DamianoMelotti</u>

- ■ Ex security researcher @ Quarkslab

- Interested in low-level mobile security and fuzzing

- Gabrielle Viala <u>@pwissenlit</u>

- ■ Security researcher and R&D leader @ Quarkslab

- ■ Playing with low-level stuff

- Raphaël Neveu

- Security researcher @ Quarkslab

- Working on low-level mobile security

2

## Slide 3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Attacking SP derivation
Dissecting the Modern
e Need to target the TEE
Android Data Encryption + Two ateratves
Keymaster TA (accessing the first AES key)
Gatekeeper TA (validating credentials and minting auth tokens)
Scheme
{ /data/eyotem_de/<vid>/epblob/<handie),spblob
‘Gf authentication i» successful)
Maxime Rossi Bellom 15} key —>y/AS decrypt
Damiano Melotti
decrypt K-key—Snasi2e
Quarkslab Framers
| Passworo
Bruteforce of the password
pwd = generate new password
token = scrypt(pwd, R, N, P, Salt)
Application_id = token || Prehashed value
Key = SHA512("application_id" || application_id) Quarkslab
AES_Decrypt(value_from_keymaster, key)
$ python3 bruteforce-tee.py
workers will cycle through the last 5 chars
Found it: 1234
the plaintext is '1234'
Done in 18.031058311462402s
Throughput: 1478.448992816657 tries/s
```

## Slide 4

#### **Our Device**

- Samsung Galaxy A225F

   - Cheap (~300€)

   - Mediatek SoC MT6769V

   - Main OS: Android

   - Mix of Mediatek and Samsung code

   - Trustzone OS: TEEGRIS

   - Secure Boot Bypass using MTKClient<sup>1</sup>

      - → making debugging easier

[1]: https://github.com/bkerler/mtkclient

4

## Slide 5

#### **Mediatek Secure Boot Process**

5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Mediatek Secure Boot Process
EL3 ELI ELO
ARM Trusted
Firmware
Boot ROM Preloader TEEGRIS
Secure World
Normal World
LK Android
```

## Slide 6

#### **Mediatek Secure Boot Process**

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Mediatek Secure Boot Process
ELS ELI ELO
ARM Trusted
Firmware
Boot ROM Preloader TEEGRIS
Secure World
Normal World
Android
Our
target
```

## Slide 7

#### **Little Kernel (LK)**

- Open-source OS<sup>2</sup>

- Common as bootloader in the Android world

- Allows to boot Android or other modes (Recovery)

- Implements **A** ndroid **V** erified **B** oot v2

   - Verification of Android images

   - Involving boot and vbmeta partitions

   - Anti-rollback

[2]: https://github.com/littlekernel/lk

7

## Slide 8

#### **Little Kernel by Samsung**

- Samsung modified LK to include:

   - The Odin recovery protocol

   - Knox Security Bit

   - ● Etc…

   - And a JPEG parser/renderer

- This version is closed source

8

## Slide 9

#### **Why Targeting the JPEG Loader/Parser**

- JPEGs are placed in a TAR archive in the _up_param_ partition

- ■ The archive is signed… but the signature is not checked at boot Anyone able to write the flash can modify these JPEGs

- ■ Parsing JPEG is known to be hard (cf. LogoFail<sup>3</sup> )

[3]: https://www.binarly.io/blog/inside-the-logofail-poc-from-integer-overflow-to-arbitrary-code-execution

9

## Slide 10

#### **Why Targeting the JPEG Loader/Parser**

- JPEGs are placed in a TAR archive in the _up_param_ partition

- ■ The archive is signed… but the signature is not checked at boot Anyone able to write the flash can modify these JPEGs

- ■ Parsing JPEG is known to be hard (cf. LogoFail<sup>3</sup> )

How are these JPEGs loaded by LK?

[3]: https://www.binarly.io/blog/inside-the-logofail-poc-from-integer-overflow-to-arbitrary-code-execution

10

## Slide 11

#### **Heap Overflow in JPEG Loading**

_JPEG_BUF = alloc(0x100000); if (_JPEG_BUF == 0) { log("%s: img buf alloc fail\n","drawimg"); uVar2 = 0xffffffff; } else { memset(_JPEG_BUF,0,0x100000); iVar1 = read_jpeg_file(file_name,_JPEG_BUF,0); if (iVar1 == 0) {

log("%s: read %s from up_param as 0, size\n","drawimg",file_name); uVar2 = 0xffffffff; } // ...

pimage(*(undefined4 *)(&DAT_4c5107fc + param_1 * 0x3c), *(undefined4 *)(&DAT_4c510800 + param_1 * 0x3c), 0x2d0,0x640,1,_JPEG_BUF,iVar1);

11

## Slide 12

#### **Heap Overflow in JPEG Loading**

Heap allocation of constant size for the buffer

_JPEG_BUF = alloc(0x100000); if (_JPEG_BUF == 0) { log("%s: img buf alloc fail\n","drawimg"); uVar2 = 0xffffffff; }

else {

memset(_JPEG_BUF,0,0x100000); iVar1 = read_jpeg_file(file_name,_JPEG_BUF,0); if (iVar1 == 0) {

log("%s: read %s from up_param as 0, size\n","drawimg",file_name); uVar2 = 0xffffffff; } // ...

pimage(*(undefined4 *)(&DAT_4c5107fc + param_1 * 0x3c), *(undefined4 *)(&DAT_4c510800 + param_1 * 0x3c), 0x2d0,0x640,1,_JPEG_BUF,iVar1);

12

## Slide 13

#### **Heap Overflow in JPEG Loading**

_JPEG_BUF = alloc(0x100000); if (_JPEG_BUF == 0) { log("%s: img buf alloc fail\n","drawimg"); uVar2 = 0xffffffff; } else {

memset(_JPEG_BUF,0,0x100000);

Read the JPEG in the buffer

iVar1 = read_jpeg_file(file_name,_JPEG_BUF,0); if (iVar1 == 0) {

log("%s: read %s from up_param as 0, size\n","drawimg",file_name); uVar2 = 0xffffffff; }

// ...

pimage(*(undefined4 *)(&DAT_4c5107fc + param_1 * 0x3c), *(undefined4 *)(&DAT_4c510800 + param_1 * 0x3c), 0x2d0,0x640,1,_JPEG_BUF,iVar1);

13

## Slide 14

#### **Heap Overflow in JPEG Loading**

_JPEG_BUF = alloc(0x100000); if (_JPEG_BUF == 0) { log("%s: img buf alloc fail\n","drawimg"); uVar2 = 0xffffffff; } else { memset(_JPEG_BUF,0,0x100000); iVar1 = read_jpeg_file(file_name,_JPEG_BUF,0); if (iVar1 == 0) { log("%s: read %s from up_param as 0, size\n","drawimg",file_name); uVar2 = 0xffffffff; } // ...

Parse and render the JPEG

pimage(*(undefined4 *)(&DAT_4c5107fc + param_1 * 0x3c), *(undefined4 *)(&DAT_4c510800 + param_1 * 0x3c), 0x2d0,0x640,1,_JPEG_BUF,iVar1);

14

## Slide 15

#### **Heap Overflow in JPEG Loading**

_JPEG_BUF = alloc(0x100000); if (_JPEG_BUF == 0) { log("%s: img buf alloc fail\n","drawimg"); uVar2 = 0xffffffff; } else { memset(_JPEG_BUF,0,0x100000); iVar1 = read_jpeg_file(file_name,_JPEG_BUF,0); if (iVar1 == 0) {

log("%s: read %s from up_param as 0, size\n","drawimg",file_name); uVar2 = 0xffffffff; } // ...

pimage(*(undefined4 *)(&DAT_4c5107fc + param_1 * 0x3c), *(undefined4 *)(&DAT_4c510800 + param_1 * 0x3c), 0x2d0,0x640,1,_JPEG_BUF,iVar1);

15

## Slide 16

#### **Heap Overflow in JPEG Loading**

■ read_jpeg_file takes a size as 3<sup>rd</sup> argument ■ It triggers an error if the file does not fit the size provided

file_size = string_to_int(tar_header_file.size,0,8); if (size != 0 && size < file_size) {

file_size = print("read fail! (%d < %d)\n",size,file_size,size); return file_size;

} iVar1 = read(data_addr,index + 1,file_size,outbuf);

16

## Slide 17

#### **Heap Overflow in JPEG Loading**

■ read_jpeg_file takes a size as 3<sup>rd</sup> argument

■ It triggers an error if the file does not fit the size provided Unless the size provided is 0…

file_size = string_to_int(tar_header_file.size,0,8); if (size != 0 && size < file_size) {

file_size = print("read fail! (%d < %d)\n",size,file_size,size); return file_size;

}

iVar1 = read(data_addr,index + 1,file_size,outbuf);

17

## Slide 18

### _Is it exploitable?_

18

## Slide 19

#### **Exploiting a Heap Overflow in Little Kernel**

- The heap algorithm is _miniheap_

   - It relies on a doubly linked list

- Chunks are in a unique memory pool

   - An overflow may overwrite the metadata of next chunk

struct free_chunk_head { struct free_chunk_head *prev; struct free_chunk_head *next; size_t len; }

19

## Slide 20

#### **From Heap Overflow to Arbitrary Write**

- After allocation, a chunk is removed from the free list

- next and prev <u>are dereferenced to change the corresponding nodes</u> ⇒ Controlling a free chunk leads to a write-what-where

node->next->prev = node->prev; node->prev->next = node->next; node->prev = node->next = 0;

20

## Slide 21

#### **From Heap Overflow to Arbitrary Write**

- After allocation, a chunk is removed from the free list

- next and prev <u>are dereferenced to change the corresponding nodes</u> ⇒ Controlling a free chunk leads to a write-what-where Both values must writable addresses

node->next->prev = node->prev; node->prev->next = node->next; node->prev = node->next = 0;

21

## Slide 22

#### **From Arbitrary Write to Code Execution**

##### Important details about LK

No ASLR No canaries

No bounds checks in the heap algorithm Heap is executable!

22

## Slide 23

#### **From Arbitrary Write to Code Execution**

##### Important details about LK

No ASLR

No canaries

No bounds checks in the heap algorithm Heap is executable!

Exploit strategy becomes simple:

1. Overwrite a pointer that the code will jump to the return address in the stack

2. Make it point to a shellcode in our JPEG buffer

23

## Slide 24

#### **Exploiting a Heap Overflow in Little Kernel**

24

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploiting a Heap Overflow in Little Kernel
Stack
Step |
JPEG Buffer
Allocation
Freeliot
head mo
QZ Anz Qajiz
Free JPEG
Chunk Buffer Free Free
Chunk Chunk 24
```

## Slide 25

#### **Exploiting a Heap Overflow in Little Kernel**

25

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploiting a Heap Overflow in Little Kernel
Stack
Step 2
Reading The Jpeg
Freeliot
head oo \
At) C
aie Z aed
Free JPEG
Chunk Buffer Free Free
Chunk Chunk 25
```

## Slide 26

#### **Exploiting a Heap Overflow in Little Kernel**

26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploiting a Heap Overflow in Little Kernel
Stack
Step 2
Reading The Jpeg
Freeliot
head mo
Free JPEG
Chunk Buffer Free Free
Chunk 26
Chunk
```

## Slide 27

#### **Exploiting a Heap Overflow in Little Kernel**

27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploiting a Heap Overflow in Little Kernel
Stack
Step 2
Reading The Jpeg
Freeliot
head oo
QZ OZ Qajiz
Free JPEG
Chunk Buffer Free Free
Chunk 27
Chunk
```

## Slide 28

#### **Exploiting a Heap Overflow in Little Kernel**

28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploiting a Heap Overflow in Little Kernel
Stack
Step 2
Reading The Jpeg
And overwriting next chunk
Freelist
head \
XQ po
aie oie) ale
Free JPEG
Chere Buffer Free Free
Chunk 28
Chunk
```

## Slide 29

#### **Exploiting a Heap Overflow in Little Kernel**

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploiting a Heap Overflow in Little Kernel
Stack
Step 2%
Making a fake Chunk Return
Address
point to the stack
Freelist
ne Sia 7 9// Ss) S48
Ay? 72 Shelicode Ue! Vg
Free JPEG
Chunk Buf fer Fake Free Free
Chunk Chunk 29
```

## Slide 30

#### **Exploiting a Heap Overflow in Little Kernel**

30

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploiting a Heap Overflow in Little Kernel
Stack
Step 3
Af id oe next Shellcode
— address
Freelist
head _*
ne Y~byYYyyy ee WY), Sle
ie, 73//)| Shellcode CVs
[ow 4 YY) Wp NON
a JPEG
F
ins Buffer Fake Free Free
Chunk Chunk 30
Chunk
```

## Slide 31

#### **To sum-up**

- SVE-2023-2079/CVE-2024-20832 Leads to code execution Persistent (it survives reboots and factory reset) Gives full control over Normal World EL1/0 Impacts Samsung devices based on Mediatek SoCs

- Including those for which MTKClient does not work

- Requires to flash the _up_param_ partition

31

## Slide 32

_How to write our JPEGs in the up_param partition?_

32

## Slide 33

#### **Odin: Samsung's recovery protocol**

- Odin is implemented in LK

- It is available through the _Download Mode_

   - It allows to flash partitions over USB

- The Odin official client is closed source

- ■ There is an open-source client: Heimdall<sup>4</sup>

[4]: https://github.com/Benjamin-Dobell/Heimdall

33

## Slide 34

#### **Odin: Samsung's recovery protocol**

- Images are authenticated and contain a footer signature

- Two internal structures indicate which partitions to flash

   - The _Partition Information Table_ (PIT)

   - A global structure indicating which partitions to authenticate

34

## Slide 35

#### **Odin: Partition Information Table**

- PIT is retrieved statically from the eMMC

- It indicates where partitions are stored

   - Memory type, block count, etc

- A partition not present in PIT <u>can't be f</u> l <u>ashed</u>

- ■ PIT can be updated, but requires a signed image

--- Entry #1 --Binary Type: 0 (AP) Device Type: 2 (MMC) Identifier: 70 Attributes: Read/Write Update Attributes: 1 Block Size/Offset: 0 Block Count: 34 Partition Name: pgpt

…

35

## Slide 36

#### **Odin: Image Authentication**

- A global array indicates how an image should be authenticated

- ■ An image not present in this array will not be authenticated

   - (Except for some specific images)

- Comparing this array with PIT gives a set of images flashable without authentication

**md5hdr** , **md_udc** , **pgpt** , **sgpt** , and **vbmeta_vendor**

36

## Slide 37

#### **GPT: GUID Partition Table**

- **pgpt** points to the Primary GPT Header

- ■ **sgpt** points to the Secondary GPT Header

- ■ Similarly to the PIT, it describes the partitions

   - (Names, sizes, addresses, etc)

- Any GPT can be flashed through Odin No authentication required

Source: https://en.wikipedia.org/wiki/GUID_Partition_Table

37

## Slide 38

#### **GPT vs PIT**

- **PIT** and **GPT** are used for the same thing: to describe partitions

- ■ **PIT** is mainly used for Samsung features in LK

   - Odin, JPEGs loading, etc

- And **GPT** is used the rest of the time

We can't just rename a partition to _up_param_ to flash our JPEGs

38

## Slide 39

#### **PIT Loading**

pit_address = 0x4400; exist = get_part_table("pit"); if (exist == 0) { pit_address = get_partition_offset("pit"); } type = storage(3); iVar1 = storage_read(type,0x4000,(int)pit_address, (int)((ulonglong)pit_address >> 0x20), &ODIN_TEMP_BUF_PIT,0x4000);

39

## Slide 40

#### **PIT Loading**

##### PIT default address

pit_address = 0x4400; exist = get_part_table("pit"); if (exist == 0) { pit_address = get_partition_offset("pit"); } type = storage(3); iVar1 = storage_read(type,0x4000,(int)pit_address, (int)((ulonglong)pit_address >> 0x20), &ODIN_TEMP_BUF_PIT,0x4000);

40

## Slide 41

#### **PIT Loading**

PIT default address
pit_address = 0x4400;
exist = get_part_table("pit"); Check for pit partition
if (exist == 0) { And use it if it exists
  pit_address = get_partition_offset("pit");
}
type = storage(3);
iVar1 = storage_read(type,0x4000,(int)pit_address,
  (int)((ulonglong)pit_address >> 0x20),
                      &ODIN_TEMP_BUF_PIT,0x4000);

41

## Slide 42

#### **PIT Loading**

PIT default address pit_address = 0x4400; Uses GPT table exist = get_part_table( " pit " ); if (exist == 0) { pit_address = get_partition_offset( " pit " ); } type = storage(3); iVar1 = storage_read(type,0x4000,(int)pit_address, (int)((ulonglong)pit_address >> 0x20), &ODIN_TEMP_BUF_PIT,0x4000);

42

## Slide 43

#### **Strategy to Bypass Odin Authentication**

43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Strategy to Bypass Odin Authentication
PIT Flash Memory GPT
md5hdr eee LIL md5hde
PIT default |, LLL
vbmeta_vendor v an | Me A vometa_vendor
up_param “ woo. 7 up_param
a md5hde = yA /
“ vbmeta_vendor /* # ER
J
J
up_param a
43
```

## Slide 44

#### **Strategy to Bypass Odin Authentication**

44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Strategy to Bypass Odin Authentication
PIT Flash Memory GPT
md5hdr eee LIL md5hde
PIT default |, LLL
vbmeta_vendor v 7 M A vometa_vendor
up_param “ New aw up_param
Ds up_pacam AA
“ vbmeta_vendor /* ff
f
P
J
up_param a
44
```

## Slide 45

#### **Strategy to Bypass Odin Authentication**

45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Strategy to Bypass Odin Authentication
PIT Flash Memory GPT
md5hde Ra OLED, md5hde
PIT default
vbmeta_vendor v a WW A vometa_vendor
‘. ,
up_param New i Thy of / up_param
up_param ff
fx
rs as
[ NewPirT Fo 4
P
New PIT if
rs
up_param up_pacam = &
vbmeta_vendor
md5hdr
45
```

## Slide 46

#### **Strategy to Bypass Odin Authentication**

46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Strategy to Bypass Odin Authentication
PIT Flash Memory GPT
mdShde [one PT mdSihde
PIT default
vbmeta_vendor v a “S. pit
up_param we New up_param
up_param
| New PIT
New PIT
up_param up_param
vbmeta_vendor
mdShde
46
```

## Slide 47

#### **Strategy to Bypass Odin Authentication**

47

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Strategy to Bypass Odin Authentication
PIT Flash Memory GPT
md5hde SVU ) mdshde |
PIT default, A Yooh
vb ta_vesdor ne ef pit
up param New | up_param
up_param /
New PIT
New PIT
Up_param Up_param
vbmeta_vendor
md5hde
47
```

## Slide 48

#### **To sum up**

■ SVE-2024-0234/CVE-2024-20865 Can bypass authentication in Odin We can flash anything in the eMMC Including our _up_param_ partition Seems to impact most Samsung using Mediatek SoCs

48

## Slide 49

#### **Chaining Everything Together**

49

## Slide 50

#### **To Conclude**

- Chain based on 2 vulnerabilities

- Leads to code execution in LK Persistent (it survives reboots and factory reset) Impacts Samsung devices based on Mediatek SoCs

- Including those for which MTKClient does not work

- Can be triggered over USB thanks to Odin authentication bypass Gives full control over Normal World EL1/0 Still no access to secrets stored in Secure World

50

## Slide 51

#### **Targeting ARM Trusted Firmware**

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Targeting ARM Trusted Firmware
EL3 ELI ELO
ARM Trusted
Firmware
Boot ROM Preloader TEEGRIS
Secure World
Normal World
LK — Android
51
```

## Slide 52

#### **Targeting ARM Trusted Firmware**

52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Targeting ARM Trusted Firmware
Our next tar get
EL3 ELI ELO
: ARM Trusted
Firmware
Boot ROM Preloader TEEGRIS
Secure World
Normal World
LK Andtoid
52
```

## Slide 53

#### **Communication between NSW and SW**

53

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Communication between NSW and SW
ELO Userland ELI Kernel
Be ginOperation()
Keystore
seryice
yy yj) iy /dev/tzdev
L/BEONICE 7
i’. tziwsock
SMC.
on an, Secure ELI
Monitore
Yih
TEEGRIS
Kernel
Secure ELO
TA
MK
i
a
A) Shared
Memory
|Keymaster TA
53
```

## Slide 54

#### **Vulnerability Research on ATF**

- Motivation:

   - Highest privilege level → A bug here can be devastating

   - ● Reachable from Normal World through SMCs

- Code is simple

- Interacts a lot with HW through unknown registers

- Fuzzing not particularly interesting in this case

- ■ Our approach: focus on static analysis

54

## Slide 55

#### **Extracting ATF**

■ Inside an Android ROM Image:

● tee-verified.img: **ATF** , TEEGRIS kernel, userboot.so…

55

## Slide 56

#### **SMC Handlers**

if ((is_secure & 1) == 0) {

puVar1 = mediatek_plat_sip_handler_secure(smc_id,arg1,arg2,arg3 ,arg4,arg5,output);

return puVar1;

} [...]

if ((origin < 2) && (IN_BOOTLOADER == 0)) {

puVar1 = mediatek_plat_sip_handler_kernel(smc_id,arg1,arg2,arg3

,arg4,arg5,output);

return puVar1;

}

56

## Slide 57

#### **SMC Handlers**

if ((is_secure & 1) == 0) { puVar1 = mediatek_plat_sip_handler_secure(smc_id,arg1,arg2,arg3 ,arg4,arg5,output); return puVar1; } Arguments of SMC [...] if ((origin < 2) && (IN_BOOTLOADER == 0)) { puVar1 = mediatek_plat_sip_handler_kernel(smc_id,arg1,arg2,arg3 ,arg4,arg5,output);

return puVar1;

}

57

## Slide 58

#### **Leaking from Virtual Address Space**

uint* global_array = (uint *)0x4ce2f578; [...] if (smcid == 0x82000526) { out_value = global_array[arg1 * 4]; goto exit; } [...] output[2] = out_value; output[1] = arg1; *output = 0; return output;

58

## Slide 59

#### **Leaking from Virtual Address Space**

uint* global_array = (uint *)0x4ce2f578; [...] if (smcid == 0x82000526) { out_value = global_array [arg1 * 4]; goto exit; **Fully controlled by** } **attacker** [...] output[2] = out_value; output[1] = arg1; *output = 0; return output;

59

## Slide 60

#### **Leaking from Virtual Address Space**

uint* global_array = (uint *)0x4ce2f578; [...] if (smcid == 0x82000526) { out_value = global_array [arg1 * 4]; goto exit; **Fully controlled by** } **attacker… And never** [...] **checked** output[2] = out_value; output[1] = arg1; *output = 0; return output;

60

## Slide 61

#### **SVE-2023-2215 (CVE-2024-20820)**

- In mediatek_plat_sip_handler_kernel _,_ reachable from Linux Kernel

- ■ To exploit it, send the SMC 0x82000526 with

   - ( **arbitrary_address** - 0x4ce2f578) / 4

- Bug introduced by Samsung only in some devices (including A225F)

- ■ It leaks 4 bytes from ATF virtual address space

   - We can read all the internal data of ATF

   - But we can't leak anything from other SW components

61

## Slide 62

#### **SVE-2023-2215 (CVE-2024-20820)**

62

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SVE-2023-2215 (CVE-2024-20820)
IF WE.COULD MMAP ANY
=—=PHYSICAL ADDRESS IN ATF
y.
“THAT WOULD BE GREAT
```

## Slide 63

#### **Mapping Any Physical Address in ATF**

SMC 0x8200022A calls function spm_actions

if (smc_id == 0x8200022a) { spm_actions(arg1,arg2,arg3);

63

## Slide 64

#### **Mapping Any Physical Address in ATF**

SMC 0x8200022A calls function spm_actions

undefined * spm_actions(ulong cmdid,undefined *addr,ulong size) { switch(cmdid & 0xffffffff) { [...] case 1: if (size < 0x100001) { mmap_wrap(addr,size); [...] }

64

## Slide 65

#### **Mapping Any Physical Address in ATF**

SMC 0x8200022A calls function spm_actions

undefined * spm_actions (ulong cmdid,undefined *addr,ulong size) { switch(cmdid & 0xffffffff) { [...] **Arguments fully** case 1: **controlled** if (size < 0x100001) { mmap_wrap(addr,size); [...] }

**Arguments fully controlled**

65

## Slide 66

#### **Mapping Any Physical Address in ATF**

SMC 0x8200022A calls function spm_actions

undefined * spm_actions (ulong cmdid,undefined *addr,ulong size) { switch(cmdid & 0xffffffff) { [...] **Arguments fully** case 1: **controlled** if (size < 0x100001) { mmap_wrap (addr, size); [...] **And still no checks on** } **the address**

66

## Slide 67

#### **Mapping Any Physical Address in ATF**

SMC 0x8200022A calls function spm_actions

undefined * spm_actions(ulong cmdid ,undefined *addr, ulong size) { switch(cmdid & 0xffffffff) { [...] **Physical Address** case 1: if (size < 0x100001) { mmap_wrap (addr, size); [...] **And still no checks on** } **the address**

67

## Slide 68

#### **CVE-2024-20021**

- Also in mediatek_plat_sip_handler_kernel

- Will mmap with physical base address to the same virtual address

   - … however we can't munmap

      - So we are limited to 8 consecutive mmaps

      - Meaning we can leak up to **8MB** of data

- Introduced by Mediatek (impacts plenty of Mediatek SoCs)

- Chained to our leak, we can read everything in Secure World

   - Including TEEGRIS

68

## Slide 69

_Can we use this vulnerability to leak Keystore keys?_

69

## Slide 70

#### **Android Keystore system**

- Key storage and crypto services

- ■ Keys are stored as encrypted _key blobs_

- ■ Three protection levels: ● Software only

- ● TEE (default)

   - Hardware-backed (StrongBox)

- Raw key should never leave protected environment

70

## Slide 71

#### **Android Keystore system**

71

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Android Keystore system
, F Keymaster TA or
ormal Worl Trusted Chip
—
Be ‘o. (key blob)
Decrypt blob and
extract key material
UpdateOperation (input)
UpdateOperation (input)
‘i es Use key
FinishOperation (input)
output:
```

## Slide 72

#### **Our PoC**

1. **Import** a key into the Android Keystore

2. **Encrypt** using that key

3. **Stop the execution** after BeginOperation is called

   - To makes sure the key stays in memory

4. **Leak** the identified region of memory

5. Try all possible keys from leak to decrypt ciphertext

72

## Slide 73

#### **Demo**

73

## Slide 74

### _What’s next?_

74

## Slide 75

#### **Key Attestation**

- Proves that a key pair is stored in the secure hardware ● Trustzone or Security Chip

- Contains information about the device state

- Such as bootloader locked status and verified boot state

- ■ Used by SafetyNet<sup>5</sup> to tell if a device has been compromised

[5]: <u>https://www.sstic.org/media/SSTIC2022/SSTIC-actes/droidguard_a_deep_dive_into_safetynet/SSTIC2022-Article-droidguard_a_deep_dive_into_safetynet-thomas.pdf</u>

75

## Slide 76

#### **First Key Attestation test**

Attestation generated with a demo app<sup>6</sup> Our exploit seems not detected!

[6]: https://github.com/vvb2060/KeyAttestation

76

## Slide 77

#### **What about SafetyNet?**

SafetyNet detects the exploit ■ Possibly through heuristics to detect Magisk

[6]: https://github.com/RikkaW/YASNAC

77

## Slide 78

#### **Certificate Chain**

78

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Certificate Chain
Application Key Cert
Android Keystore Key Cert
[om
GAK Cect
jew
ROOT Certificate
Self
Signed
78
```

## Slide 79

#### **Certificate Chain**

79

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Certificate Chain
Stored inthe |
Keystore
Stored in Google's __|
servers
Application Key Cert
| Sign
Android Keystore Key Cert
Sign
GAK Cert
ROOT Certificate S Self
Signed
79
```

## Slide 80

#### **Certificate Chain**

80

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Certificate Chain
Stored in the
Keystore
Stored in Google's __|
servers
Application Key Cert
| Sign
Android Keystore Key Cert
| im
GAK Cert
] Sign
ROOT Certificate
Generated at
first boot
Same for all
Le Samsung AZZ
>
Self
Signed
80
```

## Slide 81

#### **Certificate Chain**

81

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Certificate Chain
Storedinthe |
Keystore
Stored in Google's __|
servers
Application Key Cert
| Sign
Android Keystore Key Cert
Sign
GAK Cert
| ese
ROOT Certificate
Root of trust
verifiedBootKey:
07EFE057CEBF085AAA79D1FB2090CCCB59
9D6A51B027FEABF1 23FD78E84D3D63
deviceLocked: true
verifiedBootState: Verified
verifiedBootHash:
E07ADF185A36CE4A2FED204CF9C3103D54
1B7A90305F89785154A460688553E0
OS version
130000
OS patch level
202306
Attestation application ID
Package info 1/1:
io.github.vvb2060.keyattestation (version
code 165)
Certificate sha256 digest 1/1:
D8B53693490D6E7467F985165001A547F72
2E75735B34E6AA13BF949F5216F1E
81
```

## Slide 82

#### **Strategy to leak GAK**

■ Stored as EKEY in Android Filesystem ● /mnt/vendor/efs/DAK/GAK_EC.private

82

## Slide 83

#### **Strategy to leak GAK**

- Stored as EKEY in Android Filesystem

   - /mnt/vendor/efs/DAK/GAK_EC.private

1. **Forge a valid** Begin request with GAK keyblob

2. **Stop the execution** after BeginOperation is called

3. **Leak** memory (as in previous PoC)

4. Try to every possible private keys in the dump

   - By generating the public key out of it

83

## Slide 84

#### **Strategy to leak GAK**

- Stored as EKEY in Android Filesystem

   - /mnt/vendor/efs/DAK/GAK_EC.private

1. **Forge a valid** Begin request with GAK keyblob

2. **Stop the execution** after BeginOperation is called

3. **Leak** memory (as in previous PoC)

4. Try to every possible private keys in the dump

   - By generating the public key out of it

      - → Still WIP

84

## Slide 85

#### **Strategy to leak GAK**

- Stored as EKEY in Android Filesystem ● /mnt/vendor/efs/DAK/GAK_EC.private

- 1. **Forge a valid** Begin request with GAK keyblob

- 2. **Stop the execution** after BeginOperation is called

3. **Leak** memory (as in previous PoC) 4. Try to every possible private keys in the dump

   - By generating the public key out of it

→ Still WIP

85

## Slide 86

#### **Conclusion**

- We presented 4 vulnerabilities leading to

   - Authentication bypass in Odin

   - Code execution with persistence in LK

- Leak of SW memory, including Keystore keys ■ Still unclear if we can leak Attestation Keys

- ■ Impact low/middle end Samsung devices

   - Vulnerabilities are simple, and yet super impactful

   - No mitigations in LK nor ATF

- All the vulnerabilities are now fixed

86

## Slide 87

## **Thank you!**

contact@quarkslab.com

@max_r_b
@DamianoMelotti
@pwissenlit
