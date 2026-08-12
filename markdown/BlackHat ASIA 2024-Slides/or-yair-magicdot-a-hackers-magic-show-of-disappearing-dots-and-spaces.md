---
title: "Magicdot A Hacker's Magic Show of Disappearing Dots and Spaces"
speakers: ["Or Yair"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Or Yair-Magicdot A Hacker's Magic Show of Disappearing Dots and Spaces.pdf"
pages: 67
sha256: "4e3ed71af0da6e7e9d3c8eb6a012ff4edc79c676ff4b58ecb929d9cb567c8d47"
text_chars: 13574
ocr_pages: 27
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:50:13Z"
---
# Magicdot A Hacker's Magic Show of Disappearing Dots and Spaces

**Speakers:** Or Yair  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Or Yair-Magicdot A Hacker's Magic Show of Disappearing Dots and Spaces.pdf` (67 pages)

## Slide 1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
A HACKER'S MAGIC SHOW OF
DISAPPEARING DOTS AND SPACES
```

## Slide 2

Or Yair

Security Research Team Lead at SafeBreach 6+ years in security research Linux, embedded and some Android research 3 years Windows research

Creator of Aikido Wiper, DoubleDrive

## Slide 3

Agenda Windows Known Issue Introduction Research Goals Post-Exploitation Techniques Vulnerabilities CVEs + Fixes Takeaways GitHub + Q&A

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Windows Known Issue Introduction
Research Goals
Post-Exploitation Techniques
Vulnerabilities
CVEs + Fixes
Takeaways
aS
GitHub + Q&A “sy
\
```

## Slide 4

Windows Backwards Compatibility

More than **1.4 billion** active devices

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
: Windows Backwards ,
Compatibility i) ir
"4
More than 1.4 billion active devices
```

## Slide 5

My first encounter with “Magic"

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Name Date moc
Y Today
B aoc. 2/6/2024
B att 2/6/2024
```

## Slide 6

## Microsoft’s Documentation

Do not end a file or directory name with a space or a period. Although the underlying file system may support such names, the Windows shell and user interface does not. However, it is acceptable to specify a period as the first character of a name. For example, “.temp”.

## Slide 7

Normal (DOS) to NT Path Conversion Win32 APIs path arguments are normal DOS paths. Conversion is needed. RtlpDosPathNameToRelativeNtPathName()

C:\Users\User\Documents\example.txt

\??\C:\Users\User\Documents\example.txt

## Slide 8

Normal (DOS) to NT Path Conversion

RtlpDosPathNameToRelativeNtPathName() Removes:

Trailing dots from any path element Trailing spaces from the last path element

## Slide 9

#### **DOS Path**

#### **NT Path**

C:\example\example **.** \??\C:\example\example C:\example\example **…** \??\C:\example\example C:\example\example **<space>** \??\C:\example\example C:\example\example **<space><space>** \??\C:\example\example C:\example **.** \example \??\C:\example\example C:\example **<space>** \example \??\C:\example **<space>** \example

## Slide 10

“The Definitive Guide on Win32 to NT Path Conversion”

by James Forshaw with Google Project Zero <u>https://googleprojectzero.blogspot.com/2016/02/thedefinitive-guide-on-win32-to-nt.html</u>

## Slide 11

## #1 Research Goal

**Rootkit-like abilities** Utilize the issue for concealments

## Slide 12

Typical Rootkits

Primary Goal – Concealments Types User-Space Kernel

## Slide 13

Kernel Rootkit

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Kernel Rootkit
CALL \
FindFirstFilew( }
:
Sy PROCESS
USER-SPACE <
q y,
**<
KERNE NtQueryDirectoryFile_hook( ) “ss
\
3s
G
```

## Slide 14

## Kernel Rootkit Requirements

Ability to run in the kernel: Admin Privileges + Handle Obstacles: Driver Signature Enforcement Driver Block List HVCI

## Slide 15

User-Space Rootkit

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CALL FindFirstFileW( )
PROCESS ROOTKIT ©) FindFirstFilew()
USER-SPACE — | FindFirstFilew_hook() | <—
<7
KERNEL
```

## Slide 16

User-Space Rootkit Requirements

Ability to write or run code in all processes: Admin Privileges

## Slide 17

Something is Missing

How can unprivileged malwares conceal themselves? Do they must have a 0-day PE?

## Slide 18

New - Unprivileged Rootkit

The rootkit does not need to be part of the chain of calls

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
@ -SPACE- e e @ -SPACE- @ .
— BR > Bee —>| Rt1pDosPathNameToRelativeNtPathName() |
© @ ~ -SPACE- @ -SPACE- @
|
The rootkit does not need to :
be part of the chain of calls MT APL ‘
```

## Slide 19

#1 Research Goal

Rootkit-like abilities Utilize the issue for concealments + No special required privileges

## Slide 20

#2 Research Goal Prove that an unfixed known issue is a security risk: **Find vulnerabilities caused by the known issue.**

## Slide 21

Files and Directories Concealments

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Files and Directories //f |
Concealments ——
```

## Slide 22

Concealing Files and Directories

Inoperable File/Directory:

Result:

Name File/Directory “…” or “blabla…” (using NT path)

Directory can’t be listed, deleted, added with files File can’t be deleted, written, or read

## Slide 23

Concealing Files and Directories

Impersonated Directory/File: Name a file **“benign.”** (using NT path)

Result:

File operations on **“benign.”** affect **“benign”** instead.

## Slide 24

Short Names (8.3 filename) An old filename convention. Backwards Compatibility (Again). Used by old versions of DOS & Windows.

**Short Names: Normal Names:**

## Slide 25

## Concealing Files and Directories

Improved Impersonated File/Directory Name a file/directory

**“lol.”** (using NT path) Result

**Short Names: Normal Names:**

File operations on **“lol.”** affect a file with the short name **“LOL”** instead.

## Slide 26

## Concealing Files and Directories

ZIP Hidden Files: End a file name in a ZIP archive with a dot

Result:

Listing the archive with File Explorer does not show the file

## Slide 27

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
01
C:\Users\Or\Downloads\test>
| dirt haha. a.txt a.txt a.txt. lol zip.zip
-el
Gan
Titems | =] }
& Untitled x +
File Edit View 8
Ln 1, Col 1 140% Windows (CRLF) UTF-8
C:\Users\Or\Downloads\test>
```

## Slide 28

Processes Concealments

## Slide 29

## Concealing Processes

Untraceable Process: NtCreateUserProcess - “\??\C:\Windows **.** \blabla\blabla.exe” Result: Executable cannot be accessed Executable’s properties cannot be viewed from Task Manager / ProcExp…

## Slide 30

Concealing Processes

Impersonated Process:

NtCreateUserProcess - “\??\C:\Windows **.** \System32\svchost.exe” Result:

File operations on the executable affect the original svchost.exe

## Slide 31

## Concealing Processes

Also:

Task Manager, ProcExp show that the executable is verified and signed by Microsoft Prefetch analysis tools show details about the original svchost.exe

## Slide 32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
any)
Ble Options View Process Find Users Help
BE Cm mex £8 —i ] Filter by name>
C:\Users\Or\Downloads\test> Process PID User Name
oAggregatorHostiexe |
Biaj.exe 24300 LAPTOP-8VNJORA8\Or
j -apimonitor-x64.exe 18888 LAPTOP-8VNJORAS8\Or
i BApplicationFrameH... 15904 LAPTOP-8VNJORA8\Or
@audiodg.exe 8300 NT AUTHORITY\LOCAL.. 0
@backgroundTaskHo... 2432 LAPTOP-8VNJORA8\Or
m|backgroundTaskHo... 33392LAPTOP-8VNJORA8\Or Suspend
|backgroundTaskHo... 16440LAPTOP-8VNJORA8\Or Suspend
mBluetoothMouseThe... 5624NT AUTHORITY\SYSTEM
=@CamtasiaRecorder.... 17204 LAPTOP-8VNJORA&\Or 0.
=&CamtasiaStudio.exe 34584 LAPTOP-8VNJORA8\Or <0.
= @chrome.exe 26568 LAPTOP-8VNJORAS&\Or 0.
@chrome.exe 27448LAPTOP-8VNJORA8\Or
@chrome.exe 1800 LAPTOP-8VNJORA8\Or
®chrome.exe 8384 LAPTOP-8VNJORAS8\Or <0.
®@chrome.exe 27124LAPTOP-8VNJORAS8\Or
@chrome.exe 8084 LAPTOP-8VNJORA8\Or
@chrome.exe 25152LAPTOP-8VNJORA8\Or
®@chrome.exe 32692 LAPTOP-8VNJORA8\Or
@chrome.exe 22280 LAPTOP-8VNJORA8\Or
@chrome.exe 440 LAPTOP-8VNJORA8\Or
@chrome.exe 30048 LAPTOP-8VNJORA8\Or
®@chrome.exe 4656 LAPTOP-8VNJORA8\Or
®@chrome.exe a TT an
PU Usoge 0
eomit Charge: 58.10% | Proces:
```

## Slide 33

Anti Analysis

## Slide 34

## ProcExp DoS – A Built In “Safe” Feature

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ProcExp DoS -
A Built In “Safe” Feature
91:
wcscpy_S(process_name_with_pid_ parentheses, | 256ui64,| process_name) ;
92:
```

## Slide 35

## ProcExp DoS – A Built In “Safe” Feature

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ProcExp DoS -
A Built In “Safe” Feature
01;
wcscpy_s(process_name_with_pid_parentheses, 256ui64, |process_name) ;
D2e
sprintf_s<32>(pid_str_with_parentheses, L"(%d)", v116[22]);
wcscat_s(process_name_with_pid_ parentheses, 256ui64, |(const wchar_t *)pid_str_with_parentheses) ;
```

## Slide 36

ProcExp DoS – A Built In “Safe” Feature

<u>https://learn.microsoft.com/en-us/cpp/c-runtime-library/securityenhanced-versions-of-crt-functions</u>

Safe C-Runtime Functions:

The more secure versions Microsoft’s docs – “If there's an error, they invoke an error handler.”

## Slide 37

ProcExp DoS – A Built In “Safe” Feature

wcscat_s:

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ProcExp DoS -
A Built In “Safe” Feature
wcscat_s:
if ( !--SizeInWords )
{
v5 = errno();
Wish = syle
goto invalid_parameter;
}
invalid_parameter:
*¥v5 = v3;
invalid_parameter_noinfo();
return v3;
```

## Slide 38

ProcExp DoS – A Built In “Safe” Feature

<u>https://learn.microsoft.com/en-us/cpp/c-runtime-library/parameter-validation</u>

“The invalid parameter handler dispatch function calls the currently assigned invalid parameter handler. By default, the invalid parameter calls _invoke_watson, which causes the application to close and generate a mini-dump.”

## Slide 39

ProcExp DoS – A Built In “Safe” Feature

invalid_parameter_noinfo():

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ProcExp DoS -
A Built In “Safe” Feature
invalid_parameter_noinfo():
if ( !invalid parameter_handler )
invoke_watson(Expression, FunctionName, FileName, LineNo, Reserved) ;
return invalid_parameter_handler(Expression, FunctionName, FileName, LineNo, Reserved) ;
```

## Slide 40

## ProcExp DoS – A Built In “Safe” Feature

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ProcExp DoS -
A Built In “Safe” Feature
01;
wcscpy_s(process_name_with_pid_parentheses, 256ui64, |process_name) ;
D2e
sprintf_s<32>(pid_str_with_parentheses, L"(%d)", v116[22]);
wcscat_s(process_name_with_pid_ parentheses, 256ui64, |(const wchar_t *)pid_str_with_parentheses) ;
```

## Slide 41

ProcExp DoS – A Built In “Safe” Feature

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ProcExp DoS -
A Built In “Safe” Feature
b Downloads
© New NL Sort
> T.. > Dow.
Name
Quick access
Desktop Today (1)
Downloads
3 Documents Earlier this year (1)
a
WA Pictures Cl procexp64
BD Music A long time ago (1)
Bi videos HW) ntrun_exe
@ OneDrive
v WB this pc
Wl Desktop
j Documents
Downloads
5D Music
DA Pictures
3 items
6:53 AM
~ 6» 4/9/2023 e
```

## Slide 42

Vulnerabilities

## Slide 43

EoP Deletion Vuln – The disappearing act Permissions for a.txt and b.txt Permissions to write into C:\demo

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EoP Deletion Vuln —
The disappearing act
| x Permissions for a.txt and b.txt
MM Permissions to write into C:\demo
C:\DEMO:
>A. TXT
```

## Slide 44

EoP Deletion Vuln – The disappearing act

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EoP Deletion Vuln —
The disappearing act
C:\DEMO:
>A. TXT
>B. TXT
>... <SPACE>
>C. TXT
```

## Slide 45

EoP Deletion Vuln – The disappearing act

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EoP Deletion Vuln -
The disappearing act
= Local Disk (C:) < +
€ * G Paste This PC > Local Disk (C:) > Search Local Disk 2
® New iB ~ Sort View ™ ® Details
@Home Name Date modif... Type Size
La)
cme een demo 4/8/2024 1... File folder
PerfLogs 3/8/2024 1... File folder
™Desktc Program Files 4/3/2024 6... File folder
« Downl
3 Docun Program Files (x86) 3/9/2024 1:... File folder
Picture Users 4/2/2024 1... File folder
ola Windows 4/3/2024 6... File folder
> BThis PC
6 items
12:07 AM
Qa
```

## Slide 46

EoP Deletion Vuln – The disappearing act

Deleting “C:\demo\...<space>”: 1. List all files inside “...<space>”

## Slide 47

“C:\demo\...<space>\” == “C:\demo\”

v

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“C:\demo\...<space>\" == “C:\demo\”
Local Disk (C:) >| demo >
™ Sort = View
Date modified
```

## Slide 48

“C:\demo\...<space>\...<space>” == “C:\demo\...<space>”

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
“C:\demo\...<space>\...<space>” == “C:\demo\...<space>”
Local Disk (C:) >| demo > ...
N Sort = View
```

## Slide 49

EoP Deletion Vuln – The disappearing act

2. Delete all listed files

3. Delete the top directory:

   - “C:\demo\...<space>\” == “C:\demo\”

## Slide 50

EoP Write Vuln – Changing your memories

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EoP Write Vuln —
Changing your memories
SHADOW
COPY
MALICIOUS
C:\DEMO\TEST <+-+-.,,
```

## Slide 51

EoP Write Vuln – Changing your memories

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EoP Write Vuln —
Changing your memories
C:\DEMO:
>TEST
>TEST<SPACE>
```

## Slide 52

## EoP Write Vuln – Changing your memories

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EoP Write Vuln —
Changing your memories
dministrator: ae
® “Sort =View
C:\demo> < * - Local Disk (C:) » demo c Search demo
~ © Quick access Name Date mod... Type Size
™Desktop test 2/21/202..._ File fol
« Downloads test 4/3/2024... File fol.
§ Documents
Pictures
demo
demo
in_test
test
© OneDrive
¥ @This PC
=Desktop
4 Documents
¢ Downloads
® Music
Pictures
BVideos
Local Disk (C:
= Shared Folde|
‘a Network
20
426M
AB BMD sro O
```

## Slide 53

RCE Vuln – Hypnotizing Remote Computers

Archive

## Slide 54

Windows 11 New Archive Types

.rar .tar.bz2 .tbz2 .7z .tar.zst .tzst .tar .tar.xz .txz .tar.gz .tgz

## Slide 55

Symlinks – Extraction Vulnerabilities Lead

**Is it dangerous?**

## Slide 56

Symlinks – Extraction Vulnerabilities Lead

**Not really, because writing to the symlink’s target is not a feature**

## Slide 57

Symlinks – Extraction Vulnerabilities Lead

**“Create Symbolic Links” user right** or **“Developer Mode”**

## Slide 58

Symlinks – Extraction Vulnerabilities Lead

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Symlinks — Extraction
Vulnerabilities Lead
LINK.LINK
LINK.LINK.
```

## Slide 59

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Copy File
There is already a file with the same name in this location.
Click the file you want to keep
— Copy and Replace
Replace the file in the destination folder with the file you are copying:
link
Size: 0 bytes
Date modified: 9/1/2023 10:42 PM
— Don't copy
No files will be changed. Leave this file in the destination folder:
link
link (C:\Users\Or\Downloads\test\archive\archive)
Size: 0 bytes
Date modified: 9/1/2023 10:42 PM
x
```

## Slide 60

## Slide 61

RCE Vuln – Hypnotizing Remote Computers

## Slide 62

RCE Demo

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Startup
Programs > Startup
© New
Home
Gallery
© OneDrive
® Sort
Date modified
= View
Type
This folder is empty.
= Desktop
Downloads *
& Documents
Pictures
® Music
Videos
@This PC
“DVD Drive (D
‘ Network
Search Startup
® Details
Size
Downloads
* ©
© New
Home
Gallery
© OneDrive
= Desktop
Downloads
3 Documents
® Pictures
® Music
Videos
=This PC
DVD Drive (D.
‘aNetwork
S > Downloads >
* Sort = View
Name Date modifi
Today
archive.tar.az 4/3/2024 4:
o
Search Download s
© Details
Type Size
Compres.
GE Q Search
Sune Kono
```

## Slide 63

# CVEs and Responses

## Slide 64

CVEs (Fixed)

**Extraction RCE** CVE-2023-36396, CVSS: 7.8 **Shadow Copy EoP** CVE-2023-32054, CVSS: 7.3 **Process Explorer DoS** CVE-2023-42757 (Reserved)

## Slide 65

## Unfixed

### Deletion EoP

“Thank you again for submitting this issue to Microsoft. We determined that this issue does not require immediate security service but did reveal unexpected behavior. A fix for this issue will be considered in a future version of this product or service.”

### MagicDot Post-Exploitation Techniques

“We have assessed this issue as not a security vulnerability. One reason for that is that no security boundary is crossed. This issue is a post exploitation technique an attacker might leverage once they have already compromised the target machine.”

## Slide 66

## Takeaways

Backwards compatibility & known issues create security risks

Malware can be completely hidden without admin privileges More DOS-to-NT path conversion vulnerabilities Use NT paths instead of DOS paths

## Slide 67

## MagicDot GitHub + Q&A

@oryair1999 https://www.linkedin.com/in/or-yair or.yair@safebreach.com

https://github.com/SafeBreach-Labs/MagicDot
