---
title: "0-click RCE on Tesla Model 3 through TPMS Sensors"
speakers: ["David Berard", "Thomas Imbert"]
conference: "Hexacon"
conference_full: "Hexacon 2024"
edition: ""
year: 2024
source_pdf: "Hexacon 2024 Slides/David Berard & Thomas Imbert_0-click RCE on Tesla Model 3 through TPMS Sensors.pdf"
pages: 44
sha256: "fd97ff428afb7fb10d81377daeccc27a391c0a47952fc5eabb4a61f8785c5a37"
text_chars: 13411
ocr_pages: 8
has_ocr: true
redacted_secrets: 0
ocr_confidence: 89.2
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:49:40Z"
---
# 0-click RCE on Tesla Model 3 through TPMS Sensors

**Speakers:** David Berard, Thomas Imbert  
**Conference:** Hexacon 2024  
**Source:** `Hexacon 2024 Slides/David Berard & Thomas Imbert_0-click RCE on Tesla Model 3 through TPMS Sensors.pdf` (44 pages)


## Slide 1

**0-click RCE on Tesla Model 3 through TPMS Sensors**

**Hexacon 2024**

**October 4th 2024**

## Slide 2

# **<u>Who are we</u>**

#### **Synack�v**

#### **David Berard**

@_p0ly_

**Thomas Imbert** @masthoon

- Offensive security

■ 170 Experts

■ Pentest, Reverse Engineering, Development, Incident Response

**Reverse Engineering team**

- 50 reversers

#### **Vincent Dehors**

@vdehors

- Low level research, reverse engineering,

- vulnerability research, exploit development, etc.

**2**

## Slide 3

# **<u>Synacktiv vs Tesla: Previous work</u>**

**Pwn2Own Pwn2Own Vancouver 2022 Vancouver 2023**

WiFi exploit preBluetooth RCE + auth Zero click + Kernel LPE + network Security sandbox escape Gateway RCE

**Pwn2Own Pwn2Own Tokyo 2024 Vancouver 2024**

Cellular Network RCE + Tesla's VCSEC Infotainment RCE through RCE + network TPMS sandbox escape

**3**

## Slide 4

# **Architecture**

**4**

## Slide 5

# **<u>Architecture</u>**

VCSEC ECU

## **Features**

■ Endpoint for the Tesla Mobile App ■ Open the car, start driving, basic remote control

■ NFC

■ Open the car, start driving

- TPMS

■ Measure �res pressure and temperature

## **Connectivity**

■ Bluetooth Low Energy

■ Tesla App + TPMS sensors

■ Ultra Wide Band

   - Tesla App

- Vehicule CAN

■ UDS for maintenance /

provisionning

■ Standard CAN signals

**5**

## Slide 6

# **<u>Architecture</u>**

VCSEC ECU

## **Hardware**

- Now embedded in VCLe� ECU, used to be

- a standalone ECU

- S�ll a dedicated SoC on this ECU

- PowerPC SoC: SPC56 from ST

   - run in VLE mode

- No BLE connec�vity on the PCB

   - Mul�ple BLE Endpoints connected with

   - UART to CAN transceivers

**6**

## Slide 7

# **<u>Architecture</u>**

VCSEC ECU

###### Firmwares

- VCSEC is updated by the Security Gateway that fetches firmware from the infotainment

- Present in the roo�s filesystem of the infotainment for many board revisions

- Firmwares are not encrypted

##### **Software**

##### **Reverse engineering**

- Opera�ng system: FreeRTOS

- Look to be Tesla code

   - `PPC VLE` is well supported by IDA Pro, a

   - decompiler is available

- Standard librairies used: Mbed-TLS,

- nanopb

- `PPC VLE` emulators are not widespread,

- qemu does not support it

- SPC56 SDK gives many useful informa�on ■ Used version of FreeRTOS

   - Low level drivers, etc...

**7**

## Slide 8

# **<u>Architecture</u>**

VCSEC ECU

## **Protocol**

- BLE and UWB interfaces use Protobuf

- messages

- The .proto is shared between differents

- features (TPMS & Tesla Applica�on for example)

- The size of the protobuf message is just

- prepended to the message

- Some projects on Github already extracted

- the .proto from the Tesla App

**8**

## Slide 9

# **TPMS**

**9**

## Slide 10

**<u>TPMS Sensor</u>** Tire-Pressure Monitoring System

- Report real-�me �re-pressure informa�on

- Mandatory in new vehicles

- One for each wheel `FL/FR/RL/RR`

**10**

## Slide 11

# **<u>TPMS Sensor</u>**

Monitor and Alert

Warn the user on any �re abnormali�es

- Older `TPMS` used 433 MHz Radio for connec�vity

■ Now, `TPMS` leverages Bluetooth Low Energy

- 5 BLE endpoints in Tesla cars

■

■ `Center/Left/Right/Rear/Rear Left`

■ Used to locate TPMS posi�on

**11**

## Slide 12

# **<u>TPMS Sensor</u>**

Connectivity

- Only BLE implementa�on studied

- Messages exchanged over BLE GATT characteris�cs

   - `00000211-b2d1-43f0-9b88-960cebf8b91e` GATT service

   - But VCSEC does not use UUIDs but only BLE handles

- Data serialized with Protocol Buffer

**12**

## Slide 13

# **<u>TPMS Sensor</u>**

#### Protocol

**13**


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TPMS Sensor
Protocol
BLE ADV
<—_
vehicleStatus
>
p >
< updaterResponse
Only in
genealogyRequest > adoption
” genealogyResponse phase
Adoption messages specific to the TPMS version—=>
VCSEC TPMS
13
```

## Slide 14

**<u>TPMS Sensor</u>** Example of standard messages

■ Received from TPMS

\```
// Received:
TPData {
    pressure: 101
    temperature: 22
}
// Received:
TPWheelUnitInfo {
    TIAppCRC: "[..]"
    MLXAppCRC: "[..]"
    batteryVoltage_mV: 3011
}
\```

**14**

## Slide 15

# **VCSEC Vulnerability and Exploitation**

**15**

## Slide 16

# **<u>VCSEC</u>**

How to start reverse engineering

###### The Plan

- Study why they are mul�ple firmwares of VCSEC

- Choose the firmware that matches the test setup and is valid for Pwn2Own

- Reverse engineering

###### Reality

- `number`

- Picked firmware with the largest

- Found vulnerability

   - Not present on other firmwares

- Understood the `number` , which is the hardware revision

- Asked the vendor (thanks Tesla!) for the right hardware and if it was valid for Pwn2Own

- Used half of research �me to have a working setup

**16**

## Slide 17

# **<u>VCSEC</u>**

Model3 versions

- `# Firmwares on the infotainment filesystem`

- `$ cat signed_metadata_map.tsv |grep vcsec`

\```
vcsec:50397185vcsec/7/UDSBoot-VCSEC-P_3-A_0-U_0-CONFIG_1704-GIT_AE006F26D00A5C6D.bhx
vcsec:117440513vcsec/23/UDSBoot-VCSEC-P_7-CONFIG_700-GIT_8D34551F13E4371E.bhx
vcsec:134217729vcsec/24/UDSBoot-VCSEC-P_8-CONFIG_702-GIT_3ACAF2AD323CEBCC.bhx
vcsec:50397185vcsec/7/UDSBoot-VCSEC-P_3-A_0-U_0-CONFIG_1705-GIT_AE006F26D00A5C6D.bhx
vcsec:117440513vcsec/23/UDSBoot-VCSEC-P_7-CONFIG_701-GIT_8D34551F13E4371E.bhx
vcsec:134217729vcsec/24/UDSBoot-VCSEC-P_8-CONFIG_703-GIT_3ACAF2AD323CEBCC.bhx
vcsec:50397185vcsec/7/VCSEC_ConfigID_7_crc_formatted_lithium-signed.bhx
vcsec:117440513vcsec/23/VCSEC_ConfigID_23_crc_formatted_lithium-signed.bhx
vcsec:134217729vcsec/24/VCSEC_ConfigID_24_crc_formatted_lithium-signed.bhx
\```

###### Version analyzed: hw-id 134217729

- Seems to be used in recent Model 3 version ("highland" since October 2023)

- VCSEC_ConfigID_24 is the main applica�on code

- VCSEC_ConfigID_23 (HW_ID 117440513) has a very similar code (don't know where is it used)

**17**

## Slide 18

# **<u>VCSEC</u>**

Reversing

> ■ `PPC VLE` IDA decompiler for ■ Time consuming to reverse

■ ~1MB (3k func�ons) ■ No symbols ■ Large structures and func�on callbacks used everywhere ■ Not many strings

Main task

**18**

## Slide 19

# **<u>VCSEC</u>**

Reversing Protobuf messages

■ Used `anvilsecure/nanopb-decompiler` to retrieve Protobuf

■ Patched for BE support (version 3 with 16-bit fields)

\```
// ToVCSECMessage
message Message_10403C1 {
required Message_10416BD field_1 = 1; // SignedMessage
required Message_10407AE field_2 = 2; // UnsignedMessage
}
// SignedMessage
message Message_10416BD {
requiredbytes field_1 = 1 [(nanopb).max_size = 20];
requiredbytes field_2 = 2 [(nanopb).max_size = 282];
// ...
\```

**19**

## Slide 20

# **<u>VCSEC Vulnerability</u>**

x509 Certiûcate in parts

- During enrollment, VCSEC can ask

- for the TPMS cer�ficate

- Only for type 5 TPMS

- TPMS of this type are not in

- produc�on yet

**20**

## Slide 21

# **<u>VCSEC Vulnerability</u>**

Protobuf certiûcate in parts

- Cer�ficate x509 sent in parts

- Part encoded with Protocol Buffer `CertificateResponse`

\```
message CertificateInParts {
uint32 startIndex = 1;
uint32 certificateSize = 2;
bytes data_ = 3;  // nanopb.max_size:128
}
\```

**21**

## Slide 22

**<u>VCSEC Vulnerability</u>** Integer overüow in certiûcate reassembly

> ■ `startIndex` Integer overflow in the valida�on of

> ■ Results in Out-Of-Bounds write with a nega�ve `startIndex char g_cert_buffer[512]; void handle_certificate_response( u32_t tpms_id, u8_t *data,                 // certificateInParts.data_.bytes u32_t data_size,            // certificateInParts.data_.size u32_t start_index,          // certificateInParts.startIndex u32_t certificate_size)     // certificateInParts.certificateSize { // Integer overflow ex: (start_index:-8 + data_size:64) = 56` **`if (data_size <= 512 && (u32_t)(start_index + data_size) <= 512)`** `{ // startIndex can be negative -> OOB write before the global` **`memcpy(g_cert_buffer+start_index, data, data_size);`**

**22**

## Slide 23

# **<u>VCSEC Vulnerability</u>**

Exploitation primitive

- Maximum `data_` buffer size is 128 (enforced by `nanopb` )

- ■ Could overwrite up to 128 bytes of global data before `g_cert_buffer`

- Pointer to a structure containing a func�on pointer just before the buffer

\```
structtpms_auth_s {
bool (*validate_subject_name)(/*...*/);
// ...
};
structtpms_auth_s * g_tpms_auth;
u8 tpms_auth_id;
u8 tpms_auth_state;
char g_cert_buffer[512];
\```

- Sending a valid x509 cer�ficate triggers the `validate_subject_name` call

**23**

## Slide 24

# **<u>VCSEC Exploitation</u>**

Mitigation

- No CFI

- No ASLR

- MMU/MPU not configured ■ Everything RWX

**24**

## Slide 25

# **<u>VCSEC Exploitation</u>**

Exploitation

- Overwrite structure pointer to point to the controlled buffer

- Func�on pointer points to the controlled buffer

- During cer�ficate parsing, it jumps to shellcode ( `PPC VLE` )

- Shellcode can be built from C code using a `powerpc-eabivle toolchain`

   - C code can directly call firmware func�ons (used in post-exploit)

**25**

## Slide 26

# **TPMS auto learn**

**26**

## Slide 27

# **<u>VCSEC Exploitation</u>**

1-click to 0-click

### 1-click to 0-click

■ The vulnerability requires VCSEC to adopt a new TPMS sensor

■ UDS was used to configure VCSEC to add/remove TPMS sensors

■ This is not valid for pwn2own

■ Need another way to adopt TPMS

- Look at the auto learn mechanism

**27**

## Slide 28

# **<u>TPMS</u>**

#### Auto learn

Why VCSEC needs a TPMS auto learn feature

- User can have two set of wheels

■ Users are encouraged to switch front and back wheels to level �re wear

###### Auto learn is started if

- Car is moving for more than 90s

- Speed is at least 25 km/h

- VCSEC will compute TPMS posi�on based on its BLE

- endpoints measurements

###### Adop�on of new TPMS

If a TPMS is disconnected during the auto learn phase VCSEC try to adopt new ones based on BLE adver�sements

**28**

## Slide 29

# **<u>TPMS</u>**

Force the adoption of new TPMS

###### TPMS BLE connec�on mechanism

1. TPMS sensor wakes up by the movement of the wheels.

2. TPMS sends BLE adver�sements.

3. VCSEC receives BLE adver�sement.

4. VCSEC connects to TPMS if the MAC address matches its list of enrolled sensors.

5. BLE connec�on is established, TPMS stop adver�sing.

###### Act as a TPMS sensors

- There is no security except the MAC address list.

- If an a�acker sends adver�sement with the correct MAC address VCSEC will connect on the fake sensor and

- accept messages (like fake �re pressure or temperature)

- In that case VCSEC will not do the TPMS adop�on phase (where our vulnerability lives)

**29**

## Slide 30

# **<u>TPMS</u>**

Force the adoption of new TPMS

###### How to DoS a TPMS sensor

- Just connect on it before VCSEC does when the sensor wake up

-

   - Probably many other ways: JAM signal etc...

- During auto learn phase, having a disconnected sensor allows to enroll arbitrary new sensors

###### Two ESP32 to the rescue

- First try with BlueZ (one of the major bluetooth stack on Linux) but was too slow, VCSEC connects before us

- Automa�c connec�on on adver�sed TPMS was implemented on ESP32: good success rate in racing VCSEC

- TPMS simulator implemented on another ESP32, VCSEC enrolls it during the auto learn phase

- TPMS adop�on messages are sent to the TPMS simulator, vulnerability can be exploited

**30**

## Slide 31

**31**


> Recovered by OCR — confidence 94/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vehicle starts moving and
TPMS wakes up
31
```

## Slide 32

**32**


> Recovered by OCR — confidence 93/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Vehicle starts moving and
TPMS wakes up
32
```

## Slide 33

**33**

## Slide 34

**34**


> Recovered by OCR — confidence 85/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
<> Vehicle starts moving and > VCSEC cannot connect to TPMS
> TPMS starts advertising <> After a 90 sortautlernng and
Enrolled TPMS 4 Tesla VCSEC
34
```

## Slide 35

**35**


> Recovered by OCR — confidence 88/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
<> TPMS starts advertising <s> ae a 90 seconds, unenroll TPMS and
start auto-learning
Enrolled TPMS 4 Tesla VCSEC
Attacker advertizes as a fake new
TPMS
35
```

## Slide 36

**36**


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
> TPMS starts advertising > After a 90 seconds, unenroll TPMS and
start auto-learning
Enrolled TPMS s Tesla VCSEC
Attacker advertizes as a fake new
TPMS
9 re connects to TPMS to I
prevent VCSEC from > VCSEC connects to enroll our
connecting fake TPMS and exploitation starts
36
```

## Slide 37

**37**

## Slide 38

**38**


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VCSEC » TPMS
VCSEC =» TPMS
certificateRead
certificateResponse
Exploit vulnerability
38
```

## Slide 39

**39**


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
VCSEC =» TPMS
VCSEC =» TPMS
certificateRead
certificateResponse
Exploit vulnerability
Code execution on
VCSEC
39
```

## Slide 40

# **Conclusion**

**40**

## Slide 41

# **<u>Conclusion</u>**

#### Final payload

- Shellcode: send `SYNACKTI V<3TESLA` on the vehicule CAN on CAN ID `0x444` :

- Locate and use the fonc�on in the firmware to send CAN messages

- Used as proof of exploita�on for Pwn2Own: Abritrary CAN message on vehicule CAN from a

- remote connec�on

\```
#define fnsend_can_raw ((void (*)(char *msg, int id))0x10B7D60)
intmain_payload()
{
while(1) {
       fnsend_can_raw("\x44\x44\x08SYNACKTI", 60);
       fnsend_can_raw("\x44\x44\x08V<3TESLA", 60);
   }
return0;
}
\```

**41**

## Slide 42

# **<u>VCSEC Exploitation</u>**

Result

- First try at Pwn2Own Vancouver 2024 (March)

- ■ Win: 200 000$ plus a Tesla Model 3 (2024)

- A lot more easier than our three other Tesla

- Pwn2own entries (2022, 2023, january 2024)

■ Infotainment a�acks are difficult because of good defense in depth User isola�on, sandboxing, ASLR, PIE, ...

■ Try your luck, standalone ECUs are a good candidate to start

**42**

## Slide 43

# **<u>Conclusion</u>**

Impacts

- VCSEC is a cri�cal ECU for the car security

   - It manages access to the car and grants the user the right to start the car

   - It has access to the vehicule CAN and can send messages to do some ac�on on the car

- Having code execu�on in this ECU gives an a�acker the ability to perform these ac�ons

- A�ack can be implemented on very small devices

Fixes

- Tesla quickly released a new version that fixes the bug

   - Vulnerability is fixed and other variables are also checked

**43**

## Slide 44

**https://www.linkedin.com/company/synacktiv https://twitter.com/synacktiv https://synacktiv.com**
