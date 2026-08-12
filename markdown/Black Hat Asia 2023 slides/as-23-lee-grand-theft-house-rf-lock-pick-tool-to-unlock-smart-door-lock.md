---
title: "Grand Theft House RF Lock Pick Tool to Unlock Smart Door Lock"
speakers: ["Lee"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Lee-Grand-Theft-House-RF-Lock-Pick-Tool-to-Unlock-Smart-Door-Lock.pdf"
pages: 65
sha256: "c411813b751095de10999da3b2219b1c71681db643498bcb9cee1ec852c3724c"
text_chars: 41738
ocr_pages: 5
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:54:51Z"
---
# Grand Theft House RF Lock Pick Tool to Unlock Smart Door Lock

**Speakers:** Lee  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Lee-Grand-Theft-House-RF-Lock-Pick-Tool-to-Unlock-Smart-Door-Lock.pdf` (65 pages)


## Slide 1

# Grand Theft House: RF Lock Pick Tool to Unlock Smart Door Lock

Seungjoon Lee, Kwonyoup Kim

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
ASIA
MAY 11-12
BRIEFINGS
Grand Theft House: RF Lock Pick
Tool to Uniock Smart Door Lock
Seungjoon Lee, Kwonyoup Kim
```

## Slide 2

## Prologue

“Replay Attack” Aired in 2019

Apartment Complex
Bulk Installation
Same Models

###### **_Korea Table of Frequency Allocations(Low-power wireless device for security & safety systems)_**

###### **_Registration Status (Korea National Radio Research Agency)_**

|Application|Band|Power|
|---|---|---|
|Guidance
euiment for the|235.300MHz
(Fixed)|< 10m|
|qp
visually impaired|358.500MHz
(Mobile)|W|
|Transportation
suort sstem for|235.3125MHz|< 100m|
|pp y
disabilities|…|W|
|Security system,
Anti-theft system,
fire alarms, etc.|447.2625
MHz
~447.5625
MHz|< 10m
W|

|Application|‘17|‘18|19|tot.|
|---|---|---|---|---|
|447MHz Module||2|2|4|
|alarm detector|1|6|-|7|
|**Digital Doorlock**|**23**|**16**|**18**|**57**|
|Guidance for disabilities|10|8|14|32|
|Thermal Detector|5|3|-|8|

#BHASIA @BlackHatEvents

## Slide 3

## Wireless Door Lock System

❏ It can be used in a variety of settings, including homes, offices, and other commercial or industrial.

Receiver
Doorlock Backside

Wallpad
2) NTSC/PAL & Serial
3) Wallpad Switch
Wallpad Backside

3) Key Fob

Door lock
1) Video Doorbell
Wireless Router 3) Smartphone APP

Enterance

#BHASIA @BlackHatEvents

## Slide 4

## Summary

Analyze FW
Find Vulnerabilities
•
Classic Replay Attack
•
Rollback Attack
•
Loop Playback Attack
RF Signal Analysis Key Seed
Jamming Replay
TxID
•
Sniffing and Unlock Attack
Demodulation Decrypt Sync Counter
•
Lock Picking Attack
Device R.E.
EC
Baseband Decoding Descrambling

#BHASIA @BlackHatEvents

**Doorlock**

## Slide 5

## Agenda

###### **Background**

- Wireless Door Lock System

- Hardware Teardown

- Door Lock RF Signal Basic

**Encryption & Authentication**

- Door Lock RF Packet Encryption

- Key Generation

- Packet Confusing

- TxID Matching  and Authentication

**The Art of Lockpicking**

- Sniffing and Unlock Door Locks

- Resynchronization

- Force Synchronization

- Lock Picking Time Analysis

###### **Rolling Code and Replay**

- Rolling code nutshell

- Roll Jam/ Roll Back Attack

- Loop Back Attack

###### **Gadget Preparation**

   - Direct Mode and Synchronization

   - Proprietary Baseband Encoding

   - Build Receiver and Transmitter

- Evaluation

#BHASIA @BlackHatEvents

## Slide 6

## Types of Door Lock RX

- ❏ Door Lock Mainboard MCU

**Mainboard-based Auth. (RX MCU +  RF IC Dongle)**

   - ❏ Usually use one of “16Bit RL78” or “32Bit ARM”or “8bit STM”

   - ❏ usage : Ten-key pad, E-Mortise Control,  Authentication

- ❏ RX MCU

   - ❏ Usually use one of “8bit 8051” or “8bit PIC” or “8bit STM” or “16bit PIC”

- ❏ RX MCU

   - ❏ Usually use  transceiver, TH71120 /CMT 2219 / CMT 2300

   - ❏ Transceiver IC used but Simplex Communication

Receiver-based Auth.
(RX MCU +  RF IC Dongle)
INT CMD (SPI)
Door lock Rx
RF
MCU MCU
CMD (direct) BB Signal
•
RF Settings
•
Sampling
•
Authentication

INT CMD (SPI)
Door lock Rx
RF
MCU MCU
BB Signal BB Signal
• •
Sampling RF Settings
• •
Authentication Sampling
Mainboard-based Auth.
(RF IC Only Dongle)
I/O Pin for RF Settings
Door lock
RF
MCU
BB Signal
•
Sampling
•
RF Settings
•
Authentication
#BHASIA @BlackHatEvents

#BHASIA @BlackHatEvents

## Slide 7

## Types of Door Lock TX

###### ❏ Simplex Communication

Command (SPI)
MCU RF
TX Data (Serial)
Switch

TH72011
16bit PIC
8bit STM
TH72011
CC1070
CMT 2113
16bit ARM
16bit PIC

###### **Feature of Transmitter HW**

- **MCU**

   - **16Bit ARM /16bit PIC /8bit PIC /8bit STM**

   - **Digital Encoding**

   - **Message Encryption**

- **RF Chip**

   - **Tx Only, FSK Modulation**

   - **Low-cost(<$3) Discontinuous Phase Type (CC1070 /TH72011 /CMT 21113)**

#BHASIA @BlackHatEvents

## Slide 8

Understanding Rolling Code and Variant Replay Attack Concise summary and Applied to Door Lock

#BHASIA @BlackHatEvents

## Slide 9

## Principles of Secure Rolling Code

To ensure Secure Rolling Code transmission

1. No transmission is ever repeated

   - Each transmitted message should have **different contents**

   - Receiver should **ignore messages** that have already been sent

   - Keep track of the last used code

      - ❏ But, re-synchronization should be considered (securely)

2. The packet contents are virtually impossible to predict, even if previous messages are known

- Protect the confidentiality of the rolling code (Encryption Algorithm)

❏ "TxID" and "rolling counter" are the information that needs to be kept confidential

   - ❏ it can only be read by the intended recipient

3. Prevent some unauthorized access

- Filtering mechanism, a unique serial number(TxID) is used to achieve

- ❏ TxID should not be guessable and should not appear in a sequential format

#BHASIA @BlackHatEvents

## Slide 10

## Rolling Code in essence

**It is used to protect the packet from being replayed**

enc(
enc(
𝑠 𝑠 𝑠 𝑠 ) 𝑇𝑇𝑥𝑥𝐼 𝑠 𝑠 𝑠 𝑠 ||𝑪 𝑪 𝑪𝑪 𝑺 𝑺 𝑺 𝑺 )
𝑇𝑇𝑥𝑥𝐼
𝐼
𝐼
𝑠 𝑠 𝑠 𝑠 𝑠 𝑠 𝑠 𝑠 𝑠 )
(𝑇𝑇𝑥𝑥𝐼 == 𝑇𝑇𝑥𝑥𝐼
𝑠 𝑠 𝑠 𝑠 𝑠 𝑠 𝑠 𝑠 𝑠 )
(𝑇𝑇𝑥𝑥𝐼 == 𝑇𝑇𝑥𝑥𝐼
※  TxID = Serial  𝑰 𝑰 (𝑪 𝑪 𝑪𝑪𝑷 𝑷 𝑺𝑺𝑷𝑷 < 𝑪 𝑪 𝑪𝑪𝑺 𝑺 𝑺 𝑺 )
Number 𝑡 𝑡 𝑡 𝑈𝑈𝑡𝑡𝑈 𝑈 𝑈 𝑈 ( )
𝑡 𝑡 𝑡 𝑈𝑈𝑡𝑡𝑈 𝑈 𝑈 𝑈 ( )
Fixed Code Rolling Code

#BHASIA @BlackHatEvents

## Slide 11

Fixed Code on Door locks
❏ Fixed code is very weak in “classic replay attack”  Wall pad Capture
Unlock Code
If pressing the button, produces 17 identical message for robustness
Replay
Unlock Code
1 2 3 4 5 6 7 8 9 10 111213 14 151617
SYNC symbol End SYM
0x75 0xA3 0x00 0x80 0x01(Spacer) 0x99(CS)
Serial Number(=TxID) Vendor E

###### Received 5-Byte in door lock mainboard(volatile)

Registered 4-Byte TXID in door lock mainboard(non-volatile)

Rest 3bytes comparison

2 nd Byte CMP
3 rd Byte CMP
4 th Byte CMP

**The comparison of the value of the first byte stored**

#BHASIA @BlackHatEvents

## Slide 12

## Roll Jam Attack (DEFCON23)

❏ Variant of Replay Attack

**Capture + Jamming Car**

① **Owner try**

❏ No time stamp, difficult to prevent unused code replay attack

❏ RollJam Concept

signal1(cnt=n)

Eve capture unused code(signal) Replay unused code later

**Capture + Jamming**

② **Owner Retry**

❏ Process ① Capture signal1 + Jamming ② Capture signal2 + Jamming ③ Capture Signal1 Replay (for her) ④ Capture Signal2 Replay (for carjack)

Why Won't Door Open?

signal2(cnt=n+1)

③

signal1(cnt=n)

Drive

④

signal2(cnt=n+1) Parking

#BHASIA @BlackHatEvents

## Slide 13

## Jamming & Capture on Doorlock

❏ The important point is that the jamming signal should effectively interfere with the original signal without completely overpowering it. (< 30KHz gap is best)

Spectrogram View Frequency View
: 447.244e6
𝑰𝑰𝒄
𝑰𝑰𝒄 𝒄 : 447.274e6
Jamming
Jamming( 𝑰𝑰𝒄 𝒄 )
𝟑 𝟑 𝟑 𝟑 𝟑𝟑
Key Signal( 𝑰𝑰𝒄 𝒄 )
The captured signal
Fail Success Success Success Success Success
during jamming

#BHASIA @BlackHatEvents

## Slide 14

## RollJam Attack on Door Lock

- ❏ Eve capture unused code(signal), Replay Later

**Capture + Jamming Doorlock Owner try 1)** signal1(cnt=n)

- ❏ Process

   - 1) Capture signal1 + Jamming

   - 2) Capture signal2 + Jamming

Knock Knock

   - 3) Capture Signal1 Replay (for her)

   - 4) Capture Signal2 Replay (for theft)

- ❏ Two drawbacks of RollJam

   - ❏ An attacker has to be precise

      - the timing is crucial.

   - ❏ The attack can be launched once

      - If the attacker wants to gain access to the same door lock again, they would need to start the process all over again from the beginning.

Capture + Jamming
Owner Retry
2)
signal2(cnt=n+1)
Knock Knock

3)

signal1(cnt=n))

She Leaving the house

**4)** signal2(cnt=n+1) **Unlock** “Unused Code” **Because signal 1 has been used, but signal 2 has not been used**

#BHASIA @BlackHatEvents

## Slide 15

## RollBack Attack (BHUSA2022)

###### **Capture + Jamming**

- ❏ **Rollback Attack Process**

1) Send Unlock signal

   - 2) Capture + Jamming

   - 3) Send Unlock signal

   - 4) Capture

   - 5) Owner uses the key fob as usual(many times)

   - 6) replay the two consecutive signal

- ❏ **Characteristic**

   - ❏ At any time in the future

Attacker
Victim

cnt=n
Capture
cnt=n+1
Usual Usage
cnt=n+2
cnt=n+k

- ❏ As many times as desired

Consecutive Two signal Sending
cnt=n
cnt=n+1
Unlock

**note: vehicle re-synchronize to a previous code**

#BHASIA @BlackHatEvents

## Slide 16

Root cause of RollBack on Door Lock ❏ If a received message is valid, then the counter value always be stored on memory **Doorlock Wall pad Capture + Jamming** Input 𝑈𝑈𝑡 **𝑡** 𝑠 **𝑠** 𝑠 𝑽 **𝑽** 𝑷𝑷𝑽 **𝑽** 𝑽 **𝑽** 𝑺𝑺𝑈𝑈𝑡 **𝑡** 𝑃𝑃𝑠 **𝑠** 𝑃𝑃 // _received counter_ 𝑽 **𝑽** 𝑷𝑷𝑽 **𝑽** 𝑽 **𝑽** 𝑺𝑺𝑈𝑈𝑡 **𝑡** 𝐴𝐴𝑠 **𝑠** 𝑠𝑠𝐴𝐴𝑠 **𝑠** 𝑠𝑠 // _Last Accepted Counter_ // _If valid counter_ 𝑈𝑈𝑡 **𝑡** 𝑠 **𝑠** 𝑠 **𝑠** = 𝑡𝑡 𝑽𝑽𝑰𝑰𝑀𝑀𝑡𝑡𝑀 **𝑀** 𝑀 **𝑀** 𝑡𝑡𝑖𝑖𝑀𝑀𝑣𝑣𝑀𝑀𝑈𝑈𝑖𝑖𝑣𝑣𝒕 **𝒕** 𝑺 **Capture** 𝑽𝑽𝑰𝑰𝑈𝑈𝑡 **𝑡** 𝑠 **𝑠** 𝑠 **𝑠** > 𝑈𝑈𝑡 **𝑡** 𝑃𝑃𝑠 **𝑠** 𝑃𝑃 𝒕 **𝒕** 𝑺 𝑈𝑈𝑡 **𝑡** 𝐴𝐴𝑠 **𝑠** 𝑠𝑠𝐴𝐴𝑠 **𝑠** 𝑠𝑠 ←𝑈𝑈𝑡 **𝑡** 𝑠 **𝑠** 𝑠 **𝑠** // _update Last Accepted Counter_ 𝑈𝑈𝑡 **𝑡** 𝑃𝑃𝑠 **𝑠** 𝑃𝑃 ←𝑈𝑈𝑡 **𝑡** 𝑠 **𝑠** 𝑠 **𝑠** // _received counter stored_ **_Last Accepted Counter = n+1_** 𝑈𝑈𝑡 **𝑡** 𝑠 **𝑠** 𝑠 **𝑠** = 𝑡𝑡+ 1 𝐃 **𝐃** 𝐃 **𝐃** 𝐃 **𝐃** 𝐃 𝐎 **𝐎** 𝐎 **𝐎** ( ) **Consecutive signals Sending** 𝑺𝑺𝑽𝑽𝒆𝒆𝑺𝑺 𝒕 **𝒕** 𝑺 𝑈𝑈𝑡 **𝑡** 𝑃𝑃𝑠 **𝑠** 𝑃𝑃 ←𝑈𝑈𝑡 **𝑡** 𝑠 **𝑠** 𝑠 **𝑠** // _received counter stored ??? Why?_ 𝑈𝑈𝑡 **𝑡** 𝑠 **𝑠** 𝑠 **𝑠** = 𝑡𝑡 𝑈𝑈𝑡 **𝑡** 𝐴𝐴𝑠 **𝑠** 𝑠𝑠𝐴𝐴𝑠 **𝑠** 𝑠𝑠 𝑈𝑈𝑡 **𝑡** 𝑃𝑃𝑠 **𝑠** 𝑃𝑃 **𝑡 𝑠 𝑠**

Doorlock
Wall pad
Capture + Jamming
𝑈𝑈𝑡 𝑡 𝑠 𝑠 𝑠 𝑠 = 𝑡𝑡
Capture
Last Accepted Counter = n+1 𝑈𝑈𝑡 𝑡 𝑠 𝑠 𝑠 𝑠 = 𝑡𝑡+ 1
Consecutive signals Sending
𝑈𝑈𝑡 𝑡 𝑠 𝑠 𝑠 𝑠 = 𝑡𝑡
Last Accepted Counter = n+1 𝑈𝑈𝑡 𝑡 𝑠 𝑠 𝑠 𝑠 = 𝑡𝑡+ 1
𝑈𝑈𝑡 𝑡 𝐴𝐴𝑠 𝑠 𝑠𝑠𝐴𝐴𝑠 𝑠 𝑠𝑠 (Last Accepted Counter)
𝑈𝑈𝑡 𝑡 𝑃𝑃𝑠 𝑠 𝑃𝑃 (Previous Counter)

**𝑡 𝑠 𝑡 𝑠 𝑠** _received counter stored ??? Why?_ cnt=n+1 cnt=n+1 𝑈𝑈𝑡 **𝑡** 𝐴𝐴𝑠 **𝑠** 𝑠𝑠𝐴𝐴𝑠 **𝑠** 𝑠𝑠 𝑈𝑈𝑡 **𝑡** 𝑃𝑃𝑠 **𝑠**

cnt=n+1 cnt=n+1 **𝑡 𝑠 𝑠 𝑡 𝑠** cnt=n+1 cnt=n **First signal Sending** 𝑈𝑈𝑡 **𝑡** 𝑠 **𝑠** 𝑠 **𝑠** = 𝑡𝑡 cnt=n+1 cnt=n **Second signal** 𝑈𝑈𝑡 **𝑡** 𝑠 **𝑠** 𝑠 **𝑠** = 𝑡𝑡+ 1 cnt=n+1 cnt=n+1 #BHASIA @BlackHatEvents 𝑈𝑈𝑡 **𝑡** 𝐴𝐴𝑠 **𝑠** 𝑠𝑠𝐴𝐴𝑠 **𝑠** 𝑠𝑠 **has been rolled back**

## Slide 17

# Rollback Attack on Door Lock Demo Video

#BHASIA @BlackHatEvents

## Slide 18

## Loop Playback Attack (Variant)

Doorlock
Wall pad
Capture
(𝑀𝑀𝑖𝑖𝑀𝑀𝑡𝑡𝑀𝑀𝑈𝑈 Capture 1)𝑈𝑈𝑡 𝑡 𝑠 𝑠 𝑠 𝑠 = 𝑡𝑡
Phase 1: Capture Three Consecutive Signals
The follow signals does not have to be strictly consecutive
(𝑀𝑀𝑖𝑖𝑀𝑀𝑡𝑡𝑀𝑀𝑈𝑈2)𝑈𝑈𝑡 𝑡 𝑠 𝑠 𝑠 𝑠 = 𝑡𝑡+ 1
Capture
𝑀𝑀𝑖𝑖𝑀𝑀𝑡𝑡𝑀𝑀𝑈𝑈3 𝑈𝑈𝑡 𝑡 𝑠 𝑠 𝑠 𝑠 = 𝑡𝑡+ 2
Usual Usage of user
Phase 2: Repeating replay of consecutive three signal
𝑀𝑀𝑖𝑖𝑀𝑀𝑡𝑡𝑀𝑀𝑈𝑈1 𝑀𝑀𝑖𝑖𝑀𝑀𝑡𝑡𝑀𝑀𝑈𝑈2 𝑀𝑀𝑖𝑖𝑀𝑀𝑡𝑡𝑀𝑀𝑈𝑈3 𝑏 𝑏 𝑠 𝑠 𝑠𝑠
Transmit to “Valid Counter Buffer Length”
𝑀𝑀𝑖𝑖𝑀𝑀𝑡𝑡𝑀𝑀𝑈𝑈1 𝑀𝑀𝑖𝑖𝑀𝑀𝑡𝑡𝑀𝑀𝑈𝑈2 𝑀𝑀𝑖𝑖𝑀𝑀𝑡𝑡𝑀𝑀𝑈𝑈3 𝑏 𝑏 𝑠 𝑠 𝑠𝑠
#BHASIA @BlackHatEvents
𝑀𝑀𝑖𝑖𝑀𝑀𝑡𝑡𝑀𝑀𝑈𝑈1 𝑀𝑀𝑖𝑖𝑀𝑀𝑡𝑡𝑀𝑀𝑈𝑈2 𝑀𝑀𝑖𝑖𝑀𝑀𝑡𝑡𝑀𝑀𝑈𝑈3 𝑏 𝑏 𝑠 𝑠 𝑠𝑠
…

## Slide 19

# Loop Playback Attack Demo Video

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bidek hat
ASIA &
Loop Playback Attack
Demo Video
#BHASIA @BlackHatEvents
```

## Slide 20

## Rollback attack won't fly!

❏ Most of door locks keep track of the last used code, and  never accept used counter

Rollback Attack
Doorlock
Wall pad
Capture + Jamming
cnt1= n
Wall pad Counter window
Capture + Jamming
Accepted Counter
cnt2= n+1 cnt1=n (reject)
cnt2=n+1(reject)
Capture
Last Accepted counter
cnt3 = n+2
cnt3 = n+2
Accept
Unused Counter
cnt1  (reject “less than n+2” )
cnt2  (reject “less than n+2” )
cnt3  (reject “used code”)
Last Accepted Counter = n+2

#BHASIA @BlackHatEvents

## Slide 21

## Evaluation : Replay Attack

###### ❏ Evaluation on a limited set of door locks(2021~2022)

|**Vendors**|**Models**|**Classic Replay**|**Rolljam**|**Rollback**|**Loop Playback**|**Remarks**||
|---|---|---|---|---|---|---|---|
|**A**|**A-1**|**√**|✗|✗|✗|**Consecutive two**
**signals**||
||**B-1**|**√**|✗|**√**|✗|||
||**B-2**|**√**|✗|**√**|✗|||
|**B**|**B-3**|**√**|✗|**√**|✗|**10 Minute**||
||**B-4**|**√**|✗|**√**|✗|||
||**C-1**|**√**|✗|**√**|**√**|||
|**C**|**C-2**|**√**|✗|**√**|**√**|||
||**C-3**|**√**|✗|**√**|**√**||✗Very weak|
||**D-1**|**√**|✗|**√**|**√**||✗Weak|
|**D**|**D-2**|**√**|✗|**√**|**√**|||
|**E**|**E-1**|✗|||||**√**Moderate|
|**F**|**F-1**|✗|||||**√**Probably safe|
|**G**|**G-1**|✗|**-**|**-**|**-**|**one signal**||
|**H**|**H-1**|✗||||||
|**I**|**I-1**|**√**|✗|**√**|**√**|||
|**J**|**J-1**|**√**|✗|**√**|**√**|||

#BHASIA @BlackHatEvents

## Slide 22

Protect the confidentiality of the code Unveiling the Vulnerabilities in Door Lock RF Encryption Design

#BHASIA @BlackHatEvents

## Slide 23

## Principles of Secure Rolling Code

To ensure Secure Rolling Code transmission (The three critical properties)

1. No transmission is ever repeated

- Each transmitted message should have **different contents**

- Receiver should **ignore messages** that have already been sent

   - Keep track of the last used code

      - ❏ But, re-synchronization should be considered

2. The packet contents are virtually impossible to predict, even if previous messages are known

   - Ultimately, the system should be designed to make it difficult for an attacker to guess and replicate the message

      - ❏ “Serial number(=TxID)" and “sync counter" are the information that needs to be kept confidential

      - ❏ It can only be read by the intended recipient

3. Prevent unauthorized access

- Filtering mechanism, a unique serial number(TxID) is used to achieve

- ❏ TxID should not be guessable and should not appear in a sequential format

#BHASIA @BlackHatEvents

## Slide 24

#### Cipher Key management On 1- Way RF

❏ **Type1:** Pre-programmed cipher key

Type1-1 Fixed Key

   - ❏ The implementation is simple and cost-effective

   - ❏ same cipher key is used across multiple transmitters, increased security risk

   - Type1-2 Random Key

   - ❏ Random like generated cipher keys is used, better protection

   - ❏ **Lost or damaged, a new transmitter cannot be used with the receiver, if not have a learning mechanism**

- ❏ **Type2:** Derives the encryption key by using received data during normal operation

   - ❏ It is more secure than Fixed Key, and more flexible than random key

   - ❏ **<u>This method requires additional security measures for enhancing</u>**

- ❏ **Type3:** Transmit key generation seed value at learning time

   - ❏ The receiver uses this seed value to derive the same encryption key

   - ❏ During normal operation, attacker will not have any information about the encryption key used

#BHASIA @BlackHatEvents

## Slide 25

## AES-based Door Lock RF Encryption

- ❏ Using hardcoded values for the IV and plaintext in every key generation operation

###### ❏ The values are hard-coded in code area

Stack Area
0x00, 0x01,0x02, 0x03, 0x04…..0x0e 16
𝑀𝑀 1 , 𝑀𝑀 2 , . . . , 𝑀𝑀
IV
Key2
Key1 AES-ENC AES-DEC
Data Area
Mode CBC AES
IV
Key generation step 𝐶𝐶1
Message  Decryption
𝑃𝑃

#BHASIA @BlackHatEvents

## Slide 26

## The Flaws in Key Generation

❏ Derives the encryption key by using received data during normal operation

**If M[0] ‘1’ is even**

Received Packet 17-Bytes AA CA BE 63 39 FE 06 BF 10 72 52 2C 6A 8B D7 C2 78 **AA = b’1010_1010 (number of bit 1 is EVEN)** Generated Key1 16-Bytes

= **AA AB AC AD AE AF B0 B1 B2 B3 B4 B5 B6 B7 B8 B9**

**If M[0] ‘1’ is odd**

Received Packet 17-Bytes BC 0E 2C 19 35 44 1B F7 52 1D 43 6D 0A 10 C6 20 DA **BC = b’1011_1100 (number of bit 1 is ODD)** ~ 0xBC = 0x43 (Bit inversion)

**If M[0] ‘1’ is even** 0 + 15} **If M[0] ‘1’ is even** 𝐭 **𝐭** 𝐎 key1 = 𝑀𝑀 0 , 𝑀𝑀 0 + 1, 𝑀𝑀 0 + 2, … 𝑀𝑀 0 + 15} **then** key1 = ~𝑀𝑀 0 , ~𝑀𝑀 0 + 1, ~𝑀𝑀 0 + 2, … ~𝑀𝑀 **Little trick, confusion to an attacker**

**= 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F 50 51 52**

#BHASIA @BlackHatEvents

## Slide 27

## Inadequate Security of LUT-Based Key Generation

###### ❏ Key1  LUT[sync counter]

- The tables have fixed values across all product lines. not derived by secret.(pre-set and static)

|𝐿𝑈𝑇𝑖|𝐿𝑈𝑇𝑖
p[0]
|C[0]|C[1]|C[2]
C[3]|C[4]
C[5]|C[6]|C[7]
…
|C[14] C[15]
𝐶||
|---|---|---|---|---|---|---|---|---|---|
|𝐿𝐿𝑈𝑈𝑇𝑇[𝑖𝑖|𝐿𝑈𝑇𝑖]
Encryption Ke|y See|d||**B**|**aseban**|
**d Data =**|{Key1[0] ||𝐶𝐶2}||
|𝐿𝑈𝑇𝑖|𝐿𝑈𝑇𝑖||||**j**|**Upper**|**_Nibble**
|**Lower_Nibble**
𝐶|**E.g., Table[j]**|
|𝐿𝑈𝑇𝑖|𝐿𝑈𝑇𝑖||||0x00||0|8|0x08|
||||||0x01||1|E|0x1E|
||||||0x02||0|1|0x02|
||||||0x03||1|8|0x19|
||||||0x04||0|E|0x0F|
||||||31
**_For_**_i_∈_0,_|_2, 4, 6,_|1
_8, 10, 12, 14_|5|0x16|
||||||**_Fo_**|**_r_**_(j = 0 : 3_|_1)_|||
|||||||_(Upp_|_er_Nibble[ j ]_|_+ i ) << 4  | Lower_|__Nibble [ j ]_|

**256 Byte Loockup Table**

**LUT Generation Method**

#BHASIA @BlackHatEvents

## Slide 28

### Counter as Key Generation Seed

- ❏ **<u>The Encryption key seed is also used to sync counter</u>**

- ❏ The key seed is exposed on is being transmitted in plaintext

   - ❏ An attacker could decrypt ciphertext at any time

- ❏ It rely on the secrecy of the encryption scheme and key generation mechanism

   - ❏ It may potentially allow an attacker to break other devices that use the similar implementation

###### **Inferred Encryption scheme**

###### **Sync Counter**

###### **Plaintext**

…
p[0] p[1] p[2] p[3] p[4] p[5] p[6] p[7] p[14] p[15]
Encryption
Ciphertext
…
p[0] C[0] C[1] C[2] C[3] C[4] C[5] C[6] C[7] C[14] C[15]
Baseband Data =
Encryption Key Seed
{Key1[0] ||  𝐶𝐶2 }
Identical Value

#BHASIA @BlackHatEvents

## Slide 29

### **Packet Format** Proprietary Cipher on Door Lock

- ❏ Transmit cipher key at learning time

   - ❏ Preprogrammed 8-byte key for 8 rounds, with the 5th key being exposed in the packet for 2 rounds

   - ❏ This cipher is to use a combination of substitution and operator table to generate a rolling counter

###### **Packet Structure**

|`ID[0]`|`ID[1]`|`ID[2]`|`ID[3]`|**`CNT[0]`**|**`CNT[1]`**|**`CNT[2]`**|**`CNT[3]`**|**`CNT[4]`**|**`CNT[5]`**|**`CNT[6]`**|**`CNT[7]`**|`CMD`
**8~9 Rou**|**`Key[4]`**
**nd Encryption Key**|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

**Load from EEPROM**

|**Mem**|𝐼𝑀𝑡𝑀
**ory**|
|---|---|
|BANK1|𝐼𝐼𝑀𝑀𝑡𝑡𝑀|
|29h|𝐼𝑀𝑡𝑀
60|
|2Ah|𝐼𝑀𝑡𝑀
EF|
|2Bh|DF|
|2Ch|13|
|2Dh|00|
|2Eh|00|
|2Fh|00|
|30h|00|
|31h|00|
|32h|00|
|33h|58|
|34h|47|

If Key[4] 0x2D
Preprogramed 8Byte Key 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
03 0C 11 49 6B 3B E5 75 8D C1 15 79 47 C9 E7 57
Lookup C7 83 61 17 5D 49 D1 89 AD 2F 2B 8F 59 27 A7 63
Key[i] & 0x0F
(Lower Nibble)
89 0D 1F 5B 4D BD 65 0B 1D 53 43 9F D5 B7 6F F7 Operand1
D7 B3 F1 83 BF 95 25 99 81 A3 EB D9 35 05 13 FD
8-Byte Key
(1~8Round) T1: Byte Substitution Table
and If Key[4]0x2D Calculation
Key[4] 00 10 20 30 40 50 60 70 80 90 A0 B0 C0 D0 E0 F0
(9~10Round)
ADD SUB XOR -1 +1 NOT NOT +1 -1 XOR SUB ADD XOR -1 ADD NOT
Key[i] & 0xF0 Lookup update
SUB XOR +1 ADD NOT XOR ADD ADD SUB ADD NOT XOR SUB NOT ADD -1
(Upper Nibble)
ADD ADD SUB XOR ADD NOT +1 ADD XOR NOT SUB ADD NOT +1 SUB ADD
Total 10 Round XOR XOR NOT SUB SUB ADD XOR NOT +1 ADD ADD XOR ADD XOR NOT XOR
Operand2
Operator

###### **T2: Operator(Arithmetic+Logical) Table**

#BHASIA @BlackHatEvents

## Slide 30

## Monotonous Pattern of Code

❏ The consistent pattern code may be due to the absence of a permutation feature

- ❏ The generated rolling counter has a somewhat monotonous pattern, making it easy for attackers to predict

06 9E EC 77 54 B7 B1 5B D8 26 3D 25 62 42 35 2D
+0x71 +8F-4 -8F+2
07 0F EC 77 54 B7 B1 5B D8 B1 3D 25 62 B5 35 2D
+0x71 +8F -8F-2
07 80 EC 77 54 B7 B1 5B D8 40 3D 25 62 24 35 2D
+0x71 -1 +8F+4 +1 -8F-6
07 F1 EC 77 54 B7 B1 5B D7 D3 3D 25 63 8F 35 2D
+0x71 +8F -8F+6
08 62 EC 77 54 B7 B1 5B D7 62 3D 25 63 06 35 2D
+0x71 +8F-4 +1 -8F+2
08 D3 EC 77 54 B7 B1 5B D6 ED 3D 25 64 79 35 2D
EEPROM
Counter +0x71 +8F -8F-2
09 44 EC 77 54 B7 B1 5B D6 7C 3D 25 64 E8 35 2D
+0x71 -1 +8F+4 +1 -8F-6
09 B5 EC 77 54 B7 B1 5B D5 0F 3D 25 65 53 35 2D
+0x71 +8F -8F+6
09 B5 EC 77 54 B7 B1 5B D5 9E 3D 25 65 CA 35 2D
+0x71 -1 +8F-4 +1 -8F+2
0A 26 EC 77 54 B7 B1 5B D4 29 3D 25 66 3D 35 2D
+0x71 +8F -8F-2
0A 97 EC 77 54 B7 B1 5B D4 B8 3D 25 66 AC 35 2D
+0x71 +8F+4 -8F+6
0B 08 EC 77 54 B7 B1 5B D44 4B 3D 25 666 17 35 2D

**TxID Sync Counter Command Key[4]**

EC 77 54 B7 B1 5B D44 4B 3D 25 666 17 35 2D
#B HASIA @BlackHatEvents

## Slide 31

## Evaluation : Confidentiality

###### ❏ Evaluation on a limited set of doorlocks

###### ❏ All models are vulnerable to picking the lock with sniffed RF packets

|**Vendors**|**Models**|**Algorithm**|**Confidentialit**|**y**
**Remarks**||
|---|---|---|---|---|---|
|**A**|**A-1**|AES-128|✗|||
||**B-1**|AES-128|✗|||
|**B**|**B-2**|AES-128|✗|||
||**B-3**|AES-128|✗|1Dii th ti k f id dt||
||**B-4**|AES-128|✗|) ervng e encrypon ey rom receve aa
||
||**C-1**|AES-128|✗|2) Sync counter is leaked on Packet
||
|**C**|**C-2**|AES-128|✗|3) Key Seed is leaked on Packet||
||**C-3**|AES-128|✗||✗Compromised|
||**D-1**|AES-128|✗|||
|**D**|**D-2**|AES-128|✗||✗Potentially compromise|
|**E**|**E-1**||||**√**Probably safe|
|**F**|**F-1**|||||
|**G**|**G-1**|None|✗|-||
|**H**|**H-1**|||||
|**I**|**I-1**|XTEA|✗|1) Pre-programmed Fixed Key(Hardcoded)||
|**J**|**J-1**
**J-2**|Proprietary
Encryption|✗|1)Pre-programmed random key is transmitted at learning time
2) It is feasible to deduce the next code from the packet
3)Serial Number(=TxID)is leaked toplaintext||

#BHASIA @BlackHatEvents

## Slide 32

###### Authentication in RF-based Door Locks

The crucial of ID in RF system

#BHASIA @BlackHatEvents

## Slide 33

## Principles of Secure Rolling Code

To ensure Secure Rolling Code transmission (The three critical properties)

1. No transmission is ever repeated

- Each transmitted message should have **different contents**

- Receiver should **ignore messages** that have already been sent

- Keep track of the last used code

❏ But, re-synchronization should be considered

2. The packet contents are virtually impossible to predict, even if previous messages are known

- Protect the confidentiality of the rolling code (Encryption Algorithm)

❏ "TxID" and "rolling counter" are the information that needs to be kept confidential

❏ It can only be read by the intended recipient

3. Prevent unauthorized access

❏ Serial Number is learning information in most of door lock, ID verification is a common method for authorizing

❏ Serial Number (=ID)  should not be guessable and should not appear in a sequential format

#BHASIA @BlackHatEvents

## Slide 34

## Authentication check

###### ❏ Filtering mechanism, a unique serial number(TxID) is used to achieve

###### ❏ When a valid message is received, the message is decrypted, and the serial number is used to determine if it is from a learned transmitter. If it is from a learned transmitter, the synchronization counter is verified

Received Message numbers indicate the order of execution.
(1)Decryption
Encrypted Data
Algorithm
(5) Perform
Lock/Unlock
Sync Counter TxID Operation Checksum
Checksum
(2) Check
Learned TxID
for Match
(3) Check
Sync Counter
for Match
Non-volatile Area
(4) Check
for Match

#BHASIA @BlackHatEvents

## Slide 35

## Packet Confusing before Encryption

❏ It may be difficult to keep track of the original order of the elements

Encryption Key Seed

p[0] **p[1] p[2] p[3] p[4] p[5] p[6]** p[7] p[8] p[9] p[10] p[11] p[12] p[13] p[14] p[15] **Confusing Area S1 (Original order of the elements) p[1] p[2] p[3] p[4] p[5] p[6] S2 p[3] p[6] p[1] p[4] p[2] p[5] S3 p[4] p[2] p[5] p[1] p[6] p[3]**

**Vendor-specific**

###### **3-States (vendor-specific)**

###### **Circular Shift based confusing**

#BHASIA @BlackHatEvents

## Slide 36

## Sequential ID values

❏ TxID(=Serial Number) should not be guessable and should not appear in a sequential format

❏ If the TxID values are sequential or predictable, the attacker can easily predict the next door’s value

❏ Actual TxID changed by only 2~3Bytes, the number of possible values is significantly reduced ❏ It is important to use unique and non-sequential TxID values to prevent potential attacks. 1<sup>= {0xBA, 0xA4, 0x0A, 0xA6}</sup> **Vendors Models Serial Number Remarks A A-1** ✗ ≈ 2.5 ~ 3Bytes 2<sup>= {0xBA, 0xA3, 0x0A, 0x43}</sup> **B-1** ✗ **B-2** ✗ 𝑇𝑇𝑥𝑥𝐼 3<sup>= {0xBA, 0xA6, 0x08, 0x6C}</sup> **B B-3** ✗ 𝑇𝑇𝑥𝑥𝐼 4<sup>= {0xBA, 0xA2, 0x09, 0x5E}</sup> **B-4** ✗ 𝑇𝑇𝑥𝑥𝐼 **C-1** ✗ ≈ 2 Bytes ✗ Very Weak 5<sup>= {0xBA, 0xA4, 0x09, 0xC4}</sup> **C C-2** ✗ 𝑇𝑇𝑥𝑥𝐼 6<sup>= {0xBA, 0xA4, 0x06, 0xC4}</sup> **C-3** ✗ ✗ Weak 𝑇𝑇𝑥𝑥𝐼 **E.g., Vendor B D-1** ✗ **D √** Moderate **D-2** ✗ 𝑇𝑇𝑥𝑥𝐼 1<sup>= {0x95, 0xA5, 0x28, 0xAE}</sup> **E E-1** ✗ ≈ 3 Bytes **√** Strong 2<sup>= {0x95, 0xA4, 0x26, 0xFC}</sup> **F F-1** ✗ **G G-1** ✗ 𝑇𝑇𝑥𝑥𝐼 3<sup>= {0x95, 0xA4, 0x1B, 0xDB}</sup> ≈ 2.5 ~ 3Bytes **H H-1** ✗ 𝑇𝑇𝑥𝑥𝐼 4<sup>= {0x95, 0xA5, 0x26, 0xAE}</sup> **I I-1** ✗ **J J-1 √** ≈ 4 Bytes 𝑇𝑇𝑥𝑥𝐼 **E.g., Vendor A** 𝑇𝑇𝑥𝑥𝐼

|**Vendors**|**Models**|**Serial Number**|**Remarks**||
|---|---|---|---|---|
|**A**|**A-1**|✗|≈2.5 ~ 3Bytes||
||**B-1**|✗|||
||**B-2**|✗|||
|**B**|**B-3**|✗|||
||**B-4**|✗|||
||**C-1**|✗|≈2 Bytes|✗Very Weak|
|**C**|**C-2**|✗|||
||**C-3**|✗||✗Weak|
||**D-1**|✗||**√**|
|**D**|**D-2**|✗||Moderate|
|**E**|**E-1**|✗|≈3 Bytes|**√**Strong|
|**F**|**F-1**|✗|||
|**G**|**G-1**|✗|||
|**H**|**H-1**|✗|≈2.5 ~ 3Bytes||
|**I**|**I-1**|✗|||
|**J**|**J-1**|**√**|≈4 Bytes||

#BHASIA @BlackHatEvents

## Slide 37

###### Technical Details of RF Lockpicking Tool Tools for RF Capture, Decoding, and Transmission

#BHASIA @BlackHatEvents

## Slide 38

### An overview of making a RF lock picking tool set

❏ The RF Lock Picking tool set : **CodeCatcher** + **CodeCrusher**

- ❏ **CodeCatcher** : The sniffer could include for demodulation, decoding, descrambling, decrypt, digital data recording

❏ **CodeCrusher** :The transmitter includes the reverse of the above functions, replaying signals or sending custom signals

###### **Essential Information gathering**

x
x

**3) Baseband Decoding 4) Examine Packet And Symbol Mapping Structure**

**1) RF parameter 2) Training sequence Measurement confirmation**

**Two method for making RF Lock Picking tool set**

**RF Chip + MCU (Cost Effective & Easier to conceal & multiple deployment)**

**SDR + GNURadio (Performance & Flexible)**

#BHASIA @BlackHatEvents

## Slide 39

## Viewing Door Lock RF Signal

- ❏ Center frequency  : 447.274 MHz  or 447.261 MHz

- ❏ Modulation and Deviation : 2KHz Fix (Regulation)

Spectrogram

Model 1 Model 2 Model 3 Model 4 Model 5 Model6
F1= 447.2779 F1=447.2777 F1=447.2777 447.2786 447.2778 447.2716
F2=447.2723 F2=447.2719  F2=447.2721 447.2744 447.2718 447.2752

###### Discontinues Phase

Discontinues Phase
Time Domain
F2 F1

Discontinues Phase
Time Domain
F2 F1

F2 F1
Deviation Frequency :  ≈ 2KHz

#BHASIA @BlackHatEvents

## Slide 40

❏

## Viewing RF Baseband

- ❏ URH can provide insights for base band analysis, without any RF knowledge

   - ❏ But, It may be impractical to continuously monitor and collect signals for our real-world attack

- ❏ Tapping into the connection between the RF IC and MCU is also best option

- ❏ PS. Small deviation frequency might cause interference in the IF signal

   - ❏ Note : Super heterodyne receiver, HackRF one, the optimal deviation frequency was found to be 100Khz or higher **USRP**

PlutoSDR

**Tapping into the connection between the RF IC and MCU**

HackRF

#BHASIA @BlackHatEvents

## Slide 41

#### Training Sequence for custom packet

- ❏ Vendor-specific training sequence for timing synchronization

- The preamble and syncword generated by the RF chip handler are not used in door locks
Training Sequence
Chip Preamble Chip SyncWord Len
Vendor 1
They send the packets(burst) a couple times (for robustness)
Soft  Soft  Training Sequence Vendor 2
SYNC DATA END SYNC DATA …
Training Sequence Vendor 3
Rx (Captured in door lock side)
Tx (Wallpad Transmission)
Training Sequence Vendor 4
Training Sequence Vendor 5
Chip  Chip  SYNC
Preamble

Soft SYNC Detection (Compare Pattern & Duration)
If there is a match, the data is accepted

**Training Sequence**

#BHASIA @BlackHatEvents

## Slide 42

## Proprietary Baseband Encoding

❏ Vendor-specific digital encodings in RAW transmission mode

Vendor J
Proprietary 0 0 1 1 0 1 Tapping into the connection between the RF IC and MCU
(Little Endian)
variable-length
encoding
Vendor A
Proprietary 1 0 0 0 0 1
(Big Endian)
variable-length
encoding
Vendor B 𝑡𝑡1 𝑡𝑡2 𝑡𝑡3
Proprietary 1 0 0 0 0 1
(Big Endian)
t1 t1
Fixed-length
PreambleGenuineSYM 1
encoding
Vendor I t2 t2
Manchester 1 0 0 0 0 0 0 0 1
Bit 0SYM 2
(Little Endian)
t3 t3
Bit 1SYM 3

Tapping into the connection between the RF IC and MCU

t1
t2
t3 t3
#BHASIA @BlackHatEvents

## Slide 43

## Let’s make it

$10~(excluding battery)

$18~(excluding battery)

(Cost Effective & Easier to conceal & multiple deployment)

$200~(excluding Laptop)
SDR
(Performance & Flexible)

#BHASIA @BlackHatEvents

## Slide 44

## Configuring RF Chip for Direct Mode

❏ Validate through signal debugging for RF parameter decision

- ❏ According to Transmission Mode..

   - ❏ Direct Mode(Aka. RAW transmission mode)

      - Received RXDATA is output on a physical output pin in real-time

**DATA CLK**

Choosing Chips that Support Direct Mode
Direct / Packet (o) Packet Mode Only  Direct Mode Only (o)
(x)
CMOSTEK  Analog Device  Melexis
CMT2219B/CMT2300 MAX4147 TH71101/71120
Silicon LABS  CMOSTEK  Analog Device
Si4455x/443x CMT2217 MAX7042
TI CC1000/1101 TI CC1125 -
TDA 5150 - -

❏ Packet Mode

- The data is packaged into a specific format

SYM1 SYM2 SYM3
Chip Demod.
Signal
Transmitter
B.B. Signal

Debugging

𝐼𝐼𝑠𝑠 = 447.274 MHz Data rate: Don’t care Deviation: 2KHz tolerance range ±2 Mode : Direct Mode

**When analog debugging is complete, export the configuration file**

RF Config. Value

#BHASIA @BlackHatEvents

## Slide 45

❏

## Portable Door Lock RF Sniffer

❏ Depending on the HW Spec and sampling rate, capture and store either four or more signals of a door lock

❏ Using an 1800mAh battery, can run for approximately 90 hours(3.75Days)

RFM219S
DATA Sub 1GHz Rx IC
$3
Arduino Uno
(For RF chip settings)
$5(copy)

RFM219S
DATA Sub 1GHz Rx IC
$3
Arduino Uno
(For RF chip settings)
Total Cost  $5(copy)
< $20(Batt. x)
5v 1800mAh Poly
SRAM 8K, EEPROM 4K
(For Capture & Store)
$10(copy)
Capture access
Retrieve
Wake On Radio
To file
Store
Demod

###### **Retrieval of captured data**

**Target Training Symbol**

**EEPROM  Readout**

**Write signal to EEPROM**

access
Retrieve readout
To file

1) Suffixed at a hidden spot

2) Capture and store to EEPROM

3) Retrieve and EEPROM Readout

**4) Decode and Decrypt** #BHASIA @BlackHatEvents

## Slide 46

### : RF IC Based Tx

$5
Total Cost
< $10
"It can be attached near by target, and the operating time can be extended as  $3
much as desired depending on the Lithium Polymer Battery that is installed."
ANT
Lock pick Mode
𝐏 𝐏 𝐃 𝐃 𝐎𝐎𝐭𝐭𝟑𝟑 = {𝑼𝑼𝑺𝑺𝑽𝑽𝑼𝑼𝒄𝒄𝑼𝑼𝒄𝒄𝑼𝑼𝑺 𝑺 𝒄𝒄 ,  𝑼𝑼𝑺𝑺𝑽𝑽𝑼𝑼𝒄𝒄𝑼𝑼𝒄𝒄𝑼𝑼𝑺 𝑺 𝒄𝒄 }
𝐏 𝐏 𝐃 𝐃 𝐎𝐎𝐭𝐭𝒄𝒄 = {𝑼𝑼𝑺𝑺𝑽𝑽𝑼𝑼𝒄𝒄𝑼𝑼𝒄𝒄𝑼𝑼𝑺 𝑺 𝒄𝒄 ,  𝑼𝑼𝑺𝑺𝑽𝑽𝑼𝑼𝒄𝒄𝑼𝑼𝒄𝒄𝑼𝑼𝑺 𝑺 𝒄𝒄 }
𝐏 𝐏 𝐃 𝐃 𝐎𝐎𝐭𝐭𝑺𝑺 = {𝑼𝑼𝑺𝑺𝑽𝑽𝑼𝑼𝒄𝒄𝑼𝑼𝒄𝒄𝑼𝑼𝑺 𝑺 𝒄𝒄 ,  𝑼𝑼𝑺𝑺𝑽𝑽𝑼𝑼𝒄𝒄𝑼𝑼𝒄𝒄𝑼𝑼𝑺 𝑺 𝒄𝒄 }
CLK
$20
Sniff and Unlock Mode
RF Chip Programmer
𝐏 𝐏 𝐃 𝐃 𝐎𝐎𝐭𝐭𝟑𝟑 = 𝑼𝑼𝑺𝑺𝑽𝑽𝑼𝑼𝒄𝒄𝑼𝑼𝒄𝒄𝑼𝑼𝑺 𝑺 𝒄𝒄 = 𝐎 𝐎 𝐃𝐃(𝒄𝒄𝑺𝑺𝒕𝒕𝑺 𝑺 𝒏𝒏𝒕𝒕, 𝒕𝒕𝒏𝒏𝑽𝑽𝑺𝑺, 𝒄𝒄𝒆𝒆)
Suffixed at a hidden spot #BHASIA @BlackHatEvents
VDD GND

###### **"It can be attached near by target, and the operating time can be extended as much as desired depending on the Lithium Polymer Battery that is installed."**

#BHASIA @BlackHatEvents

## Slide 47

## gr-block for Door Lock RF Sniffing

sample rate decision
vendor training sequence
De-glitching

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
ASIA 2023
Options Variable Variable Variable Variable QT GUI Range
Output Language: Python Id: fsk_deviation_hz1 | | Id: frequency Id: variable_O Id: samp_rate | | Id: sample_variable
Generate Options: QT GUI Value: 2k Value: 447.274M Value: 1.618k Value: 2M Default Value: 50
Start: 20
Stop: 250
Step: 1
UHD: USRP Source Low Pass Filter
Sync: Unknown PPS Decimation: 1
Samp rate (Sps): 2M Simple Squelch Gain: 1
ChO: Center Freq (Hz): ...74M Sample Rate: 2M Virtual Sink
command) no: AGC: Default USE AIC) Bae! Cutoff Freq: 20k joi Qurerre Pome een
Cho: Gain Value: 30 meen BE Transition Width: 10k
ChO: Gain Type: Absolute (dB) Window: Hamming
ChO: Antenna: RX2 Beta: 6.76
sample rate decision
Rational Resampler Clock Recovery MM
Interpolation: 1 Threshold Omega: 50
Virtual Source [Sut] Decimation: 2 ‘out [in| Soest Multiply Const | Gain Omega: 7.65625m Virtual Sink
Stream ID: demod o a . High: 10 Constant: 2 Mu: 500m Stream ID: synchro
ET Initial State: 0 Gain Mu: 175m
Omega Relative Limit: 5m
File Sink
File: ...e BHASIA23/164 demod
Unbuffered: Off
Correlate Access Code
Access Code: 11110...11111111
Threshold: 1
Low Pass Filter
eens 1 Append file: Overwrite
in:
Virtual Source Add Const Sample Rate: 2M ini
Stream ID: synchro out Constant: -1 out in Cutoff Freq: 100k vendor training sequence
QT GUI Time Sink
Transition Width: 2k
Window: Hamming
Beta: 6.76
Char To Float
Scale: 1
Char To Float
Scale: 1 ea
QT GUI Time Sink
<Ga| Number of Points: 1.024k
Sample Rate: 2M
Autoscale: No
— | See
in Sample Rate: 2M
Autoscale: No
De-glitching
```

## Slide 48

## configuration for Sniffing

_numbers indicate the order of step._

Correlation Peak
1) Adjust Sampling Freq. based on the  symbol rate
Parameter : 164
2) Update to appropriate value
Generally, Door Locks (50~200)
Syncword
4) Check Correlation
3) Update Vendor’s
Parameter : 50
Syncword Symbol
Syncword

#BHASIA @BlackHatEvents

## Slide 49

## Decode and Decrypt

###### **Capture and Demodulation**

BIN

###### **Demodulated Signal**

**Decode and Decrypt**

###### Transmitter A

###### Transmitter B

Sync Counter

TXID: 95 A4 1B DB

Checksum

Sync Counter

TXID: 95 A5 28 AE

Checksum

#BHASIA @BlackHatEvents

## Slide 50

##### gr block based Tx : Encode and Transmit

Encoded data

Simple BFSK TX using VCO

Message
Encrypt and Encoding

**Adjust to match the target symbol rate**

#BHASIA @BlackHatEvents

## Slide 51

###### Practical Attack

###### The Art of RF Lock Picking

#BHASIA @BlackHatEvents

## Slide 52

## Two Types of Lock Picking

###### ❏ Type1:  Sniff and unlock

- ❏ The attacker extracts the “ID” and “synchronous counter” and generates a new code

- **※ Attacker know “current synchronous counter” value, and is expected to know the next value**

2) Extract ID and Sync Counter  Capture  Demodulation Decoding
RAW Signal
Code Catcher Mini Code Catcher SDR
or SDR
Final Data Descrambling Decryption
3) Extract ID, Sync Counter
5) Send unlock signal
1) Sniffing lock or unlock Signal
RAW Signal Modulation Encoding
Code Crusher Mini Code Crusher SDR
or SDR
Packet Scrambling Encryption
Wallpad
4) Generate new Code

- ❏ Type2: Lock picking - Without Sniffing (=Brute Force Attack)

   - ❏ The attacker generates a new code by only changing the ID(=Serial Number) value

   - **※ Attacker don’t know “current synchronous counter” value**

2) Send unlock signal
RAW Signal Modulation Encoding
Code Crusher Mini Code Crusher SDR
…
or SDR
Packet Scrambling Encryption
1) Code generation

#BHASIA @BlackHatEvents

## Slide 53

## Lock Picking : Sniff and Unlock

**_Attacker capture and get       ID, cnt_ Wall pad** 𝑈𝑈𝑡𝑡𝑈 **𝑈** 𝑈 𝑈 **𝑈** 𝑣𝑣𝑡𝑡𝑠𝑠𝑜𝑜𝑠𝑠 = 𝑡 **𝑡** 𝑈𝑈(𝑈𝑈𝑡 **𝑡** 𝐴𝐴𝑠 **𝑠** 𝑃𝑃 , ID , 𝑈𝑈𝑀𝑀𝑠𝑠𝑜𝑜𝑠𝑠 ) **_Attacker Send next unlock code_** 𝑈𝑈𝑡𝑡𝑈 **𝑈** 𝑈 𝑈 **𝑈** 𝑣𝑣𝑡𝑡𝑠 **𝑠** 𝑛𝑛 = 𝑡 **𝑡** 𝑈𝑈(𝑈𝑈𝑡 **𝑡** 𝑠 **𝑠** 𝑛𝑛𝑠𝑠 , 𝐼 **𝐼** , 𝑈𝑈𝑀𝑀𝑠 **𝑠** 𝑛𝑛 )

Doorlock

Apartment
2)  𝑪𝑪𝑽𝑽𝑪𝑪𝒕 𝒕 𝑷𝑷𝑺𝑺

3)   𝑺 𝑺 𝑺 𝑽𝑽𝒄𝒄𝑼𝑼𝑺
𝒄𝒄) 𝑼𝑼𝒆𝒆𝑺𝑺𝑷𝑷𝒆𝒆𝑺 𝑺 𝑺𝑺𝒄𝒄𝑼𝑼𝑺

**_Set the reception range_**

**_Deploying the sniffer_**

**_Capture Signal And Extract Data_**

**_Send Signal_**

**_Unlock the door_**

#BHASIA @BlackHatEvents

## Slide 54

# Lock Picking w/ Sniffing Demo Video

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bidek hat
ASIA &
Lock Picking w/ Sniffing
Demo Video
#BHASIA @BlackHatEvents
```

## Slide 55

## Lock Picking : without sniffing

- ❏ This attack involves unlocking the victim's door without the need for any RF sniffing

- ❏ The attack is to find a Serial Number(=TxID) that matches the one used by the door lock.

- ❏ The attacker's message must always be accepted, even if the current counter value is unknown

p3
p2
p1 p4
Doorlock TxID Matching
Decrypted RF Packet

Key  Encryption Key
TxID

**Encrypted RF Packet**

#BHASIA @BlackHatEvents

## Slide 56

Considering Attacker's
Counter Value Selection
Usual acceptance for counter
Accepted If  this counter chosen by the attacker (Reject) 𝑅𝑅𝑡𝑡𝑈𝑈𝑡𝑡𝑖𝑖𝑣𝑣𝑡𝑡𝑀𝑀𝑡𝑡𝑀 𝑀 𝑀 𝑀 𝑡𝑡
Counter
𝑅𝑅𝑡𝑡𝑅𝑅𝑡𝑡𝑈𝑈𝑡𝑡
Last Accepted counter 𝑡𝑡𝑥𝑥𝑖𝑖𝑣𝑣𝐴𝐴𝑠 𝑠 𝑃𝑃 ==yes𝑡𝑡𝑥𝑥𝑖𝑖𝑣𝑣𝑠 𝑠 𝑠𝑠𝑃𝑃
END
(Attacker doesn’t know)
If  this counter chosen by the attacker (Accept) N𝑈𝑈
𝑃𝑃[1]𝐴𝐴𝑠 𝑠 𝑃𝑃 == 𝑃𝑃[1]𝑠 𝑠 𝑠𝑠𝑃𝑃
yes
Window N Window N-1
(Attacker doesn’t know)
∃𝑖𝑖(𝑖𝑖≤|𝐿𝐿𝑈𝑈𝑇𝑇| ∧𝐿𝐿𝑈𝑈𝑇𝑇[𝑖𝑖] = 𝑈 𝑈 𝑐𝑐𝑡 𝑡 _𝑟𝑟𝑡𝑡𝑈𝑈𝑣𝑣) ∃𝑖𝑖(𝑖𝑖≤|𝐿𝐿𝑈𝑈𝑇𝑇| ∧𝐿𝐿𝑈𝑈𝑇𝑇[𝑖𝑖]yes = 𝑈 𝑈 𝑐𝑐𝑡 𝑡 _𝑟𝑟𝑡𝑡𝑈𝑈𝑣𝑣)
Reject
𝑖𝑖𝑗𝑗 = 𝑖𝑖, 𝑅𝑅= 𝑅𝑅+ 1 𝑖𝑖𝐴𝐴𝑠 𝑠 𝑃𝑃 < 𝑖𝑖
cnt =< Last Accepted Counter
N𝑈𝑈
cnt > Last Accepted Counter 𝑅𝑅> 3
yes
Accept
𝐴𝐴𝑈 𝑈 𝑡𝑡𝐴𝐴𝑡𝑡
𝑹𝑹𝑺𝑺𝑹𝑹𝑺𝑺𝒄𝒄𝒕𝒕
(𝑖𝑖0 == 𝑖𝑖0 + 1) ∧(𝑖𝑖2 == 𝑖𝑖1 + 1)
𝐼
#BHASIA @BlackHatEvents
𝑇𝑇𝑟𝑟𝑐𝑐𝑡𝑡: 𝐴𝐴𝑈 𝑈 𝑡𝑡𝐴𝐴𝑡𝑡

## Slide 57

## Re-Synchronization and Acceptable Counter Range

- ❏ There is always the possibility that the transmitter has been activated several times outside the receiver's range, the receiver must accept values

- ❏ To address this issue, many door locks have a synchronization function that allows them to accept in a specific range of counter values

   - ❏ Door locks will not accept a large counter value exceed to specific range

Accepted
Counter

END

Last Accepted counter

**_If  this counter would be accept Acceptable range_**

Doorlock
Owner try
cnt=n
Last Accepted Counter = n
Owner try Interference
cnt=n+1
….
cnt = n+k
Owner try
cnt = n+k+1
cnt = n+k+2
Last Accepted Counter = n+k+2

#BHASIA @BlackHatEvents

## Slide 58

## Force Synchronization

𝑅𝑅𝑡𝑡𝑈𝑈𝑡𝑡𝑖𝑖𝑣𝑣𝑡𝑡𝑀𝑀𝑡𝑡𝑀 𝑀 𝑀 𝑀 𝑡𝑡
Within the same window  (=p[1]),
𝑅𝑅𝑡𝑡𝑅𝑅𝑡𝑡𝑈𝑈𝑡𝑡
never accept used counter N𝑈𝑈 𝑡𝑡𝑥𝑥𝑖𝑖𝑣𝑣𝐴𝐴𝑠 𝑠 𝑃𝑃 ==yes𝑡𝑡𝑥𝑥𝑖𝑖𝑣𝑣𝑠 𝑠 𝑠𝑠𝑃𝑃
𝑃𝑃[1]𝐴𝐴𝑠 𝑠 𝑃𝑃 == 𝑃𝑃[1]𝑠 𝑠 𝑠𝑠𝑃𝑃
yes
∃𝑖𝑖(𝑖𝑖≤|𝐿𝐿𝑈𝑈𝑇𝑇| ∧𝐿𝐿𝑈𝑈𝑇𝑇[𝑖𝑖] = 𝑈 𝑈 𝑐𝑐𝑡 𝑡 _𝑟𝑟𝑡𝑡𝑈𝑈𝑣𝑣) ∃𝑖𝑖(𝑖𝑖≤|𝐿𝐿𝑈𝑈𝑇𝑇| ∧𝐿𝐿𝑈𝑈𝑇𝑇[𝑖𝑖]yes = 𝑈 𝑈 𝑐𝑐𝑡 𝑡 _𝑟𝑟𝑡𝑡𝑈𝑈𝑣𝑣)
𝑖𝑖𝑗𝑗 = 𝑖𝑖, 𝑅𝑅= 𝑅𝑅+ 1 𝑖𝑖𝐴𝐴𝑠 𝑠 𝑃𝑃 < 𝑖𝑖
"This is sent as three consecutive codes, but the
N𝑈𝑈
𝑅𝑅> 3yes number of codes sent for resynchronization may
vary between vendors."
𝐴𝐴𝑈 𝑈 𝑡𝑡𝐴𝐴𝑡𝑡 𝑅𝑅𝑡𝑡𝑅𝑅𝑡𝑡𝑈𝑈𝑡𝑡
(𝑖𝑖0 == 𝑖𝑖0 + 1) ∧(𝑖𝑖2 == 𝑖𝑖1 + 1)
#BHASIA @BlackHatEvents
𝐼
𝑇𝑇𝑟𝑟𝑐𝑐𝑡𝑡: 𝐴𝐴𝑈 𝑈 𝑡𝑡𝐴𝐴𝑡𝑡

p[0] p[1] p[2] p[3] p[4] p[5] p[6] p[7] p[8] p[9] … p[15]
TxID(=Serial Number) CS
cnt
𝑳𝑳𝑼𝑼𝑪𝑪[𝑽𝑽] Window
Resynchronization for Attack
Send consecutive Code
to another window
Accept & Resynchronized
Accept, but not permitted
Start
Unused Counter
Choose New Window p[1]

**Minimizing the transmission packets necessary for resynchronization is crucial factor**

## Slide 59

## Packet count for Force Synchronization

❏ The number of consecutive code transmissions required for force synchronization

❏ It is an important factor for increasing overall attack time

###### **_Test Method_**

Wall pad Doorlock
1)
𝑀𝑀(𝑈𝑈𝑡 𝑡 𝑠 𝑠 𝑠 𝑠 = 𝑡𝑡)
SDR
2)
𝑀𝑀(𝑈𝑈𝑡 𝑡 𝑠 𝑠 𝑠 𝑠 = 𝑡𝑡+ 𝑈𝑈+ 𝑖𝑖)
∃k (k > n + 256)
i = i + 1

###### **_Code Counts for force resynchronization_**

|**Vendors**|**Models**|**code count for force resync.**
**max(i)**|
|---|---|---|
|A|A-1|**1 or 2**|
||B-1|**3**|
||B-2|**3**|
|B|B-3|**3**|
||B-4|**3**|
||C-1|**2**|
|C|C-2|**2**|
||C-3|**2**|
||D-1|**2**|
|D|D-2|**2**|
|I|I-1|**1**|
|J|J-1|**1**|

#BHASIA @BlackHatEvents

## Slide 60

## Lock Picking Attack Scenario

**Case : Vendor B**

**_(The products Send Three Consecutive Code for Re-synchronization)_**

Hallway
Suffixed at a hidden spot

###### **_Attack Scenario_**

**Attach RF lock pick tool in the ventilation And catch the Door Lock sound**

Deploying

𝑀𝑀𝑡𝑡𝑀 **𝑀** 𝑀 **𝑀** 𝑡𝑡 𝑈 **𝑈 𝑡 𝑡 𝑈 𝑡 𝑡 𝑈 𝑡 𝑡**

- **𝑀 𝑀** 𝑡𝑡 𝑈 **𝑈** 𝑣𝑣𝑡𝑡1 = 𝑡 **𝑡** 𝑈𝑈(𝑈𝑈𝑡 **𝑡** 0 , 𝑤𝑤𝑖𝑖𝑡𝑡𝑣𝑣𝑈𝑈𝑤𝑤𝑁𝑁 , 𝑡𝑡𝑥𝑥𝑖𝑖𝑣𝑣 , 𝑈𝑈𝑀𝑀 ) 𝑈 **𝑈** 𝑣𝑣𝑡𝑡2 = 𝑡 **𝑡** 𝑈𝑈(𝑈𝑈𝑡 **𝑡** 1 , 𝑤𝑤𝑖𝑖𝑡𝑡𝑣𝑣𝑈𝑈𝑤𝑤𝑁𝑁 , 𝑡𝑡𝑥𝑥𝑖𝑖𝑣𝑣 , 𝑈𝑈𝑀𝑀 ) 𝑈 **𝑈** 𝑣𝑣𝑡𝑡3 = 𝑡 **𝑡** 𝑈𝑈(𝑈𝑈𝑡 **𝑡** 2 , 𝑤𝑤𝑖𝑖𝑡𝑡𝑣𝑣𝑈𝑈𝑤𝑤𝑁𝑁 , 𝑡𝑡𝑥𝑥𝑖𝑖𝑣𝑣 , 𝑈𝑈𝑀𝑀 )

- 𝑈 **𝑈** 𝑣𝑣𝑡𝑡1 = 𝑡 **𝑡** 𝑈𝑈(𝑈𝑈𝑡 **𝑡** 0 , 𝑤𝑤𝑖𝑖𝑡𝑡𝑣𝑣𝑈𝑈𝑤𝑤𝑁𝑁 , 𝑡𝑡𝑥𝑥𝑖𝑖𝑣𝑣+ 𝑡𝑡 , 𝑈𝑈𝑀𝑀 ) 𝑈 **𝑈** 𝑣𝑣𝑡𝑡2 = 𝑡 **𝑡** 𝑈𝑈(𝑈𝑈𝑡 **𝑡** 1 , 𝑤𝑤𝑖𝑖𝑡𝑡𝑣𝑣𝑈𝑈𝑤𝑤𝑁𝑁 , 𝑡𝑡𝑥𝑥𝑖𝑖𝑣𝑣+ 𝑡𝑡 , 𝑈𝑈𝑀𝑀 ) 𝑈 **𝑈** 𝑣𝑣𝑡𝑡3 = 𝑡 **𝑡** 𝑈𝑈(𝑈𝑈𝑡 **𝑡** 2 , 𝑤𝑤𝑖𝑖𝑡𝑡𝑣𝑣𝑈𝑈𝑤𝑤𝑁𝑁 , 𝑡𝑡𝑥𝑥𝑖𝑖𝑣𝑣+ 𝑡𝑡 , 𝑈𝑈𝑀𝑀 )

- Vendor B serial number Range is {0xBA, 0xA0, 0x00, 0x00}~ {0xBA, 0xAF, 0x0F, 0xFF} _Total Tx time in the worst case_

- 𝑁𝑁𝑐𝑐𝑁 **𝑁** 𝑡𝑡𝑟𝑟𝑈𝑈𝐼𝐼𝐶𝐶𝑈𝑈𝑣𝑣𝑡𝑡𝑀𝑀: 2 𝐵 **𝐵** 𝑡 **𝑡** 𝑀𝑀= 2<sup>16</sup> = 65536

- **𝑁 𝐵 𝑡**

- _=(Number of Codes_ × _Packet count for Force Sync) / Transmission Rate (MPS)_

**Vendor X**

- _= 65536 * 3 / 5_

**Attacker**

- _= approximately 39321 sec = 10.9 Hours_

#BHASIA @BlackHatEvents

## Slide 61

# Lock Picking w/o Sniffing Demo Video

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bidek hat
ASIA &
Lock Picking w/o Sniffing
Demo Video
#BHASIA @BlackHatEvents
```

## Slide 62

###### Discussion and Conclusion

#BHASIA @BlackHatEvents

## Slide 63

## Takeaways

- ❏ Variant Replay Attack

- **“RollJam”** is inevitable without timestamps and **“RollBack”** is also feasible in door lock systems

- Our new variant attack called **"Loop Play Back"** has been confirmed as feasible in door lock systems

- At least in door lock system, the root cause of these attacks is confirmed

- ❏ Lock Picking Attack

- Easily exploitable by picking the lock w/ sniffing one signal

   - If signal archetype is known,  it would be possible to recover the next code with one time

- It may still be vulnerable to open any door lock that's the same model w/o the use of sniffing

   - Depending on the properties of the TxID(=Serial#), it can be more practical to carry out this attack

   - Re-synchronization process is also key factor for brute force attack

- ❏ Easy-to-make and affordable tool

- We provided a diverse set of options to make tools using various methods (from SDR to DIY electronic parts)

- Detailed guide using affordable and easily accessible parts

#BHASIA @BlackHatEvents

## Slide 64

## Lessons Learned

- RF security testing is essential

   - It is an important component of a comprehensive security strategy, especially for systems that rely on wireless

- Security through obscurity is not an answer

   - It's important to design systems that are resilient to attacks even if an attacker knows how they work

- The implementation should be based on elaborate principles and best practices

   - Mutually complementary and interdependent

- Assigning a unique key to each product is a better secure approach in one-way RF

   - If an attacker steals a key from one product, it will not affect communication with other products

   - Of course, using secure encryption algorithms is essential for security.

#BHASIA @BlackHatEvents

## Slide 65

Thank you! If you have any question, please send me email

Kwonyoup Kim CEO/founder kkyoup@sntworks.kr

Seungjoon Lee Senior Researcher sj.lee@sntworks.kr shaftmom@gmail.com

#BHASIA @BlackHatEvents
