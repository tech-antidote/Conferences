---
title: "Lost Control Breaking Hardware-Assisted Kernel Control-Flow Integrity with Page-Oriented Programming"
speakers: ["Seunghun Han"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Seunghun Han _Lost Control Breaking Hardware-Assisted Kernel Control-Flow Integrity with Page-Oriented Programming.pdf"
pages: 76
sha256: "c2f26fda97ca9db3a2e01b2c6a37e0881225e06633b8a197edeba5134ed5f580"
text_chars: 51884
ocr_pages: 2
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:24:03Z"
---
# Lost Control Breaking Hardware-Assisted Kernel Control-Flow Integrity with Page-Oriented Programming

**Speakers:** Seunghun Han  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Seunghun Han _Lost Control Breaking Hardware-Assisted Kernel Control-Flow Integrity with Page-Oriented Programming.pdf` (76 pages)

## Slide 1

**Lost Control: Breaking Hardware-Assisted Kernel Control-Flow Integrity with Page-Oriented Programming Seunghun Han hanseunghun@nsr.re.kr**

**Seong-Joong Kim, Byung-Joon Kim (sungjungk || bjkim)@nsr.re.kr**

#BHUSA @BlackHatEvents

## Slide 2

###### **Who Am I?**

- **Senior security researcher** at the Affiliated Institute of ETRI

- - **Review board member** of **Black Hat Asia** and **KimchiCon** - **Speaker** at **USENIX Security** , **Black Hat USA/Asia/Europe** , **HITBSecConf** , **BlueHat Shanghai** , **TyphoonCon** , **etc.**

- - **Author** of “64-bit multi-core OS principles and structure”

- **Debian Linux maintainer** and **Linux kernel contributor**

- - a.k.a kkamagui,        (     ) **@kkamagui1**

#BHUSA @BlackHatEvents

## Slide 3

###### **Goal of This Presentation**

- **I present weaknesses of state-of-the-art kernel CFIs** - Hardware- and software-based CFIs focus on indirect branches

   - All CFIs, including kernel CFIs, need non-writable code, but it is ensured by the page-level protection mechanism

- **I introduce a novel and page-level code reuse attack called Page-Oriented Programming (POP)**

   - POP utilizes the weaknesses of kernel CFIs

   - It programs page tables within the kernel to create new control flows with an existing kernel memory read and write vulnerability

#BHUSA @BlackHatEvents

## Slide 4

###### **Huge Mistake …**

BEFORE STARTING PH.D.

Thinking Outside the Box

GRADUATION IS POSSIBLE!

AFTER …

**Entering Sleep Mode …** DID YOU TRUST ME, HUH?

#BHUSA @BlackHatEvents

## Slide 5

###### **But, there was light …**

WHAT A SECURE WORLD!

ME COLLEAGUE

###### CONTROL-FLOW INTEGRITY IS EVERYWHERE

#BHUSA @BlackHatEvents

## Slide 6

###### **Wait … What?!**

**WHAT A SECURE WORLD! Control-Flow Integrity (CFI) can make a SECURE world?!** **ME COLLEAGUE CONTROL-FLOW INTEGRITY IS EVERYWHERE**

#BHUSA @BlackHatEvents

## Slide 7

###### **Wait … What?!**

WHAT A SECURE WORLD!
Control-Flow Integrity (CFI) can make
a SECURE world?!
A CRITICAL EVENT is detected!
ME COLLEAGUE
ARE YOU SERIOUS NOW?
CONTROL-FLOW INTEGRITY IS EVERYWHERE

#BHUSA @BlackHatEvents

## Slide 8

###### **Wait … What?!**

WHAT A SECURE WORLD!
CFI
Control-Flow Integrity (CFI) can make
a SECURE world?!
A CRITICAL EV ENT is  detected!
ME
Breaking!
ME MY COLLEAGUE
CHECK ARE YOU THE SECURE WORLDSERIOUS NOW? !
CONTROL-FLOW INTEGRITY IS EVERYWHERE

#BHUSA @BlackHatEvents

## Slide 9

##### **So, this presentation is about Breaking Hardware-Assisted Kernel Control-Flow Integrity with Page-Oriented Programming**

#BHUSA @BlackHatEvents

## Slide 10

###### **So, this presentation is about**

##### **Breaking Hardware-Assisted Kernel Control-Flow Integrity with Page-Oriented Programming**

#BHUSA @BlackHatEvents

## Slide 11

###### **So, this presentation is about**

##### **Breaking Hardware-Assisted Kernel Control-Flow Integrity with Page-Oriented Programming**

#BHUSA @BlackHatEvents

## Slide 12

###### **So, this presentation is about**

##### **Breaking Hardware-Assisted Kernel Control-Flow Integrity with Page-Oriented Programming**

#BHUSA @BlackHatEvents

## Slide 13

##### **So, this presentation is about Breaking Hardware-Assisted Kernel Control-Flow Integrity with Page-Oriented Programming**

#BHUSA @BlackHatEvents

## Slide 14

###### **Contents**

###### **- Control-Flow Integrity (CFI) - Hardware-Assisted Kernel CFI in Use - Page-Oriented Programming - Demo - Conclusion and Black Hat Sound Bytes**

#BHUSA @BlackHatEvents

## Slide 15

###### **Contents**

**- Control-Flow Integrity (CFI) - Hardware-Assisted Kernel CFI in Use - Page-Oriented Programming - Demo - Conclusion and Black Hat Sound Bytes**

#BHUSA @BlackHatEvents

## Slide 16

###### **Control-Flow Integrity (CFI)**

###### **- A control-flow graph (CFG) contains legitimate execution flows of a program**

   - It can be generated from static and dynamic analysis

   - It has forward and backward edges

      - Forward edges consist of indirect calls and jumps

      - Backward edges consist of returns

- **Control-flow integrity (CFI) monitors execution flows with the CFG at run-time and prevents control-flow deviations**

   - The ideal CFI can prevent control-flow hijackings

#BHUSA @BlackHatEvents

## Slide 17

###### **Control-Flow Integrity (CFI)**

: Indirect branch (indirect call or jump) Forward Edge

: Indirect branch (return)

<Example of the CFG and CFI – from  Abadi et al.>

: Direct branch

Backward Edge

#BHUSA @BlackHatEvents

## Slide 18

###### **Control-Flow Integrity (CFI)**

: check the target and transfer

: Indirect branch (indirect call or jump) Forward Edge

: Indirect branch (return) : Direct branch

<Example of the CFG and CFI – from  Abadi et al.>

Backward Edge

#BHUSA @BlackHatEvents

## Slide 19

###### **Control-Flow Integrity (CFI)**

: check the target and transfer **Precise CFGs have more overhead!** : Indirect branch (indirect call or jump) : Indirect branch (return) : Direct branch <Example of the CFG and CFI – from  Abadi et al.> Forward Edge Backward Edge

#BHUSA @BlackHatEvents

## Slide 20

###### **CFI Research**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
rat
CFI Research -
Opaque Control-Flow Integrity
Vishwath Mohan*, Per Larsen’, Stefan Brunthaler!, Kevin W. Hamlen*, and Michael Franz!
*{vishwath.mohan, hamlen}@utdallas.edu
The University of Texas at Dallas
'{perl,s.brunthaler, franz}@uci.edu
LTNSesiaare uw @rUlvsnr tani
Modular Control-Flow Integrity
Ben Niu Gang Tan
Lehigh University
ben210@lehigh.edu _gtan@cse.lehigh.edu
Enforcing Forward-Edge Control-Flow Integrity in GCC & LLVM
Caroline Tice Tom Roeder Peter Collingbourne Stephen Checkoway
Google, Inc. Google, Inc. Google, Inc. Johns Hopkins University
Ulfar Erlingsson Luis Lozano Geoff Pike
Google, Inc. Google, Inc. Google, Inc.
HCFI: Hardware-enforced Control-Flow Integrity
Nick Christoulakis George Christou Elias Athanasopoulos
. FORTH _ FORTH VU University, Amsterdam
christoulak@ics.forth.gr gchri@ics.forth.gr i.a.athanasopoulos@vu.nl
Sotiris loannidis
___ FORTH
sotiris@ics.forth.gr
Per-Input Control-Flow Integrity
Ben Niu
Lehigh University
19 Memorial Dr West
Bethlehem, PA, 18015
ben210@lehigh.edu
Gang Tan
Lehigh University
19 Memorial Dr West
Bethlehem, PA, 18015
gtan@cse.lehigh.edu
Practical Context-Sensitive CFI
Victor van der Veent*
Lionel Sambuc~
Ben Gras*
Cristiano Giuffrida®
Dennis Andriesse** Enes Géktas*
Asia Slowinska® Herbert Bos*
‘Equal contribution joint first authors
ent Danatimannel ComiiataSciancs saciid
Efficient Protection of Path-Sensitive Control Security
Ren Ding” Chenxiong Qian* Chengyu Song William Harris Taesoo Kim
Georgia Tech Georgia Tech UC Riverside Georgia Tech Georgia Tech
Wenke Lee
Georgia Tech
* Equal contribution joint first authors
Origin-sensitive Control Flow Integrity
Mustakimur Rahman Khandaker Wenging Liu Abu Naser
Florida State University Florida State University Florida State University
mrk15e@my,fsu.edu wl16c@my,fsu.edu anl6e@my,fsu.edu
Zhi Wang Jie Yang
Florida State University Florida State University
zwang @cs.fsu.edu Jjyang @cs.fsu.edu
Abstract performance, direct access to resources, and rich legacy. How-
CFlis an effective, generic defense against control-flow hijack-
ing attacks, especially for C/C++ programs. However, most
previous CFI systems have poor security as demonstrated by
their large equivalence class (EC) sizes. An EC is a set of
targets that are indistinguishable from each other in the CFI
policy; ie., an attacker can “bend” the control flow within an
EC without being detected. As such, the large ECs denote the
weakest link in a CFI system and should be broken down in
order to improve security.
An approach to improve the security of CFI is to use
contextual information, such as the last branches taken, to
refine the CFI policy, the so-called context-sensitive CFI.
However, contexts based on the recent execution history are
often inadequate in breaking down large ECs due to the limited
number of incoming execution paths to an indirect control
ever, they lack security and safety guarantees of more modern
programming languages, such as Rust and Go. Vulnerabilities
in C/C++ can lead to serious consequences, especially for
low-level software. Many defenses have been proposed to
retrofit security into C/C++ programs. Control-flow integrity
(CFI) is a generic defense against most, if not all, control-flow
hijacking attacks. It enforces the policy that run-time control
flows must follow valid paths in the program’s control-flow
graph (CFG). Since its introduction in the seminal work by
Abadi et al. [2], there has been a long stream of research in
CFI [1,3,6,9, 11-14, 16, 17,21,25,28,29,31,38,40,41,43,44].
Many earlier systems aim at improving the performance by
trading security for efficiency [25,41,43, 44], making them
vulnerable to various attacks [6, 13, 15, 16]. Recent work
focuses more on improving the precision and security of
CFI [14, 17,21, 38], which can roughly be quantified by the
Enforcing Unique Code Target Property
for Control-Flow Integrity
Hong Hu, Chenxiong Qian, Carter Yagemann, Simon Pak Ho Chung,
William R. Harris", Taesoo Kim and Wenke Lee
Georgia Institute of Technology _* Galois Inc.
ABSTRACT
De cal ab contol los inteoin CH iste sop contal backing
R. Harris, Taesoo Kim and Wenke Lee. 2018. Enforcing Unique Code Tar-
get Property for Control-Flow Integrity. In 2018 ACM SIGSAC Conference
Taming Transactions: Towards Hardware-Assisted
Control Flow Integrity using Transactional Memory
Marius Muench!, Fabio Pagani!, Yan Shoshitaishvili?, Christopher Kruegel?,
Giovanni Vigna”, and Davide Balzarotti!
1 Burecom, Sophia Antipolis, France
2 University of California, Santa Barbara
Abstract. Control Flow Integrity (CFI) is a promising defense technique against
code-reuse attacks. While proposals to use hardware features to support CFI al-
ready exist, there is still a growing demand for an architectural CFI support on
commodity hardware. To tackle this problem, in this paper we demonstrate that
the Transactional Synchronization Extensions (TSX) recently introduced by Intel
in the x86-64 instruction set can be used to support CFI.
The main idea of our approach is to map control flow transitions into transactions.
This way, violations of the intended control flow graphs would then trigger trans-
actional aborts, which constitutes the core of our TSX-based CFI solution. To
prove the feasibility of our technique, we designed and implemented two coarse-
grained CFI proof-of-concept implementations using the new TSX features. In
particular, we show how hardware-supported transactions can be used to enforce
both loose CFI (which does not need to extract the control flow graph in advance)
and strict CFI (which requires pre-computed labels to achieve a better precision).
All solutions are based on a compile-time instrumentation.
2019 IEEE European Symposium on Security and Privacy (EuroS&P)
Adaptive Call-site Sensitive Control Flow Integrity
Mustakimur Khandaker* Abu Naser* Wenging Liu* Zhi Wang* Yajin Zhou! Yuegiang Cheng*
* Deparment of Computer Science, Florida State University, Tallahassee, USA
Email: {mrkl5e, an16e, wl16c} @my.fsu.edu, zwang@cs.fsu.edu
t School of Computer Science, Zhejiang University, Hangzhou, China
Email: yajin_zhou@zju.edu.cn
+ Baidu X-lab, Sunnyvale, USA
iia
In-Kernel Control-Flow Integrity on Commodity OSes
using ARM Pointer Authentication
Sungbae Yoo"? Jinbum Park*? Seolheui Kim* Yeji Kim* Taesoo Kim**
t Samsung Research,
* Georgia Institute of Technology
Abstract
This paper presents an in-kernel, hardware-based control-flow
integrity (CFI) protection, called PAL, that utilizes ARM’s
Pointer Authentication (PA). It provides three important ben-
efits over commercial, state-of-the-art PA-based CFls like
i0S’s: 1) enhancing CFI precision via automated refinement
techniques, 2) addressing hindsight problems of PA for in-
kernel uses such as preemptive hijacking and brute-forcing
attacks, and 3) assuring the algorithmic or implementation
correctness via post validation.
PAL achieves these goals in an OS-agnostic manner, so
could be applied to commodity OSes like Linux and FreeBSD.
The precision of the CFI protection can be adjusted for better
performance or improved for better security with minimal en-
gineering efforts. Our evaluation shows that PAL incurs neg-
ern operating systems like Android, Windows, and iOS all
implement some forms of CFI [8,55, 67, 68].
During the last several years, there has been exhaustive
research exploration of CFI’s design space [16], which falls
broadly into two categories: D enhancing the precision of
CFI (i.e., reducing the number of targets that an indirect call
can take); and @ making CFI protection faster and practical
(ie., incurring minimum CPU and memory overheads). The
community has improved CFI precision by providing better
algorithmic advances to model control-flow transitions accu-
rately [30,45], or by utilizing exact run-time contexts [27,31].
However, in practice, the performance overhead often de-
termines the feasibility of actual deployment—it would be
acceptable to prevent the most common cases with negligible
overhead rather than fully preventing all of them with obtru-
ive overhead One recent anpnroach taken hy Annle [2] and
```

## Slide 21

###### **Contents**

**- Control-Flow Integrity (CFI) - Hardware-Assisted Kernel CFI in Use - Page-Oriented Programming - Demo - Conclusion and Black Hat Sound Bytes**

#BHUSA @BlackHatEvents

## Slide 22

###### **CFIs in use are …**

###### **- Microsoft Control-Flow Guard (CFG)**

- Has a **bitmap-based** forward-edge verification policy

- Utilizes Intel Control-flow Enforcement Technology (CET)

- **Clang/LLVM CFI**

   - Has a **function type-based** forward-edge verification policy - Can utilize Intel CET

- **FineIBT**

   - Is based on the Clang/LLVM CFI and Intel CET but has a callee-side verification policy

   - Is applied to the Linux kernel from v6.2.0

#BHUSA @BlackHatEvents

## Slide 23

###### **CFIs in use are …**

**- Microsoft Control-Flow Guard (CFG)**

- Has a **bitmap-based** forward-edge verification policy

- Utilizes Intel Control-flow Enforcement Technology <u>(CET)</u> - **Clang/LLVM CFI** - Has a **function type-based** forward-edge verification policy **What is Intel CET?** - Can utilize Intel CET

- **FineIBT**

   - Is based on the Clang/LLVM CFI and Intel CET but has a callee-side verification policy

- Is applied to the Linux kernel from v6.2.0

#BHUSA @BlackHatEvents

## Slide 24

###### **Intel Control-flow Enforcement Technology (CET)**

- **Has Indirect Branch Tracking (IBT)**

   - It utilizes ENDBR32 and ENDBR64 instructions to mark valid target locations of indirect calls and jumps

   - They can only transfer to the ENDBRANCH instruction (ENDBR32 for x32 or ENDBR64 for x64)

- **Has Shadow Stack (SS)**

   - It saves the return address to the protected area when calling a function

   - It pops return addresses from both the stack and protected area and compares them when returning to the call-site

#BHUSA @BlackHatEvents

## Slide 25

###### **Intel Control-flow Enforcement Technology (CET)**

```
400000: <main>
endbr64
```

```
...
movq $0x400200, %rcx
call *%rcx
...
retq
400200: <func>
endbr64
...
instructions
...
retq
```

**Indirect Branch Tracking (IBT) Example**

#BHUSA @BlackHatEvents

## Slide 26

###### **Intel Control-flow Enforcement Technology (CET)**

**`400000: <main>` Stack Shadow Stack** `endbr64 ... movq $` **`0x400200`** `, %rcx` **`Return Addr. Return Addr. call *%rcx <0x3f0010> <0x3f0010>`** Before `... Local` **`Return Addr.`** SSP `retq Variables` **`<0x400040>`** After SSP **`400200: <func>`** `Parameters` Before **`endbr64`** RSP **`Return Addr.`** `...` After **`<0x400040>`** `instructions` RSP `... retq`

**Indirect Branch Tracking (IBT) Example**

**Shadow Stack (SS) Example**

#BHUSA @BlackHatEvents

## Slide 27

###### **So, what is the hardware-assisted CFI?**

- **It means the software-based CFI assisted by the hardwarebased CFI**

   - The software-based CFI cannot restrict indirect branches strictly - Indirect branches (call, jump, and return) can still transfer to any location of a program under CFI enforcement

   - The hardware-based CFI (CET) can enforce strong policies to the branches

      - The target of the indirect call or jump has to start with the ENDBRANCH instruction (IBT)

      - The return address has to match the exact call-site (SS)

#BHUSA @BlackHatEvents

## Slide 28

###### **Then, the hardware-assisted KERNEL CFI?**

###### **- It has special features that support various control flows and languages**

   - System calls, interrupts, and exceptions

   - C, C++, Rust, and even assembly!

- **Commodity OSes have their own kernel CFIs**

   - Microsoft CFG with Intel CET for the Windows kernel

   - Clang/LLVM kCFI (kernel CFI) with Intel CET and FineIBT for the Linux kernel

      - The shadow stack of Intel CET is not ready for the Linux kernel yet

#BHUSA @BlackHatEvents

## Slide 29

###### **Hardware-Assisted KERNEL CFI – Clang/LLVM kCFI**

- `1:` **`ffff4000: <_stext>`** `2:  endbr64`

```
...
```

`; Address of <func>` **S/W-based** `;` **`-0x00050794 (-Function signature)`** `;` **`0xfffaf86c`** `+` **`0x50794 = (DWORD) 0` CFI and** `;` **`CFI check` caller-side** `; CFI error` **verification**

- `3:  movq` **`$0xffff4200`** `, %r11 4:  mov` **`$0xfffaf86c`** `, %r10d 5:  add` **`-0x4(%r11),`** `%r10d 6:  je .indirect_call 7:  ud2 8:` **`.indirect_call:`** `9:` **`call *%r11`**

- `10:  instructions ...`

###### **H/W-based CFI**

```
11: ffff41fc: <__cfi_func>
12:94 07 05 00; 0x00050794 (Function signature)
```

```
13: ffff4200: <func>
14:endbr64
15:  instructions ...
```

#BHUSA @BlackHatEvents

## Slide 30

###### **Hardware-Assisted KERNEL CFI – FineIBT**

- `1:` **`ffff4000: <_stext>`**

- `2:  endbr64`

```
...
```

   - `3:  movq $` **`0xffff4200`** `, %r11       ; Address of <func> 4:  mov` **`$0xb4cf680c`** `, %r10d      ;` **`0x0xb4cf680c (Function signature)`** `5:  sub` **`$0x10`** `, %r11             ; Address of <__cfi_func> 6:` **`call %r11`**

   - `7:` **`ffff41f0: <__cfi_func>`**

   - `8:` **`endbr64`**

- `9:` **`sub  $0xb4cf680c, %r10d      ; 0xb4cf680c - 0xb4cf680c = 0`**

- `10:  je   $0xffff4200             ;` **`CFI check`**

- `11:  ud2                          ; CFI error`

- `12:  nop`

###### **Callee-side verification**

```
...
```

- `13:` **`ffff4200: <func>`**

```
14:  endbr64
15:  instructions ...
```

#BHUSA @BlackHatEvents

## Slide 31

###### **Assumption of CFIs – Non-Writable Code**

- `1:` **`ffff4000: <_stext>`** `2:  endbr64 ...`

- `3:  movq $` **`0xffff4200`** `, %r11`

- `4:  mov  $0xb4cf680c, %r10d`

- `5:` **`sub  $0x10, %r11`**

- `6:  call %r11`

```
7: ffff41f0: <__cfi_func>
8:  endbr64
9:  sub  $0xb4cf680c, %r10d
10:  je   $0xffff4200
11:  ud2
12:  nop
```

```
...
13:ffff4200: <func>
14:  endbr64
15:  instructions ...
```

```
1: ffff4000: <_stext>
Other Indirect
2:  endbr64
Branches
...
```

```
3:  movq $0xffff4200, %r11
4:  mov  $0xb4cf680c, %r10d
5:  nop
6:  call %r11
```

```
7: ffff41f0: <__cfi_func>
8:  endbr64
9:  sub  $0xb4cf680c, %r10d
10:  je   $0xffff4200
```

```
11:  nop
12:  nop
...
```

```
13:ffff4200: <func>
14:  endbr64
15:  instructions ...
```

#BHUSA @BlackHatEvents

## Slide 32

###### **Assumption of CFIs – Non-Writable Code**

`1:` **`ffff4000: <_stext>`** `1:` **`ffff4000: <_stext>`** `Other Indirect 2:  endbr64 2:  endbr64 Branches ... ... 3:  movq $` **`0xffff4200`** `, %r11 3:  movq $` **`0xffff4200`** `, %r11 4:  mov  $0xb4cf680c, %r10d 4:  mov  $0xb4cf680c, %r10d 5:` **`sub  $0x10, %r11`** `5:` **`nop`** `6:  call %r11 6:  call %r11 7: ffff41f0: <__cfi_func> 7: ffff41f0: <__cfi_func> 8:  endbr64 8:  endbr64 9:  sub  $0xb4cf680c, %r10d 9:  sub  $0xb4cf680c, %r10d 10:  je   $0xffff4200 10:  je   $0xffff4200 11:` **`ud2`** `11:` **`nop`** `12:  nop 12:  nop` **Without non-writable code,** `... ... 13:` **`ffff4200: <func>`** `13:` **`ffff4200: <func>` CFI can be neutralized!** `14:  endbr64 14:  endbr64 15:  instructions ... 15:  instructions ...`

#BHUSA @BlackHatEvents

## Slide 33

###### **Non-Writable Code for Commodity OSes**

- **The kernel ensures non-writable code for applications**

   - It sets read-only permissions to page tables for code pages of applications

   - Kernel vulnerabilities are needed to change the permissions - ~~Because~~ CFI can prevent control-flow deviations like calling **If** VirtualProtect() or mprotect()

- **Then, what ensures non-writable code for the kernel?**

   - **PAGE TABLES!**

#BHUSA @BlackHatEvents

## Slide 34

**Non-Writable Code for Commodity OSes - The kernel ensures non-writable code for applications** SO, YOU ENSURE IT FOR THE KERNEL? - It sets read-only permissions to page tables for code pages of applications - Kernel vulnerabilities are needed to change the permissions - ~~Because~~ CFI can prevent control-flow deviations like calling **If** VirtualProtect() or mprotect() **- Then, what ensures non-writable code for the kernel?** - **<u>PAGE TABLES!</u>** ME PAGE TABLE

TRUST ME, DUDE! TRUST ME!

#BHUSA @BlackHatEvents

## Slide 35

**Non-Writable Code for Commodity OSes - The kernel ensures non-writable code for applications** SO, YOU ENSURE IT FOR THE KERNEL? - It sets read-only permissions to page tables for code pages of applications - Kernel vulnerabilities are needed to change the permissions - ~~Because~~ CFI can prevent control-flow deviations like calling **If** VirtualProtect() or mprotect() **-We need the  Then, what ensures non-writable code for the kernel?non-writable code mechanism** - **<u>PAGE TABLES!</u>** ME PAGE TABLE **~~for th~~ e kerne** **l, no t** **the TRUS T!** TRUST ME, DUDE! TRUST ME!

#BHUSA @BlackHatEvents

## Slide 36

###### **Hypervisor-Based Non-Writable Code Mechanism (1)**

Commodity OS Hypervisor
Guest Host
Page Table SLAT Table* **
Logical Address Physical Address
Guest Physical Host Physical S U
R W X R W
Address Address X X
0x00401000 1 0 1 0x88001000 1 0 1 0 Kernel
Kernel
Code
0x00402000 1 0 1 0x88002000 1 0 1 0 Code
RO Data 0x0040a000 1 0 0 0x8800a000 1 0 0 0
RO Data
RW Data 0x0040b000 1 1 0 0x8800b000 1 1 0 0 RW Data
SX: Supervisor Execute    UX: User Execute

**`*` Intel Extended Page Table (EPT) and AMD Rapid Virtualization Indexing (RVI) support Second-Level Address Translation (SLAT)** **`**` Intel Mode-Based Execution Control (MBEC) and AMD Guest Mode Execution Trap (GMET) support the mode-based execution**

#BHUSA @BlackHatEvents

## Slide 37

###### **Hypervisor-Based Non-Writable Code Mechanism (2)**

Commodity OS Hypervisor
Guest Host
Page Table SLAT Table
Logical Address Physical Address
Guest Physical Host Physical S U
R W X R W
Address Address X X
0x00401000 1 10 1 0x88001000 1 0 1 0 Kernel
Kernel
Code
0x00402000 1 0 1 0x88002000 1 0 1 0 Code
RO Data 0x0040a000 1 10 0 0x8800a000 1 0 0 0
RO Data
RW Data 0x0040b000 1 1 0 0x8800b000 1 1 0 0 RW Data

###### **`SX: Supervisor Execute    UX: User Execute`**

#BHUSA @BlackHatEvents

## Slide 38

###### **Hypervisor-Based Non-Writable Code Mechanism (3)**

Commodity OS Hypervisor
Guest Host
Page Table SLAT Table
Logical Address Physical Address
Guest Physical Host Physical S U
R W X R W
Address Address X X
0x00401000 1 10 1 0x88001000 1 0 1 0 Kernel
Kernel
Code
0x00402000 1 0 1 0x88002000 1 0 1 0 Code
RO Data 0x0040a000 1 0 0 0x8800a000 1 0 0 0
Kernel RO Data
Data
Code 0x0040b000 1 1 01 0x8800b000 1 1 0 0 RW Data
SX: Supervisor Execute    UX: User Execute

###### **`SX: Supervisor Execute    UX: User Execute`**

#BHUSA @BlackHatEvents

## Slide 39

###### **Hypervisor-Based Non-Writable Code Mechanism (3)**

**Commodity OS Hypervisor Guest Host Page Table SLAT Table Logical Address Physical Address Guest Physical Host Physical S U R W X R W Address Address X X** **`0x00401000 1 10 1 0x88001000 1 0 1 0` Kernel Kernel Code** **`0x00402000 1 0 1 0x88002000 1 0 1 0` Code RO Data** **`0x0040a000 1 0 0 0x8800a000 1 0 0 0` KernelU** **~~na~~** **~~u~~** **thoriz e** **~~d m~~** **~~o~~** **difica tio** **~~n an~~ dRO Data Data Code** **~~i~~** **~~n~~** **`0x0040b000`** **jectio** **`1` n** **`1 01`** **~~are~~** **preven** **`0x8800b000 1 1` te** **`0 0`** **~~d!~~ RW Data** **`SX: Supervisor Execute    UX: User Execute`**

#BHUSA @BlackHatEvents

## Slide 40

###### **Contents**

**- Control-Flow Integrity (CFI) - Hardware-Assisted Kernel CFI in Use - Page-Oriented Programming - Demo - Conclusion and Black Hat Sound Bytes**

#BHUSA @BlackHatEvents

## Slide 41

#### **The hypervisor-based non-writable code mechanism and hardware-assisted kernel CFI are effective and work properly**

#BHUSA @BlackHatEvents

## Slide 42

## **The hypervisor-based non-writable code mechanism and hardware-assisted kernel CFI** **~~are~~ ed effective and work properly because of this talk!**

#BHUSA @BlackHatEvents

## Slide 43

###### **Weakness of the Hypervisor-Based Mechanism**

Commodity OS Hypervisor
Guest Host
Page Table SLAT Table
Logical Address Physical Address
Guest Physical Host Physical S U
R W X R W
Address Address X X
0xff881211: 0x00401000 1 0 1 0x88001000 1 0 1 0
kset_
system_call(arg)
… 0x00402000 1 0 1 0x88002000 1 0 1 0 time()
0xff885211: 0x00405000 1 0 1 0x88005000 1 0 1 0 commit
commit_creds(arg)
… 0x00406000 1 0 1 0x88006000 1 0 1 0 creds()
Page offsets are identical!
SX: Supervisor Execute    UX: User Execute

#BHUSA @BlackHatEvents

## Slide 44

###### **Weakness of the Hypervisor-Based Mechanism**

Commodity OS Hypervisor
Guest Host
Page Table SLAT Table
Logical Address Physical Address
Guest Physical Host Physical S U
R W X R W
Address Address X X
0xff881211: 0x004051000 1 0 1 0x88001000 1 0 1 0
kset_
system_call(arg)
… 0x004062000 1 0 1 0x88002000 1 0 1 0 time()
0xff885211: 0x00405000 1 0 1 0x88005000 1 0 1 0 commit
commit_creds(arg)
… 0x00406000 1 0 1 0x88006000 1 0 1 0 creds()

```
SX: Supervisor Execute    UX: User Execute
```

#BHUSA @BlackHatEvents

## Slide 45

###### **Weakness of the Hypervisor-Based Mechanism**

Commodity OS Hypervisor
Guest Host
Page Table SLAT Table
Logical Address Physical Address
Guest Physical Host Physical S U
R W X R W
Address Address X X
0xff881211: 0x004051000 1 0 1 0x88001000 1 0 1 0
kset_
system_call(arg)
… 0x004062000 1 0 1 0x88002000 1 0 1 0 time()
0xff885211: 0x00405000 1 0 1 0x88005000 1 0 1 0 commit
commit_creds(arg)
… 0x00406000 1 0 1 0x88006000 1 0 1 0 creds()
call_syscall(root_cred)
SX: Supervisor Execute    UX: User Execute

#BHUSA @BlackHatEvents

## Slide 46

### **Weakness of the Hardware-Assisted Kernel CFI The hardware-assisted kernel CFI JUST focuses on INDIRECT BRANCHES!**

#BHUSA @BlackHatEvents

## Slide 47

###### **Page-Oriented Programming (POP)**

- **Is a novel page-level code reuse attack such as ROP and JOP** - It exploits the **weaknesses** of **state-of-the-art kernel CFIs**

      - It utilizes legitimate code pages and direct branches

   - It programs **page tables** within the kernel with a kernel memory read and write vulnerability

- **Can make new control flows**

   - It identifies page-level gadgets and stitches them

   - So, it can **bypass** strong **CFI** enforcement!

#BHUSA @BlackHatEvents

## Slide 48

###### **Stage of POP**

Remapping Pages
NOP
01010 Disassembling Call
01010 Gadget
NOP
10...
SYS . . .
Kernel Gadget and System Call commit_ NOP
Call Gadget creds() Gadget
Binary System Call List
(1) Page Carving (2) Page Stitching
; Syscall number for exploitation
CPU CPU
mov $syscall_number, %rax
Flushing
TLB* TLB
OLD NEW ; Argument for commit_creds()
OLD NEW mov $0xdeafbeef, %rdi or %rbx
... ... ; Execute the new control flow!
* Translation Lookaside Buffer syscall or int $0x80

**(3) Page Flushing**

**(4) Exploitation**

#BHUSA @BlackHatEvents

## Slide 49

###### **POP - Page Carving Stage**

**- Identifies gadgets and system call candidates**

- Gadgets and system call candidates are functions

- Call gadgets connect system call candidates to commit_creds() - NOP (no-operation) gadgets unlink unessential functions of gadgets, system call candidates, and commit_creds()

```
<NOP_gadget_1>:
endbr64
<no_calls_and_jumps_here>
ret
```

```
<call_gadget>:endbr64
endbr64<no_calls_and_jumps_here>
...ret
call $0xdeadbeef||
<NOP_gadget_2>:
jmp  $0xcafebebe
endbr64
...
retxor %rax, %rax
ret
```

#BHUSA @BlackHatEvents

## Slide 50

###### **POP - Page Stitching Stage**

- **Chains gadgets with data to create new control flows**

   - It remaps a gadget’s physical page to the logical address of the direct branch target with page tables

   - It also remaps an argument that is passed to commit_creds()

- **Builds private page tables for the exploitation**

   - Kernel page tables are shared for all processes and kernel threads

   - It allocates new page tables whenever the remapping is needed

- **Allocates free physical pages from the system RAM**

   - It allocates and accesses them in reverse order with the direct mapping area (page_offset_base)

#BHUSA @BlackHatEvents

## Slide 51

###### **<Original Control Flow>**

```
0xffff1220:0xffff1330:
<commit_creds(arg)>:<subfunction_1>
<updating creds>ret
call 0xffff1330
call 0xffff14400xffff1440:
...
<subfunction_2>
retret
```

```
<sys_set_uid>:
<validating creds>
mov arg_ptr, %rdi
call 0xffff1220
...
ret
```

**Page Remapping**

**Page Replacing**

###### **<New Control Flow>**

```
0xffffa350:0xffffa220:0xffffa330:
<sys_candidate>:
<NOP_gadget_1>:
mov arg_ptr, %rdi<call_gadget>:<commit_creds(arg)>:
ret
call 0xffffa350......
...call 0xffffa220<updating creds>
ret...call 0xffffa330
retcall 0xffffa440
0xffffa440:440::
...
0xfffff000:<NOP_gadget_2>:
ret
ret
```

```
0xffffa440:440::
<NOP_gadget_2>:
ret
```

```
0xfffff000:
<modified_cred>:
uid = 0 (root)
```

#BHUSA @BlackHatEvents

## Slide 52

###### **POP - Page Flushing Stage**

**- Flushes stale mappings in the TLB to apply new ones** - Modern CPUs manage TLB data to accelerate the logical to physical address translation

   - Remapped physical pages are not accessed until old mappings are flushed out

- **Sleeps for a sufficient time after removing global bits in page tables**

   - The TLB has limited space, so it cannot hold all kernel mapping data - System services, applications, and various interrupts help us!

**- Considers the CPU affinity because each core has its own TLB** #BHUSA @BlackHatEvents

## Slide 53

###### **POP - Exploitation Stage**

**- Executes the target system call with an arbitrary argument** - Then, the new control flow calls commit_creds() without verification - It must be executed on the same core where the page flushing stage was done!

```
<main of the malicious application>:
; Syscall number to exploit
mov $syscall_number, %rax
; Argument for commit_creds()
mov $0xfffff000, %rdior %rbx
; Execute the new control flow
syscall orint $0x80
<DO MALICIOUS BEHAVIORS WITH ROOT>
```

- Both x64 and x32 system calls can be used!

#BHUSA @BlackHatEvents

## Slide 54

POP - Exploitation Stage
SO, YOU MEAN THIS REALLY WORKS?
- Executes the target system call with an arbitrary argument
- Then, the new control flow calls commit_creds() without verification
- It must be executed on the same core where the page flushing stage
was done!
<main of the malicious application>:
- Both x64 and x32 system ; Syscall number to exploit
mov $syscall_number, %rax
calls can be used!
; Argument for commit_creds()
mov $0xfffff000, %rdi or %rbx
YOU ; Execute the new control flow ME
syscall or int $0x80
<DO MALICIOUS BEHAVIORS WITH ROOT>
TRUST THE DEMO, DUDE! TRUST IT!

#BHUSA @BlackHatEvents

## Slide 55

###### **Contents**

**- Control-Flow Integrity (CFI) - Hardware-Assisted Kernel CFI in Use - Page-Oriented Programming - Demo - Conclusion and Black Hat Sound Bytes**

#BHUSA @BlackHatEvents

## Slide 56

###### **Environment**

###### **- Machine: ASUS TUF DASH F15**

      - **Intel Core i7-12650H** , 16GB RAM

- **OS and Linux kernel**

   - **Ubuntu 22.04 LTS** and **LLVM 6.0.0**

   - **Linux kernel 6.3.11** with **FineIBT** for the kernel CFI

      - Without CONFIG_JUMP_LABEL and CONFIG_RETHUNK to reduce runtime code patches

      - A kernel driver with **information disclosure** and **memory read and write vulnerabilities**

- **Open-source hypervisor**

   - **Shadow-box** (from Black Hat Asia 2017) with **Intel CET** and **MBEC** supports

#BHUSA @BlackHatEvents

## Slide 57

```
0xffffffff81122220 <commit_creds>:
endbr64
```

```
0xffffffff812bc9a0
<__x64_sys_bpf>(arg1):
call 0xffffffff812bd5e0
...
```

```
; gs: 0xffff8884a0200000 <__per_cpu_offset[0]>
; rip: 0xffffffff8112223a
; rbx: 0xffff8884a02327c0=> <current>
mov  %gs:0x7ef10586(%rip), %rbx
```

```
; rip: 0xffffffff811222f4
; esi: 0xffffffff844e2798<suid_dumpable>
mov  0x33c04a4(%rip), %esi
```

```
0xffffffff81c605e0
```

```
<xhci_address_device>:
call 0xffffffff81c61a90
...
```

```
0xffffffff8153da90
```

```
<configfs_open_file>:
call 0xffffffff8153e220
...
```

```
call 0xffffffff814732d0<set_dumpable>
call 0xffffffff81640120<key_fsuid_changed>
call 0xffffffff81640180<key_fsgid_changed>
```

`call` **`0xffffffff811263d0`** `<` **`inc_rlimit_ucounts`** `> ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;` **`<Instructions for updating new credentials>`** `;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; call` **`0xffffffff81126460`** `<` **`dec_rlimit_ucounts`** `> call` **`0xffffffff81aa8fb0`** `<` **`proc_id_connector`** `> call` **`0xffffffff811a7d90`** `<` **`call_rcu`** `> ret` #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 58

```
0xffffffff81122220 <commit_creds>:
```

```
endbr64
```

```
0xffffffff812bc9a0
```

```
<__x64_sys_bpf>(arg1):
call 0xffffffff812bd5e0
...
-0x9a3000
```

```
; gs: 0xffff8884a0200000 <__per_cpu_offset[0]>
; rip: 0xffffffff8112223a
; rbx: 0xffff8884a02327c0=> <current>
mov  %gs:0x7ef10586(%rip), %rbx
```

```
; rip: 0xffffffff811222f4
; esi: 0xffffffff844e2798<suid_dumpable>
mov  0x33c04a4(%rip), %esi
```

```
0xffffffff812bd0xffffffff81c605e05e0
```

```
<xhci_address_device>:
call 0xffffffff812bec61a90
...
```

```
0xffffffff8153da90
```

```
<configfs_open_file>:
call 0xffffffff8153e220
...
```

```
call 0xffffffff814732d0<set_dumpable>
call 0xffffffff81640120<key_fsuid_changed>
call 0xffffffff81640180<key_fsgid_changed>
```

`call` **`0xffffffff811263d0`** `<` **`inc_rlimit_ucounts`** `> ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;` **`<Instructions for updating new credentials>`** `;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; call` **`0xffffffff81126460`** `<` **`dec_rlimit_ucounts`** `> call` **`0xffffffff81aa8fb0`** `<` **`proc_id_connector`** `> call` **`0xffffffff811a7d90`** `<` **`call_rcu`** `> ret` #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 59

0xffffffff812bc9a0
<__x64_sys_bpf>(arg1):
call  0xffffffff812bd5e0
...
- 0x9a3000

```
0xffffffff812bd0xffffffff81c605e05e0
<xhci_address_device>:
call 0xffffffff812bec61a90
...
-0x27f000
```

```
0xffffffff812be0xffffffff8153da90  a90
<configfs_open_file>:
call 0xffffffff812bf53e220
...
```

```
0xffffffff81122220 <commit_creds>:
```

```
endbr64
```

```
; gs: 0xffff8884a0200000 <__per_cpu_offset[0]>
; rip: 0xffffffff8112223a
; rbx: 0xffff8884a02327c0=> <current>
mov  %gs:0x7ef10586(%rip), %rbx
```

```
; rip: 0xffffffff811222f4
; esi: 0xffffffff844e2798<suid_dumpable>
mov  0x33c04a4(%rip), %esi
```

```
call 0xffffffff814732d0<set_dumpable>
call 0xffffffff81640120<key_fsuid_changed>
call 0xffffffff81640180<key_fsgid_changed>
```

`call` **`0xffffffff811263d0`** `<` **`inc_rlimit_ucounts`** `> ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;` **`<Instructions for updating new credentials>`** `;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; call` **`0xffffffff81126460`** `<` **`dec_rlimit_ucounts`** `> call` **`0xffffffff81aa8fb0`** `<` **`proc_id_connector`** `> call` **`0xffffffff811a7d90`** `<` **`call_rcu`** `> ret` #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 60

0xffffffff812bc9a0
<__x64_sys_bpf>(arg1):
call  0xffffffff812bd5e0
...
- 0x9a3000
0xffffffff812bd 0xffffffff81c605e0 5e0
<xhci_address_device>:
call  0xffffffff812bec61a90
...
- 0x27f000

```
0xffffffff812be0xffffffff8153da90  a90
<configfs_open_file>:
call 0xffffffff812bf53e220
...
```

```
+0x19d000
```

```
0xffffffff812bf0xffffffff81122220 <commit_creds>:220
```

```
endbr64
```

```
; gs: 0xffff8884a0200000 <__per_cpu_offset[0]>
; rip: 0xffffffff8112223a2bf
; rbx: 0xffff8884a02327c03cf=> <current>
mov  %gs:0x7ef10586(%rip), %rbx
```

```
; rip: 0xffffffff812bf1222f4
; esi: 0xffffffff8467f4e2798<suid_dumpable>
mov  0x33c04a4(%rip), %esi
```

```
call 0xffffffff816104732d0<set_dumpable>
call 0xffffffff817dd640120<key_fsuid_changed>
call 0xffffffff817dd640180<key_fsgid_changed>
call 0xffffffff812c31263d0<inc_rlimit_ucounts>
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
<Instructions for updating new credentials>
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
call 0xffffffff812c3126460<dec_rlimit_ucounts>
```

`call` **`0xffffffff81c45aa8fb0`** `<` **`proc_id_connector`** `> call` **`0xffffffff813441a7d90`** `<` **`call_rcu`** `> ret` #BHUSA

#BHUSA @BlackHatEvents

## Slide 61

0xffffffff812bc9a0
<__x64_sys_bpf>(arg1):
call  0xffffffff812bd5e0
...
- 0x9a3000
0xffffffff812bd 0xffffffff81c605e0 5e0
<xhci_address_device>:
call  0xffffffff812bec61a90
...
- 0x27f000

```
0xffffffff812be0xffffffff8153da90  a90
<configfs_open_file>:
call 0xffffffff812bf53e220
...
```

```
+0x19d000
```

```
0xffffffff812bf0xffffffff81122220 <commit_creds>:220
```

```
endbr64
```

```
; gs: 0xffff8884a0200000 <__per_cpu_offset[0]>
; rip: 0xffffffff8112223a2bf
; rbx: 0xffff8884a02327c03cf=> <current>
mov  %gs:0x7ef10586(%rip), %rbx
```

```
; rip: 0xffffffff812bf1222f4
; esi: 0xffffffff8467f4e2798<suid_dumpable>
mov  0x33c04a4(%rip), %esi
```

`call` **`0xffffffff816104732d0`** `<` **`set_dumpable`** `> call` **`0xffffffff817dd640120`** `<` **`key_fsuid_changed`** `> call` **`0xffffffff817dd640180`** `<` **`key_fsgid_changed`** `> call` **`0xffffffff812c31263d0`** `<` **`inc_rlimit_ucounts`** `> ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;` **`<Instructions for updating new credentials>`** `;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; call` **`0xffffffff812c3126460`** `<` **`dec_rlimit_ucounts`** `> call` **`0xffffffff81c45aa8fb0`** `<` **`proc_id_connector`** `> call` **`0xffffffff813441a7d90`** `<` **`call_rcu`** `> ret` #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 62

```
0xffffffff812bf0xffffffff81122220 <commit_creds>:220
```

```
endbr64
```

`0xffffffff812bc9a0 ; gs: 0xffff8884a0200000 <__per_cpu_offset[0]>` ~~`<__x64_sys_bpf>(arg1): ; rip:`~~ **~~`0xffffffff8112223a2bf`~~** **`+ 0x19d000`** `call` **`0xffffffff812bd5e0`** `;` **`rbx`** `:` **`0xffff8884a02327c03cf`** `=> <` **`current`** `> ... mov  %gs:0x7ef10586(%` **`rip`** `), %rbx ; rip:` **`0xffffffff812bf1222f4 - 0x9a3000`** `;` **`esi`** `:` **`0xffffffff8467f4e2798`** `<` **`suid_dumpable`** `> mov  0x33c04a4(%` **`rip`** `), %esi` **`0xffffffff812bd`** `0xffffffff81c605e0` **`5e0`** `<xhci_address_device>: call` **`0xffffffff816104732d0`** `<` **`set_dumpable`** `> call` **`0xffffffff812bec61a90`** `call` **`0xffffffff817dd640120`** `<` **`key_fsuid_changed`** `> ... call` **`0xffffffff817dd640180`** `<` **`key_fsgid_changed`** `> call` **`0xffffffff812c31263d0`** `<` **`inc_rlimit_ucounts`** `>` **Let’s REPLACE unessential functions** `;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;` **`- 0x27f000 <Instructions for updating new credentials> 0xffffffff812be`** `0xffffffff8153da90` **`a90`** `;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;` **with NOP gadgets** `call` **`0xffffffff812c3126460`** `<` **`dec_rlimit_ucounts`** `> <configfs_open_file>: call` **`0xffffffff812bf53e220`** `... call` **`0xffffffff81c45aa8fb0`** `<` **`proc_id_connector`** `> call` **`0xffffffff813441a7d90`** `<` **`call_rcu`** `> ret` #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 63

###### **`0xffffffff812bf`** `0xffffffff81122220 <commit_creds>:` **`220`**

```
endbr64
```

```
; gs: 0xffff8884a0200000 <__per_cpu_offset[0]>
; rip: 0xffffffff8112223a2bf
; rbx: 0xffff8884a02327c03cf=> <current>
mov  %gs:0x7ef10586(%rip), %rbx
```

```
; rip: 0xffffffff812bf1222f4
; esi: 0xffffffff8467f4e2798<suid_dumpable>
mov  0x33c04a4(%rip), %esi
```

```
call0xffffffff816104732d0<set_dumpable>
call 0xffffffff817dd640120<key_fsuid_changed>
call 0xffffffff817dd640180<key_fsgid_changed>
```

**`0xffffffff8161032a2d0`**  **`NOP gadget`** ~~`<bpf_lsm_inode_need_killpriv>:`~~ `xor %eax, %eax ret`

```
call 0xffffffff812c31263d0<inc_rlimit_ucounts>
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
<Instructions for updating new credentials>
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
call 0xffffffff812c3126460<dec_rlimit_ucounts>
```

**Replacing it with a NOP gadget**

```
call 0xffffffff81c45aa8fb0<proc_id_connector>
call 0xffffffff813441a7d90<call_rcu>
ret
```

#BHUSA @BlackHatEvents

## Slide 64

```
0xffffffff812bf0xffffffff81122220 <commit_creds>:220
```

```
endbr64
```

`; gs: 0xffff8884a0200000 <__per_cpu_offset[0]>` ~~`; rip:`~~ **~~`0xffffffff8112223a2bf`~~** `;` **`rbx`** `:` **`0xffff8884a02327c03cf`** `=> <` **`current`** `> mov  %gs:0x7ef10586(%` **`rip`** `), %rbx ; rip:` **`0xffffffff812bf1222f4`** `;` **`esi`** `:` **`0xffffffff8467f4e2798`** `<` **`suid_dumpable`** `> mov  0x33c04a4(%` **`rip`** `), %esi` **Identical page!** `call` **`0xffffffff816104732d0`** `<` **`set_dumpable`** `> call` **`0xffffffff817dd640120`** `<` **`key_fsuid_changed`** `> call` **`0xffffffff817dd640180`** `<` **`key_fsgid_changed`** `> call` **`0xffffffff812c31263d0`** `<` **`inc_rlimit_ucounts`** `> ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;` **`<Instructions for updating new credentials>`** `;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; call` **`0xffffffff812c3126460`** `<` **`dec_rlimit_ucounts`** `> call` **`0xffffffff81c45aa8fb0`** `<` **`proc_id_connector`** `> call` **`0xffffffff813441a7d90`** `<` **`call_rcu`** `> ret`

```
0xffffffff8880003ff000
<malicious_cred>:
uid, gid, euid, egid = 0
thread_keyring= NULL
```

**Remapping them and setting cred.thread_keyring to NULL**

#BHUSA @BlackHatEvents

## Slide 65

```
0xffffffff812bf0xffffffff81122220 <commit_creds>:220
endbr64
```

```
; gs: 0xffff8884a0200000 <__per_cpu_offset[0]>
; rip: 0xffffffff8112223a2bf
; rbx: 0xffff8884a02327c03cf=> <current>
mov  %gs:0x7ef10586(%rip), %rbx
```

```
; rip: 0xffffffff812bf1222f4
; esi: 0xffffffff8467f4e2798<suid_dumpable>
mov  0x33c04a4(%rip), %esi
```

```
call 0xffffffff816104732d0<set_dumpable>
call 0xffffffff817dd640120<key_fsuid_changed>
call 0xffffffff817dd640180<key_fsgid_changed>
```

```
call0xffffffff812c31263d0<inc_rlimit_ucounts>
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
<Instructions for updating new credentials>
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
call0xffffffff812c3126460<dec_rlimit_ucounts>
```

###### **Inline functions!**

**Remapping them because of no external function calls**

`call` **`0xffffffff81c45aa8fb0`** `<` **`proc_id_connector`** `>` **`344`** `call` **`0xffffffff81` Identical page!** **`1a7d90`** `<` **`call_rcu`** `> ret`

#BHUSA @BlackHatEvents

## Slide 66

###### **`0xffffffff812bf`** `0xffffffff81122220 <commit_creds>:` **`220`**

```
endbr64
```

>
>

- `; gs: 0xffff8884a0200000 <__per_cpu_offset[0]>` ~~`; rip:`~~ **~~`0xffffffff8112223a2bf`~~** `;` **`rbx`** `:` **`0xffff8884a02327c03cf`** `=> <` **`current`** `> mov  %gs:0x7ef10586(%` **`rip`** `), %rbx`

```
; rip: 0xffffffff812bf1222f4
; esi: 0xffffffff8467f4e2798<suid_dumpable>
mov  0x33c04a4(%rip), %esi
```

```
call 0xffffffff816104732d0<set_dumpable>
call 0xffffffff817dd640120<key_fsuid_changed>
call 0xffffffff817dd640180<key_fsgid_changed>
```

```
call 0xffffffff812c31263d0<inc_rlimit_ucounts>
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
```

**`<Instructions for updating new credentials>`** `;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;` **External function calls in them!** `call` **`0xffffffff812c3126460`** `<` **`dec_rlimit_ucounts`** `> call` **`0xffffffff81c45aa8fb0`** `<` **`proc_id_connecto`** **`r`** `>` `call` **`0xffffffff813441a7d90`** `<` **`call_rc`** **`u`** `>` `ret`

**`0xffffffff81c45329fb0`**  **`NOP gadget`** `<bpf_lsm_inode_mkdir>:`

```
xor %eax, %eax
ret
```

**`0xffffffff81344033d90`**  **`NOP gadget`** `<xen_apic_icr_read>: xor %eax, %eax ret`

**Replacing them with NOP gadgets**

#BHUSA @BlackHatEvents

## Slide 67

**`0xffffffff812bf`** `0xffffffff81122220 <commit_creds>:` **`220 0xffffffff81c45329fb0`**  **`NOP gadget`** `endbr64 <bpf_lsm_inode_mkdir>: ; gs: 0xffff8884a0200000 <__per_cpu_offset[0]>` <u>`xor %eax, %eax`</u> ~~`; rip:`~~ **~~`0xffffffff8112223a2bf`~~** `ret ;` **`rbx`** `:` **`0xffff8884a02327c03cf`** `=> <` **`current`** **Remapping Table** `> mov  %gs:0x7ef10586(%` **`rip`** `), %rbx ; rip:` **`0xffffffff812bf1222f4 0xffffffff81344033d90`**  **`NOP gadget`** `;` **`esi`** `:` **`0xffffffff8467f4e2798`** `<` **`suid_dumpable`** `> <xen_apic_icr_read>: xor %eax, %eax mov  0x33c04a4(%` **`rip`** `), %esi ret call` **`0xffffffff816104732d0`** `<` **`set_dumpable`** `> call` **`0xffffffff817dd640120`** `<` **`key_fsuid_changed`** `> call` **`0xffffffff817dd640180`** `<` **`key_fsgid_changed`** `> call` **`0xffffffff812c31263d0`** `<` **`inc_rlimit_ucounts`** `> ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;` **`<Instructions for updating new credentials>` Replacing them with** `;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;` **External function calls in them!** `call` **`0xffffffff812c3126460`** `<` **`dec_rlimit_ucounts`** `>` **NOP gadgets** `call` **`0xffffffff81c45aa8fb0`** `<` **`proc_id_connecto`** **`r`** `>` `call` **`0xffffffff813441a7d90`** `<` **`call_rc`** **`u`** `>` `ret` #BHUSA @BlackHatEvents

## Slide 68

# **~~DEMO~~**

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fo - 2-2-2222 2-2 - eee ---- +
| |
| Breaking the
| Kernel CFI with | /---
| Page-Oriented | ;
| Programming | |
eee eee eee ee eee eee ! a Oe |
fate aoe Ee SG eS EES Sai ae!
[| oo000000000000000 .0. oooo /,
/ ==000000000000000==.0. o00= //
Lost Control PoC Made by Seunghun Han
```

## Slide 69

###### BONUS: INDIRECT BRANCH

```
arg1: pointer of modified_cred
arg2: 0xff…ff81122220 <commit_creds>
```

```
0xffffffff812bc9a0
<__x64_sys_bpf>(arg1, arg2):
mov arg1, %rdi
mov arg2, %rsi
call 0xffffffff812bd5e0
...
```

```
0xffffffff?????5e0
jmp %rsi
...
```

**`0xffffffff81122220 <commit_creds>`** `:` **`endbr64`**  **`Is it needed?`**

```
; gs: 0xffff8884a0200000 <__per_cpu_offset[0]>
; rip: 0xffffffff8112223a
; rbx: 0xffff8884a02327c0=> <current>
mov  %gs:0x7ef10586(%rip), %rbx
```

```
; rip: 0xffffffff811222f4
; esi: 0xffffffff844e2798<suid_dumpable>
mov  0x33c04a4(%rip), %esi
```

```
call 0xffffffff814732d0<set_dumpable>
call 0xffffffff81640120<key_fsuid_changed>
call 0xffffffff81640180<key_fsgid_changed>
```

`call` **`0xffffffff811263d0`** `<` **`inc_rlimit_ucounts`** `> ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;` **`<Instructions for updating new credentials>`** `;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; call` **`0xffffffff81126460`** `<` **`dec_rlimit_ucounts`** `> call` **`0xffffffff81aa8fb0`** `<` **`proc_id_connector`** `> call` **`0xffffffff811a7d90`** `<` **`call_rcu`** `> ret` #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 70

###### **Contents**

**- Control-Flow Integrity (CFI) - Hardware-Assisted Kernel CFI in Use - Page-Oriented Programming - Demo - Conclusion and Black Hat Sound Bytes**

#BHUSA @BlackHatEvents

## Slide 71

###### **Mitigation of POP**

- **Escorting page table updates with hypervisors**

   - Many researchers have introduced mechanisms that intercept and check updates

   - However, they have performance overhead

- **Utilizing the Hypervisor-Managed Linear Address Translation (HLAT) feature**

   - 12th Gen Intel CPUs support it to prevent page-remapping attacks

   - HLAT tables translate logical addresses of the kernel to physical addresses instead of the guest OS’s page tables

   - However, hypercalls are needed to update the tables (new opportunity?)

#BHUSA @BlackHatEvents

## Slide 72

**Mitigation of POP** <u>LEGACY SYSTEMS STILL NEED</u> **- Escorting page table updates with hypervisors 12th Gen Intel** - Many researchers have introduced mechanisms that intercept and **CPUs and over** check updates - However, they have performance overhead **- Utilizing the Hypervisor-Managed Linear Address Translation Legacies, and other CPU (HLAT) feature vendors**

- 12th Gen Intel CPUs support it to prevent page-remapping attacks - HLAT tables translate logical addresses of the kernel to physical addresses instead of the guest OS’s page tables PRACTICAL SOLUTIONS! - However, hypercalls are needed to update the tables (new opportunity?)

#BHUSA @BlackHatEvents

## Slide 73

###### **Conclusion and Black Hat Sound Bytes**

**- State-of-the-art kernel CFIs are effective but have weaknesses** - They focus on indirect branches and the page-level non-writable code mechanism

- **POP is a new code reuse attack that can subvert kernel CFIs** - It exploits weaknesses of them to create new control flows

   - It can break kernel CFIs with page-level gadgets like ROP and JOP

- **Mitigation of POP is an open problem**

   - Intel HLAT needs interactions between the OS and the hypervisor

      - The changes can give us **new opportunities** !

   - Legacy systems are still vulnerable, so practical solutions are needed

#BHUSA @BlackHatEvents

## Slide 74

###### **QnA**

YOUR FUTURE WORK IS EVERYWH…
ME ???
PLEASE! I JUST FINISHED MY TALK!

**Project: https://github.com/kkamagui/page-oriented-programming Contact: hanseunghun@nsr.re.kr, @kkamagui1** #BHUSA

#BHUSA @BlackHatEvents

## Slide 75

###### **Reference**

- Martín Abadi, Mihai Budiu, Ú lfar Erlingsson, and Jay Ligatti. Control-flow integrity principles, implementations, and applications. ACM CCS. 2005.

- - Vishwath Mohan, Per Larsen, Stefan Brunthaler, Kevin W Hamlen, and Michael Franz. Opaque control-flow integrity. NDSS. 2015.

- Ben Niu and Gang Tan. Modular control-flow integrity. PLDI. 2014.

- Caroline Tice, Tom Roeder, Peter Collingbourne, Stephen Checkoway, Ú lfar Erlingsson, Luis Lozano, and Geoff Pike. Enforcing forward-edge control-flow integrity in GCC & LLVM. USENIX Security. 2014.

- Nick Christoulakis, George Christou, Elias Athanasopoulos, and Sotiris Ioannidis. HCFI: Hardware-enforced control-flow integrity. ACM CODASPY. 2016.

- Ben Niu and Gang Tan. Per-input control-flow integrity. ACM CCS. 2015.

- Victor Van der Veen, Dennis Andriesse, Enes Göktaş , Ben Gras, Lionel Sambuc, Asia Slowinska, Herbert Bos, and Cristiano Giuffrida. Practical context-sensitive CFI. ACM CCS. 2015.

- Ren Ding, Chenxiong Qian, Chengyu Song, William Harris, Taesoo Kim, and Wenke Lee. Efficient protection of path-sensitive control security. USENIX Security. 2017.

- Hong Hu, Chenxiong Qian, Carter Yagemann, Simon Pak Ho Chung, William R Harris, Taesoo Kim, and Wenke Lee. Enforcing unique code target property for control-flow integrity. ACM CCS. 2018.

- - Mustakimur Khandaker, Abu Naser, Wenqing Liu, Zhi Wang, Yajin Zhou, and Yueqiang Cheng. Adaptive call-site sensitive control flow integrity. EuroS&P. 2019.

- Mustakimur Khandaker, Wenqing Liu, Abu Naser, Zhi Wang, and Jie Yang. Origin-sensitive control flow integrity. USENIX Security. 2019.

- Marius Muench, Fabio Pagani, Yan Shoshitaishvili, Christopher Kruegel, Giovanni Vigna, and Davide Balzarotti. Taming transactions: Towards hardware-assisted control flow integrity using transactional memory. RAID. 2016. #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 76

###### **Reference**

- Sungbae Yoo, Jinbum Park, Seolheui Kim, Yeji Kim, and Taesoo Kim. In-kernel control-flow integrity on commodity OSes using ARM pointer authentication. USENIX Security. 2022.

- - Intel Control-flow Enforcement Technology, https://edc.intel.com/content/www/us/en/design/ipla/software-developmentplatforms/client/platforms/alder-lake-desktop/12th-generation-intel-core-processors-datasheet-volume-1-of-2/intel-control-flowenforcement-technology/

- GCC, The GNU Compiler Collection. https://gcc.gnu.org/

- LLVM. The LLVM compiler infrastructure. https://llvm.org/

- Microsoft. Enable Control Flow Guard. https://msdn.microsoft.com/en-us/library/dn919635.aspx. 2023.

- Joao Moreira. "Hardware-Assisted Fine-Grained Control-Flow Integrity: Adding Lasers to Intel's CET/IBT." Linux Security Summit. 2021.

- Seunghun Han, Junghwan Kang, Wook Shin, H Kim, and Eungki Park. Myth and truth about hypervisor-based kernel protector: The reason why you need shadow-box. Blackhat-ASIA. 2017.

- - Images from: https://pixabay.com/, https://wallpapersafari.com, https://www.asus.com, https://www.twitter.com, https://www.debian.org, https://www.kernel.org, and Toy story 2 of Pixar

- ASCII arts from: https://www.asciiart.eu/computers/computers and https://ascii.co.uk/art/fire

#BHUSA @BlackHatEvents
