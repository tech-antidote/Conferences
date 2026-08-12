---
title: "When The Front Door Becomes a Backdoor The Security Paradox of OSDP"
speakers: ["Eran Jacob", "Ariel Harush", "Roy Hodir"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Eran Jacob, Ariel Harush, Roy Hodir_When The Front Door Becomes a Backdoor The Security Paradox of OSDP.pdf"
pages: 107
sha256: "6f2f97b6c1fa0d930df2729a45c67e3c889cb69087bccb4d9681d4682576897d"
text_chars: 27685
ocr_pages: 11
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.2
ocr_unreliable_blocks: 0
vision_verified_blocks: 3
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:03:05Z"
---
# When The Front Door Becomes a Backdoor The Security Paradox of OSDP

**Speakers:** Eran Jacob, Ariel Harush, Roy Hodir  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Eran Jacob, Ariel Harush, Roy Hodir_When The Front Door Becomes a Backdoor The Security Paradox of OSDP.pdf` (107 pages)


## Slide 1

**When The Front Door Becomes a Backdoor: The Security Paradox of OSDP Eran Jacob** , Head of Research **Ariel Harush** , Security Researcher **Roy Hodir** , Security Researcher

## Slide 2

## **About us**

Eran Jacob Ariel Harush Roy Hodir Head of Research Security Researcher Security Researcher _/in/eranj_ /in/arielhar _/in/roy-h-858b69_

## Slide 3

**Physical Access Controls Systems (PACS)**


> Recovered by OCR — confidence 88/100 on the text kept, 56/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Physical Access Controls Systems (PACS)
7
aa" 7
```

## Slide 4

## **Agenda**

**1. Quick overview** Physical Access Controls & OSDP

**2. Bypassing modern Physical Access Controls** Targeting fully secured OSDP setups

**3. Attacking OSDP implementations** Gaining foothold in the IP network - over a serial channel

## Slide 5

## **PACS Architecture**

Open/Close
IP Network
Serial Communication
TCP/IP Security server
OSDP / Wiegand
TCP/IP
Administrator
Open/Close

## Slide 6

## **PACS Architecture**

Open/Close
IP Network
Serial Communication
TCP/IP Security server
OSDP / Wiegand
TCP/IP
Administrator
Open/Close

## Slide 7

## **PACS Architecture**

Open
IP Network
Serial Communication
TCP/IP Security server
OSDP / Wiegand
TCP/IP
Administrator
Open/Close

## Slide 8

**Attacking PACS**


> Recovered by OCR — confidence 96/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Attacking PACS
ly Attacks
```

## Slide 9

### **Attacking Modern Reader <–> Controller Communication**

Open/Close
Serial Communication
OSDP / Wiegand
Open/Close

## Slide 10

## **Reader – Controller Communication**

#### **Wiegand**

- **The dominant protocol and physical layer**

- **Limited capabilities:** unidirectional, limited transfer rates

- **Insecure** : easy to eavesdrop and perform replay attacks

## Slide 11

## **Reader – Controller Communication**

**_Open Supervised Device Protocol_**

•

•

•

**Increasingly deployed, RS-485 physical layer Extended capabilities** bi-directional, increased transfer rates

**Security:** <u>option</u> for secure channel with encryption and data integrity

## Slide 12

## **Attacking OSDP!**

Open/Close
IP Network
Wireless
Serial Communication
MIFARE
DESFIRE
TCP/IP
…
Security server
RS485
TCP/IP
Administrator
Open/Close

## Slide 13

## **1. Bypassing access control**

Open/Close
IP Network
Wireless
Serial Communication
MIFARE
DESFIRE
TCP/IP
…
Security server
RS485
TCP/IP
Open Administrator

## Slide 14

## **2. Attacking OSDP – Breaching the internal network**

Open/Close
IP Network
Wireless
Serial Communication
MIFARE
DESFIRE
TCP/IP
…
Security server
RS485
TCP/IP
Administrator
Open/Close

## Slide 15

## **2. Attacking OSDP – Breaching the internal network**

Open/Close
IP Network
Wireless
Serial Communication
MIFARE
DESFIRE
TCP/IP
…
Security server
RS485
TCP/IP
Administrator
Open/Close
Serial to E TH(!)

## Slide 16

**1. Bypassing Access Control!**

***On properly configured and fully secured environments**

## Slide 17

## **Our (research) setup**

Open/Close
IP Network
Serial Communication
Management PC
WEB
INTERFACE
Red teaming
€9 €9
RS485
RS485

## Slide 18

## **Our (research) setup**

Serial Communication
€9
Virtual
Controller
(libOSDP)
RS485

## Slide 19

## **Connecting to the reader**

RS485

## Slide 20

## **Connecting to the reader**

RS485

## Slide 21

**Tamper protection?**

## Slide 22

## **Tamper protection?**

Reader case is
close

Tamper
Protection
RS485

## Slide 23

## **Tamper protection?**

Reader case is
open!

Tamper
Protection
RS485

## Slide 24

**Tamper protection - Testing**

## Slide 25

**Bypassing tamper protection!**

## Slide 26

**Bypassing tamper protection!**

## Slide 27

**Tamper protection..**

**Still highly recommended..**

**Tamper protection – NOT ENOUGH!**

## Slide 28

## **Understanding OSDP**

###### Peripheral Device (PD)

**_<u>PD</u>_**

**_Command: …_**

**_Reply: …_**

###### Control Panel (CP)

**_<u>CP</u>_**

**_Command: …_**

**_Reply: … Command: Poll_**

**_Reply: Ack_**

## Slide 29

## **Understanding OSDP - Secure Channel**

**Shared secret: Secure Channel Base Key**

**SCBK**

_<u>PD</u>_

**_Secure Channel - initialization_** _<u>CP</u>_

**_Command: CHLNG_**

**_Reply: CCRYPT_**

**SCBK**

**_Command: SCRYPT_**

**_Reply: RMAC_I Secure Channel_**

**_CMD:_** _…._

**_REPLY:_** _…_

**_CMD:_** _Poll_

**_REPLY: Card Data Report_**

## Slide 30

## **Understanding OSDP - Secure Channel**

Secure Channel - initialization
PD CP
SCBK CP random challenge
Command: CHLNG
Reply: CCRYPT

**SCBK**

**_Command: SCRYPT Reply: RMAC_I Secure Channel_**

**_CMD:_** _…._ **_REPLY:_** _…_ **_CMD:_** _Poll_

**_REPLY: Card Data Report_**

## Slide 31

## **Understanding OSDP - Secure Channel**

###### **PD Generates Session Keys**

Secure Channel - initialization
PD CP
SCBK CP random challenge
Command: CHLNG SCBK
Reply: CCRYPT
Generate Session Keys…
Command: SCRYPT
Reply: RMAC_I
Secure Channel
Session Keys
CMD:  ….
REPLY:  …
CMD:  Poll
REPLY: Card Data Report

## Slide 32

## **Understanding OSDP - Secure Channel**

###### **PD proof of successful enc**

Secure Channel - initialization
PD CP

SCBK CP random challenge
Command: CHLNG SCBK
PD random challenge
Proof for successful enc
Reply: CCRYPT
Generate Session Keys…
Command: SCRYPT
Reply: RMAC_I
Secure Channel
Session Keys
CMD:  ….
REPLY:  …
CMD:  Poll
REPLY: Card Data Report

**_REPLY: Card Data Report_**

## Slide 33

## **Understanding OSDP - Secure Channel**

**CP generates session keys & validates PD**

Secure Channel - initialization
PD CP
SCBK CP random challenge
Command: CHLNG SCBK
PD random challenge
Proof for successful enc
Reply: CCRYPT
Generate Session Keys…
Proof for successful enc Verifies PD..
Command: SCRYPT
Reply: RMAC_I
Secure Channel
Session Keys
Session Keys
CMD:  ….
REPLY:  …
CMD:  Poll
REPLY: Card Data Report

## Slide 34

## **Understanding OSDP - Secure Channel**

###### **CP proof of successful enc**

**_Secure Channel - initialization_** _<u>PD CP</u>_ **SCBK** **_CP random challenge Command: CHLNG_ SCBK** **_PD random challenge Proof for successful enc Reply: CCRYPT Proof for successful enc Command: SCRYPT Reply: RMAC_I Secure Channel Session Keys Session Keys CMD:_** _…._ **_REPLY:_** _…_ **_CMD:_** _Poll_ **_REPLY: Card Data Report_**

## Slide 35

## **Understanding OSDP - Secure Channel**

> **Both are mutually auth** 👍 **Both have session keys**

**_Secure Channel - initialization_** _<u>PD CP</u>_ **SCBK** **_CP random challenge Command: CHLNG_ SCBK** **_PD random challenge Proof for successful enc Reply: CCRYPT Proof for successful enc Command: SCRYPT Reply: RMAC_I Secure Channel Session Keys Session Keys_**

**_CMD:_** _…._

**_REPLY:_** _…_ **_CMD:_** _Poll_

**_REPLY: Card Data Report_**

## Slide 36

## **Understanding OSDP - Secure Channel**

> **Both are mutually auth** 👍 **Both have session keys**

**<u>initialization vector (IV)</u> must change every message!**

**_Secure Channel - initialization_** _<u>PD CP</u>_ **SCBK** **_CP random challenge Command: CHLNG PD random challenge Proof for successful enc Reply: CCRYPT Proof for successful enc Command: SCRYPT Reply: RMAC_I Secure Channel Session Keys Session Keys_**

**SCBK**

**_CMD:_** _Poll_ **_REPLY:_** _…_ **_CMD:_** _Poll_

**≠**

**_REPLY: Card Data Report_**

## Slide 37

## **Understanding OSDP - Secure Channel**

**_Secure Channel - initialization_** _<u>PD CP</u>_

> **Both are mutually authBoth have session keys**<sup>👍</sup>

**<u>initialization vector (IV)</u> based on previous message received**

**SCBK** **_CP random challenge Command: CHLNG_ SCBK** **_PD random challenge Proof for successful enc Reply: CCRYPT Proof for successful enc Command: SCRYPT Reply: RMAC_I Secure Channel Session Keys_** **~~MAC~~ 1** **_Session Keys CMD:_** _…._ **_IV2_ MAC2** **_REPLY:_** _…_ **~~MAC~~** **3** **_IV3 CMD:_** _Poll_ **_IV4 REPLY: Card Data Report_**

## Slide 38

## **Understanding OSDP - Secure Channel**

> **Both are mutually authBoth have session keys**<sup>👍</sup>

**<u>initialization vector (IV)</u> based on previous message received**

**_Secure Channel - initialization_** _<u>PD CP</u>_ **SCBK** **_CP random challenge Command: CHLNG_ SCBK** **_PD random challenge Proof for successful enc Reply: CCRYPT Proof for successful enc Command: SCRYPT Reply: RMAC_I Secure Channel Session Keys_** **~~MAC~~ 1** **_Session Keys CMD:_** _…._ **_IV1 IV2_ MAC2** **_REPLY:_** _…_ **~~MAC~~** **3** **_IV3 CMD:_** _Poll_ **_IV4 REPLY: Card Data Report_**

## Slide 39

## **Understanding OSDP - Secure Channel**

**PD generates the initial MAC value, and sends it to CP**

**_Secure Channel - initialization_** _<u>PD CP</u>_ **SCBK** **_CP random challenge Command: CHLNG_ SCBK** **_PD random challenge Proof for successful enc Reply: CCRYPT Proof for successful enc Command: SCRYPT_**

**_Reply: RMAC_I_ Initial MAC value [16 BYTES]** **_Secure Channel Session Keys_** **~~MAC~~ 1** **_Session Keys CMD:_** _…._ **_IV1 IV2_ MAC2** **_REPLY:_** _…_ **~~MAC~~** **3** **_IV3 CMD:_** _Poll_ **_IV4_**

**_REPLY: Card Data Report_**

## Slide 40

## **Understanding OSDP - Secure Channel**

**_Secure Channel - initialization_** _<u>PD CP</u>_ **SCBK** **_CP random challenge Command: CHLNG_ SCBK** **_PD random challenge Proof for successful enc Reply: CCRYPT Proof for successful enc Command: SCRYPT Reply: RMAC_I_ Initial MAC value [16 BYTES]** **_Secure Channel Session Keys_** **~~MAC~~ 1** **_Session Keys CMD:_** _…._ **_IV1 IV2_ MAC2** **_REPLY:_** _…_ **~~MAC~~** **3** **_IV3 CMD:_** _Poll_ **_IV4 REPLY: Card Data Report_**

## Slide 41

## **Understanding OSDP - Secure Channel**

**_Secure Channel - initialization_** _<u>PD</u>_

_<u>CP</u>_

**SCBK** **_CP random challenge Command: CHLNG_ SCBK** **_PD random challenge Proof for successful enc Reply: CCRYPT Proof for successful enc Command: SCRYPT Reply: RMAC_I Secure Channel Session Keys Session Keys IV: Last MAC CMD:_** _…._

**_Session Keys IV: Last MAC_**

**_CMD:_** _…._

**_REPLY:_** _…_

**_CMD:_** _Poll_

**_REPLY: Card Data Report_**

## Slide 42

## **Understanding OSDP - Secure Channel**

Secure Channel - initialization
PD CP
SCBK
SCBK
Reply: RMAC_I
Secure Channel
Session Keys
Session Keys
IV1
1. CMD:  Poll
IV2
2. REPLY:  Ack
IV3
3. CMD:  Poll
IV4
4. REPLY: Card Data Report

## Slide 43

## **Attacking the Secure Channel**

###### **Reply attack?**

Secure Channel - initialization
PD CP
SCBK
SCBK
Reply: RMAC_I
Secure Channel
Session Keys
Session Keys
IV1
1. CMD:  Poll
IV2
2. REPLY:  Ack
IV3
3. CMD:  Poll
IV4
4. REPLY: Card Data Report
IV5
5. CMD:  Poll
IV4
4. REPLY: Card Data Report

## Slide 44

## **Attacking the Secure Channel**

###### **Reply attack?**

Secure Channel - initialization
PD CP
SCBK
SCBK
Reply: RMAC_I
Secure Channel
Session Keys
Session Keys
IV1
1. CMD:  Poll
IV2
2. REPLY:  Ack
IV3
3. CMD:  Poll
IV4
4. REPLY: Card Data Report
IV5
5. CMD:  Poll
Expected: IV6
IV4
4. REPLY: Card Data Report
Enc (& MAC) error

## Slide 45

## **IV Reverting**

###### **Reply attack!**

💡 !

Secure Channel - initialization
PD CP
SCBK
SCBK
Reply: RMAC_I
Secure Channel
Session Keys
Session Keys
IV1
1. CMD:  Poll
IV2
2. REPLY:  Ack
IV3
3. CMD:  Poll
IV4
4. REPLY: Card Data Report
IV5
5. CMD:  Poll
Expected: IV6
IV4
4. REPLY: Card Data Report

**_Enc (& MAC) error_**

## Slide 46

## **IV Reverting**

###### **Reply attack**

**What if we could change the IV?** 🤔

Secure Channel - initialization
PD CP
SCBK
SCBK
Reply: RMAC_I
Secure Channel
Session Keys
Session Keys
IV1
1. CMD:  Poll
IV2
2. REPLY:  Ack
IV3
3. CMD:  Poll
IV4
4. REPLY: Card Data Report
IV5 IV1
5. CMD:  Poll
Expected: IV6
IV4
4. REPLY: Card Data Report

Enc (& MAC) error

## Slide 47

## **IV Reverting**

###### **Reply attack**

Secure Channel - initialization
PD CP
SCBK
SCBK
Reply: RMAC_I
Secure Channel
Defines the
Session Keys
first IV  Session Keys
IV1
1. CMD:  Poll
IV2
2. REPLY:  Ack
IV3
3. CMD:  Poll
IV4
4. REPLY: Card Data Report
IV5
5. CMD:  Poll
Expected: IV6
IV4
4. REPLY: Card Data Report
Enc (& MAC) error

## Slide 48

## **IV Reverting**

###### **Reply attack**

Secure Channel - initialization
PD CP
SCBK
SCBK
Reply: RMAC_I
Secure Channel
Defines the
Session Keys
first IV  Session Keys
IV1
1. CMD:  Poll
IV2
2. REPLY:  Ack
IV3
3. CMD:  Poll
IV4
4. REPLY: Card Data Report
Reply: RMAC_I IV5 IV1
5. CMD:  Poll
Expected: IV6
IV4
4. REPLY: Card Data Report
Enc (& MAC) error

## Slide 49

## **IV Reverting**

###### **Reply attack**

Secure Channel - initialization
PD CP
SCBK
SCBK
Reply: RMAC_I
Secure Channel
Defines the
Session Keys
first IV  Session Keys
IV1
1. CMD:  Poll
IV2
2. REPLY:  Ack
IV3
3. CMD:  Poll
IV4
4. REPLY: Card Data Report
Reply: RMAC_I IV5 IV1
1. CMD:  Poll
Expected: IV2! REPLY

## Slide 50

## **IV Reverting**

###### **Reply attack**

Secure Channel - initialization
PD CP
SCBK
SCBK
Reply: RMAC_I
Secure Channel
Defines the
Session Keys
first IV  Session Keys
IV1
1. CMD:  Poll
IV2
2. REPLY:  Ack
IV3
3. CMD:  Poll
IV4
4. REPLY: Card Data Report
Reply: RMAC_I IV5 IV1
1. CMD:  Poll
IV2
2. REPLY:  Ack
IV3
3. CMD:  Poll
IV4
4. REPLY: Card Data Report

## Slide 51

## **IV Reverting - LibOSDP**

<u>https://github.com/goToMain/libosdp</u>

Siddharth Chandrasekaran


> Recovered by OCR — confidence 95/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IV Reverting - LIbOSDP
https://github.com/goToMain/libosdp
LibOSDP - Open Supervised Device Protocol Library
This is an open source implementation of IEC 60839-11-5 Open Supervised Device Protocol (OSDP). The protocol is
intended to improve interoperability among access control and security products. It supports Secure Channel (SC) for
encrypted and authenticated communication between configured devices.
OSDP describes the communication protocol for interfacing one or more Peripheral Devices (PD) to a Control Panel
(CP) over a two-wire RS-485 multi-drop serial communication channel. Nevertheless, this protocol can be used to
transfer secure data over any stream based physical channel. Read more about OSDP
This protocol is developed and maintained by (SIA).
Siddharth Chandrasekaran
```

## Slide 52

## **IV Reverting**

**An implementation error..**

**Could be defined more clearly..**

## Slide 53

## **By the book**

🤔 …

**_PD Busy Reply (0x79)_**

_1. Unencrypted, ALWAYS (even during secure channel)_

_2. Can be sent continuously, without any time constraints_

?

## Slide 54

## **Time-Delays in OSDP**

###### **_Secure Channel_**

_<u>PD</u>_

_<u>CP</u>_ **_CMD REPLY CMD REPLY CMD REPLY CMD REPLY_**

## Slide 55

## **Time-Delays in OSDP**

**_Secure Channel_** _<u>CP</u>_

_<u>PD</u>_

**_CMD REPLY CMD REPLY_**

CMD
REPLY
CMD
REPLY

## Slide 56

## **Time-Delays in OSDP**

**_Secure Channel_** _<u>CP</u>_

_<u>PD</u>_

CMD
REPLY
CMD
REPLY
CMD
8 sec
REPLY
CMD
REPLY

## Slide 57

## **Time-Delays in OSDP**

Secure Channel
PD CP
CMD
REPLY
CMD
REPLY
CMD
8 sec
New secure channel initialization…

## Slide 58

## **Time-Delays with PD Busy**

###### **_Secure Channel_**

_<u>PD</u>_

_<u>CP</u>_ **_CMD REPLY CMD REPLY CMD REPLY CMD REPLY_**

## Slide 59

## **Time-Delays with PD Busy**

**_PD Busy Reply (0x79)_**

_1. Unencrypted ALWAYS_

**_Secure Channel_** _<u>CP</u>_

_<u>PD</u>_

CMD
REPLY
CMD
REPLY
CMD
timeout reset
REPLY: PD Busy
REPLY
CMD
REPLY

## Slide 60

## **Time-Delays with PD Busy**

**_PD Busy Reply (0x79)_**

_1. Unencrypted ALWAYS_

_2. Can be sent continuously_

**_Secure Channel_** _<u>CP</u>_

_<u>PD</u>_

**_CMD REPLY CMD REPLY CMD timeout reset REPLY: PD Busy REPLY: PD Busy REPLY: PD Busy REPLY: PD Busy REPLY CMD REPLY_**

## Slide 61

## **OSDP Time-Delay Attack!**

**_PD Busy Reply (0x79)_**

_Fully control_ **_WHEN to open the door!_**

**_Secure Channel_** _<u>CP</u>_

_<u>PD</u>_

**_CMD REPLY CMD REPLY CMD timeout reset REPLY: PD Busy REPLY: PD Busy REPLY: PD Busy REPLY: PD Busy REPLY: Card Data Report_**

## Slide 62

## **Getting into the facility – Time Delay Attack**

**_PD Busy Reply (0x79)_** _Fully control_ **_WHEN to open the door!_**

**_Secure Channel_** _<u>PD CP</u>_ **_CMD REPLY CMD REPLY CMD timeout reset REPLY: PD Busy REPLY: PD Busy REPLY: PD Busy REPLY: PD Busy REPLY: Card Data Report_**

## Slide 63

## **Getting into the facility – Time Delay Attack**

**_PD Busy Reply (0x79)_** _Fully control_ **_WHEN to open the door!_**

Secure Channel
PD CP
CMD
REPLY
CMD
REPLY
CMD
timeout reset
REPLY: PD Busy
REPLY: PD Busy
REPLY: PD Busy
REPLY: PD Busy
Stop with the busy messages…
“I’ll try”
REPLY: Card Data Report

## Slide 64

## **Getting into the facility – Time Delay Attack**

**_PD Busy Reply (0x79)_** _Fully control_ **_WHEN to open the door!_**

Secure Channel
PD CP
CMD
REPLY
CMD
REPLY
CMD
timeout reset
REPLY: PD Busy
REPLY: PD Busy
REPLY: PD Busy
REPLY: PD Busy
Stop with the busy messages…
“I’ll try”
REPLY: Card Data Report

## Slide 65

## **Getting into the facility – Time Delay Attack**

**_PD Busy Reply (0x79)_** _Fully control_ **_WHEN to open the door!_**

**_Secure Channel_** _<u>PD CP</u>_ **_CMD REPLY CMD REPLY CMD timeout reset REPLY: PD Busy REPLY: PD Busy REPLY: PD Busy REPLY: PD Busy REPLY: Card Data Report … REPLY: Card Data Report_**

## Slide 66

## **Getting into the facility – Time Delay Attack**

**_PD Busy Reply (0x79)_** _Fully control_ **_WHEN to open the door!_**

**_Secure Channel_** _<u>PD CP</u>_ **_CMD REPLY CMD REPLY CMD timeout reset REPLY: PD Busy REPLY: PD Busy REPLY: PD Busy REPLY: PD Busy REPLY: Card Data Report …_**

**_REPLY: Card Data Report_**

## Slide 67

**Getting into the facility – Time Delay Attack**

**_PD Busy Reply (0x79)_**

_Fully control_ **_WHEN to open the door!_**

**_Effecting ALL implementations (following the specs..)_**

**_* And no mitigation is expected to be available at the near future_**

## Slide 68

**Getting into the facility – Time Delay Attack**

**(secure channel)**


> Recovered by OCR — confidence 84/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Getting into the facility — Time Delay Attack
C:\home\kal i\osdp- fuzz> python osdp_mitm_tool.py /tmp/cp_usock serial=/dev
```

## Slide 69

**A Security Paradox More security, More features More (attack) opportunities!**

## Slide 70

## **Increased Functionality & Complexity**

**AES Encryption**

**Remote Configuration**

**Remote FW update**

**Status Reports**

**Complex Data Formats**

## Slide 71

## **Increased Functionality & Complexity**

Wiegand C / C++ implementation ~200 code lines

OSDP implementation over 4K lines of code … (+ additional linked libs)

## Slide 72

**More logic - More bugs..**

**LibOSDP**

_Bugs from 2022_

_New DOS_


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
More logic - More bugs.. New DOS “82 Seeule-channe!
v Fix null pointer deref issue osdp_reply name
LibOSDP Signed-off-by: Siddharth Chandrasekaran <sidcha.dev@gmail .com>
Bugs from 2022 master
@% sidcha committed last week
overflow bugs
© Closed
Showing 1 changed file with 1 addition and 1 deletion.
own address
src/osdp_common.c
}
name = names[reply id - REPLY_ACK];
if (name[@] == *\@") {
if (!name) {
```

## Slide 73

## **A Security Paradox..**

## **Classic Attacks**

## **Attack Surface**

## Slide 74

## **Beyond Physical Access Control!**

**_Gaining access to the IP network!_**

**POST EXPLOITATION:** Jos Wetzels’ “Nakatomi Space: Lateral Movement as L1 Post-exploitation in OT” (Black Hat Asia 23)

## Slide 75

**Gaining a foothold in the internal IP network Over serial OSDP connection (RS-485)**

## Slide 76

## **OSDP - Entry point the network**

Open/Close
IP Network
Wireless
Serial Communication
MIFARE
DESFIRE
TCP/IP
…
Security server
RS485
TCP/IP
Administrator
Open/Close
Serial to E TH(!)

## Slide 77

## **The process towards our vision**

• CP (AXIS A1001) with debug abilities.

## Slide 78

## **Firmware Extraction**

- Firmware extraction

• Bin walk – using binwalk we located the file system as JFFS2 ( file system for use with flash memory devices) :

- By using Jefferson (JFFS2 filesystem extraction tool) we were able to extract the FS

## Slide 79

## **Debugging the OSDP service**

System configuration that easily leads to RCE. By using the upload web Files: * upload netcat

- shtml script to target netcat

## Slide 80

**Assessing AXIS A1001 – Full Setup**

Client, AXIS, GDB, firmware analysis

ssh connection
ssh server ssh client
gdb connection
gdb client
gdb server

## Slide 81

## **Targeting relevant logics**

- Secure channel handshake?

- OSDP message header processing (always unencrypted)?

- Message receival logic?

## Slide 82

## **Message Receival Logic**

• Performed before secure-channel validation / initialization

PD CP
OSDP_PACKET
ANY_PACKET
Receive data over layer 2 ( Message receival logic )
Validate Message
Message handling
REPLY

## Slide 83

## **Standard Flow Of Message receival**

0x100

1. Received legit osdp message

0x100

2. Received 2nd legit message

## Slide 84

## **Message receival in two chunks:**

**0x100**

**0x20**

**d. Copy the first part to the resized buffer.**

**0x120**

**a. Received first part of OSDP message.**

**c. Allocates new buffer of 0x100 + additional bytes from last message**

**b. Received second part of the OSDP message**

## Slide 85

## **The Issue**

**Additional bytes are copied to the new buffer**

additional_bytes_length + 0x100

**additional_bytes_length**

**overflow**

## Slide 86

**The Issue – message flow**

**0x100**

**1. Valid OSDP message + additional invalid bytes**

**2. 2**<sup>**nd**</sup> **message: 0x100 + additional bytes length**

> **Additional bytes length** **0x100**

**Additional bytes length Additional bytes length (0x100 + Additional bytes length)**

**(0x100 + Additional bytes length)**

**3. Writing to buffer starts here**

**Heap overflow**

## Slide 87

## **Heap-overflow potential**

**buffer Chunk 1 Interesting chunk empty Chunk 2 structure override Interesting chunk Chunk 3 data … data … By overriding ‘callback_ptr’ for example we will Callback_ptr cause the program to execute a code of our choice**

## Slide 88

## **Heap-overflow**

• Override potential heap structures which will lead to arbitrary behaviors such as: dos, PE, etc. • Override structures and variables of the process

|our buffer|empty chunk|
|---|---|
|Interesting|structure
|
|callb|ack func|

## Slide 89

## **Successful exploitation?**

##### **PACSIOD becomes a bind-shell**


> Recovered by OCR — confidence 88/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Successful exploitation?
PACSIOD becomes a bind-shell
| grep LISTEN
LISTEN
CISTEW
LISTEN ae server-/.7.
LISTEN 516/monoLlith
LISTEN
LISTEN
LISTEN
LISTEN
```

## Slide 90

## **Why not FUZZING?**

##### **Using the framework, we were able to detect more several vulnerabilities.**

Fuzzing serial channels
Master Serial Killer  DNP3
DEF CON 22 - ICS Village Fuzzing

## Slide 91

## **Assessment Tool in our architecture:**

Open/Close
IP Network
Serial Communication
Management PC
WEB
INTERFACE
Fuzzer
Dump  Assessment
communication €9 Tool €9
Execute
exploits
RS485
RS485

## Slide 92

**OSDP Assessment Tool**


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
OSDP Assessment Tool
usage: osdp_mitm_tool.py [-h] [—dump e] [exploit EXPLOIT] [-cp_dev device PD_DEVICE] [-fuzzer_trigger_command FUZZER_TRIGGER_COMMAND] [-fuzzer_ta FUZZER_TARGET]
[-fuz 5 FUZZER. SESSION | TIMEOUT] [-f v | thr d FUZZER_INACTIVITY_CRASH_THRESHOLD] [ -fuz er FUZZER_SESSION_SAVE_TRIGGER]
[- REPLY] [-s SEQUENCE [SEQUENCE ... ]] [-p PRIMITIVE [PRIMITIVE - -e, —exclude-primitive EXCLUDE [EXCLUDE ... ]]
show this help message and exit
act as a MITM and dump the packets
_mode act as MITM and fuzz one of the end-points
loit EXPLOIT run an exploit from list of exploits (either replay or delay)
levice CP_DEVICE cp device path, you can specify serial using the following format : ‘serial=/dev/ttyUSBO,baud=9600' (instead of a pipe)
PD_DEVICE pd device path, you can specify serial using the following format : ‘serial=/dev/ttyUSBO,baud=9600' (instead of a pipe)
er_command FUZZER_TRIGGER_COMMAND
the OSDP command to trigger the fuzzing (default REPLY_ACK)
-fuzzer_target FUZZER_TARGET
whether to fuzz the PD or CP (default CP)
how much time to fuzz a session (default 30 min)
tivity_crash_threshold FUZZER_INACTIVITY_CRASH_THRESHOLD
how much time of inactivity will be considered as a crash (default 1000 ms)
ave trigger FUZZER_SESSION_SAVE_TRIGGER
what can cause session restart, either crash or invalid_content (default crash)
-r REPLY reply command and payload, provide a hex values of the packet command and payload (i.e. 102030)
-S SEQUENCE [SEQUENCE ... ]
reply sequence of commands and payloads, provide a hex values of the packet command and payload (i.e. 102030)
-p PRIMITIVE [PRIMITIVE ...], —primitive PRIMITIVE [PRIMITIVE ... ]
run only these primitives, values can be from the following [enlarge_payload, increase_sequence, replace_payload, fixed_payload, random_message_code, random_message_code_and_data,
invert_control_crc, invert_control_scb, invert_control_multi, remove_payload, random_som, increase_size, message_code_all, message_code_50, random_size, constant_payload,
trigger_overflow]
e EXCLUDE [EXCLUDE ... ]
do not run these primitives, values can be from the following [enlarge_payload, increase sequence, replace payload, fixed_payload, random_message_code,
random_message_code_and_data, invert_control_crc, invert_control_scb, invert_control_multi, remove_payload, random_som, increase_size, message_code_all, message_code_50,
random_size, constant_payload, trigger_overflow]
```

## Slide 93

## **Mutation FUZZER**

'538f08000540 91fa '
'538f08000550a0e8'
Assessment
Tool
Fuzz

##### **applied mutation message_code_50**

## Slide 94

## **FUZZ MODE**

- **Custom mutation primitives.**

- **Easy to extend.**

- **Auto-crash detection.**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 82/100 on the text kept, 68/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
FUZZ MODE

- Custom mutation primitives.
- Easy to extend.
- Auto-crash detection

[terminal panel - ariel.harush]
[illegible - one line clipped by the panel header]
2023-06-18 03:40:27,374 cp -> pd:
b'5318070000602e5319070000602d531a070000602c531b070000602b531c070000602a531d0700006029531e0700006028531f070000602753200700006026532107000060255322070[cut off by slide edge]
00601e5329070000601d532a070000601c532b070000601b532c070000601a532d0700006019532e0700006018532f07000060175330070000601653310700006015533207000060145333[cut off by slide edge]
2023-06-18 03:40:27,425 cp -> pd: b'53360700006010'
2023-06-18 03:40:27,446 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,492 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,538 pd -> cp: b'538f18000450a0c9538f08000440a0c9538f0800044098e6' (original:b'538f08000440a0c9538f08000440a0c9538f08000440a0c9') ap[cut off by slide edge]
2023-06-18 03:40:27,583 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,629 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,675 pd -> cp: b'538f18000450a0c9538f08000440a0c9538f0800044098e6' (original:b'538f08000440a0c9538f08000440a0c9538f08000440a0c9') ap[cut off by slide edge]
2023-06-18 03:40:27,721 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,767 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,813 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,859 pd -> cp: b'538f18000450a0c9538f08000440a0c9538f0800044098e6' (original:b'538f08000440a0c9538f08000440a0c9538f08000440a0c9') ap[cut off by slide edge]
2023-06-18 03:40:27,905 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,951 pd -> cp: b'538f10000450a0c9538f08000440ffcb' (original:b'538f08000440a0c9538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:40:27,996 pd -> cp: b'538f18000450a0c9538f08000440a0c9538f0800044098e6' (original:b'538f08000440a0c9538f08000440a0c9538f08000440a0c9') ap[cut off by slide edge]
2023-06-18 03:40:28,046 pd -> cp: b'538f0800045091db' (original:b'538f08000440a0c9') applied mutation message_code_50
2023-06-18 03:48:11,022 ***** crash detected timeout: 462.97612953186035

[code panel - ariel.harush]
def pri_invert_control_SCB(msg: OSDPMessage):
    msg.CTRL_SCB = not msg.CTRL_SCB
    msg.recalculate_all()
```

## Slide 95

**FUZZ Example**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 75/100 on the text kept, 57/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
FUZZ Example

pd -> cp: b'53e508000440d296' (original:b'53e508000440d29653e508000440d29653e508000440d296') applied mutation remove_payload
pd -> cp: b'53e508000440d296'
pd -> cp: b'53e5100004b7d29653e50800044041cb' (original:b'53e508000440d29653e508000440d296') applied mutation random_message_code
pd -> cp: b'53e5100004b7d29653e50800044041cb'
pd -> cp: b'b8e510000440d29653e50800044045e9' (original:b'53e508000440d29653e508000440d296') applied mutation random_som
pd -> cp: b'b8e510000440d29653e50800044045e9'
pd -> cp: b'53e510000440d29653e50800044081ae' (original:b'53e508000440d29653e508000440d296') applied mutation random_size
pd -> cp: b'53e510000440d29653e50800044081ae'
pd -> cp: b'53e518000040d29653e508000440d29653e50800044098' (original:b'53e508000440d29653e508000440d29653e508000440d296') applied mutation invert_control_crc
pd -> cp: b'53e518000040d29653e508000440d29653e50800044098'
pd -> cp: b'53e510000401d29653e50800044079da' (original:b'53e508000440d29653e508000440d296') applied mutation message_code_all
pd -> cp: b'53e510000401d29653e50800044079da'
pd -> cp: b'53e588000450ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff56d2' (original:b'53e508000440d29653e508000440d296') applied mutation trigger_overflow
pd -> cp: b'53e588000450ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff56d2'
```

## Slide 96

## **Fuzzing results**

- **Three 0-day vulnerabilities!**

## Slide 97

**Message Code 0x50 – CRASH (1st)**

0x50 payload **osdp_get_message_data_size(                                  )** 0x50 payload **size = 0x10** 0x10

## Slide 98

## **Message Code 0x50 – CRASH (1st)**

0x50 **osdp_get_message_data_size(** 0x50 **) size = -0x3 crush**

Wait, what??

## Slide 99

**Message Code 0x50 – CRASH (1st)**

osdp_get_message_data_size( ) signed number signed unsigned 0xFFFFFFFC -0x3 Malloc ( 0xFFFFFFFC )

## Slide 100

**Catch the crush using fuzzer**


> Recovered by OCR — confidence 86/100 on the text kept, 63/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Catch the crush using fuzzer
48
48
48
48
48
48
48
48
48
:27,721
:27,813
:27,905
:27,996
:28,046
:11,022
pd ->
pd ->
pd ->
pd ->
pd ->
pd ->
pd ->
pd ->
cp:
cp:
cp:
cp:
cp:
cp:
cp:
cp:
b'538F0800045091db" (original:b‘'538f@8000440a0c9") applied mutation message _code_5@
crash detected timeout: 462.97612953186035
```

## Slide 101

**DEMO – Crashing the CP’s OSDP Service**


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 45/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
DEMO - Crashing the CP's OSDP Service

door close

[terminal tabs] 6. kali_tty (1)   8. kali_tty (1)   9. kali_tty (1)

cp -> pd: b'536007000060e6'
cp -> pd: b'536007000060e6'
cp -> pd: b'536107000060e5'
cp -> pd: b'536107000060e5'
cp -> pd: b'536207000060e4'
cp -> pd: b'536207000060e4'
cp -> pd: b'536307000060e3'
cp -> pd: b'536307000060e3'
cp -> pd: b'536407000060e2'
cp -> pd: b'536407000060e2'
cp -> pd: b'536507000060e1'
cp -> pd: b'536507000060e1'
pd -> cp: b'53e50700004081'
pd -> cp: b'53e50700004081'
cp -> pd: b'53650800006200de'
cp -> pd: b'53650800006200de'
pd -> cp: b'53e53400004601000002000003010004040105020106000007000008010009'
pd -> cp: b'53e53400004601000002000003010004040105020106000007000008010009'
***** message is not valid
pd -> cp: b'01010a92030b92030c00000e00000f00001001009c'
pd -> cp: b'01010a92030b92030c00000e00000f00001001009c'
cp -> pd: b'53650900056100e94d'
cp -> pd: b'53650900056100e94d'
pd -> cp: b'53e51400054500068e0101f5098036053800b9f7'
pd -> cp: b'53e51400054500068e0101f5098036053800b9f7'
cp -> pd: b'536516000669000000000000000000010101010150e4'
cp -> pd: b'536516000669000000000000000000010101010150e4'
pd -> cp: b'53e508000640b0f0'
pd -> cp: b'53e508000640b0f0'
cp -> pd: b'53650d00076a00020101031e8f'
cp -> pd: b'53650d00076a00020101031e8f'
pd -> cp: b'53e50800074081c3'
pd -> cp: b'53e50800074081c3'
cp -> pd: b'53651600056900000000000000000001010101011d0c'
cp -> pd: b'53651600056900000000000000000001010101011d0c'
pd -> cp: b'53e508000540e3a5'
pd -> cp: b'53e508000540e3a5'
cp -> pd: b'53650d00066a0001000000c198'
cp -> pd: b'53650d00066a0001000000c198'
pd -> cp: b'53e508000640b0f0'
pd -> cp: b'53e508000640b0f0'
cp -> pd: b'53650800076033c5'
cp -> pd: b'53650800076033c5'
pd -> cp: b'53e50800074081c3'
pd -> cp: b'53e50800074081c3'
cp -> pd: b'53650800056051a3'
cp -> pd: b'53650800056051a3'
```

## Slide 102

## **Message Code 0x50 – CRASH (2th)**

0x50 payload

0xFF + 0xFF * 0x100 = 0xFFFF.

## Slide 103

## **Message Code 0x50 – CRASH (2th)**

0x50 payload
payload program memory
0xFFFF
override0x8

## Slide 104

# **WHATS next?**

**And how to prepare for it..**

## Slide 105

## **Only the beginning..**

**ID to Controller communication?**

**OSDP Transparent Mode**

**Complex ID Data Processing**

**Forwarding complex data types to the security server?**

## Slide 106

## **Takeaways**

**OSDP is new.. (and not perfect)**

**Serial connections should not be ignored!**

**Prepare! auditing, monitoring and assessing..**

- ✓ **Configure it carefully**

- ✓ **Use cameras..**

- ✓ **Don’t leave them publicly exposed**

- ✓ **Controller logs** ✓ **Products assessment**

## Slide 107

# **Stay Safe**

Eran Jacob Ariel Harush Roy Hodir Head of Research Security Researcher Security Researcher _/in/eranj_ /in/arielhar _/in/roy-h-858b69_
