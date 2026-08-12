---
title: "0-click RCE on the IVI component Pwn2Own Automotive edition"
speakers: ["Mikhail Evdokimov"]
conference: "Hexacon"
conference_full: "Hexacon 2024"
edition: ""
year: 2024
source_pdf: "Hexacon 2024 Slides/Mikhail Evdokimov_0-click RCE on the IVI component Pwn2Own Automotive edition.pdf"
pages: 189
sha256: "6d663cde6ecb5f4a191103660ceaf58c3240e0213afb8c2197fc35ec2f549c14"
text_chars: 66923
ocr_pages: 48
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:21:11Z"
---
# 0-click RCE on the IVI component Pwn2Own Automotive edition

**Speakers:** Mikhail Evdokimov  
**Conference:** Hexacon 2024  
**Source:** `Hexacon 2024 Slides/Mikhail Evdokimov_0-click RCE on the IVI component Pwn2Own Automotive edition.pdf` (189 pages)


## Slide 1

0-click RCE on the IVI component: Pwn2Own Automotive edition

#### Hexacon 2024

1

## Slide 2

#### Agenda

- Introduction

- Bluetooth Internals

- Demonstrating vulnerability in the code

- Exploitation strategy

- Exploit stability improvement

- Impact and Implications

- Pwn2Own results and timeline

2

## Slide 3

## Introduction

3

## Slide 4

#### Intro :: About me

- Mikhail Evdokimov

- Senior Security Researcher at PCAutomotive

- Reverse-Engineering & Vulnerability Research

- Keen interest in wireless technologies

- ● Have been pwning Bluetooth since 2021

tw: <u>@konatabrk</u>

4

## Slide 5

#### Intro :: Pwn2Own IVI Targets

5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Intro :: Pwn2Own IVI Targets
Master of Pwn
Target Prize Points
Sony XAV-AX5500
Alpine Halo9 iLX-F509
Pioneer DMH-WT7600NEX
```

## Slide 6

#### Intro :: Alpine Halo9

- <u>Alpine Halo9 iLX-F509</u>

- External In-Vehicle Infotainment (IVI)

- Touchscreen display

- USB / WLAN / Bluetooth

- Apple Carplay & Android Auto

- <u>iDatalink Maestro Compatible</u> ○ External CAN adapter

6

## Slide 7

#### Intro :: Alpine Halo9

7

## Slide 8

#### Intro :: Alpine Halo9 :: Firmware

- Firmware was obtained from EMMC chip

- Without desoldering

- Used X-ray to identify traces

- Was conducted by our teammate <u>Polina Smirnova</u>

8

## Slide 9

## Bluetooth Internals

9

## Slide 10

#### Bluetooth :: Stack

reference: Dissect Android Bluetooth for Fun & Profit

10

## Slide 11

#### Bluetooth :: HCI Link Connection

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bluetooth :: HCI Link Connection
HCI Link Connection Establishment
BDADDR: aa:bb:cc:dd:ee: ff Device A
HCI Handle:
8x188
HCI Create Connection
>
HCI Accept Connection
i
HCI Link Connection
Authentication Requested
>
Link Key Request
<
Link Key Reply Negative
I0 Capability
< >|
User Confirmation
< >|
Authentication Completed
K<
Device Bo BDADDR: 11:22:33:44:55:66
HCI Handle:
6x41
Prior Authentication
11
```

## Slide 12

#### Bluetooth :: HCI ACL Fragmentation

12

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bluetooth :: HCI ACL Fragmentation
HCI ACL Data Packet
Connection handle to be used for transmitting data
over a HCI Link Connection (primary controller)
2HCI ACL fragment's maximum length depends on
the controller. Usually it's 1021 bytes
’ L2CAP PDU Header n
nm
```

## Slide 13

#### Bluetooth :: L2CAP Channels

- The logical connection between two endpoints in peer devices ○ Endpoints are BT Profiles identified by PSM (analog to TCP/IP ports)

- Multiplexing over HCI Link

- Identified by Channel ID (CID):

   - SCID - Source endpoint CID

   - DCID - Destination endpoint CID

13

## Slide 14

#### Bluetooth :: L2CAP Channels

##### Two types of L2CAP Channels:

- FIxed Channels

   - Static SCID / DCID

   - L2CAP Signalling Channel (SCID=1) ■ Creating dynamic L2CAP Channels

- Dynamic Channels

   - Dynamically allocated SCID / DCID

   - Types: Basic, ERTM, Streaming, etc

   - Service Discovery Protocol (SDP) is accessible before authentication

14

## Slide 15

#### Bluetooth :: L2CAP Channels

15

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Bluetooth :: L2CAP Channels
HCI Handle:
8x180
L2CAP Channels
HCI Create Connection
>|
HCI Accept Connection
<
HCI Link Connection
L2CAP Connection Request
|
L2CAP Connection Response
L2CAP SDP Communication
< >}
HCI Handle:
8x41
PSM=1 E
SDP Profile :
MTU, Channel Type,
other params
Multiple L2CAP Channels over the same
HCI Link Connection are possible (multiplexing)
15
```

## Slide 16

#### Bluetooth :: Summary

- HCI Link Connection is the initial step for BT communication

- HCI Handle is an identification of a HCI Link Connection

- L2CAP Channels are multiplexed connections to BT services

- L2CAP Channels types: Basic, ERTM

- The number of L2CAP Channels is limited (Alpine: ~50)

- L2CAP PDU consists of multiple HCI ACL fragments

- SDP service is accessible prior to authentication

16

## Slide 17

## BT :: Alpine

17

## Slide 18

#### Alpine :: btapp

● ARM 32-bit architecture.

- Launched as root.

● Security mitigations:

○ Stack: No canary found ○ PIE: No PIE (0x10000)

- `libc-2.20.so` - no Tcache.

● Multithreaded – “BT thread” is responsible for BT communication

- Bluetooth Stack – a proprietary implementation

○ Other devices might be vulnerable

- Contains symbols – simplifies reverse-engineering

18

## Slide 19

#### Alpine :: Disclaimer

A few warnings before going further:

● All the code examples are heavily simplified for readability.

- A lot of checks of the original code are omitted.

- Only mandatory exploitation steps are discussed.

_You can find all the details in the upcoming whitepaper_

19

## Slide 20

#### Alpine :: HCI ACL Rx

```
__int32 __fastcallprh_l2_sar_data_ind(
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
{
p_link=prh_l2_acl_find_handle((int)hci_handle);
data =inbf->data;
aclLen=inbf->len-4;
switch(flags){
caseprh_hci_ACL_START_FRAGMENT:
...
caseprh_hci_ACL_CONTINUE_FRAGMENT:
...
}
}
```

`p_link` is the representation of an established HCI Link Connection

20

## Slide 21

#### Alpine :: HCI ACL Rx :: ACL Start

```
__int32 __fastcallprh_l2_sar_data_ind(
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
{
p_link=prh_l2_acl_find_handle((int)hci_handle);
data =inbf->data;
aclLen=inbf->len-4;
switch(flags){
caseprh_hci_ACL_START_FRAGMENT:
...
caseprh_hci_ACL_CONTINUE_FRAGMENT:
```

```
...
}
}
```

21

## Slide 22

#### Alpine :: HCI ACL Rx :: ACL Start

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length =data[0]|(data[1]<<8);
p_link->cur_len=0;
p_link->pending_cid=(data[2]|(data[3]<<8));
if(cid==2&&p_link->length>0x4F1) {
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
chan=prh_l2_chn_get_p_channel(p_link->pending_cid);
if(p_link->length >chan->inMTU){
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_buf->len=p_link->length;
```

```
p_link->cur_pos=p_link->cur_buf;
memcpy(p_link->cur_buf,data +4,aclLen);
p_link->cur_pos+=aclLen;
p_link->cur_len+=aclLen;
```

```
if(aclLen!=p_link->length )
```

```
return0;
```

```
pkt_handler:
```

```
p_link->cur_pos=0;
p_link->mtu_complete=1;
prh_l2_pkt_handler(
```

```
p_link->pending_cid,hci_handle,p_link->cur_buf);
returnret;
```

22

## Slide 23

#### Alpine :: HCI ACL Rx :: ACL Start

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length =data[0]|(data[1]<<8);
p_link->cur_len=0;
```

```
p_link->pending_cid=(data[2]|(data[3]<<8));
if(cid==2&&p_link->length>0x4F1) {
```

```
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
chan=prh_l2_chn_get_p_channel(p_link->pending_cid);
if(p_link->length >chan->inMTU){
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_buf->len=p_link->length;
```

```
p_link->cur_pos=p_link->cur_buf;
memcpy(p_link->cur_buf,data +4,aclLen);
p_link->cur_pos+=aclLen;
p_link->cur_len+=aclLen;
```

```
if(aclLen!=p_link->length )
```

```
return0;
```

```
pkt_handler:
```

```
p_link->cur_pos=0;
p_link->mtu_complete=1;
prh_l2_pkt_handler(
```

```
p_link->pending_cid,hci_handle,p_link->cur_buf);
returnret;
```

23

## Slide 24

#### Alpine :: HCI ACL Rx :: ACL Start

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length =data[0]|(data[1]<<8);
p_link->cur_len=0;
```

```
p_link->pending_cid=(data[2]|(data[3]<<8));
```

```
if(cid==2&&p_link->length>0x4F1) {
```

```
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
chan=prh_l2_chn_get_p_channel(p_link->pending_cid);
```

```
if(p_link->length >chan->inMTU){
```

```
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
```

```
p_link->cur_buf->len=p_link->length;
```

```
p_link->cur_pos=p_link->cur_buf;
```

```
memcpy(p_link->cur_buf,data +4,aclLen);
p_link->cur_pos+=aclLen;
p_link->cur_len+=aclLen;
```

```
if(aclLen!=p_link->length )
```

```
return0;
```

```
pkt_handler:
```

```
p_link->cur_pos=0;
```

```
p_link->mtu_complete=1;
```

```
prh_l2_pkt_handler(
```

```
p_link->pending_cid,hci_handle,p_link->cur_buf);
returnret;
```

24

## Slide 25

#### Alpine :: HCI ACL Rx :: ACL Start

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length =data[0]|(data[1]<<8);
p_link->cur_len=0;
p_link->pending_cid=(data[2]|(data[3]<<8));
if(cid==2&&p_link->length>0x4F1) {
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
chan=prh_l2_chn_get_p_channel(p_link->pending_cid);
if(p_link->length >chan->inMTU){
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_buf->len=p_link->length;
p_link->cur_pos=p_link->cur_buf;
memcpy(p_link->cur_buf,data +4,aclLen);
p_link->cur_pos+=aclLen;
p_link->cur_len+=aclLen;
```

```
if(aclLen!=p_link->length )
```

```
return0;
```

```
pkt_handler:
```

```
p_link->cur_pos=0;
```

```
p_link->mtu_complete=1;
prh_l2_pkt_handler(
```

```
p_link->pending_cid,hci_handle,p_link->cur_buf);
returnret;
```

25

## Slide 26

#### Alpine :: HCI ACL Rx :: ACL Start

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length =data[0]|(data[1]<<8);
p_link->cur_len=0;
p_link->pending_cid=(data[2]|(data[3]<<8));
```

```
if(cid==2&&p_link->length>0x4F1) {
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
chan=prh_l2_chn_get_p_channel(p_link->pending_cid);
```

```
if(p_link->length >chan->inMTU){
```

```
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_buf->len=p_link->length;
```

```
p_link->cur_pos=p_link->cur_buf;
```

```
memcpy(p_link->cur_buf,data +4,aclLen);
```

```
p_link->cur_pos+=aclLen;
```

```
p_link->cur_len+=aclLen;
```

```
if(aclLen!=p_link->length )
```

```
return0;
```

```
pkt_handler:
```

```
p_link->cur_pos=0;
```

```
p_link->mtu_complete=1;
prh_l2_pkt_handler(
```

```
p_link->pending_cid,hci_handle,p_link->cur_buf);
returnret;
```

26

## Slide 27

#### Alpine :: HCI ACL Rx :: ACL Start

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length =data[0]|(data[1]<<8);
p_link->cur_len=0;
```

```
p_link->pending_cid=(data[2]|(data[3]<<8));
```

```
if(cid==2&&p_link->length>0x4F1) {
```

```
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
chan=prh_l2_chn_get_p_channel(p_link->pending_cid);
```

```
if(p_link->length >chan->inMTU){
```

```
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_buf->len=p_link->length;
```

```
p_link->cur_pos=p_link->cur_buf;
```

```
memcpy(p_link->cur_buf,data +4,aclLen);
p_link->cur_pos+=aclLen;
p_link->cur_len+=aclLen;
```

```
if(aclLen!=p_link->length )
```

```
return0;
```

```
pkt_handler:
```

```
p_link->cur_pos=0;
```

```
p_link->mtu_complete=1;
```

```
prh_l2_pkt_handler(
```

```
p_link->pending_cid,hci_handle,p_link->cur_buf);
returnret;
```

27

## Slide 28

#### Alpine :: HCI ACL Rx :: ACL Start

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length =data[0]|(data[1]<<8);
p_link->cur_len=0;
```

```
p_link->pending_cid=(data[2]|(data[3]<<8));
if(cid==2&&p_link->length>0x4F1) {
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
chan=prh_l2_chn_get_p_channel(p_link->pending_cid);
```

```
if(p_link->length >chan->inMTU){
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_buf->len=p_link->length;
```

```
p_link->cur_pos=p_link->cur_buf;
```

```
memcpy(p_link->cur_buf,data +4,aclLen);
```

```
p_link->cur_pos+=aclLen;
```

```
p_link->cur_len+=aclLen;
```

```
if(aclLen!=p_link->length )
return0;
```

```
pkt_handler:
```

```
p_link->cur_pos=0;
```

```
p_link->mtu_complete=1;
```

```
prh_l2_pkt_handler(
```

```
p_link->pending_cid,hci_handle,p_link->cur_buf);
returnret;
```

28

## Slide 29

#### Alpine :: HCI ACL Rx :: ACL Start

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length =data[0]|(data[1]<<8);
p_link->cur_len=0;
p_link->pending_cid=(data[2]|(data[3]<<8));
if(cid==2&&p_link->length>0x4F1) {
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
chan=prh_l2_chn_get_p_channel(p_link->pending_cid);
```

```
if(p_link->length >chan->inMTU){
p_link->mtu_complete=1;
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_buf->len=p_link->length;
```

```
p_link->cur_pos=p_link->cur_buf;
memcpy(p_link->cur_buf,data +4,aclLen);
p_link->cur_pos+=aclLen;
p_link->cur_len+=aclLen;
```

```
if(aclLen!=p_link->length )
```

```
return0;
```

```
pkt_handler:
```

```
p_link->cur_pos=0;
p_link->mtu_complete=1;
```

```
prh_l2_pkt_handler(
```

```
p_link->pending_cid,hci_handle,p_link->cur_buf);
returnret;
```

29

## Slide 30

#### Alpine :: HCI ACL Rx

```
__int32 __fastcallprh_l2_sar_data_ind(
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
{
p_link=prh_l2_acl_find_handle((int)hci_handle);
data =inbf->data;
aclLen=inbf->len-4;
switch(flags){
caseprh_hci_ACL_START_FRAGMENT:
...
caseprh_hci_ACL_CONTINUE_FRAGMENT:
...
}
}
```

`p_link` is the representation of an established HCI Link Connection

30

## Slide 31

#### Alpine :: HCI ACL Rx :: ACL Continue

```
__int32 __fastcallprh_l2_sar_data_ind(
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
{
p_link=prh_l2_acl_find_handle((int)hci_handle);
data =inbf->data;
aclLen=inbf->len-4;
switch(flags){
caseprh_hci_ACL_START_FRAGMENT:
...
```

```
caseprh_hci_ACL_CONTINUE_FRAGMENT:
...
}
}
```

31

## Slide 32

#### Alpine :: HCI ACL Rx :: ACL Continue

```
if(!p_link->cur_pos){
p_link->mtu_complete=1;
return0;
}
if(p_link->cur_len+inbf->len>p_link->length ){
host_buf_free(p_link->cur_buf);
p_link->cur_pos=0;
p_link->mtu_complete=1;
return 0;
}
memcpy(p_link->cur_pos,data,inbf->len);
p_link->cur_len+=inbf->len;
if(p_link->length !=p_link->cur_len){
p_link->cur_pos+=inbf->len;
returnret;
}
gotopkt_handler;
pkt_handler:
p_link->cur_pos=0;
p_link->mtu_complete=1;
prh_l2_pkt_handler(
p_link->pending_cid,hci_handle,p_link->cur_buf);
```

32

## Slide 33

#### Alpine :: HCI ACL Rx :: ACL Continue

`if ( !p_link->cur_pos ) { p_link->mtu_complete = 1; return 0; } if ( p_link->cur_len+inbf->len > p_link->length ) {` **`host_buf_free`** `(p_link->cur_buf); p_link->cur_pos = 0; p_link->mtu_complete = 1; return 0; }` **`memcpy`** `(p_link->cur_pos, data, inbf->len); p_link->cur_len += inbf->len; if ( p_link->length != p_link->cur_len ) { p_link->cur_pos += inbf->len; return ret; } goto pkt_handler; pkt_handler: p_link->cur_pos = 0; p_link->mtu_complete = 1;` **`prh_l2_pkt_handler`** `(` 33 `p_link->pending_cid, hci_handle, p_link->cur_buf);`

## Slide 34

#### Alpine :: HCI ACL Rx :: ACL Continue

```
if(!p_link->cur_pos){
p_link->mtu_complete=1;
return0;
}
if(p_link->cur_len+inbf->len>p_link->length ){
host_buf_free(p_link->cur_buf);
p_link->cur_pos=0;
p_link->mtu_complete=1;
return 0;
}
memcpy(p_link->cur_pos,data,inbf->len);
p_link->cur_len+=inbf->len;
if(p_link->length !=p_link->cur_len){
p_link->cur_pos+=inbf->len;
returnret;
}
gotopkt_handler;
pkt_handler:
p_link->cur_pos=0;
p_link->mtu_complete=1;
prh_l2_pkt_handler(
p_link->pending_cid,hci_handle,p_link->cur_buf);
```

34

## Slide 35

#### Alpine :: HCI ACL Rx :: ACL Continue

```
if(!p_link->cur_pos){
p_link->mtu_complete=1;
return0;
}
if(p_link->cur_len+inbf->len>p_link->length ){
host_buf_free(p_link->cur_buf);
p_link->cur_pos=0;
p_link->mtu_complete=1;
return0;
}
memcpy(p_link->cur_pos,data,inbf->len);
p_link->cur_len+=inbf->len;
if(p_link->length !=p_link->cur_len){
p_link->cur_pos+=inbf->len;
returnret;
}
gotopkt_handler;
pkt_handler:
p_link->cur_pos=0;
p_link->mtu_complete=1;
prh_l2_pkt_handler(
p_link->pending_cid,hci_handle,p_link->cur_buf);
```

35

## Slide 36

## Bug :: Use-After-Free in HCI ACL Reception

36

## Slide 37

#### Bug :: UAF Root Cause

1. TX HCI ACL Start -> SDP Profile

```
__int32 __fastcallprh_l2_sar_data_ind(
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
```

```
{
```

```
switch(flags){
```

```
caseprh_hci_ACL_START_FRAGMENT:
```

```
if(!p_link->mtu_complete&&p_link->cur_buf){
```

```
host_buf_free(p_link->cur_buf);
```

```
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length=data[0]|(data[1]<<8);
```

```
if(cid==2&&p_link->length>0x4F1) {
```

```
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_pos=p_link->cur_buf;
```

```
caseprh_hci_ACL_CONTINUE_FRAGMENT:
```

```
memcpy(p_link->cur_pos,data,inbf->len);
p_link->cur_len+=inbf->len;
if(p_link->length !=p_link->cur_len){
p_link->cur_pos+=inbf->len;
returnret;
}
```

37

## Slide 38

#### Bug :: UAF Root Cause

```
__int32 __fastcallprh_l2_sar_data_ind(
```

```
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
```

1. TX HCI ACL Start -> SDP Profile

```
{
```

```
switch(flags){
```

```
caseprh_hci_ACL_START_FRAGMENT:
```

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length=data[0]|(data[1]<<8);
```

```
if(cid==2&&p_link->length>0x4F1) {
```

```
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_pos=p_link->cur_buf;
```

```
caseprh_hci_ACL_CONTINUE_FRAGMENT:
```

```
memcpy(p_link->cur_pos,data,inbf->len);
p_link->cur_len+=inbf->len;
if(p_link->length !=p_link->cur_len){
p_link->cur_pos+=inbf->len;
returnret;
```

```
}
```

38

## Slide 39

#### Bug :: UAF Root Cause

```
__int32 __fastcallprh_l2_sar_data_ind(
```

```
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
```

1. TX HCI ACL Start -> SDP Profile

2. TX HCI ACL Start -> L2CAP Conless (cid=2) L2CAP PDU Length (0x800) > 0x4F1, i.e. `p_link->length` > `0x4F1`

```
{
```

```
switch(flags){
```

```
caseprh_hci_ACL_START_FRAGMENT:
```

```
if(!p_link->mtu_complete&&p_link->cur_buf){
```

```
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length=data[0]|(data[1]<<8);
```

```
if(cid==2&&p_link->length>0x4F1) {
```

```
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_pos=p_link->cur_buf;
```

```
caseprh_hci_ACL_CONTINUE_FRAGMENT:
```

```
memcpy(p_link->cur_pos,data,inbf->len);
p_link->cur_len+=inbf->len;
if(p_link->length !=p_link->cur_len){
p_link->cur_pos+=inbf->len;
returnret;
}
```

39

## Slide 40

#### Bug :: UAF Root Cause

```
__int32 __fastcallprh_l2_sar_data_ind(
```

```
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
```

1. TX HCI ACL Start -> SDP Profile

2. TX HCI ACL Start -> L2CAP Conless (cid=2) L2CAP PDU Length (0x800) > 0x4F1, i.e. `p_link->length` > `0x4F1`

```
{
```

```
switch(flags){
```

```
caseprh_hci_ACL_START_FRAGMENT:
```

```
if(!p_link->mtu_complete&&p_link->cur_buf){
```

```
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
```

```
p_link->length=data[0]|(data[1]<<8);
```

```
if(cid==2&&p_link->length>0x4F1) {
```

```
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_pos=p_link->cur_buf;
```

```
caseprh_hci_ACL_CONTINUE_FRAGMENT:
```

```
memcpy(p_link->cur_pos,data,inbf->len);
```

```
p_link->cur_len+=inbf->len;
```

```
if(p_link->length !=p_link->cur_len){
```

```
p_link->cur_pos+=inbf->len;
returnret;
```

```
}
```

40

## Slide 41

#### Bug :: UAF Root Cause

```
__int32 __fastcallprh_l2_sar_data_ind(
```

```
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
```

1. TX HCI ACL Start -> SDP Profile

2. TX HCI ACL Start -> L2CAP Conless (cid=2) L2CAP PDU Length (0x800) > 0x4F1, i.e. `p_link->length` > `0x4F1`

```
{
```

```
switch(flags){
```

```
caseprh_hci_ACL_START_FRAGMENT:
```

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
```

```
p_link->length=data[0]|(data[1]<<8);
```

```
if(cid==2&&p_link->length>0x4F1) {
```

```
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_pos=p_link->cur_buf;
```

```
caseprh_hci_ACL_CONTINUE_FRAGMENT:
```

```
memcpy(p_link->cur_pos,data,inbf->len);
```

```
p_link->cur_len+=inbf->len;
```

```
if(p_link->length !=p_link->cur_len){
```

```
p_link->cur_pos+=inbf->len;
returnret;
}
```

41

## Slide 42

#### Bug :: UAF Root Cause

```
__int32 __fastcallprh_l2_sar_data_ind(
```

```
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
```

1. TX HCI ACL Start -> SDP Profile

2. TX HCI ACL Start -> L2CAP Conless (cid=2) L2CAP PDU Length (0x800) > 0x4F1, i.e. `p_link->length` > `0x4F1`

```
{
```

```
switch(flags){
```

```
caseprh_hci_ACL_START_FRAGMENT:
```

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
```

```
p_link->length=data[0]|(data[1]<<8);
```

```
if(cid==2&&p_link->length>0x4F1) {
```

```
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_pos=p_link->cur_buf;
```

```
caseprh_hci_ACL_CONTINUE_FRAGMENT:
```

```
memcpy(p_link->cur_pos,data,inbf->len);
p_link->cur_len+=inbf->len;
if(p_link->length !=p_link->cur_len){
p_link->cur_pos+=inbf->len;
returnret;
}
```

42

## Slide 43

#### Bug :: UAF Root Cause

```
__int32 __fastcallprh_l2_sar_data_ind(
```

```
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
```

1. TX HCI ACL Start -> SDP Profile

2. TX HCI ACL Start -> L2CAP Conless (cid=2) L2CAP PDU Length (0x800) > 0x4F1, i.e. `p_link->length` > `0x4F1`

```
{
```

```
switch(flags){
```

```
caseprh_hci_ACL_START_FRAGMENT:
```

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
```

```
p_link->length=data[0]|(data[1]<<8);
```

```
if(cid==2&&p_link->length>0x4F1) {
```

```
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_pos=p_link->cur_buf;
```

```
caseprh_hci_ACL_CONTINUE_FRAGMENT:
```

```
memcpy(p_link->cur_pos,data,inbf->len);
p_link->cur_len+=inbf->len;
```

```
if(p_link->length !=p_link->cur_len){
p_link->cur_pos+=inbf->len;
returnret;
```

```
}
```

43

## Slide 44

#### Bug :: UAF Root Cause

```
__int32 __fastcallprh_l2_sar_data_ind(
```

```
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
```

1. TX HCI ACL Start -> SDP Profile

2. TX HCI ACL Start -> L2CAP Conless (cid=2) L2CAP PDU Length (0x800) > 0x4F1, i.e.

3. TX HCI ACL Continue

```
{
```

```
switch(flags){
```

```
caseprh_hci_ACL_START_FRAGMENT:
```

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length=data[0]|(data[1]<<8);
...
```

```
if(cid==2&&p_link->length>0x4F1) {
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_pos=p_link->cur_buf;
```

```
caseprh_hci_ACL_CONTINUE_FRAGMENT:
```

```
memcpy(p_link->cur_pos,data,inbf->len);
p_link->cur_len+=inbf->len;
if(p_link->length !=p_link->cur_len){
```

```
p_link->cur_pos+=inbf->len;
returnret;
```

```
}
```

44

## Slide 45

#### Bug :: UAF Root Cause

```
__int32 __fastcallprh_l2_sar_data_ind(
```

```
char*hci_handle,host_buf*inbf,HCI_ACL_FLAGS flags)
```

1. TX HCI ACL Start -> SDP Profile

2. TX HCI ACL Start -> L2CAP Conless (cid=2) L2CAP PDU Length (0x800) > 0x4F1, i.e.

3. TX HCI ACL Continue

```
{
```

```
switch(flags){
```

```
caseprh_hci_ACL_START_FRAGMENT:
```

```
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
```

```
}
```

```
p_link->mtu_complete=0;
p_link->length=data[0]|(data[1]<<8);
...
```

```
if(cid==2&&p_link->length>0x4F1) {
return 0;
```

```
}
```

```
p_link->cur_buf=host_buf_alloc(p_link->length);
p_link->cur_pos=p_link->cur_buf;
```

```
caseprh_hci_ACL_CONTINUE_FRAGMENT:
```

```
memcpy(p_link->cur_pos,data,inbf->len);
p_link->cur_len+=inbf->len;
if(p_link->length !=p_link->cur_len){
```

```
p_link->cur_pos+=inbf->len;
returnret;
```

```
}
```

45

## Slide 46

## Why is it a 0-click?

46

## Slide 47

#### Bug :: Why is it 0-click?

- UAF in L2CAP protocol.

- L2CAP is processed prior to authentication.

- BDADDR can be obtained from:

   - Sniff air traffic via Ubertooth.

   - WLAN module’s MAC address (coexistence).

   - Bruteforce lower 3 bytes.

47

## Slide 48

#### Bug :: Why is it 0-click?

- UAF in L2CAP protocol.

- L2CAP is processed prior to authentication.

- BDADDR can be obtained from:

   - Sniff air traffic via Ubertooth.

   - WLAN module’s MAC address (coexistence).

   - Bruteforce lower 3 bytes.

- No user interaction for exploitation

48

## Slide 49

## Exploitation Strategy

49

## Slide 50

#### Exploit :: Limitations

- `p_link` is created per HCI Link Connection

- We can’t manipulate the heap using the tampered `p_link` due to inability of sending complete L2CAP PDUs

- Tampered `p_link` can be used only for writes into the freed heap chunk

50

## Slide 51

#### Exploit :: Limitations

- `p_link` is created per HCI Link Connection

- We can’t manipulate the heap using the tampered `p_link` due to inability of sending complete L2CAP PDUs

- Tampered `p_link` can be used only for writes into the freed heap chunk

Solution: Use an additional controller!

link#2

51

## Slide 52

#### Exploit :: New Controller

- Now we have `link#1` and `link#2` :

   - `link#1` (Master): Corrupted with UAF

   - `link#2` (Slave): Used for heap manipulations

- The UAF condition of `link#1` is maintained by utilizing it only for HCI ACL Continue fragments

52

## Slide 53

#### Exploit :: UAF Approach

Can we substitute the chunk in `link#1->cur_pos` (UAF) with something useful? using link#2 HCI Link Connection

53

## Slide 54

#### Exploit :: UAF Approach

Can we substitute the chunk in `link#1->cur_pos` (UAF) with something useful? using link#2 HCI Link Connection

`1.struct host_buf` - object allocated for a complete L2CAP PDU (elastic object) `2.struct prh_t_l2_channel` - object allocated for an L2CAP channel

`3.struct prh_t_l2_acl_link` - object allocated for a HCI Link Connection

54

## Slide 55

#### Exploit :: UAF Approach

Can we substitute the chunk in `link#1->cur_pos` (UAF) with something useful? using link#2 HCI Link Connection

`1.struct host_buf` - object allocated for a complete L2CAP PDU (elastic object) `2.struct prh_t_l2_channel` - object allocated for an L2CAP channel

`3.struct prh_t_l2_acl_link` - object allocated for a HCI Link Connection

Problems:

- Fastbins are way too hot for this

● Unsortedbin works in a queue-like way (not suitable for reliable remote UAF)

● Some objects don’t have interesting fields ( `struct host_buf` )

55

## Slide 56

## Solution?

56

## Slide 57

## Solution? Convert UAF into Heap Overflow.

57

## Slide 58

#### Exploit :: Heap Overflow

- Assign arbitrary `p_link->length` after free

- ● Out-of-boundary of the original heap chunk ● ACL Continue can overflow data further Due to increased length

```
caseprh_hci_ACL_START_FRAGMENT:
if(!p_link->mtu_complete&&p_link->cur_buf){
host_buf_free(p_link->cur_buf);
p_link->cur_buf=NULL;
}
p_link->length=data[0]|(data[1]<<8);
...
if(cid==2&&p_link->length>0x4F1) {
return 0;
}
...
caseprh_hci_ACL_CONTINUE_FRAGMENT:
...
memcpy(p_link->cur_pos,data,inbf->len);
```

58

## Slide 59

#### Exploit :: Heap Overflow :: Targets

Heap-based buffer overflow exploitation:

- Freed chunk metadata overwriting (attacking the allocator): ○ Knowledge of the allocator’s internals

   - Precise heap offsets and operations

- Allocated objects data overwriting (attacking the logic):

   - Requires good objects with useful members

   - Heap Feng-Shui is still needed

59

## Slide 60

#### Exploit :: Heap Overflow :: Targets

Heap-based buffer overflow exploitation:

- Freed chunk metadata overwriting (attacking the allocator):

   - Knowledge of the allocator’s internals

   - Precise heap offsets and operations

- Allocated objects data overwriting (attacking the logic):

   - Requires good objects with useful members

   - Heap Feng-Shui is still needed

60

## Slide 61

#### Exploit :: Heap Layout

61

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Heap Layout
Main
Heap Arena
Thread#1
Heap Arena
Thread#2
Heap Arena
Thread#3
Heap Arena
61
```

## Slide 62

#### Exploit :: Heap Layout :: Spraying :: L2CAP Channel

62

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Heap Layout :: Spraying :: L2CAP Channel
Heap Spraying via L2CAP Channels Legend:
To eliminate the heap fragmentation allocated
freed
1. Start heap spraying by establishing multiple L2CAP channels to SDP profile.
2. After a dozen objects, the following layout will be achieved.
3. Let's choose the target channel and enumerate the channels' sled.
62
```

## Slide 63

#### Exploit :: Heap Layout :: Overview

L2CAP Channels spraying was done via `link#1` before triggering the vulnerability

63

## Slide 64

#### Exploit :: Heap Layout :: Overview

64

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Heap Layout :: Overview
L2CAP Channels Layout :
z)
64
```

## Slide 65

# How do we use the obtained Heap Overflow?

65

## Slide 66

#### Exploit :: Heap Layout :: Trigger

66

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
expiort :: Heap Layout :: Trigger
. Initial state of the L2CAP Channels layout after spraying
2. Disconnect channel#1 from link#1, it will free the heap chunk
3. Reallocate the freed channel#1 with L2CAP PDU via link#1
66
```

## Slide 67

#### Exploit :: Heap Layout :: Trigger

67

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Heap Layout :: Trigger
4. Subsequent heap overflow will go into channel#2
67
```

## Slide 68

#### Exploit :: Heap Layout :: Trigger

By utilizing the heap overflow primitive, we’re able to corrupt other objects in the channels sled created after spraying.

`prh_host_gen_ll` content must be set to NULL to bypass the application crashes. (more info you will find in the whitepaper) Now that we demonstrated the nature of Heap Overflow, the next step is to understand what we can corrupt in L2CAP Channel objects.

68

## Slide 69

# ERTM Channels

69

## Slide 70

#### Exploit :: ERTM Channel :: General Information

- ERTM - Enhanced Retransmission mode

- ● Type of dynamic L2CAP channels

- Segmentation of ERTM PDU: I-frames and S-frames

- The information frames (I-frames): information transfer between L2CAP entities. I-frame is transmitted in L2CAP PDU

- ● The supervisory frames (S-frames): acknowledge I-frames and request retransmission

- PDUs exchanged with a peer entity are numbered and acknowledged

70

## Slide 71

#### Exploit :: ERTM Channel :: General Information

- ERTM - Enhanced Retransmission mode

- Type of dynamic L2CAP channels

- Segmentation of ERTM PDU: I-frames and S-frames

- The information frames (I-frames): information transfer between L2CAP entities. I-frame is transmitted in L2CAP PDU

- The supervisory frames (S-frames): acknowledge I-frames and request retransmission

- PDUs exchanged with a peer entity are numbered and acknowledged

71

## Slide 72

#### Exploit :: ERTM Channel :: Frames

72

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: ERTM Channel :: Frames
Supervisory frame (S-frame) Information frame (I-frame)
16 16 16/32 8/16 te a/ 16
*S. Basic L2CAP 4+” _ Basic L2CAP .
header ' header
72
```

## Slide 73

#### Exploit :: ERTM Channel :: Frames

73

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: ERTM Channel :: Frames
Supervisory frame (S-frame) Information frame (I-frame)
. ,
. ¢
~s. Basic L2CAP |-*
16 16 16 / 32 8 / 16 16
header '
~<. Basic L2CAP |-”
header '
; 1FCS is optional
20nly present in Start of L2CAP SDU
I-frame is one L2CAP PDU
73
```

## Slide 74

#### Exploit :: ERTM Channel :: Frames

74

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: ERTM Channel :: Frames
Supervisory frame (S-frame) Information frame (I-frame)
. ,
‘
nN
*<_ Basic L2CAP | -*
header
*s. Basic L2CAP | -*
16 | 16 16 / 32. 8 / 16 16 16
'
header '
TFCS is optional
20nly present in Start of L2CAP SDU
I-frame is one L2CAP PDU
74
```

## Slide 75

#### Exploit :: ERTM Channel :: I-frames

```
int__fastcalll2_reassemble_sdu(
intsar,prh_t_l2_channel *chan,host_buf *l2pdu)
{
switch(sar)
{
caseERTM_PDU_START:
ertm_pdu_len=*((uint16_t*)l2pdu->data +1);
ertm_pdu=host_buf_alloc(ertm_pdu_len);
chan->p_ertm_pdu=ertm_pdu;
ertm_pdu->len= ertm_pdu_len;
l2len =l2pdu->len-4-hdr_off;
memcpy(ertm_pdu->data,l2pdu->data +4, l2len);
chan->ertm_pdu_len=l2len;
```

```
caseERTM_PDU_CONTINUE:
```

```
l2len =l2pdu->len-2-hdr_off;
ertm_cur=&chan->p_ertm_pdu->data[chan->ertm_pdu_len];
memcpy(ertm_cur,l2pdu->data +2,l2len);
chan->ertm_pdu_len+=l2len;
}
return0;
}
```

75

## Slide 76

#### Exploit :: ERTM Channel :: I-frames

```
int__fastcalll2_reassemble_sdu(
intsar,prh_t_l2_channel *chan,host_buf *l2pdu)
{
switch(sar)
{
caseERTM_PDU_START:
ertm_pdu_len=*((uint16_t*)l2pdu->data +1);
ertm_pdu=host_buf_alloc(ertm_pdu_len);
chan->p_ertm_pdu=ertm_pdu;
ertm_pdu->len= ertm_pdu_len;
l2len =l2pdu->len-4-hdr_off;
memcpy(ertm_pdu->data,l2pdu->data +4, l2len);
chan->ertm_pdu_len=l2len;
caseERTM_PDU_CONTINUE:
l2len =l2pdu->len-2-hdr_off;
ertm_cur=&chan->p_ertm_pdu->data[chan->ertm_pdu_len];
memcpy(ertm_cur,l2pdu->data +2,l2len);
chan->ertm_pdu_len+=l2len;
}
return0;
}
```

76

## Slide 77

#### Exploit :: ERTM Channel :: I-frames

```
int__fastcalll2_reassemble_sdu(
intsar,prh_t_l2_channel *chan,host_buf *l2pdu)
{
switch(sar)
{
caseERTM_PDU_START:
ertm_pdu_len=*((uint16_t*)l2pdu->data +1);
ertm_pdu=host_buf_alloc(ertm_pdu_len);
chan->p_ertm_pdu=ertm_pdu;
ertm_pdu->len= ertm_pdu_len;
l2len =l2pdu->len-4-hdr_off;
memcpy(ertm_pdu->data,l2pdu->data +4, l2len);
chan->ertm_pdu_len=l2len;
caseERTM_PDU_CONTINUE:
l2len =l2pdu->len-2-hdr_off;
ertm_cur=&chan->p_ertm_pdu->data[chan->ertm_pdu_len];
memcpy(ertm_cur,l2pdu->data +2,l2len);
chan->ertm_pdu_len+=l2len;
}
return0;
}
```

77

## Slide 78

#### Exploit :: ERTM Channel :: I-frames

```
int__fastcalll2_reassemble_sdu(
intsar,prh_t_l2_channel *chan,host_buf *l2pdu)
{
switch(sar)
{
caseERTM_PDU_START:
ertm_pdu_len=*((uint16_t*)l2pdu->data +1);
ertm_pdu=host_buf_alloc(ertm_pdu_len);
chan->p_ertm_pdu=ertm_pdu;
ertm_pdu->len= ertm_pdu_len;
l2len =l2pdu->len-4-hdr_off;
```

```
memcpy(ertm_pdu->data,l2pdu->data +4, l2len);
chan->ertm_pdu_len=l2len;
```

```
caseERTM_PDU_CONTINUE:
```

```
l2len =l2pdu->len-2-hdr_off;
ertm_cur=&chan->p_ertm_pdu->data[chan->ertm_pdu_len];
memcpy(ertm_cur,l2pdu->data +2,l2len);
chan->ertm_pdu_len+=l2len;
```

```
}
return0;
}
```

78

## Slide 79

#### Exploit :: ERTM Channel :: I-frames

```
int__fastcalll2_reassemble_sdu(
intsar,prh_t_l2_channel *chan,host_buf *l2pdu)
{
switch(sar)
{
caseERTM_PDU_START:
ertm_pdu_len=*((uint16_t*)l2pdu->data +1);
ertm_pdu=host_buf_alloc(ertm_pdu_len);
chan->p_ertm_pdu=ertm_pdu;
ertm_pdu->len= ertm_pdu_len;
l2len =l2pdu->len-4-hdr_off;
memcpy(ertm_pdu->data,l2pdu->data +4, l2len);
chan->ertm_pdu_len=l2len;
caseERTM_PDU_CONTINUE:
l2len =l2pdu->len-2-hdr_off;
ertm_cur=&chan->p_ertm_pdu->data[chan->ertm_pdu_len];
memcpy(ertm_cur,l2pdu->data +2,l2len);
chan->ertm_pdu_len+=l2len;
```

```
}
return0;
}
```

79

## Slide 80

#### Exploit :: ERTM Channel :: I-frames

```
int__fastcalll2_reassemble_sdu(
intsar,prh_t_l2_channel *chan,host_buf *l2pdu)
{
switch(sar)
{
```

```
caseERTM_PDU_START:
ertm_pdu_len=*((uint16_t*)l2pdu->data +1);
ertm_pdu=host_buf_alloc(ertm_pdu_len);
chan->p_ertm_pdu=ertm_pdu;
ertm_pdu->len= ertm_pdu_len;
l2len =l2pdu->len-4-hdr_off;
memcpy(ertm_pdu->data,l2pdu->data +4, l2len);
chan->ertm_pdu_len=l2len;
```

```
caseERTM_PDU_CONTINUE:
```

```
l2len =l2pdu->len-2-hdr_off;
```

```
ertm_cur=&chan->p_ertm_pdu->data[chan->ertm_pdu_len];
memcpy(ertm_cur,l2pdu->data +2,l2len);
chan->ertm_pdu_len+=l2len;
```

```
}
```

```
return0;
```

```
}
```

80

## Slide 81

# ERTM Channel Universal Heap Spraying

81

## Slide 82

#### Exploit :: ERTM Channel :: I-frames :: Universal Spraying

There is no check if `p_ertm_pdu` is already assigned. Therefore, we can send `ERTM_L2CAP_SDU_START` to create as many elastic `host_buf` objects as we need

The minimal size of the elastic object is 0x24 bytes, there is no upper boundary

```
int__fastcalll2_reassemble_sdu(
intsar,prh_t_l2_channel *chan,host_buf *l2pdu)
{
switch(sar)
{
caseERTM_PDU_START:
ertm_pdu_len=*((uint16_t*)l2pdu->data +1);
ertm_pdu=host_buf_alloc(ertm_pdu_len);
chan->p_ertm_pdu=ertm_pdu;
ertm_pdu->len= ertm_pdu_len;
l2len =l2pdu->len-4-hdr_off;
memcpy(ertm_pdu->data,l2pdu->data +4, l2len);
chan->ertm_pdu_len=l2len;
caseERTM_PDU_CONTINUE:
```

```
l2len =l2pdu->len-2-hdr_off;
ertm_cur=&chan->p_ertm_pdu->data[chan->ertm_pdu_len];
memcpy(ertm_cur,l2pdu->data +2,l2len);
chan->ertm_pdu_len+=l2len;
```

```
}
return0;
}
```

82

## Slide 83

#### Exploit :: ERTM Channel :: I-frames :: Universal Spraying

83

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: ERTM Channel :: I-Frames :: Universal Spraying
-prh.t.12. channel
Universal Heap Spraying
83
```

## Slide 84

#### Exploit :: ERTM Channel :: I-frames :: Universal Spraying

● The spraying steps will be omitted in the talk

● However, the exploit heavily relies on the heap spraying

● A lot of steps require predictable free lists

_More details you will find in the upcoming whitepaper_

84

## Slide 85

# ERTM Channel AAW Primitive

85

## Slide 86

#### Exploit :: ERTM Channel :: I-frames :: AAW

```
int__fastcalll2_reassemble_sdu(
intsar,prh_t_l2_channel *chan,host_buf *l2pdu)
```

```
{
switch(sar)
{
```

What if we could control the content of `chan->p_ertm_pdu->data` ?

In that case, `ERTM_L2CAP_SDU_CONTINUE` might be used to write data under the controlled pointer.

```
caseERTM_PDU_START:
ertm_pdu_len=*((uint16_t*)l2pdu->data +1);
ertm_pdu=host_buf_alloc(ertm_pdu_len);
chan->p_ertm_pdu=ertm_pdu;
ertm_pdu->len= ertm_pdu_len;
l2len =l2pdu->len-4-hdr_off;
memcpy(ertm_pdu->data,l2pdu->data +4, l2len);
chan->ertm_pdu_len=l2len;
```

```
caseERTM_PDU_CONTINUE:
```

```
l2len =l2pdu->len-2-hdr_off;
```

```
ertm_cur=&chan->p_ertm_pdu->data[chan->ertm_pdu_len];
memcpy(ertm_cur,l2pdu->data +2,l2len);
chan->ertm_pdu_len+=l2len;
```

```
}
```

```
return0;
```

```
}
```

86

## Slide 87

#### Exploit :: ERTM Channel :: I-frames :: AAW

87

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: ERTM Channel :: Il-Frames :: AAW
AAW Primitive Strategy
1. Initial state of the ERTM L2CAP Channel 2. Allocate a new L2CAP SDU via ERTM_L2CAP_SDU_START
3. Overwrite data pointer within the host_buf object 4. TX ERTM_L2CAP_SDU_CONTINUE with the payload
i
87
```

## Slide 88

#### Exploit :: ERTM Channel :: Primitives

Using the ERTM channels we can obtain the following primitives:

- Universal Heap Spraying

- Arbitrary Address Write (AAW)

88

## Slide 89

#### Exploit :: ERTM Channel :: Primitives

Using the ERTM channels we can obtain the following primitives:

- Universal Heap Spraying

- Arbitrary Address Write (AAW)

However, ERTM Channels are not accessible prior to authentication.

89

## Slide 90

#### Exploit :: ERTM Channel :: Primitives

Using the ERTM channels we can obtain the following primitives:

● Universal Heap Spraying

- Arbitrary Address Write (AAW)

However, ERTM Channels are not accessible prior to authentication.

Let’s make our own ERTM channel via the Heap Overflow vulnerability!

90

## Slide 91

#### Exploit :: ERTM Channel :: Primitives :: Overview

91

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: ERTM Channel :: Primitives :: Overview
. Initial state after reallocating channel#1
cur_ sat eposh
2. Overflow link#1—cur_pos into channel#2 creating a new ERTM channel
cur_pos
91
```

## Slide 92

#### Exploit :: ERTM Channel :: Primitives :: Overview

92

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: ERTM Channel :: Primitives :: Overview
. Initial state after reallocating channel#1
cur_pos
2. Overflow link#1—cur_pos into channel#2 creating a new ERTM channel
cur_pos
emer eee ee ee ee ee eee ee ee ee ee ee ee ee ee ee ee ee ee eee eee,
3.1 channel#2 is used for Universal Heap Spraying ~>,
via link#2
—we a
wea |
see ee ee ee ee ee eee ee ee ee ee ee ee ee ee eee
92
```

## Slide 93

#### Exploit :: ERTM Channel :: Primitives :: Overview

93

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: ERTM Channel :: Primitives :: Overview
1. Initial state after reallocating channel#1
cur_pos
ay Overflow link#1—>cur_pos into channel#2 creating a new ERTM channel
a | pos
emer eee ee ee ee ee eee ee ee ee ee ee ee ee ee ee ee ee ee eee eee,
3.1 channel#2 is used for Universal Heap Spraying ~~. .’
via link#2
```

## Slide 94

# Address Leak

94

## Slide 95

#### Exploit :: Address Leak :: Reason

Alpine Bluetooth application doesn’t have PIE enabled, therefore we know executable section addresses

Just write into GOT / bss and do the magic?

95

## Slide 96

#### Exploit :: Address Leak :: Reason

Alpine Bluetooth application doesn’t have PIE enabled, therefore we know executable section addresses

Just write into GOT / bss and do the magic?

Well, yes and no

96

## Slide 97

#### Exploit :: Address Leak :: Reason

It’s possible to take the GOT overwrite approach, however:

- Hard to choose which entity to overwrite

- High possibility of crashes if GOT entity is hot

- Vendors tend to patch targets right before the Pwn2Own competition

   - PIE is an obvious target to patch

   - Very likely the exploit will be useless afterwards

97

## Slide 98

#### Exploit :: Address Leak :: Reason

It’s possible to take the GOT overwrite approach, however:

- Hard to choose which entity to overwrite

- High possibility of crashes if GOT entity is hot

- Vendors tend to patch targets right before the Pwn2Own competition

   - PIE is an obvious target to patch

   - Very likely the exploit will be useless afterwards

Presume that all security mitigations are enabled ASLR bypass is needed

98

## Slide 99

#### Exploit :: Address Leak :: Approach

The module of the Bluetooth stack that is about to be used for Virtual Memory Address (VMA) leak must satisfy the following requirements:

- Transmit responses to a remote device

- Accessible prior to authentication

- Preferably leak from the heap arena

99

## Slide 100

#### Exploit :: Address Leak :: Approach

The module of the Bluetooth stack that is about to be used for Virtual Memory Address (VMA) leak must satisfy the following requirements:

- Transmit responses to a remote device

- Accessible prior to authentication

- Preferably leak from the heap arena

L2CAP Echo Request / Response

100

## Slide 101

#### Exploit :: Address Leak :: L2CAP Echo Request

L2CAP Echo module works in the same manner as ping.

Data in Echo Request must be sent back to a remote device via Echo Response. L2CAP Signalling channel is used for communication.

101

## Slide 102

#### Exploit :: Address Leak :: L2CAP Echo Request

The content of `pdu_info->p_data` is sent to a remote device

Length of Echo Request must be lower than 0x100

```
caseL2CAP_ECHO_REQUEST:
length =pdu_info->length;
out_pdu_info.identifier=pdu_info->identifier;
if(length >0x100)
```

```
return0;
```

```
rsp_opcode=L2CAP_ECHO_RESPONSE;
out_pdu_info.p_data=pdu_info->p_data;
out_pdu_info.length=length;
```

```
// TX out_pdu_infoback to remote device
prh_l2_encode_packet(hci_handle,rsp_opcode,&out_pdu_info);
```

102

## Slide 103

#### Exploit :: Address Leak :: L2CAP Echo Request

103

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Address Leak :: L2CAP Echo Request
Echo Request
Use heap overflow
This data will be sent back
to an attacker which might
contain addresses
Echo Request
103
```

## Slide 104

#### Exploit :: Address Leak :: L2CAP Echo Request :: Issues

- How can we modify the content of an Echo Request before it’s processed by the shown routine?

- How can we overwrite a specific member in the middle of a structure?

104

## Slide 105

#### Exploit :: Address Leak :: L2CAP Echo Request :: Solution 1

- The lifetime of an Echo Request heap chunk can be controlled by L2CAP fragmentation

- L2CAP PDU will not be sent to an upper-layer until the complete PDU is reassembled from HCI ACL fragments

- Keeping the Echo Request PDU incomplete is required to modify its content via heap overflow

- When all the needed modifications are done, Echo Request can be completed and sent to the processing routine

105

## Slide 106

#### Exploit :: Address Leak :: L2CAP Echo Request

How can we overwrite a specific member in the middle of a structure?

106

## Slide 107

#### Exploit :: Address Leak :: L2CAP Echo Request :: Solution 2

107

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Address Leak :: L2CAP Echo Request :: Solution 2
1. Initial state after converting channel#2 into ERTM
channel#2
L2CAP PDU : ERTM
+ channel#3  : channel#4
cur_pos
link#1
107
```

## Slide 108

#### Exploit :: Address Leak :: L2CAP Echo Request :: Solution 2

108

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Address Leak :: L2CAP Echo Request :: Solution 2
1. Initial state after converting channel#2 into ERTM
: channel#2
ERTM
cur_pos
L2CAP PDU + channel#3  : channel#4
link#1
2. Overflow to place cur_pos at the target position
: channel#2
ERTM
cur_pos
L2CAP PDU : channel#3  : channel#4
link#1
108
```

## Slide 109

#### Exploit :: Address Leak :: L2CAP Echo Request :: Solution 2

109

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Address Leak :: L2CAP Echo Request :: Solution 2
1. Initial state after converting channel#2 into ERTM
cur_pos
2. Overflow to place cur_pos at the target position
cur_pos
3. Disconnect channel#3 to free the heap chunk
_
cur_pos
unsortedbin
109
```

## Slide 110

#### Exploit :: Address Leak :: L2CAP Echo Request :: Solution 2

110

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Address Leak :: L2CAP Echo Request :: Solution 2
. Initial state after converting channel#2 into ERTM
cur_pos
2. Overflow to place cur_pos at the target position
cur_pos
3. Disconnect channel#3 to free the heap chunk
Be ie ee
sin
cur_pos
unsortedbin
4, Allocate an Echo Request which is smaller than channel#3
cur_pos
=
> ngortedbin
remainder
110
```

## Slide 111

#### Exploit :: Address Leak :: L2CAP Echo Request :: Solution 2

111

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Address Leak :: L2CAP Echo Request :: Solution 2
. Initial state after converting channel#2 into ERTM
cur_pos
2. Overflow to place cur_pos at the target position
cur_pos
3. Disconnect channel#3 to free the heap chunk
Be ie ee
sin
cur_pos
unsortedbin
4, Allocate an Echo Request which is smaller than channel#3
cur_pos
ean
remainder
5. Overwrite the target structure member (Echo Request length)
‘ase: RR co YE amon
cur_pos
unsortedbin
remainder
111
```

## Slide 112

#### Exploit :: Address Leak :: L2CAP Echo Request :: Leak

```
41 41 41 41 41 41 41 41  41 41 41 41 41 41 41 41
41 41 41 41 41 41 41 41  41 41 41 41 41 41 41 41
41 41 41 41 41 41 41 41  41 41 41 41 41 41 41 41
41 41 41 41 41 41 41 41  41 41 41 41 41 41 41 41
41 41 41 41 41 41 41 41  00 00 00 00 21 00 00 00
```

- `58 00 f0 af 58 00 f0 af 00 00 00 00 00 00 00 00`

- `00 00 00 00 00 00 00 00  20 00 00 00 1c 00 00 00`

- `00 00 00 00 80 00 00 00  00 00 00 00 00 00 00 00 00 00 00 00 59 00 00 00  90 00 f0 af 90 00 f0 af`

- `01 00 f0 ff 00 00 ff ff 30 00 00 01 30 00 00 01 ff ff 00 00 00 00 00 00  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00`

```
00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00
00 00 00 00 07 00 00 00  58 00 00 00 14 00 00 00
00 00 00 00 58 ebf0 af00 00 00 00 9d 00 00 00
```

```
00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00
00 00 f0 af
```

112

## Slide 113

#### Exploit :: Address Leak :: L2CAP Echo Request :: Leak

```
41 41 41 41 41 41 41 41  41 41 41 41 41 41 41 41
41 41 41 41 41 41 41 41  41 41 41 41 41 41 41 41
41 41 41 41 41 41 41 41  41 41 41 41 41 41 41 41
41 41 41 41 41 41 41 41  41 41 41 41 41 41 41 41
remainder->fd
41 41 41 41 41 41 41 41  00 00 00 00 21 00 00 00
58 00 f0 af58 00 f0 af00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00  20 00 00 00 1c 00 00 00
remainder->bk
00 00 00 00 80 00 00 00  00 00 00 00 00 00 00 00
00 00 00 00 59 00 00 00  90 00 f0 af90 00 f0 af
01 00 f0 ff 00 00 ff ff30 00 00 01 30 00 00 01
ff ff00 00 00 00 00 00  00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00
thread heap arena00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00
=
addr >> 20 << 2000 00 00 00 07 00 00 00  58 00 00 00 14 00 00 00
00 00 00 00 58 ebf0 af00 00 00 00 9d 00 00 00
00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00
00 00 f0 af
```

```
Heap chunk flags
```

113

## Slide 114

#### Exploit :: Mid-game

What do we have so far?

- Universal Heap Spraying

- Arbitrary Address Write (AAW)

- VMA of the current heap arena

- Heap chunk flags ( _will be needed further_ )

114

## Slide 115

#### Exploit :: Mid-game

What do we have so far?

- Universal Heap Spraying

- Arbitrary Address Write (AAW)

- VMA of the current heap arena

- Heap chunk flags ( _will be needed further_ )

Goal: Write a ROP-chain into the stack of “BT thread”

- No address of a `system` function

- No address of “BT thread” `stack`

115

## Slide 116

#### Exploit :: Mid-game

What do we have so far?

- Universal Heap Spraying

- Arbitrary Address Write (AAW)

- VMA of the current heap arena

- Heap chunk flags ( _will be needed further_ )

Goal: Write a ROP-chain into the stack of “BT thread”

● No address of a `system` function Arbitrary Address Read (AAR) ● No address of “BT thread” `stack` is needed

116

## Slide 117

## AAR Primitive

117

## Slide 118

#### Exploit :: AAR Primitive

We could use Echo Request for this (tamper `pdu->data` ), however:

● One leak per L2CAP Channel

- Run out of available L2CAP Channels

- L2CAP Channels allocation outside the current heap arena

118

## Slide 119

#### Exploit :: AAR Primitive

We could use Echo Request for this (tamper `pdu->data` ), however:

- One leak per L2CAP Channel

- Run out of available L2CAP Channels

- L2CAP Channels allocation outside the current heap arena

Solution: Use ERTM Channels again!

119

## Slide 120

#### Exploit :: ERTM Channel :: AAR

● S-frame REJ - used to request retransmission of I-frames

```
intl2_fcrt_rx_rej(prh_t_l2_channel *chan,
prh_t_ertm_seq*seq){
```

```
next_tx_seq=chan->next_tx_seq;
if(next_tx_seq!=seq->reqseq){
l2_fcrt_act_rx_reqseq(chan,seq);
if(seq->f_bit){
...
}else{
l2_fcrt_ertm_resend_all(chan);
...
}
return0;
}
```

```
}
```

```
intl2_fcrt_ertm_resend_all(prh_t_l2_channel *chan){
for(fcrt=chan->fcrt_data_list;fcrt;fcrt=fcrt->next)
```

```
{
sdu_data=fcrt->sdu_data;
sdu_len=fcrt->sdu_len;
rsp_len=sdu_len-4;
err =prh_l2_GetWriteBuffer(local_cid,rsp_len,0,&rsp);
if(!err ){
rsp->len=rsp_len;
memcpy(rsp->data,sdu_data+4,rsp_len);
prh_l2_sar_data_req(0,chan->local_cid,rsp);
```

```
}
```

```
}
}
```

120

## Slide 121

#### Exploit :: ERTM Channel :: AAR

##### ● S-frame REJ - used to request retransmission of I-frames

```
intl2_fcrt_rx_rej(prh_t_l2_channel *chan, intl2_fcrt_ertm_resend_all(prh_t_l2_channel *chan){
prh_t_ertm_seq*seq){for(fcrt=chan->fcrt_data_list;fcrt;fcrt=fcrt->next)
next_tx_seq=chan->next_tx_seq;{
if(next_tx_seq!=seq->reqseq){sdu_data=fcrt->sdu_data;
l2_fcrt_act_rx_reqseq(chan,seq);sdu_len=fcrt->sdu_len;
if(seq->f_bit){rsp_len=sdu_len-4;
...err =prh_l2_GetWriteBuffer(local_cid,rsp_len,0,&rsp);
}else{if(!err ){
l2_fcrt_ertm_resend_all(chan);rsp->len=rsp_len;
...memcpy(rsp->data,sdu_data+4,rsp_len);
}prh_l2_sar_data_req(0,chan->local_cid,rsp);
return0;}
}}
}}
```

121

## Slide 122

#### Exploit :: ERTM Channel :: AAR

122

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: ERTM Channel :: AAR
S-Frame REJ will trigger
transmitting these SDUs
to a remote device
122
```

## Slide 123

#### Exploit :: ERTM Channel :: AAR

123

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: ERTM Channel :: AAR
NULL
S-Frame REJ will trigger
transmitting these SDUs
to a remote device
123
```

## Slide 124

#### Exploit :: ERTM Channel :: AAR :: Overview

124

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: ERTM Channel :: AAR :: Overview
1. Initial state after heap arena address leak
- channel#2 =. . 5
L2CAP PDU : ERTM (AAW) ° Echo S : channel#4 ;
cur_pos A
"
link#1
124
```

## Slide 125

#### Exploit :: ERTM Channel :: AAR :: Overview

125

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Expiot :; ERTM Channel :: AAR :: Overview
. Initial state after heap arena address leak 2. Make channel#4 an ERTM channel with tampered fert_data_list
cur_pos cur_pos
Ena = f Memory within the a arena
125
```

## Slide 126

#### Exploit :: ERTM Channel :: AAR :: Overview

126

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Expiot :; ERTM Channel :: AAR :: Overview
. Initial state after heap arena address leak 2. Make channel#4 an ERTM channel with tampered fert_data_list
cur_pos Ei cur_pos
= = a Memory within the a arena
3. Use AAW to initialize the target region with zeros
cur_pos
een f Memory within = heap arena
126
```

## Slide 127

#### Exploit :: ERTM Channel :: AAR :: Overview

127

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Expiot :; ERTM Channel :: AAR :: Overview
. Initial state after heap arena address leak
cur_pos ‘Ei
2. Make channel#4 an ERTM channel with tampered fert_data_list
cur_pos
= a Memory within the a arena
3. Use AAW to initialize the target region with zeros
cur_pos
een af Memory within = heap arena
4. Use AAW to write fcrt_node and TX S-frame REJ to leak it
cur_pos
= iC Memory within = heap arena
S-frame REJ response
127
```

## Slide 128

#### Exploit :: ERTM Channel :: AAR :: Overview

128

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Expiot :;} ERTM Channel ::
. Initial state after heap arena address leak
cur_pos i
AAR :: Overview
2. Make channel#4 an ERTM channel with tampered fert_data_list
cur_pos
= a Memory within the a arena
3. Use AAW to initialize the target region with zeros
ee
cur_pos
een Memory within the heap arena
4. Use AAW to write fcrt_node and TX S-frame REJ to leak it
ee
cur_pos
pen] Memory within the heap arena
S-frame REJ response
5. Use AAW to write next fert_node and TX S-frame REJ to leak
cur_pos
= sf Memory within = heap arena
toreroue force [I
ate ote ae
S-frame REJ response
128
```

## Slide 129

#### Exploit :: ERTM Channel :: AAR :: Overview

129

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Expiot :;} ERTM Channel ::
. Initial state after heap arena address leak
cur_pos i
AAR :: Overview
2. Make channel#4 an ERTM channel with tampered fert_data_list
cur_pos
= a Memory within the a arena
3. Use AAW to initialize the target region with zeros
ee
cur_pos
een Memory within the heap arena
4. Use AAW to write fcrt_node and TX S-frame REJ to leak it
ee
cur_pos
pen] Memory within the heap arena
S-frame REJ response
5. Use AAW to write next fert_node and TX S-frame REJ to leak
cur_pos
= sf Memory within = heap arena
fort-nose
ate ote ae
S-frame REJ response
6. Use AAW to write next fcrt_node and TX S-frame REJ to leak
cur_pos
= Jf Memory within = heap arena
——
[aa < 129
S-frame REJ response
```

## Slide 130

## AAR :: Libc Address

130

## Slide 131

#### Exploit :: AAR Primitive :: Libc Address

- Every generic heap arena begins with:

   - `struct heap_arena` – arena control information, contains pointer to `malloc_state`

   - ○ `struct malloc_state` – heap control information, contains free list bins

   - Linked together via `malloc_state`

- Main arena is an exception

   - First arena for every application

   - No `struct heap_arena` object

   - `struct malloc_state` is located in libc.so

131

## Slide 132

#### Exploit :: AAR Primitive :: Libc Address

132

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: AAR Primitive :: :: Libc Address
we wee we we we ew ee ee ee ee ee ee ee ew ee ee ee ee ee ee ee ee ee eee ee ee ew
Heap segment
‘Nain Heap (siscated (GE RFE siossted
Arena | §
ee
Se Ie Threadit1 Thread#2 Thread#3
Heap Arena Heap Arena Heap Arena
Main Arena
132
```

## Slide 133

#### Exploit :: AAR Primitive :: Libc Address

133

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: AAR Primitive :: :: Libc Address
wee ew we we ew ee ee ee ee ee ee ee ee ee ee ee ee ew ee ee ee ee ee ee eee ew
Heap segment
Arena | §
---------- eee ee ee ee ee ee eee ee ee ee ee ee ee ee ee ee eee - -?”
Libe segment ; Thread#1 /  Thread#2 | Threadi#3
Main Arena Heap Arena Heap Arena Heap Arena
BT thread heap arena J
address is known
133
```

## Slide 134

#### Exploit :: AAR Primitive :: Libc Address

- BT thread heap arena address is previously leaked

- Use AAR to iterate over `malloc_state` objects and find the main arena

- Use 12 LSB of `malloc_state::next` to identify the main arena

   - `[slave ] thr_arenas[00]: 0xaff00010 [slave ] thr_arenas[01]: 0xafe00010 [slave ] thr_arenas[02]: 0xb0000010 [slave ] thr_arenas[03]: 0` `xb54d47b4` `[slave ] libc base found: 0` `xb53a2000`

134

## Slide 135

## AAR :: Thread Stack Address

135

## Slide 136

#### Exploit :: AAR Primitive :: Thread Stack Address

- libpthread.so contains API of creating new threads in Unix-like OS

- Thread Control Block (TCB) is in the end of a pthread’s stack

- TCBs are linked together:

   - Doubly-linked list

   - `__stack_user` is the list’s head located in libpthread.so

136

## Slide 137

#### Exploit :: AAR Primitive :: Thread Stack Address :: VMap

137

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: AAR Primitive :: Thread Stack Address :: VMap
_ Expected V vera Map - Observed eee Map
random offset (page aligned)
random offset (page aligned)
\ a
i 2 .
i
v
random offset (page aligned)
137
```

## Slide 138

#### Exploit :: AAR Primitive :: Thread Stack Address :: VMap

138

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: AAR Primitive :: Thread Stack Address :: VMap
Expected Virtual Map Observed Virtual Map
random offset (page aligned)
random offset (page aligned)
random offset (page aligned)
138
```

## Slide 139

#### Exploit :: AAR Primitive :: Thread Stack Address

139

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: AAR Primitive :: Thread Stack Address
libpthread
139
```

## Slide 140

#### Exploit :: AAR Primitive :: Thread Stack Address

140

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: AAR Primitive :: Thread Stack Address
libpthread VMA
address is known
140
```

## Slide 141

#### Exploit :: AAR Primitive :: Thread Stack Address

- `libpthread.so` address was leaked based on `libc.so`

- Use AAR to iterate over `pthread` TCB objects starting from `__stack_user`

- Use 12 LSB of `start_routine` to find BT thread TCB

|`[slave`|`]`
`pthread[00]: `|`0xa3d3d440`|
|---|---|---|
|`[slave`|`]`
`pthread[01]: `|`0xa453d440`|
|`[slave`|`]`
`pthread[02]: `|`0xa4d3d440`|
|`[slave`|`]`
`pthread[03]: `|`0xa553d440`|
|`[slave`|`]`
`pthread[04]: `|`0xa5d3d440`|
|`[slave`|`]`
`pthread[05]: `|`0xa653d440`|
|`[slave`|`]`
`pthread[06]: `|`0xa6d3d440`|
|`[slave`|`]`
`pthread[07]: `|`0xa753d440`|
|`[slave`|`]`
`pthread[08]: `|`0xa7d3d440`|
|`[slave`|`]`
`pthread[09]: `|`0xa853d440`|
|`[slave`|`]`
`pthread[10]: `|`0xa8d4f440`|
|`[slave`|`]`
`pthread[11]: `|`0xa954f440`|
|`[slave`|`]`
`pthread[12]: `|`0xa9d92440`|
|`[slave`|`]`
`pthread[13]: `|`0xaa592440`|
|`[slave`|`] found BT thread`|`stack address:0xaa592440`|

141

## Slide 142

#### Exploit :: End-game

What do we have so far?

- Universal Heap Spraying

- Arbitrary Address Write (AAW)

- Arbitrary Address Read (AAR)

- Heap chunk flags ( _will be needed further_ )

- Address of a `system` function

- Address of “BT thread” `stack`

142

## Slide 143

#### Exploit :: End-game

What do we have so far?

- Universal Heap Spraying

- Arbitrary Address Write (AAW)

- Arbitrary Address Read (AAR)

- Heap chunk flags ( _will be needed further_ )

- Address of a `system` function

Write a ROP-chain to BT thread stack executing `system(payload)`

- Address of “BT thread” `stack`

143

## Slide 144

#### Exploit :: End-game

144

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: End-game
2. @-click Bluetooth exploit
ie
3. Force wpa_supplicant to
1. Setup WLAN connect to an attacker's AP ]
Access Point co
4. Run reverse shell as root
144
```

## Slide 145

#### Exploit :: End-game

```
[slave ] step 40: send ERTM Continue to channel#2
```

```
[slave ] step 41: execute the ROP chain
+++++ grandefinale +++++
```

```
Waiting for the server to connect...connected.
sh: can't access tty; job control turned off
root@neusoft-tcc8034:/# id
uid=0(root) gid=0(root)
root@neusoft-tcc8034:/# uname-a
Linux neusoft-tcc8034 4.14.137-tcc #1 SMP PREEMPT Thu Nov 9 06:48:03 UTC 2023 armv7l
GNU/Linux
root@neusoft-tcc8034:/#
```

145

## Slide 146

#### Exploit :: End-game

```
[slave ] step 40: send ERTM Continue to channel#2
```

```
[slave ] step 41: execute the ROP chain
+++++ grandefinale +++++
```

```
Waiting for the server to connect...connected.
sh: can't access tty; job control turned off
root@neusoft-tcc8034:/# id
uid=0(root) gid=0(root)
root@neusoft-tcc8034:/# uname-a
```

```
Linux neusoft-tcc8034 4.14.137-tcc #1 SMP PREEMPT Thu Nov 9 06:48:03 UTC 2023 armv7l
GNU/Linux
root@neusoft-tcc8034:/#
```

Still a lot of crashes. Stability is ~60%

146

## Slide 147

## Exploit Stability Improvements

147

## Slide 148

#### Exploit :: Stability :: Why?

Why to improve stability?

- At Pwn2Own you have 3 attempts

- 10 min each of them

60%

- 60% looks good but not perfect

- A challenge for myself

60%

148

## Slide 149

#### Exploit :: Stability :: Issues

- Major issues (frequent crashes):

   - Allocations instability within the heap arena

   - Unexpected heap crashes with strange traces

   - Crash after the ROP chain transmission (final step)

- Minor issues (~rare crashes):

   - Instability of initial L2CAP channels spraying

   - Problem with HCI Link Connection RTX timers

   - ERTM Channels spraying problems

   -

- …

149

## Slide 150

#### Exploit :: Stability :: Issues

- Major issues (frequent crashes):

   - Allocations instability within the heap arena

   - Unexpected heap crashes with strange traces

   - Crash after the ROP chain transmission (final step)

- Minor issues (~rare crashes):

   - Instability of initial L2CAP channels spraying

   - Problem with HCI Link Connection RTX timers

   - ERTM Channels spraying problems

   -

- …

150

## Slide 151

#### Exploit :: Stability :: Issue #1

<u>Allocations instability within the heap arena</u>

Problem:

- For every Rx ACL fragment, a new chunk is allocated

● If a large ACL fragment is sent, target bins might be used

151

## Slide 152

#### Exploit :: Stability :: Issue #1

<u>Allocations instability within the heap arena</u>

Problem:

- For every Rx ACL fragment, a new chunk is allocated

- If a large ACL fragment is sent, target bins might be used

Solution:

- Utilize L2CAP PDU fragmentation

- Max length of Tx ACL fragments is 0x10 bytes

- The same fastbin is used for every Rx ACL

152

## Slide 153

Exploit :: Stability :: Issue #1

153

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Stability :: Issue #1
host_buf elastic object is
used to store HCI ACL data
86x18 + 8x24 = 8x34
Transmit data
ae T 1S
8x48 bytes
8x18 bytes 8x18 bytes 8x18 bytes 8x18 bytes
1
2
3
4
. ACL fragment is allocated
. ACL data is copied into L2CAP PDU
. Allocated chunk is freed
. Repeat 1 for a new ACL fragment
153
```

## Slide 154

#### Exploit :: Stability :: Issue #2

<u>Unexpected heap crashes with strange traces</u>

Problem:

- Crash in `free` API function

- Analysis revealed – problem with heap chunk flags

- Allocations happen in main heap arena instead of thread heap arena

154

## Slide 155

#### Exploit :: Stability :: Issue #2

155

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: stability : Issue #2
Heap segment
| “ce —————
* Libe segment *
Main Arena
155
```

## Slide 156

#### Exploit :: Stability :: Issue #2

156

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: stability : Issue #2
Heap segment
‘Mein HOP socates ae Fed) olscates
Arena | §
, Libe segment - Thread#1
Heap Arena
N
re a
1 '
1 1
1 '
Main Arena
pthread
XY
4 Thread
156
```

## Slide 157

#### Exploit :: Stability :: Issue #2

157

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Stability :: Issue #2
‘Mein HOP socates ae Fed) olscates
Arena | §
ob 55565655555555556556555 5555555655555 55555e555555"
.
Libe segment ; Thread#1 Thread#2
Heap Arena Heap Arena
y,
.
1 1
1 '
1 1
Main Arena
S
Thread
157
```

## Slide 158

#### Exploit :: Stability :: Issue #2

158

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Stability Issue #2
Heap segment
‘Mein HOP socates ae Fed) olscates
Arena | §
"Vibe seamen co ‘ Heap Arenas limit '
(BOG segment Thread#1 Threadi#2 Thread#3 ' reached: NCORES * 2 |
Main Arena Heap Arena Heap Arena Heap Arena (for 32-bit systems) |
ae
XY
SY Thread L pthread L pthread
158
```

## Slide 159

#### Exploit :: Stability :: Issue #2

159

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Stability :: Issue #2
Heap segment
‘Mein HOP socates ae Fed) olscates
Arena | §
"Vibe seamen co ‘ Heap Arenas limit '
(BOG segment Thread#1 Threadi#2 Thread#3 ' reached: NCORES * 2 |
Main Arena Heap Arena Heap Arena Heap Arena (for 32-bit systems) |
SY Thread L pthread L pthread L pthread
189)
```

## Slide 160

#### Exploit :: Stability :: Issue #2

<u>Unexpected heap crashes with strange traces</u>

Problem:

- Crash in `free` API function

- Analysis revealed – problem with heap chunk flags

- Allocations happen in main heap arena instead of thread heap arena

Solution:

- Use Heap chunk flags to understand which arena is used: A flag (0x4)

- Tune the exploit based on this information

- No more problems with `free`

160

## Slide 161

#### Exploit :: Stability :: Issue #3

<u>Crash after the ROP chain transmission (final step)</u>

Problem:

- ROP-chain is quite large – due to `ret` sled and `system` payload

- Unsegmented L2CAP PDU

- fastbin consolidation happens

- Some fastbin chunks are corrupted => application crashes

161

## Slide 162

#### Exploit :: Stability :: Issue #3

<u>Crash after the ROP chain transmission (final step)</u>

Problem:

- ROP-chain is quite large – due to `ret` sled and `system` payload

- Unsegmented L2CAP PDU

- fastbin consolidation happens

- Some fastbin chunks are corrupted => application crashes

Solution:

- Put the payload out of stack using AAW

● Bypass fastbin consolidations

162

## Slide 163

#### Exploit :: Stability :: Result

### 96% stability

163

## Slide 164

#### Exploit :: Stability

68%
60%
96%
84%
76%
A slavic meme

164

## Slide 165

#### Exploit :: Demonstration

165

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: Demonstration
konata@akatsu Jie sudo ./run_dev. sh] konata@akatsu > ~/dev/tools/tsh/tsh.alpine cbf]
```

## Slide 166

## PWN Results

166

## Slide 167

#### Results

##### ● 0-click Bluetooth Remote Use-After-Free

167

## Slide 168

#### Results

- 0-click Bluetooth Remote Use-After-Free

- Converted it into AAW / AAR / Universal Heap Spraying

168

## Slide 169

#### Results

- 0-click Bluetooth Remote Use-After-Free

- Converted it into AAW / AAR / Universal Heap Spraying

- Bypassed all the possible mitigations _Which might be enabled by the vendor before Pwn2Own_

169

## Slide 170

#### Results

- 0-click Bluetooth Remote Use-After-Free

- Converted it into AAW / AAR / Universal Heap Spraying

- Bypassed all the possible mitigations

_Which might be enabled by the vendor before Pwn2Own_

- Got root reverse shell on top of TCP/IP

170

## Slide 171

#### Results

- 0-click Bluetooth Remote Use-After-Free

- Converted it into AAW / AAR / Universal Heap Spraying

- Bypassed all the possible mitigations

   - _Which might be enabled by the vendor before Pwn2Own_

- Got root reverse shell on top of TCP/IP

- 96% stability

171

## Slide 172

#### Results

- 0-click Bluetooth Remote Use-After-Free

- Converted it into AAW / AAR / Universal Heap Spraying

- ● Bypassed all the possible mitigations _Which might be enabled by the vendor before Pwn2Own_

- ● Got root reverse shell on top of TCP/IP

- 96% stability

- Went to a psychotherapist

172

## Slide 173

## Impact and Implications

173

## Slide 174

#### RCE Impact

##### 0-click RCE leads to:

174

## Slide 175

#### RCE Impact

- 0-click RCE leads to:

- Deface – Faking the display image ○ Show arbitrary images

   - Ability to implement touch actions

   - ○ Run Doom! (by NCC Group EDG)

175

## Slide 176

#### RCE Impact

0-click RCE leads to:

- Deface – Faking the display image

- Stealing phone book information

176

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
RCE Impact
0-click RCE leads to:
e Deface — Faking the display image
e Stealing phone book information
co | ,
« | Recent Call Geena) |) x « | phone Bale
Back Mi Phone Download Delete Close ) Ben, Mi
N q } _—
2, YY Unknown -— Pozaio7me/8:54 | 2) CEO
wy Unknown 2024/07/16/18:54 Gumon Oo +36123456789
i, y Unknown ’ 2024/07/15/19:05 :
® Y *300, 2024/07/15/15:57
ashe Y +36 2023/05/15/16:49
a *D +25 2023/03/11/17:03 | ¥
176
```

## Slide 177

#### RCE Impact

- 0-click RCE leads to:

- Deface – Faking the display image

- Stealing phone book information

- Eavesdropping on an external microphone

177

## Slide 178

#### RCE Impact

- 0-click RCE leads to:

- Deface – Faking the display image

- Stealing phone book information

- Eavesdropping on an external microphone

- GPS coordinates (?)

178

## Slide 179

#### RCE Impact

- 0-click RCE leads to:

- Deface – Faking the display image

- Stealing phone book information

- Eavesdropping on an external microphone

- GPS coordinates (?)

- Listening to bluetooth data

   - Audio streaming

179

## Slide 180

#### RCE Implications

● Attacking a user’s phone connected via CarPlay / Android Auto / etc ● Attacking a CAN bus if an external adapter is connected

180

## Slide 181

## Pwn2Own Results And Timeline

181

## Slide 182

#### Pwn2Own :: Timeline

182

## Slide 183

#### Pwn2Own :: Results

- Vulnerability is reported to Alpine, thanks to ZDI

- Alpine conducted a Threat Assessment and Remediation Analysis

- Alpine states that they will continue to use the current software

183

## Slide 184

#### Pwn2Own :: Kudos

- <u>Danila Parnishchev</u>

   - Managing Pwn2Own preparations

- <u>Polina Smirnova</u>

   - Hardware-related activities

- <u>Radu Mostpan</u>

   - Help with Alpine update file decryption

   - Exploiting another target

184

## Slide 185

## Conclusion

185

## Slide 186

#### Conclusion

- Bluetooth is cool attack surface

   - Especially in IoT world

- Remote UAF is doable

- Was very fun

- Personal thoughts:

   - First experience of Pwn2Own

   - Unfortunately, only one real car was presented (Tesla)

   - ○ Pretty stressful

   - Cool opportunity to see people and places

186

## Slide 187

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Thank you for your attention
Q&A?
184
```

## Slide 188

## Thank you for your attention Q&A?

Twitter: konatabrk

188

## Slide 189

#### Exploit :: AAR Primitive

Solution: Use ERTM Channels again!

189

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Exploit :: AAR Primitive
SILENCE, other modules
Solution: Use ERTM Channels again!
An ERTM channel is speaking
189
```
