---
title: "One Flip is All It Takes Identifying Syscall-Guard Variables for Data-Only Attacks"
speakers: ["Song Liu", "Zhechang Zhang", "Hengkai Ye", "Hong Hu"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2024"
edition: "ASIA"
year: 2024
source_pdf: "BlackHat ASIA 2024-Slides/Song Liu & Zhechang Zhang & Hengkai Ye & Hong Hu - One Flip is All It Takes Identifying Syscall-Guard Variables for Data-Only Attacks.pdf"
pages: 37
sha256: "42a6c2a678e0b72ebc4cfe154902a0423048e067168ea339f0979e0c7c7b70b3"
text_chars: 16139
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.4
ocr_unreliable_blocks: 0
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:51:08Z"
---
# One Flip is All It Takes Identifying Syscall-Guard Variables for Data-Only Attacks

**Speakers:** Song Liu, Zhechang Zhang, Hengkai Ye, Hong Hu  
**Conference:** Black Hat ASIA 2024  
**Source:** `BlackHat ASIA 2024-Slides/Song Liu & Zhechang Zhang & Hengkai Ye & Hong Hu - One Flip is All It Takes Identifying Syscall-Guard Variables for Data-Only Attacks.pdf` (37 pages)


## Slide 1

One Flip is All It Takes: Identifying Syscall-Guard Variables for Data-Only Attacks

Speaker: Hengkai Ye The Pennsylvania State University

Other Contributors: Hong Hu, Song Liu, Zhechang Zhang

#BHASIA @BlackHatEvents

## Slide 2

## Team

Hengkai Ye Ph.D. Student Penn State University

Song Liu Ph.D. Student Penn State University

Zhechang Zhang Ph.D. Student Penn State University

Hong Hu Assistant Professor Penn State University

2

## Slide 3

## Current Exploit Method: Control-Flow Hijacking

**_Memory-Access Primitives_**

**_Control Data Primitives_** Arbitrary Read Return Address Arbitrary Write Function Pointer

**_Control-Flow Hijacking_**

Code Injection Code Reuse

3

## Slide 4

## Current Exploit Method: Control-Flow Hijacking

**_Memory-Access Primitives_** Arbitrary Read Arbitrary Write

**_Code-Pointer Integrity_**

**_Control Data_** Return Address Function Pointer

**_Control-Flow Integrity_**

**_Control-Flow Hijacking_**

Code Injection Code Reuse

4

## Slide 5

## Next Gen Exploit Method: Data-Only Attack

**_Code-Pointer Control-Flow Integrity Integrity_**

**_Control-Flow Hijacking_**

**_Memory-Access Control Data Primitives_** Arbitrary Read Return Address Arbitrary Write Function Pointer

Code Injection Code Reuse

**_Non-Control Data_**

**_Data-Only Attack_**

Data-Oriented Programming Block-Oriented Programming

5

## Slide 6

6


> Recovered by OCR — confidence 88/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
\
1S SUCH A THING EVEN POSSIBLE?
```

## Slide 7

## Data-Only Attack

CGI-BIN configuration string in Null Httpd

**_Server_**

Load CGI-BIN configuration: _/usr/local/httpd/cgi-bin /cgi-bin/_ : a CGI request _calculator:_ executable name Search _calculator_ in _/usr/local/httpd/cgi-bin_ if found Run _calculator_

**_Client_**

_POST /cgi-bin/calculator …_ What if configuration _/usr/local/httpd/cgi-bin_ gets corrupted?

_Chen, Shuo, et al. "Non-control-data attacks are realistic threats." USENIX security symposium. Vol. 5. 2005._

7

## Slide 8

## Data-Only Attack

CGI-BIN configuration string in Null Httpd

**_Server_**

Load CGI-BIN configuration: _/usr/local/httpd/cgi-bin /cgi-bin/_ : a CGI request _sh:_ executable name Search _sh_ in _/bin_

**_Client_** Heap corruption Overwrite CGI-BIN to _/bin POST /cgi-bin/sh … … rm /tmp/root-private-file_

Run _/bin/sh_ and remove _/tmp/root-private-file_

_Chen, Shuo, et al. "Non-control-data attacks are realistic threats." USENIX security symposium. Vol. 5. 2005._

8

## Slide 9

## Data-Only Attack

**_Shuo Chen et al. at USENIX Security’05_**

Attack: Root privilege in WU-FTPD server Critical Data: _seteuid( pw->pw_uid );_

**_Moritz Jodeit et al. at HITB GSEC’16_**

Attack: Bypass EMET in Windows Critical Data: _EnableProtectionPtr_

**_Yang Yu at BlackHat USA’14_**

Attack: Code execution in IE browser Critical Data: _if ( safemode & 0xB == 0 ) { Turn_on_God_Mode( ); }_

**_Bing Sun et al. at BlackHat Asia’17_**

Attack: Bypass Control Flow Guard in Windows Critical Data: _gIsCFGEnabled …_

9

## Slide 10

## Next Gen Exploit Method: Data-Only Attack

**_Code-Pointer Control-Flow Integrity Integrity_**

**_Control-Flow Hijacking_**

**_Memory-Access Control Data Primitives_** Arbitrary Read Return Address Arbitrary Write Function Pointer

Code Injection Code Reuse

**_Non-Control Data_**

**_Data-Only Attack_**

Data-Oriented Programming Block-Oriented Programming

10

## Slide 11

## Next Gen Exploit Method: Data-Only Attack

**_Code-Pointer Control-Flow Integrity Integrity Memory-Access Control-Flow Control Data Primitives Attack_** Arbitrary Read Return Address Code Injection Arbitrary Write Function Pointer Code Reuse **_How to Automatically Identify Security-Critical Non-Control Data (Critical Data)Non-Control Data-Only Data Attack_** Data-Oriented Programming **?** Block-Oriented Programming

11

## Slide 12

## Spotting Critical Data is Challenging

### Critical data

- No common low-level properties (e.g., data type, memory location)

- Difficult to infer high-level semantics

Previous work

- Manual inspection: tedious human efforts, not scalable

- FlowStitch [Security’15]: rely on explicit sources/sinks

   - e.g., argument of **_setuid_**

- KENALI [NDSS’16]: rely on error codes in Linux Kernel

12

## Slide 13

## Our Contribution

- Automatic identification of syscall-guard variables

   - Branch force

   - Corruptibility assessment

- A framework - _VIPER_

   - 34 unknown syscall-guard variables from 13 programs

   - 4 new data-only attacks on SQLite and V8

- <u>https://github.com/psu-security-universe/viper</u>

13

## Slide 14

## Motivating Example

### **_How to identify “authenticated”?_**

_Chen, Shuo, et al. "Non-control-data attacks are realistic threats." USENIX security symposium. Vol. 5. 2005._

14

## Slide 15

## Motivating Example

### **_How to identify “authenticated”?_**

Most data-only attacks rely on **_security-related syscalls_**

Security-related syscalls are often guarded by security checks **_Syscall-Guard Branch_** : security checks as conditional branches

**_Syscall-Guard Variable_** : variables in syscall-guard branches **_VIPER_** : identify syscall-guard variables

_Chen, Shuo, et al. "Non-control-data attacks are realistic threats." USENIX security symposium. Vol. 5. 2005._

15

## Slide 16

## Does Syscall-Guard Variable Matter?

A = syscall arguments C = syscall-guard variables

11 syscall arguments 6 syscall-guard variables

16

## Slide 17

## Challenges

- Identify **_sole_** contribution of each variable

   - Symbolic execution can identify a complete path

      - Limitation: cannot tell which variables are more critical

- Efficient and scalable analysis

   - Static analysis

      - Limitations: indirect calls, inter-procedural analysis, etc

17

## Slide 18

## Branch Force: Identify Syscall-Guard Branches

- Flip every branch during execution

- Hook syscalls to find newly invoked ones

- If yes, the flipped is a syscall-guard branch

I I I I
…
S ≠
S1 S2 Sn

18

## Slide 19

## Corruptibility Assessment

- Backward Data-Flow Analysis

   - Generate data flow of syscall-guard variables

- Assessment (for each memory node in the data flow)

   - Metric 1: memory location

      - **_Global > Heap > Stack_**

   - Metric 2: number of memory-write instructions

      - Assumption: every memory-write could be abused

19

## Slide 20

## Workflow of VIPER

##### **_BranchForcer_**

##### **_VariableRator_**

Record record Record original execution
pass binary execute syscalls trace memory Syscall-guard
Program Backward location variable
save branch
flipped Record data ＋ Branch
branches Compare syscall ⊕
branches uniq input execute flow ＋ Syscall
analysis #memory ＋ Input
Input
Flip flip Flip new program write insn ＋ Corruptibility
pass binary execute syscalls LLVM IR

- Unique Branch Flipping

   - Record execution trace on LLVM IR level

- Forkserver

- Simulate execution based on recorded trace

20

## Slide 21

## Evaluation (setting)

- 20 programs for evaluation

   - 9 programs with known data-only attacks (e.g., OpenSSH)

   - 7 programs from FuzzBench (e.g., SQLite)

   - 4 other well-tested programs (e.g., V8)

- Corpus

   - Testcases in source code repository

   - Online corpus (e.g., FuzzBench Dataset)

   - Fuzz with AFL++

21

## Slide 22

## Evaluation (identified syscall-guard variables)

_36 syscall-guard variables from 14 programs_

22


> Recovered by OCR — confidence 90/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Evaluation (identified syscall-guard variables)
Program Guard Variable Branch Location Syscall _ Malicious Goal
sqlite mode shell.c:5002 symlink — create symlinks to any file
shell.c:5038 chmod change any file to any mode
p->doXdgOpen shell.c:20270 execve execute arbitrary program
p->zTempFile shell.c:20560 unlink delete any file
isDelete sqlite3.c:42939 unlink delete any file
zPath sqlite3.c:43094 unlink delete any file
exists sqlite3.c:60294 unlink delete any file
isWal sqlite3.c:58492 unlink delete any file
curl tempstore cookie.c:1732 rename overwrite any file
tempstore hsts.c:386 rename overwrite any file
tempstore altsvc.c:359 rename overwrite any file
harfbuzz blob->mode hb-blob.cc:453 mprotect make RO memory writable
nginx sa_family $_connection.c:631 chmod change file mode
ngx_terminate $_process_cycle.c:305 unlink delete any file
ngx_quit $_process_cycle.c:305 unlink delete any file
ft.st_uid ($: ngx) $_file.c:631 chown change owner of any file
ft.st_mode $_file.c:640 chmod change file mode
openssh result* auth-passwd.c:128 execve login without password.
received_sigterm unlink delete any file
received_sighup sshd.c:1177 execve execute arbitrary program
sudo details->chroot exec.c:173 chroot change root path
info sudo.c:697 chdir change directory path
null httpd in_RequestURI main.c:39 execve enable CGI to run programs
ghttpd filename* protocol.c:127 execve enable CGI to run programs
wu-ftpd RootDirectory chroot change root path of current user
anonymous setgroups obtain root privilege
chroot change root path of anonymous
guest chroot change root path of guest
rval setresuid login without password
jhead RegenThumbnail execve execute arbitrary program
EditComment jhead.c:1003 execve edit any file using vi
Comment Insert fileName jhead.c:1003 execve edit any file using vi
CommentInsertLiteral jhead.c:1003 execve edit any file using vi
jasper fileobj->flags jas_stream.c:1392 unlink delete any file
pdfalto first XRef.cc:240 unlink delete files in specific folders
offsets[0] XRef.cc:240 unlink delete files in specific folders
gzip fd gzip.c:2111 unlink delete any file
v8 enable_os_system d8-posix.cc:762 execve execute any program
setgroups/setresuid
chroot/chdir
36 syscall-guard variables from 14 programs
execve
unlink/rename
15
22
```

## Slide 23

## Evaluation (exploitability investigation)

Exploit Construction 4 CVE Investigation 16 GDB Emulation 36

23


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 86/100 on the text kept, 86/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Evaluation (exploitability investigation)

Program | Guard Variable | Branch Location | Rate (S, H, G) | CK | CVE | Type | Cap
sqlite | mode | shell.c:5002 | (55, 0, 0) |  |  |  |
 | | shell.c:5038 | (75, 0, 0) |  |  |  |
 | p->doXdgOpen | shell.c:20270 | (181770, 0, 0) | ● | 2017-6983 | TC | AW
 | p->zTempFile | shell.c:20560 | (86907, 0, 0) | ● | 2017-6983 | TC | AW
 | isDelete | sqlite3.c:42939 | (8353, 29276, 0) | ● | 2017-6983 | TC | AW
 | zPath | sqlite3.c:43094 | (57, 15036, 0) |  |  |  |
 | exists | sqlite3.c:60294 | (58, 15036, 0) |  |  |  |
 | isWal | sqlite3.c:58492 | (61, 15046, 0) |  |  |  |
curl | tempstore | cookie.c:1732 | (15, 0, 0) | ◐ | 2019-3822 | H/SBoF | AW
 | tempstore | hsts.c:386 | (15, 0, 0) | ◐ | 2019-3822 | H/SBoF | AW
 | tempstore | altsvc.c:359 | (15, 0, 0) | ◐ | 2019-3822 | H/SBoF | AW
harfbuzz | blob->mode | hb-blob.cc:453 | (31, 352, 0) | ◐ | 2015-8947 | HBoF | AW
nginx | sa_family | $_connection.c:631 | (0, 84831, 0) |  |  |  |
 | ngx_terminate | $_process_cycle.c:305 | (0, 0, 208640) | ◐ | 2013-2028 | SBoF | AW
 | ngx_quit | $_process_cycle.c:305 | (0, 0, 208640) | ◐ | 2013-2028 | SBoF | AW
 | ft.st_uid | ($: ngx) $_file.c:631 | (350832, 0, 0) |  |  |  |
 | ft.st_mode | $_file.c:640 | (175218, 0, 0) |  |  |  |
openssh | result* | auth-passwd.c:128 | (5, 48153980, 0) |  |  |  |
 | received_sigterm | sshd.c:1163 | (0, 0, 1463147) |  |  |  |
 | received_sighup | sshd.c:1177 | (0, 0, 1470603) |  |  |  |
sudo | details->chroot | exec.c:173 | (0, 0, 2039) | ◐ | 2012-0809 | FS | AW
 | info | sudo.c:697 | (1702, 253382, 1982) | ◐ | 2012-0809 | FS | AW
null httpd | in_RequestURI | main.c:39 | (0, 525, 0) | ◐ | 2002-1496 | HBoF | AW
ghttpd | filename* | protocol.c:127 | (9, 0, 5912) | ◐ | 2002-1904 | SBoF | AW
wu-ftpd | RootDirectory | ftpd.c:1029 | (0, 0, 7322) |  |  |  |
 | anonymous | ftpd.c:2527 | (0, 0, 7432) |  |  |  |
 |  | ftpd.c:2893 | (0, 0, 8341) |  |  |  |
 | guest | ftpd.c:2893 | (0, 0, 37715) |  |  |  |
 | rval | ftpd.c:2708 | (8, 0, 0) |  |  |  |
jhead | RegenThumbnail | jhead.c:978 | (0, 0, 2856) | ◐ | 2016-3822 | IO | AW
 | EditComment | jhead.c:1003 | (0, 0, 2856) | ◐ | 2016-3822 | IO | AW
 | CommentInsertfileName | jhead.c:1003 | (0, 0, 2856) | ◐ | 2016-3822 | IO | AW
 | CommentInsertLiteral | jhead.c:1003 | (0, 0, 2856) | ◐ | 2016-3822 | IO | AW
jasper | fileobj->flags | jas_stream.c:1392 | (0, 219062, 0) | ◐ | 2020-27828 | HBoF | AW
pdfalto | first | XRef.cc:240 | (1952, 214, 0) |  |  |  |
 | offsets[0] | XRef.cc:240 | (92, 117, 0) |  |  |  |
gzip | fd | gzip.c:2111 | (0, 0, 11886) | ◐ | 2010-0001 | IO | AW
v8 | enable_os_system | d8-posix.cc:762 | (0, 0, 93512607) | ● | 2021-30632 | TC | AW

[Pyramid diagram, three tiers, top to bottom]
Exploit Construction — 4
CVE Investigation — 16
GDB Emulation — 36
```

## Slide 24

## Evaluation (time costs)

We can combine VIPER with other tools for automatic exploit generation

24


> Recovered by OCR — confidence 90/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Evaluation (time costs)
Time Cost
Program Version kLoC Record Flip Rate Toial Total/A Stitch
sqlite 3.40.1 273 288" 112". = 378" 778" 87"
curl 97£7£66 160 23" 32" 689" 744" 248"
harfbuzz 1.3.2 41 17" 8" 8" 33" 33"
systemd v252 543 69" 40" - >109" = =>109"
mbedtls 10ada35—- 128 2" 6" - >8" >8"
openssl 3.0.7 483 13" 61" - >74" >74"
freetype2 cd02d35 119 18" 26" - >44" >44"
nginx 1.20.2 141 238" 22" 329" 589" 118" 121"
openssh 36b00d3 119 1" 4722" 10624" 15347" | 5116" 1110"
sudo 1.9.9 110 16" 16" 260" 292" 18" 393"
null httpd 0.5.1 2 1" 10" 31" 42" 42" 358"
ghttpd 1.4.4 1 1" 36" 72" 109" 55" 48"
orzhttpd 0.0.6 3 1" 32" - >33" >33" 93"
wu-ftpd 2.6.2 18 1" 533" 189" 723" 91" 200"
jhead 3.04 4 1" 2" 288" 291" 25"
jasper 4.0.0 34 37" 16" 84" 137" 137"
pdfalto 0.4 76 342" 116" 107" 565" 282"
gzip 1.12 6 6" 1" 19" 26" 26"
v8 8.5.188 3,586 1" 5833" 874" 6708" 6708"
We can combine VIPER
with other tools for
automatic exploit generation
24
```

## Slide 25

## Case Study: Attacks on SQLite

SQLite: Most widely deployed database engine

- Used in Android, iOS, Chrome, Safari, Opera …

VIPER result

- 7 syscall-guard variables

- 3 new data-only attacks on top 3 syscall-guard variables

   - (demo 1) p->doXdgOpen: arbitrary command execution

   - (demo 2) p->zTempFile: arbitrary file deletion

   - isDelete: arbitrary file deletion

25

## Slide 26

## Case Study 1: Command Execution on SQLite

How SQLite handles query results

- Print on stdout

- Save to a file ( .output filename)

- Edit before saving ( .once –e / .once –x )

How VIPER identified p->doXdgOpen

- BranchForce flips _if (p->doXdgOpen)_ and catches _execve_

- VariableRator generates data flow graph for p->doXdgOpen and p->zTempFile

26

## Slide 27

## Case Study 1: Command Execution on SQLite

Data-flow Graph of p->doXdgOpen

27


> Recovered by OCR — confidence 91/100 on the text kept, 91/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case Study 1: Command Execution on SQLite
%26 = icmp ne i8 %25, 0, !dbg !7114 Stack,GD:0,HD:0,SD:181770
i8 0
| tack, store distance:181770
call void @llvm.memset.p0i8.i64(i8* %5, i8 0, i64 4712, i32 8, il false), !dbg !7101
i8 0
Data-flow Graph of p->doXdgOpen
27
```

## Slide 28

## Case Study 1: Command Execution on SQLite

#### Data-flow Graph of p->zTempFile

28


> Recovered by OCR — confidence 89/100 on the text kept, 89/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Case Study 1: Command Execution on SQLite
%36 = load i8*, i8** %4, align 8, !dbg !7128 Stack,GD:0,HD:0,SD:181774
io store distance:0
store i8* %34, i8** %4, align 8, !dbg !7127
%34 = call i8* (i8*, ...) @sqlite3_mprintf(i8* getelementptr inbounds ([6 x i8], [6 x i8]* @.str.1461, i32 0, i32 0), i8* %30, i8* %33), !dbg !7126
ea
%30 = load i8*, i8** %3, align 8, !dbg !7123
Sa tor distance:0 | \stack, store distance:181774
store i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.1460, i32 0, i32 0), i8** %3, align 8, !dbg !7120 call void @llvm.memset.p0i8.i64(i8* %5, i8 0, i64 4712, i32 8, il false), !dbg !7101
i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.1460, i32 0, i32 0) i8 O
Data-flow Graph of p->zTempFile
28
```

## Slide 29

## Case Study 1: Command Execution on SQLite

One memory bug to corrupt p->doXdgOpen and p->zTempFile

- CVE 2017-6983 ( Kun Yang at BlackHat USA’17 )

   - Arbitrary write primitive

   - Bypass ASLR is feasible

29

## Slide 30

## Demo 1

30


> Recovered by OCR — confidence 82/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
hfy513@ in in sqlite (1fdaa9d) [!?] via C v10.0.0-4ubuntu1-clang via 2 v2
-7.18
```

## Slide 31

## Case Study 2: File Deletion on SQLite

zTempFile is also used in other places

- Flip _if (p->zTempFile == 0)_ and _catches_ unlink

- Both syscall-guard variable and syscall argument are zTempFile

- One shot exploit

31

## Slide 32

## Demo 2

32


> Recovered by OCR — confidence 84/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
in sqlite (1fdaa9d) [!?] via C v10.0.0-4ubuntu1-clang via 2 v2
```

## Slide 33

## Case Study 3: New Attack on V8

V8: Chromium JavaScript engine

- Used in Google Chrome, Microsoft Edge, Opera, Node.js …

- 3,586 KLoC in the latest version

VIPER result

- 2 potential syscall-guard variables

- 1 highly corruptible variable

   - Location: global variable

   - Memory-Write instructions: 93,512,607

33

## Slide 34

## Case Study 3: New Attack on V8

Our Attack (CVE-2021-30632)

- Arbitrary read privilege

   - Bypass ASLR

- Arbitrary write privilege

   - Set options.enable_os_system to 1

34

## Slide 35

## Demo

35


> Recovered by OCR — confidence 77/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Demo
eee
svl6237@14-L-HQH5357-01:~/demo
+ demo i
35
```

## Slide 36

## Conclusion

- _VIPER_ : automatically spotting syscall-guard variables for data-only attacks

   - Design branch force and corruptibility assessment

   - Find 34 previous unknown syscall-guard variables

   - Build 4 new data-only attacks on SQLite and V8

- Open Source

   - VIPER: https://github.com/psu-security-universe/viper

   - Exploits: https://github.com/psu-security-universe/data-only-attacks

36

## Slide 37

# Thank You

Question? hengkai@psu.edu
