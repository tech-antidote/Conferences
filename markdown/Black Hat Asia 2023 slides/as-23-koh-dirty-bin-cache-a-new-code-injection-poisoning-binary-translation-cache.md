---
title: "Dirty Bin Cache A New Code Injection Poisoning Binary Translation Cache"
speakers: ["Koh"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Koh-Dirty-Bin-Cache-A-New-Code-Injection-Poisoning-Binary-Translation-Cache.pdf"
pages: 99
sha256: "30b0670ffe9cb69d4d463d606721f7e416dbc4fdcc82302e1a2a06d2360e3aaa"
text_chars: 43014
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
companion_files: ["AS-23-Koh-Dirty-Bin-Cache-A-New-Code-Injection-Poisoning-Binary-Translation-Cache_POC.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:54:39Z"
---
# Dirty Bin Cache A New Code Injection Poisoning Binary Translation Cache

**Speakers:** Koh  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Koh-Dirty-Bin-Cache-A-New-Code-Injection-Poisoning-Binary-Translation-Cache.pdf` (99 pages)


## Slide 1

# **Dirty Bin Cache: A New Code Injection Poisoning Binary Translation Cache**

##### Koh M. Nakagawa at FFRI Security, Inc.

#BHASIA @BlackHatEvents

## Slide 2

$ whoami – Koh M. Nakagawa (@tsunek0h)

Security Researcher at FFRI Security, Inc.

- Vulnerability research on Arm-based Windows

- Recently started macOS security

- Found multiple vulnerabilities of macOS (TCC/SIP/Gatekeeper bypass)

- Gave talks at BHEU 2020 Briefings and CODE BLUE 2021

GitHub: <u>https://github.com/kohnakagawa</u>

#BHASIA @BlackHatEvents

## Slide 3

## Agenda

- Introduction

- Rosetta 2 internals

- Code injection on macOS: AOT poisoning

- Exploitation on macOS

- A similar code injection on Arm-based Windows: XTA cache poisoning

- Exploitation on Arm-based Windows

- Summary & key takeaways

#BHASIA @BlackHatEvents

## Slide 4

## Arm-based laptops are becoming popular

<u>https://winbuzzer.com/2023/02/12/forecast-arm-cpus-to-reach-25-of-laptop-market-share-by-2027-xcxwbn/</u>

<u>https://learn.microsoft.com/ja-jp/surface/surface-pro-9-overview</u>

<u>https://www.apple.com/jp/mac/</u>

#BHASIA @BlackHatEvents

## Slide 5

## Translation/emulation technologies

###### **X86/x64 emulation**

###### **Rosetta 2**

<u>https://www.youtube.com/watch?v=GEZhD3J89ZE</u>

<u>https://learn.microsoft.com/ja-jp/events/build-2018/brk2438</u>

Translating and emulating are time-consuming. Therefore, reducing these is essential.

#BHASIA @BlackHatEvents

## Slide 6

Binary translation result is cached **How x86 emulation works on Arm (from MSDN)** _x86 emulation works by compiling blocks of x86 instructions into Arm64 instructions with optimizations to improve performance._ **_A service caches these translated blocks of code to reduce the overhead of instruction translation and allow for optimization when the code runs again._** _The caches are produced for each module so that other apps can make use of them on first launch._

<u>https://learn.microsoft.com/en-us/windows/arm/apps-on-arm-x86-emulation</u>

**Rosetta 2 on a Mac with Apple silicon (from Apple Platform Security)** _But the Rosetta runtime then sends an interprocess communication (IPC) query to the Rosetta system service, which_ **_asks whether there’s an AOT translation available for the current executable image. If found, the Rosetta service provides a handle to that translation, and it’s_** <u>https://help.apple.com/pdf/security/en_US/apple-platform-security-guide.pdf</u> **_mapped into the process and executed._**

#BHASIA @BlackHatEvents

## Slide 7

My previous research at Black Hat EU 2020 A new code injection targeting Arm-based Windows Named “XTA cache hijacking”

<u>https://www.blackhat.com/eu-20/briefings/schedule/index.html#jack-in-the-cache-a-newcode-injection-technique-through-modifying-x-to-arm-translation-cache-21324</u>

#BHASIA @BlackHatEvents

## Slide 8

My previous research at Black Hat EU 2020 Code injection by directly modifying X86-to-ARM (XTA) translation cache An attacker can inject malicious code by modifying XTA translation cache

- It requires admin privileges, but it has a unique side effect that benefits an attacker

<u>https://www.blackhat.com/eu-20/briefings/schedule/index.html#jack-in-the-cache-a-new-code-injectiontechnique-through-modifying-x-to-arm-translation-cache-21324</u>

#BHASIA @BlackHatEvents

## Slide 9

## Research motivation

Is there similar code injection for macOS Rosetta 2?

I started to study macOS security and analyzed Rosetta 2 internals

#BHASIA @BlackHatEvents

## Slide 10

## Introduction to macOS security model

System Integrity Protection (SIP) Restricts some dangerous operations such as

- Modifying system files

- Loading kernel extensions

- Debugging system processes

Root user cannot perform these operations

SIP is also known as rootless

- -> Even root does not have full access to system, unlike traditional *NIX security model

#BHASIA @BlackHatEvents

## Slide 11

## Introduction to macOS security model

Even root cannot delete system files

Even root cannot access some files

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
ASIA 20253
Introduction to macOS security model
sh-3.2# csrutil status
System Integrity Protection status: enabled.
sh-3.2# rm -f /bin/1s Even root cannot
rm: /bin/ls: Operation not permitted delete system files
sh-3.2# ls Library/Mail
ls: Library/Mail: Operation not permitted Even root cannot
access some files
```

## Slide 12

## Code injection on macOS

_the alpha and omega of macOS exploits is to run code in the context of other applications - @theevilbit https://theevilbit.github.io/shield/_

#BHASIA @BlackHatEvents

## Slide 13

## Code injection on macOS

Why code injection?

Because macOS security mechanisms heavily rely on code signatures and its entitlements

- On macOS, entitlements grant various rights to the application

`o` E.g., an application needing to access some sensitive resources (camera, mic, messages, …) should have proper entitlements

- If we can execute code in the context of other applications, we can hijack trusts of them

   - So, we can gain the rights of other applications by code injection

- Code injection is strictly prohibited on macOS

   - E.g., hardened runtime is enabled for almost all applications

If we can find a new code injection technique on macOS, we can exploit it to bypass security & privacy mechanisms -> I started to explore code injection abusing Rosetta 2

#BHASIA @BlackHatEvents

## Slide 14

## Rosetta 2 internals & a new code injection

#BHASIA @BlackHatEvents

## Slide 15

## Installing Rosetta 2

Rosetta 2 is not installed by default

When you run an app that needs Rosetta 2, popup is raised

Can also be installed by softwareupdate command like

- softwareupdate --install-rosetta --agree-to-license

Installing Rosetta 2 does not require root privileges

- If not installed, an attacker can install it manually

<u>https://support.apple.com/en-us/HT211861</u>

#BHASIA @BlackHatEvents

## Slide 16

## Quick look at Rosetta 2

**Rosetta 2 on a Mac with Apple silicon (from Apple Platform Security)** _A Mac with Apple silicon is capable of running code compiled for the x86_64 instruction set using a translation mechanism called Rosetta 2._ **_There are two types of translation offered: just in time and ahead of time._**

###### _Ahead-of-time translation_

_In the ahead-of-time (AOT) translation path, x86_64 binaries are read from storage at times the system deems optimal for responsiveness of that code._ **_The translated artifacts are written to storage as a special type of Mach object file. That file is similar to an executable image, but it’s marked to indicate it’s the translated product of another image._**

<u>https://help.apple.com/pdf/security/en_US/apple-platform-security-guide.pdf</u>

#BHASIA @BlackHatEvents

## Slide 17

## AOT file

###### Contains translated Arm64 code

Mach-O 64bit (not special format) Located at /private/var/db/oah/*/*.aot

AOT files are protected by SIP We cannot modify these files even if we have root privileges

- Note that we can modify XTA cache files with administrator privileges on Arm-based Windows

###### Cannot show content even as root

SIP protected

#BHASIA @BlackHatEvents

## Slide 18

Rosetta 2 components Some Rosetta 2 components related to this research translate_tool - A CLI tool for translating an x64 executable without executing it runtime - A runtime library injected into a translated process oahd - A management daemon of AOT files

oahd-helper - A translator of an x64 executable

/Library/Apple/usr/libexec/oah

/usr/libexec/rosetta

#BHASIA @BlackHatEvents

## Slide 19

## Simplified execution flow

x64 Mach-O
1. Pass the file descriptor of
x64 Mach-O (via Mach IPC)
runtime oahd
System Library #0
AOT file #3 2. Create a process
AOT file #1
x64 process
oahd-helper
AOT file #2
AOT file #3
…

2. Create a process
oahd-helper

AOT file #1
AOT file #2
AOT file #3
…

4. The AOT file is mapped

3. Translate it into an AOT file

Directory of AOT files (/var/db/oah)

#BHASIA @BlackHatEvents

## Slide 20

## Simplified execution flow

x64 Mach-O
runtime
5. Go to the AOT file
System Library #0
and continue its
execution
AOT file #3
AOT file #1
x64 process
AOT file #2
AOT file #3
…
…

oahd

oahd-helper

Directory of AOT files (/var/db/oah)

#BHASIA @BlackHatEvents

## Slide 21

## translate_tool

CLI tool for translating an x64 executable $ translate_tool Translates an x64 executable without executing it Sends a file descriptor of an x64 executable to oahd via Mach IPC

$ translate_tool <path to x64 executable>

Creates an AOT file of specified executable

fileport_makeport() system call for passing the file descriptor to oahd

#BHASIA @BlackHatEvents

## Slide 22

## AOT files are cached for reuse

**Apple Platform Security: “Rosetta 2 on a Mac with Apple silicon”** _But the Rosetta runtime then sends an interprocess communication (IPC) query to the Rosetta system service, which_ **_asks whether there’s an AOT translation available for the current executable image. If found, the Rosetta service provides a handle to that translation, and it’s mapped into the process and executed._**

<u>https://help.apple.com/pdf/security/en_US/apple-platform-security-guide.pdf</u>

How does Rosetta 2 determine whether the specified x64 executable was previously translated or not?

#BHASIA @BlackHatEvents

## Slide 23

How to check the binary was previously translated? oahd calculates the dedicated hash and uses it for checking I named this hash “AOT lookup hash”

AOT files are saved under the /var/db/oahd subdirectory whose name is AOT lookup hash

- If there is a directory corresponding to the AOT lookup hash, oahd reuses the AOT file in this directory

AOT lookup hash

But how oahd calculates the AOT lookup hash from an x64 executable?

- A possible candidate is calculating the cryptographic hash from the entire binary contents and the file path

- But this is time-consuming…

#BHASIA @BlackHatEvents

## Slide 24

#### How does Rosetta 2 calculate AOT lookup hash?

SHA-256 is calculated from the following data

- •full path

•Mach-O header

- •uid

- •gid

- •mtime

- •ctime

- •crtime

•file size

#BHASIA @BlackHatEvents

## Slide 25

#### How does Rosetta 2 calculate AOT lookup hash?

SHA-256 is calculated from the following data

•full path

•Mach-O header

mtime: Time when file data last modified ctime: Time when file status was last changed (inode data modification) crtime: Time of file creation

•uid

•gid •mtime

•ctime

•crtime

•file size

#BHASIA @BlackHatEvents

## Slide 26

#### How does Rosetta 2 calculate AOT lookup hash?

SHA-256 is calculated from the following data

- •full path

Code section of the target binary is not used for calculating the AOT lookup hash

If we can modify the code section while keeping the AOT lookup hash unchanged, we can cause the hash collision

- •Mach-O header

•uid

- •gid

- •mtime

- •ctime

- •crtime

•file size

#BHASIA @BlackHatEvents

## Slide 27

A plan for code injection Code injection by causing the AOT lookup hash collision

1. Inject shellcode into a benign app

2. Create an AOT file with translate_tool

**/Users/ffri/a.out**

**/var/db/oah/../a.out.aot**

3. Restore to the original benign app while keeping the AOT lookup hash unchanged

Benign app

4. The AOT file is reused because the AOT lookup hash is the same

**/Users/ffri/a.out**

5. Poisoned AOT file is used for execution 😎

#BHASIA @BlackHatEvents

## Slide 28

## A plan for code injection

Code injection by causing the AOT lookup hash collision

1. Inject shellcode into a benign app

2. Create an AOT file with translate_tool **/var/db/oah/../a.out.aot**

**/Users/ffri/a.out**

But how? Modifying the file updates the timestamps 4. The AOT file is reused because the AOT lookup hash is the same

3. **Restore to the original benign app while keeping the AOT lookup hash unchanged** Benign app

**/Users/ffri/a.out**

5. Poisoned AOT file is used for execution 😎

#BHASIA @BlackHatEvents

## Slide 29

## Timestomping after modifying

We can restore mtime and crtime after modifying the file contents We can change timestamps with SetFile command (or touch command)

However, we cannot restore ctime with this method

- Because modifying mtime and crtime always updates ctime

#BHASIA @BlackHatEvents

## Slide 30

Writing to a file via mmap According to the older UNIX specification of mmap()

_The st_ctime and st_mtime fields of a file that is mapped with MAP_SHARED and PROT_WRITE, will be marked for update at some point in the interval between a write reference to the mapped region and the next call to msync() with MS_ASYNC or MS_SYNC for that portion of the file by any process._ **_If there is no such call, these fields may be marked for update at any time after a write reference if the underlying file is modified as a result._**

“may be marked for update” drew my attention

This phrase has been changed to “shall be marked” in the latest version

Does writing to a file via mmap() without msync() update ctime and mtime on macOS?

<u>https://pubs.opengroup.org/onlinepubs/7908799/xsh/mmap.html https://pubs.opengroup.org/onlinepubs/9699919799/functions/mmap.html https://apenwarr.ca/log/20181113</u>

#BHASIA @BlackHatEvents

## Slide 31

## Experiment: writing to a file via mmap

Create a file and write some contents

Write to the file via mmap() and call munmap() (without calling msync())

Write to the file via mmap() and call msync() and munmap()

#BHASIA @BlackHatEvents

## Slide 32

## Result: writing to a file via mmap

mtime and ctime **are not updated** although contents are changed!

mtime and ctime are updated when msync is called before munmap

Summary: we can change file contents while keeping timestamps unchanged via mmap() if we don’t call msync()

#BHASIA @BlackHatEvents

## Slide 33

## AOT Poisoning

###### Steps to inject code

1. Inject shellcode into a benign app

2. Translate the target with translate_tool

3. Restore it to the original benign executable via mmap() without calling msync()

4. Poisoned AOT file is used, and injected code is executed!

#BHASIA @BlackHatEvents

## Slide 34

## Limitation

Cannot be applied to a signed x64 executable😥

There are two reasons why this technique cannot be applied to a signed executable

- 1) In-place modification of a signed executable causes the program to crash when running

2) oahd does not accept an x64 executable with an invalid code signature

#BHASIA @BlackHatEvents

## Slide 35

- Why cannot be applied to signed executables? 1) In-place modification of a signed executable causes the crash when running This mitigation is introduced in Apple Silicon Mac

Note that this occurs **even if you restore the executable to a valid signed one on disk**

- For more details, see <u>the Apple’s documentation</u> and <u>the Developer Forums post</u>

_Specifically, code signing information is hung off the vnode within the kernel, and modifying the file behind that cache will cause problems. You need a new vnode, which means a new file, that is a new inode._

   - _Quinn “The Eskimo!” @ Developer Technical Support @ Apple_

- To avoid this crash, we need to create a copy of the target executable

- But this always updates the timestamps, which means the change of AOT lookup hash…

#BHASIA @BlackHatEvents

## Slide 36

### Why cannot be applied to signed executables?

2) oahd does not accept an x64 executable with an invalid code signature Cannot create an AOT file for a signed x64 executable containing our payload

test.out has an invalid code signature

translate_tool exits abnormally

#BHASIA @BlackHatEvents

## Slide 37

How Apple fixed this issue? Fixed in Big Sur 11.6 & Monterey 12.0.1

Writing to a file via mmap() & munmap() without calling msync() updates ctime

- We cannot modify file contents while keeping AOT lookup hash unchanged

ctime is **updated**

Apple updated APFS to fix this issue

<u>https://support.apple.com/en-us/HT212804</u>

#BHASIA @BlackHatEvents

## Slide 38

## Is the Apple’s fix enough? Apple patched APFS, but is it enough?

They did not change the way to calculate the AOT lookup hash

The way to calculate AOT lookup hash is the same as the previous version of macOS -> Apple’s fix relies on the APFS’s fix

#BHASIA @BlackHatEvents

## Slide 39

## Filesystems other than APFS

macOS supports various filesystems other than APFS (e.g., HFS+, FAT32, exFAT, …) We can create a dmg file with hdiutil command and mount it

- Can specify the filesystem of the dmg image by “fs” option

- If we use the other filesystem, we can bypass Apple’s fix😎

We can still perform AOT poisoning by downgrading the filesystem

#BHASIA @BlackHatEvents

## Slide 40

## Timestamps of other filesystems

Timestamps of FAT32 mtime ctime crtime
N/A

**ctime is not defined for FAT32!** Therefore, timestomping after the file modification does not change the AOT lookup hash

<u>https://www.sans.org/white-papers/36842/</u>

#BHASIA @BlackHatEvents

## Slide 41

## How to inject code into signed executable?

We need a code injection applicable to a signed executable If we apply to a signed executable, we can abuse it for hijacking the trust

<u>There are two reasons why this technique cannot be applied to signed executables</u>

- 1) In-place modification of signed executable causes the crash when running

- 2) oahd does not accept an x64 executable with invalid code signature

We must bypass these two restrictions

#BHASIA @BlackHatEvents

## Slide 42

## How to inject code into signed executable?

We need a code injection applicable to a signed executable If we apply to a signed executable, we can abuse it for hijacking the trust There are two reasons why this technique cannot be applied to signed executables **1) In-place modification of signed executable causes the crash when running** 2) oahd does not accept an x64 executable with invalid code signature This restriction has already been We must bypass these two restrictions bypassed because we no longer need in-place modification.

#BHASIA @BlackHatEvents

## Slide 43

## How to inject code into signed executable?

We need a code injection applicable to a signed executable If we apply to a signed executable, we can abuse it for hijacking the trust

There are two reasons why this technique cannot be applied to signed executables 1) In-place modification of signed executable causes the crash when running **2) oahd does not accept an x64 executable with invalid code signature** We must bypass these two restrictionsThis restriction can be bypassed by resigning with an ad-hoc signature

#BHASIA @BlackHatEvents

## Slide 44

How to inject code into signed executable? oahd accepts an executable with an adhoc signature and translates it

adhoc signed

translated successfully

However, codesign command changes the Mach-O header

So, simply re-signing with codesign command changes the AOT lookup hash

- -> I developed a new tool to sign with an ad-hoc signature while keeping the Mach-O header unchanged

#BHASIA @BlackHatEvents

## Slide 45

## How to inject code into signed executable?

Steps to sign with an ad-hoc signature while keeping the Mach-O header unchanged

1. Create a copy of an x64 executable and remove the existing signature 2. Sign it with an adhoc signature and extract the signature in it

3. Inject the extracted signature into the original x64 executable

4. Tweak the code directory in the adhoc signature to make it a valid one

Code directory
Code directory of the
Mach-O
0x0
Mach-O header SHA-256 codeHash[0] ad-hoc signature
0x1000
SHA-256
can be changed
codeHash[1]
0x2000 SHA-256 because it does not
codeHash[2]
Code section
0x3000 contain CMS.
Please refer to *OS Internals
Code signature
Volume 3 for code signature format.
Code directory
#BHASIA @BlackHatEvents

#BHASIA @BlackHatEvents

## Slide 46

## True AOT poisoning

###### Steps to inject code

1. Create a FAT32 dmg and mount it

2. Copy an x64 executable to the mounted point

3. Inject shellcode into it and re-sign it with an ad-hoc signature

4. Run translate_tool to create an AOT file

5. Restore the target executable to the original executable having the valid code signature

6. Restore the timestamps

7. Run the executable

8. Injected code is executed!😎

#BHASIA @BlackHatEvents

## Slide 47

## Exploitation

#BHASIA @BlackHatEvents

## Slide 48

## TCC bypass

Transparency, Consent, and Control (TCC)

Prevents an attacker from accessing some sensitive information without user consent

- Sensitive information includes contacts, camera, screen, microphone, emails, …

- For more details, see excellent TCC research by Csaba & Wojciech at BHUSA 2021 and <u>BHEU 2022</u>

#BHASIA @BlackHatEvents

## Slide 49

## TCC bypass

TCC bypass can be achieved by code injection

E.g., CVE-2020-24259 in Signal.app

- Typically, microphone access is granted to Signal.app

- Old Signal.app had vulnerable allow-dyld-environment-variables and disable-library-validation entitlements

- So, we can easily execute code in the context of Signal.app by injecting dylib with DYLD_INSERT_LIBRARIES

- Similar issues were present on other applications (e.g., Zoom*)

* <u>https://objective-see.org/blog/blog_0x56.html</u>

This exploit does not work if the library validation is enabled

- Because the library validation blocks loading of an unsigned dylib

But code injection by AOT poisoning can be applied to any x64 executable

- Even if the library validation is enabled!

- Recent macOS apps are built as FAT, so even if a user uses the app natively, an attacker can still use this technique

#BHASIA @BlackHatEvents

## Slide 50

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
_ 17:04 | / ]
@ YAFLWABE WR RK WIYED AT ; oC 8 wm = Q ® 5A98(A) 17:04 }
(cdhash-HV-_GIgx-py3.9) »> O
VulnEmu
ee < > HEE e¥aU7¢e7arTNy— Q
SARS AnAG
—m FileVault FrT*PVz—-IL | FOtKY—
ADEB EDOPTUT—YavORAPTE, FOPTUT—Ya
VRBRONSORRE FA.
DF 4APPIRA
a
DPTAWEDANY S
Bim RR
TEMP
2xF 47 & Apple Music
HomekKit =
Bluetooth silos
Bm Ns
2022-0...9 17.01.52
1— FS ARERR
(
A-—hkxX-Yay
| 2
2 REG SlcisnXeEIV ILE. ?
9208880070608 €e8 af
#BHASIA @BlackHatEvents
```

## Slide 51

Hiding malicious payload in SIP-protected location If an attacker uses this technique to execute malware, IR process becomes harder Because the original x64 executable does not contain any malicious payload

- The code to be executed is in the SIP-protected /var/db/oah/*/* directory

- Cannot access these poisoned AOT files without disabling SIP

Hmm, I cannot find any suspicious indicators. Seems benign.

NotMalwareX64

SIP protected location /var/db/oah/*/* NotMalwareX64.aot

Used for execution

No AV software scans this file because it does not have SIPrelated entitlements

#BHASIA @BlackHatEvents

## Slide 52

## Anti-Debugging

AOT-poisoned x64 executable cannot be debugged with LLDB When analyzing it, we cannot perform dynamic analysis with LLDB!

- This makes a dynamic analysis harder

The AOT file of ls is poisoned

LLDB cannot start debugging the AOT-poisoned executable

#BHASIA @BlackHatEvents

## Slide 53

The Apple’s fixes Fixed at macOS Ventura 13.0 & Monterey 12.6 & Big Sur 11.7 Apple assigned CVE-2022-42789 Eligible for a generous bounty😀

<u>https://support.apple.com/en-us/HT213488</u>

#BHASIA @BlackHatEvents

## Slide 54

## Analyzing the Apple’s fixes

We cannot execute an AOT-poisoned x64 executable anymore

Kernel Log says “supplemental signature for file does not match any attached cdhash”

Rosetta 2 checks code signing status by calling fcntl_nocancel

F_ADDFILESUPPL command is used If fcntl_nocancel returns EPERM, #BHASIA @BlackHatEvents Rosetta 2 throws the exception.

#BHASIA @BlackHatEvents

## Slide 55

## About the Apple’s fixes

Apple’s fixes rely on checking the dynamic code signing status (see the Appendix)

- -> This means that **we can still inject code into non-signed executables**

So, TCC bypass is fixed, but a local attacker can still perform other exploitations

- Hiding malicious payload in SIP protected location

- Anti-debugging

#BHASIA @BlackHatEvents

## Slide 56

Supplemental signature & linkage hash Apple introduced a mitigation to code injection modifying AOT file before I reported This is performed by adding supplemental signature to the AOT file of a signed x64 executable

- Supplemental signature contains the cdhash of the original executable named linkage hash

- Kernel (at ubc_cs_blob_add_supplement()) checks linkage hash matches cdhash of the original x64 executable

- If not matched, AOT file is not used for the execution

This mitigation has already been introduced in the first Big Sur!

- So, unlike Windows, Apple limited the code injection directly modifying AOT file

However, AOT poisoning bypassed this mitigation

- For more details, see <u>the Appendix</u>

CodeDirectory struct contains members related to linkage hash from version 0x20600

<u>https://github.com/apple-ossdistributions/xnu/blob/5c2921b07a2480ab43ec66f5b</u> #BHASIA @BlackHatEvents <u>9e41cb872bc554f/osfmk/kern/cs_blobs.h#L209</u>

## Slide 57

### A similar code injection on Arm-based Windows

#BHASIA @BlackHatEvents

## Slide 58

## AOT lookup hash for Arm-based Windows?

Arm-based Windows also reuses the translation result like Rosetta 2 When we run the same application twice, existing XTA cache files are reused

- -> Are there any hashes corresponding to the AOT lookup hash on Windows?

_To find the cache file, the XtaCache service should first open the executable image, map it, and calculate its hashes._ **_Two hashes are generated based on the executable image path and its internal binary data._**

- _Windows Internals, Part2 7_<sup>_th_</sup> _edition_

#BHASIA @BlackHatEvents

## Slide 59

## Module header/path hashes

Only XtaCache service and Administrators group users can access this directory

**ADOBEARMHELPER.EXE.50B4313C4D8BC729AEA5FE0DECBF4580.6A21A56F7C6F1DFE1683646B024EE7E2.x86 .mp.2.jc**

- **module header hash**

- **module path hash**

- **cache version** But how are these hashes calculated?

#BHASIA @BlackHatEvents

## Slide 60

## How to calculate module path hash?

Module path hash is calculated by the NT device path name of the target x86/x64 executable

#BHASIA @BlackHatEvents

## Slide 61

## How to calculate module header hash?

Module header hash is calculated from the following information:

- DOS header

- NT headers (not including ImageBase)

- LastWriteTime (i.e., mtime)

#BHASIA @BlackHatEvents

## Slide 62

## How to calculate module header hash?

Module header hash is calculated from the following information:

- DOS header

- NT headers (not including ImageBase)

- LastWriteTime (i.e., mtime)

**Only mtime is used for hashing** 😅 **We can easily cause the hash collision for the module header hash by timestomping mtime**

#BHASIA @BlackHatEvents

## Slide 63

## translate_tool for Arm-based Windows?

There is no translate_tool on Arm-based Windows😥

We cannot create an XTA cache file without running an x86/x64 executable

- -> To address this issue, XtacTranslateTool is created

- This tool enables us to create an XTA cache file without running

- Does not require admin privileges

- For more details, see <u>the Appendix</u>

#BHASIA @BlackHatEvents

## Slide 64

## XTA cache poisoning

Steps to inject code

1. Inject shellcode into the target executable

2. Create an XTA cache file using XtacTranslateTool

3. Restore the target executable to the original one

4. Restore the LastWriteTime

5. Run the target executable

6. Poisoned XTA cache file is used for the execution😎

Unlike macOS, XtaCache service happily accepts an executable with an invalid code signature

- So, we can easily apply this technique to a signed executable

#BHASIA @BlackHatEvents

## Slide 65

Exploitation: stealth PE backdooring Backdooring PE files is used to achieve persistence

<u>https://www.ired.team/offensive-security/code-injection-processinjection/backdooring-portable-executables-pe-with-shellcode#final-note</u>

- We can easily detect backdoored PE by inspecting it

- Because this method typically adds new section and modifies the entrypoint of the target PE file

- PE backdooring by XTA cache poisoning does not have such downsides

- Backdoored PE file is the same as the original one, so we cannot see any suspicious indicators in this

#BHASIA @BlackHatEvents

## Slide 66

Exploitation: user-assisted EoP UAC elevation by hijacking the trust of software UAC elevation prompt shows the origin of the target executable

- If it has a valid code signature, it shows “Verified publisher,” but if not, it shows “Publisher: Unknown” with the yellow stripe

- If an attacker performs code injection with XTA cache poisoning, the code signature remains valid

- So, chances are good that a user unintentionally executes it with admin privileges

- Installer is a good target because it is typically executed with admin privileges and has a valid code signature

Publisher: Unknown

Verified publisher:
Adobe Inc.
#BHASIA @BlackHatEvents

#BHASIA @BlackHatEvents

## Slide 67

#BHASIA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ = Microsoft Remote Desktop Edit Connections Window Help
Recycle Bin
kohnakagawa — nc -| 8080 — 80x24
(sh-3.2$ ifconfig | grep inet
inet 127.0.0.1 netmask @xffee0000
inet6 ::1 prefixlen 128
inet6 fe80::1%1lo®@ prefixlen 64 scopeid 0x1
inet6 fe80::94a7:51ff:fe82:8bb6%anpil prefixlen 64 scopeid 0x4
inet6 fe80::94a7:51ff:fe82:8bb5%anpi® prefixlen 64 scopeid @x5
inet6 fe80::70ed:3cff:fe55:4a54%ap1 prefixlen 64 scopeid @xb
inet6 fe80::cde:f636:dff6:dde8%en® prefixlen 64 secured scopeid @xc
inet 192.168.0.2 netmask O@xffffff00 broadcast 192.168.0.255
inet6 2001:268:c208:cf0a:1402:309b:5b32:7cb4 prefixlen 64 autoconf :
ed
inet6 2001:268:c208:cf@a:fcd1:4cf3:2dbb:c26d prefixlen 64 autoconf {
rary
inet6 fe80::fc63:beff:fefb:9033%awd1® prefixlen 64 scopeid @xe
inet6 fe80::fc63:beff:fefb:9033%llw@ prefixlen 64 scopeid Oxf
inet6 fe80::179d:ef86:c6c5:7c94%utun® prefixlen 64 scopeid @x10@
inet6 fe80::91be:64f7:6e25:dadi%utun1 prefixlen 64 scopeid @x11
inet6 fe8@::ce81:bic:bd2c:69e%utun2 prefixlen 64 scopeid @x12
inet6 fe80::8a47:74fa:680d:4866%utun3 prefixlen 64 scopeid @x13
inet6 fe80::e@ff:537e:3b1a:8836%utun4 prefixlen 64 scopeid 0x14
[sh-3.2$ nc -1 8080
oh@ecrés
Volterra
[EX] Command Prompt x + v
C:\Users\tsune\source\repos\XtacPoisoning\Release>whoami /priv
PRIVILEGES INFORMATION
Description
Privilege Name
SeShutdownPrivil ~ - ~
SeChangeNotifyPr 4 Downloads x +
SeUndockPrivileg
SeIncreaseWorkin @ New ~ xX a ®@ ee NN sot» = View~
SeTimeZonePrivil
C:\Users\tsune\s ¢ +> v 4 >» Downloads VS
A lome Name Date modified
@ Ko - Personal © Today
BR AcroRdrDC2200320322_en_US.exe 3/24/2023 8:21 AM
Desktop ”
BE Documents #
b Downloads #
B Pictures *
@ Music ed
litem | 1 item selected 334MB |
Type
Application
Size
342,173 KB
#BHASIA
— — _ af
f FriMar 24 8:24
@BlackHatEvents
```

## Slide 68

## Microsoft response

_This issue does not meet the MSRC bar for an immediate security update - MSRC_

#BHASIA @BlackHatEvents

## Slide 69

## Is fixing this issue simple?

Naïve approach: Hashing also ChangeTime (ctime) along with LastWriteTime (mtime)*

However, this is not enough!

Because we can use the same filesystem downgrade trick on Windows

- Mount FAT32 image and copy the target executable to it, then we can easily change the timestamps

But the filesystem downgrade trick is not required on Windows even if ctime is hashed

*Here we consider $STANDARD_INFORMATION timestamps and $FILE_NAME timestamps in a directory index, which can be accessed from NtQueryInformationFile and NtQueryDirectoryFile(Ex)

#BHASIA @BlackHatEvents

## Slide 70

Changing ctime and mtime is easy on Windows NtSetInformationFile can change ctime and mtime simultaneously

FILE_BASIC_INFORMATION contains ctime, mtime, crtime, and atime

Can change all timestamps (including ctime) to the values specified by FILE_BASIC_INFORMATION

#BHASIA @BlackHatEvents

## Slide 71

Changing ctime and mtime is easy on Windows NtSetInformationFile can change ctime and mtime simultaneously

FILE_BASIC_INFORMATION contains ctime, mtime, crtime, and atime Even if ctime is hashed, we can still cause the hash collision for module header hash Can change all timestamps (including ctime) to -> Hashing ctime is not the ultimate fix to prevent the values specified by FILE_BASIC_INFORMATION XTA cache poisoning

#BHASIA @BlackHatEvents

## Slide 72

## Summary & key takeaways

#BHASIA @BlackHatEvents

## Slide 73

## Summary

Rosetta 2 and Windows x86/x64 emulation reuses binary translation cache files to reduce the amount of binary translation

These compatibility layers use the dedicated hashes to check whether the specified binary was previously translated

These hashes are calculated from timestamps, the header of the target file, the file path, etc.

New code injection techniques (AOT poisoning & XTA cache poisoning) are proposed These are achieved by causing the collision of the dedicated hash The details of these techniques and how to exploit them are covered

#BHASIA @BlackHatEvents

## Slide 74

## Black Hat Sound Bytes

For red team

New code injection techniques (AOT poisoning and XTA cache poisoning) with PoC code

- You can find the PoC code in the following links and can test these on your own environment

- <u>https://github.com/FFRI/XtacPoisoning</u>

- <u>https://github.com/FFRI/AotPoisoning</u>

For security researchers

There are few studies on these compatibility layers and offensive tooling using these

- I hope to see more vulnerability research on this topic

- I hope this talk will be the starting point of your research

#BHASIA @BlackHatEvents

## Slide 75

## Black Hat Sound Bytes

###### For OS developers

Failure to check the identity of a file correctly causes the security vulnerability to enable code injection

- Determining the identity of a file is difficult

- Implementing this correctly needs more consideration

Everyone

Be careful of these threats!

- Since Arm-based laptops are becoming more popular, an attacker will exploit these

#BHASIA @BlackHatEvents

## Slide 76

## Thank you

Any questions and comments to Twitter DM: https://twitter.com/ffri_research e-mail: research-feedback@ffri.jp

#BHASIA @BlackHatEvents

## Slide 77

## Appendix

#BHASIA @BlackHatEvents

## Slide 78

## Exploitations other than TCC bypass?

#BHASIA @BlackHatEvents

## Slide 79

Limitations of AOT poisoning Dynamic code signing becomes invalid

Therefore, this method cannot be used for bypassing dynamic code signing check

- Unfortunately, if we try to use this technique to Apple-signed executable, we cannot fully obtain its entitlements

- AMFI did a great job

#BHASIA @BlackHatEvents

## Slide 80

## Why did TCC bypass work?

Latest tccd checks the dynamic code signature for verifying its identity <u>CVE-2021-30972 – TCC bypass @ Black Hat ASIA 2022</u>

- Its root cause is that tccd does not check the dynamic code signature

- tccd is now fixed to check the dynamic code signature

However, AOT poisoning can be used for bypassing TCC although the dynamic code signature becomes invalid🤔

I did not analyze its root cause, but tccd might still contain “weak” code signature verification

#BHASIA @BlackHatEvents

## Slide 81

## How Apple fixed AOT poisoning?

#BHASIA @BlackHatEvents

## Slide 82

Analyzing the Apple’s fixes Rosetta 2 stops to execute an AOT-poisoned x64 executable

Kernel Log says “supplemental signature for file does not match any attached cdhash”

Rosetta 2 checks code signing status by calling fcntl_nocancel

F_ADDFILESUPPL command is used If fcntl_nocancel returns EPERM, Rosetta 2 throws the exception. #BHASIA @BlackHatEvents

## Slide 83

Analyzing the Apple’s fixes: Dive into XNU F_ADDFILESUPPL command of fcntl_nocancel

Its implementation resides in sys_fcntl_nocancel <u>(kern_descript.c)</u>

Load a code signing blob of an AOT file into Unified Buffer Cache (UBC)

The code signing blob is passed to the ubc_cs_blob_add_supplement() function

#BHASIA @BlackHatEvents

## Slide 84

Analyzing the Apple’s fixes: Dive into XNU <u>Patches of ubc_cs_blob_add_supplement()</u>

The validity of dynamic code signing status is checked.

EPERM is returned when the dynamic code signing is invalid

#BHASIA @BlackHatEvents

## Slide 85

## Supplemental signature & linkage hash

#BHASIA @BlackHatEvents

## Slide 86

Supplemental signature & linkage hash An AOT file for a signed x64 executable has supplemental signature Supplemental signature has linkage hash, which is the cdhash of the original x64 executable

- codesign command does not show the linkage hash

- Tool to show linkage hash is available at <u>https://github.com/FFRI/AotPoisoning</u>

   - Show cdhash of x64 app

cdhash of the original x64 app matches linkage hash

Show linkage hash of the supplement signature of AOT file

#BHASIA @BlackHatEvents

## Slide 87

Supplemental signature & linkage hash: checking ubc_cs_blob_add_supplement() checks linkage hash matches cdhash of x64 executable This check exists at least in the initial release of macOS Big Sur If cdhash != linkage

If cdhash != linkage hash

Check cdhash == linkage hash

ubc_cs_blob_add_supplement fails

<u>https://github.com/apple-ossdistributions/xnu/blob/bb611c8fecc755a0d8e56e2fa51513527c5b7a0e/bsd/kern/ubc_subr.c#L3878-L3890</u>

Why is AOT poisoning not mitigated by this check?

#BHASIA @BlackHatEvents

## Slide 88

### Supplemental signature & linkage hash: checking

Multiple code signing blobs are attached to the single vnode of the x64 executable. In this case, there are two code signing blobs for valid x64 executable and codeinjected x64 executable.

If one of the blobs contains the valid cdhash, this check passes. -> Therefore, linkage hash does not prevent from AOT poisoning

#BHASIA @BlackHatEvents

## Slide 89

## XtacTranslateTool

#BHASIA @BlackHatEvents

## Slide 90

## How XTA cache files are created?

_Communication between xtajit and XtaCache is achieved using NtAlpcSendWaitReceivePort … BTCpuNotifyMapViewOfSection is called every time a module is loaded (since NtMapViewOfSection is called every time a module is loaded). Eventually it passes a module file handle to NtAlpcSendWaitReceivePort, which sends the message to the compiler, xtac.exe. - Teardown: Windows 10 on ARM - x86 Emulation_

x86 emulation process xtajit.dll **test.dll**

Pass a module file handle & share Pass arguments for execution paths xtac.exe XtaCache.exe x86 module is newly loaded

Translate and create a new cache file %SystemRoot%\XtaCache xtac.exe TEST.DLL…x86.mp1.jc

#BHASIA @BlackHatEvents

## Slide 91

## How XTA cache files are created?

_Communication between xtajit and XtaCache is achieved using NtAlpcSendWaitReceivePort … BTCpuNotifyMapViewOfSection is called every time a module is loaded (since NtMapViewOfSection is called every time a module is loaded). Eventually it passes a module file handle to NtAlpcSendWaitReceivePort, which sends the message to the compiler, xtac.exe. - Teardown: Windows 10 on ARM - x86 Emulation_

Pass a module file handle & share Pass arguments for execution paths xtac.exe XtaCache.exe

Translate and create a new cache file xtac.exe

x86 emulation process xtajit.dll

**test.dll** If we can “emulate” IPC between xtajit.dll x86 module is and XtaCache.exe, we can create an XTA newly loaded cache file without executing it

%SystemRoot%\XtaCache TEST.DLL…x86.mp1.jc

#BHASIA @BlackHatEvents

## Slide 92

## Trace Buffer

xtajit/xtajit64 has “Trace Buffer” shared between x86/x64 emu process and XtaCache Used for sending hints about which x86/x64 code is emulated or already present in XTA cache files* _* Windows Internals, Part2 7_<sup>_th_</sup> _edition_ • xtac.exe compiler create XTA cache files based on the valid entries in this buffer Trace buffer contains the list of pairs, which consist of module ids and RVAs

- This buffer can be easily modified

We can control which code in which module should be translated by modifying the trace buffer

Trace Buffer is updated at #JccClidnetAddTrace

#BHASIA @BlackHatEvents

## Slide 93

## How to find Trace Buffer?

Since Trace Buffer is dynamically allocated, its address is determined at runtime To find the Trace Buffer, we “mark” the Trace Buffer by loading “MarkerLibrary”

######

Example of MarkerLibrary

- MarkerLibrary contains various branch instructions

- After this dll is loaded, Trace Buffer is filled with RVAs of these branch instructions

- These values are unique to this dll, so by scanning these values, we can find the Trace Buffer

#BHASIA @BlackHatEvents

## Slide 94

## Steps to translate an x86/x64 executable

1. Load target executable with LoadLibraryExA*

   - *To avoid running the DllEntry, DONT_RESOLVE_DLL_REFERENCES flag must be specified

2. Drop MarkerLibrary

3. Load the MarkerLibrary to mark the Trace Buffer

4. Find the Trace Buffer from the mark recorded in step 3

5. Change module ids and RVAs of the Trace Buffer to the id and RVAs of the module loaded at step 1

6. XtaCache file is created

- Code is available on GitHub (https://github.com/FFRI/XtacPoisoning)

#BHASIA @BlackHatEvents

## Slide 95

## Benefits of XTA cache poisoning

#BHASIA @BlackHatEvents

## Slide 96

Benefits of XTA cache poisoning Can be applied to apps not having relative path DLL load hijacking vulnerability <u>This type of EoP</u> is typically performed by hijacking vulnerable DLL loading

- But since XTA cache poisoning can be applied to any x86/x64 executable, we do not need to find such vulnerable apps

- Note that we basically cannot use other code injection techniques calling CreateProcess

- Because they fail with ERROR_ELEVATION_REQUIRED when the target app requires elevation <u>https://learn.microsoft.com/ja-jp/archive/blogs/winsdk/dealing-with-administrator-and-standard-users-context</u>

Can be used even if ValidateAdminCodeSignatures is enabled

ValidateAdminCodeSignatures: “Only elevate executables that are signed and validated policy setting”

- So, we cannot elevate a non-signed executable (or executable with invalid signature) if this setting is enabled

- But XTA cache poisoning can bypass this restriction!

<u>https://learn.microsoft.com/en-us/windows/security/identity-protection/user-account-control/useraccount-control-group-policy-and-registry-key-settings</u>

#BHASIA @BlackHatEvents

## Slide 97

## References - related research on Rosetta 2

**Project Champollion** - by me <u>https://github.com/FFRI/ProjectChampollion</u>

**Why is Rosetta 2 fast? -** @dougallj <u>https://dougallj.wordpress.com/2022/11/09/why-is-rosetta-2-fast/</u>

**TSOEnabler -** @_saagarjha <u>https://github.com/saagarjha/TSOEnabler</u>

#BHASIA @BlackHatEvents

## Slide 98

References - related research on macOS exploits **Shield - An app to protect against process injection on macOS** - @theevilbit <u>https://theevilbit.github.io/shield/</u>

**Process injection: breaking all macOS security layers with a single vulnerability** - @xnyhps <u>https://sector7.computest.nl/post/2022-08-process-injection-breaking-all-macos-security-layers-with-a-single-vulnerability/</u> **20+ Ways to Bypass Your macOS Privacy Mechanisms** - @theevilbit and @_r3ggi <u>https://www.blackhat.com/us-21/briefings/schedule/index.html#-ways-to-bypass-your-macos-privacy-mechanisms-23133</u>

**Knockout Win Against TCC - 20+ NEW Ways to Bypass Your MacOS Privacy Mechanisms** - @theevilbit and @_r3ggi

<u>https://www.blackhat.com/eu-22/briefings/schedule/#knockout-win-against-tcc----new-ways-to-bypass-your-macos-privacymechanisms-29272</u>

#BHASIA @BlackHatEvents

## Slide 99

References - related research on Arm-based Windows **Teardown: Windows 10 on ARM – x86 Emulation** - Cylance Research Team <u>https://blogs.blackberry.com/en/2019/09/teardown-windows-10-on-arm-x86-emulation</u>

**WoW64 internals …re-discovering Heaven’s Gate on ARM** - @PetrBenes <u>https://wbenny.github.io/2018/11/04/wow64-internals.html</u>

**Jack-in-the-Cache: A New Code injection Technique through Modifying X86-to-ARM Translation Cache** - by me

<u>https://www.blackhat.com/eu-20/briefings/schedule/#jack-in-the-cache-a-new-code-injection-technique-through-modifying-xto-arm-translation-cache-21324</u>

**Appearances are deceiving: Novel offensive techniques in Windows 10/11 on ARM** - by me <u>https://www.ffri.jp/assets/files/research/research_papers/Koh_Nakagawa_Appearances_are_deceiving_English.pdf</u>

#BHASIA @BlackHatEvents

## Companion resources

### `AS-23-Koh-Dirty-Bin-Cache-A-New-Code-Injection-Poisoning-Binary-Translation-Cache_POC.txt`

```text
https://github.com/FFRI/AotPoisoning
https://github.com/FFRI/XtacPoisoning
```
