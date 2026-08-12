---
title: "Crashing the Party Pwning Control-Flow Integrity with Segmentation Fault-Oriented Programming"
speakers: ["Marcos Bajo", "Ritvik Goyal"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Marcos Bajo, Ritvik Goyal - Crashing the Party Pwning Control-Flow Integrity with Segmentation Fault-Oriented Programming - Crashingthe.pdf"
pages: 140
sha256: "ec375e413944ef9a14c44bd246fb5a266201c8a683cf114552fd5480d991ff51"
text_chars: 30723
ocr_pages: 61
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:25:34Z"
---
# Crashing the Party Pwning Control-Flow Integrity with Segmentation Fault-Oriented Programming

**Speakers:** Marcos Bajo, Ritvik Goyal  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Marcos Bajo, Ritvik Goyal - Crashing the Party Pwning Control-Flow Integrity with Segmentation Fault-Oriented Programming - Crashingthe.pdf` (140 pages)


## Slide 1

#### **Crashing the Party: Pwning Control-Flow Integrity with** **_SFOP Segmentation Fault-Oriented Programming_**

**Marcos Bajo (** **_h3xduck_ ) | Ritvik Goyal (** **_RoYalGamr_ )** **_CISPA Helmholtz Center for Information Security_**

## Slide 2

###### **The Old Ages**

###### **1972**

**2000 2010**

**2020**

Buffer overflows 1<sup>st</sup> mentioned

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
The Old Ages
1972 ESD-TR-73-51, ‘Vol. 11
COMPUTER SECURITY TECHNOLOGY PLANNING STUDY
James P, Anderson
ao October 1972
Buffer
overflows 1°
mentioned
DEPUTY FOR COMMAND AND MANAGEMENT SYSTEMS
HQ ELECTRONIC SYSTEMS DIVISION (AFSC)
L. G. Hanscom Field, Bedford, Massachusetts 01730
```

## Slide 3

###### **1972**

Buffer overflows 1<sup>st</sup> mentioned

### **The Old Ages 20002000 MEMORY 2010 2020 CORRUPTION CODE EXECUTION**

## Slide 4

###### **The Old Ages**

###### **1972**

**2000 2010**

**2020**

ret2libc

Buffer overflows 1<sup>st</sup> mentioned

## Slide 5

###### **The Old Ages**

**1972**

**2000 2010**

**2020**

Stack canaries ASLR

ret2libc DEP/NX Buffer overflows 1<sup>st</sup> mentioned

## Slide 6

###### **The Old Ages**

**1972 2000 2010 2020** Stack canaries ASLR JOP ret2libc DEP/NX ROP DOP Buffer overflows 1<sup>st</sup> mentioned

## Slide 7

**Code Reuse**

## Slide 8

**Vulnerability Exploitation: Code Reuse**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Vulnerability Exploitation: Code Reuse
f:
call g()
call h()
ve execve()
ret
call a @)
cali’) -—— ~
ret ret
all i() “call i(
call) -» 7
ret ret
```

## Slide 9

###### **Code-Reuse attacks**

- Code-Reuse uses small code pieces: gadgets

- **ROP** gadgets:

   - End with a _ret_ instruction

- **JOP** gadgets:

   - End with a jmp instruction

pop

ret

mov

mov  rdi

jmp  rdi

, [

]

, [rsp+ 0

8]

## Slide 10

###### **Control-Flow Integrity**

- “Classic” defenses

   - ASLR, DEP, canaries…

   - Make exploits harder

- Control Flow Integrity

   - Construct Control Flow Graph (CFG)

   - Instrumentation to enforce CFG

   - Code-reuse techniques stopped

      - Sorry, yes, ROP is dead

## Slide 11

# **SFOP Segmentation Fault-Oriented Programming**

## Slide 12

**SFOP Segmentation Fault-Oriented Programming** • _…unlike ROP, JOP, SROP_ Bypasses Intel CET

## Slide 13

# **SFOP**

###### **Segmentation Fault-Oriented Programming**

- Bypasses Intel CET

_…unlike ROP, JOP, SROP_

• Does not require C++ programming paradigms

… _unlike COOP, CFOP, CHOP_

## Slide 14

# **SFOP**

###### **Segmentation Fault-Oriented Programming**

- Bypasses Intel CET

_…unlike ROP, JOP, SROP_

- Does not require C++ programming paradigms

   - … _unlike COOP, CFOP, CHOP_

- Does not require specific program gadgets

_…unlike FOP_

## Slide 15

**SFOP Segmentation Fault-Oriented Programming** Works **by default** in any **x86_64 Linux** program with **Intel CET** enabled

_Unlike ROP, JOP, SROP, COOP, CFOP, FOP, CHOP…_

## Slide 16

###### **What We Will Learn**

###### 1. Control-Flow Integrity

_The defenses bypassed by SFOP._

## Slide 17

###### **What We Will Learn**

###### 1. Control-Flow Integrity _The defenses bypassed by SFOP._

2. Linux Signals

_The mechanism behind SFOP._

## Slide 18

###### **What We Will Learn**

###### 1. Control-Flow Integrity _The defenses bypassed by SFOP._

###### 2. Linux Signals

_The mechanism behind SFOP._

3. Segmentation Fault-Oriented Programming _Using bSFOP and fSFOP to exploit programs protected by CET._

## Slide 19

###### **What We Will Learn**

###### 1. Control-Flow Integrity _The defenses bypassed by SFOP._

###### 2. Linux Signals

_The mechanism behind SFOP._

3. Segmentation Fault-Oriented Programming _Using bSFOP and fSFOP to exploit programs protected by CET._

4. Patching SFOP

_Patching the Linux Kernel to stop SFOP._

## Slide 20

##### **Userspace CFI Defenses**

## Slide 21

###### **Intel CET**

- SFOP bypasses Intel CET

   - Most widespread CFI scheme in modern x86

   - • Linux and Windows

   - Intel 11th generation (Tiger Lake) processors Onwards

- CET composed of two techniques:

- • Shadow Stack (SHSTK)

- • Indirect Branch Tracking (IBT)

## Slide 22

void

f()

{

g();

ret;

}

void

g()

{

h();

ret;

}

void

h()

{

i();

ret;

}

void

i()

{

ret;

}

**Intel CET (Shadow Stack)**

## Slide 23

**Intel CET (Shadow Stack)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
g()
frame
f() return
address
0)
frame
Intel CET (Shadow Stack)
ssp =>
f() return
address
```

## Slide 24

**Intel CET (Shadow Stack)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Intel CET (Shadow Stack)
h()
frame
g() return
address
g()
frame
f() return ss
Pe P -»> g() return
address
0) f() return
frame address
```

## Slide 25

**Intel CET (Shadow Stack)**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
i()
frame
h() return
address
h()
frame
g() return
address
g()
frame
f() return
address
f()
frame
Intel CET (Shadow Stack)
h() return
address
g() return
address
f() return
address
```

## Slide 26

**Intel CET (Shadow Stack)**

void

()

{

ret;
}

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
i()
frame
Intel CET (Shadow Stack)
h() return
address
h()
frame
g() return
address
g()
frame
f() return
address
f()
frame
ssp
h() return
address
g() return
address
f() return
address
```

## Slide 27

**Intel CET (Shadow Stack)**

void

h()

{

();

ret;

}

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
i()
frame
Intel CET (Shadow Stack)
void h()
h() return
address
h()
frame
g() return
address
g()
frame
f() return
address
f()
frame
ssp
h() return
address
g() return
address
f() return
address
```

## Slide 28

**Intel CET (Shadow Stack)**

void

g()

{

h();

ret;

}

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
i()
frame
Intel CET (Shadow Stack)
void g()
h() return
address
hQ);
h()
frame
ret;
g() return
address
g()
frame
f() return
address
f()
frame
| —@
h() return
address
g() return
address
f() return
address
```

## Slide 29

**Intel CET (Shadow Stack)**

void

()

{

ret;
}

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
i()
frame
void iC)
{
system()
h()
frame
ret;
Po
g() return
address
g()
frame
f() return
address
f()
frame
Intel CET (Shadow Stack)
ssp
h() return
address
g() return
address
f() return
address
```

## Slide 30

###### **Intel CET (Shadow Stack)**

- Processes allocate a dedicated memory region before calling _main_

   - Function __dl_cet_setup_features_

   - Instructs the kernel to allocate a shadow stack

arch_prctl do_arch_prctl_64 shstk_prctl shstk_setup alloc_shstk

- There is one shadow stack per thread

- This shadow stack region is mapped, but the process cannot read or write into it

   - Kernel VMA: VM_SHADOW_STACK

   - PTE: ~_PAGE_RW & _PAGE_SAVED_DIRTY

## Slide 31

###### **Intel CET (Shadow Stack)**

- For an application to be SHSTK enabled:

   - CPU Support: Intel 11<sup>th</sup> gen (Tiger Lake)

   - Kernel Support: Linux 6.6, Windows 10 19H1

   - Compiler support:

      - GCC 8.1

      - LLVM 11

      - MSVC 16.7

   - Application must be compiled with _–fcf-protection=full_ (Linux) or _/CETCOMPAT_ (Windows)

<u>https://h3xduck.github.io/cfi/2025/06/26/enabling-intel-cet.html</u>

## Slide 32

###### **Intel CET (Shadow Stack)**

- Does CET Shadow Stack protect programs against all kind of attacks?

## Slide 33

main:

push

mov

rsp

mov rsi, [rdi+0x8]

mov

, [

]

call

rax
]

leave

ret

**Intel CET (IBT)**

## Slide 34

**Intel CET (IBT)**

main:

push

rbx ]

mov

,

mov

, [

call

rax
]

leave

ret

f 1

:

add  rdi

mov

lea

add  rdi

mov

ret

0
,

x 8

0
,

10

, [

]

rax

rdx

## Slide 35

**Intel CET (IBT)**

f1:

main:

endbr64

rbx ]

push

add  rdi

, 0x8

mov

,

mov

, 0x10

lea

, [

]

mov

, [

add  rdi

rax

call

rax
]

mov

rdx

leave

ret

ret

## Slide 36

###### **Intel CET (IBT)**

- Limited availability

   - Windows: Not implemented

   - Linux: enforcement only in the kernel since 5.18

- Coarse-grained CFI

   - We still can use gadgets starting with endbr64

## Slide 37

###### **Intel CET (IBT)**

• Coarse-grained CFI still prevents classic code-reuse

- ROP

pop

ret

- JOP

mov

mov  rdi

jmp  rdi

, [

, [

]

+0x8]

## Slide 38

**Linux Signals**

## Slide 39

###### **Linux Signals**

• Signals are asynchronous inter-process notifications

SIGKILL

Killing a

process

SIGSEGV

Inaccessible

memory location

## Slide 40

###### **Linux Signals**

###### • Signals can be handled registering a signal handler

(signum=SIGSEGV,

=h)

(signum=SIGSEGV, act={

=h,…})

## Slide 41

**Linux Signals**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Linux Signals
Userspace Kernel
mov r8, 0x0
rsp
u
uv
```

## Slide 42

**Linux Signals**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
rsp
rbp
\ y
\ \
Linux Signals ~
Userspace ! Kernel
Prepare
mov r8, 0x0) | SIGSEGV [ |sigframe
mov r9, [r8]
```

## Slide 43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
J
restorer rsp handler rsp
0x0 >
64B Align
xstate
16B Align
0x80
t bytes redzone
~0xD00
old rsp
```

## Slide 44

**Linux Signals**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
rs
rb
\ ‘*
\ y
\ \
\ ¥y
Linux Signals Ie
Userspace | Kernel
Prepare
mov r8, 0x0 || SIGSEGV |sigframe
mov 19, [r8]
signal
handler
```

## Slide 45

**Linux Signals**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
rsp
rbp
Linux Signals
Userspace
Kernel
mov r8, 0x0
mov 19, [r8]
signal
handler
(SSseSy sigframe
WZ
restorer
```

## Slide 46

**Linux Signals**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
rsp
rbp
Linux Signals
Userspace
mov r8, 0x0
mov r9, [r8]
Kernel
Prepare
eoses sigframe
signal
handler
\Z
sigretu
restorer
mi
Restore
state
```

## Slide 47

**Linux Signals**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Linux Signals
Userspace Kernel
Prepare
sigframe
mov r8, 0x0
mov 19, [r8]
signal
handler
XZ
restorer
```

## Slide 48

###### **Shadow Stack with Signals**

###### • The Shadow Stack Pointer (SSP) marks the top of the Shadow Stack

## Slide 49

###### **Shadow Stack with Signals**

• The Shadow Stack Pointer (SSP) marks the top of the Shadow Stack

- The SSP is saved onto the Shadow Stack when a signal is triggered. The MSB is set to 1 to distinguish it

## Slide 50

###### **Shadow Stack with Signals**

- The SSP is checked during _sigreturn_

- • If MSB=1, the SSP is restored to the saved value

- • If MSB≠1 a SIGSEGV is triggered

## Slide 51

###### **SROP is Dead**

- In the SROP attack, the attacker:

- • Forges a fake sigframe in memory

- • Calls sigreturn directly

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SROP is Dead
In the SROP attack, the attacker:
Forges a In memory
Calls directly
Userspace : Kernel
Ts restorer ; >
normal
execution
CORRUPTED
SIGFRAME
fe) return address
6} return address
6} return address
~
```

## Slide 52

###### **SROP is Dead**

- In modern Linux, the kernel checks MSB=1

- • No return address in the shadow stack has MSB=1 naturally

- • Check always failed → SIGSEGV

## Slide 53

###### **Is It The End?**

ROP → Prevented by Shadow Stacks

JOP → Prevented by IBT

SROP → Prevented by MSB check on Shadow Stack

## Slide 54

**SFOP**

## Slide 55

**Missing IBT Checks**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Missing IBT Checks
Userspace Kernel
Prepare
mov r8, 0x0 | SIGSEGV |sigframe
mov 19, [r8]
signal
handler
Restore
state
y
restorer
```

## Slide 56

**Missing IBT Checks**

NO IBT CHECKS
SIGNAL DELIVERY

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Missing IBT Checks
Userspace Kernel
aie “GH pare
mov NO Ox sigframe
nS IGN
signal
handler
Restore
y
state
restorer
```

## Slide 57

**Missing IBT Checks**

NO IBT CHECKS
SIGNAL DELIVERY
NO IBT CHECKS
SIGNAL RETURN

## Slide 58

###### **Is This Enough?**

• Unprotected branches are not enough to create practical code-reuse attack…

## Slide 59

###### **Is This Enough?**

- Unprotected branches are not enough to create practical code-reuse attack…

   - How to trigger an arbitrary signal handler?

## Slide 60

###### **Is This Enough?**

- Unprotected branches are not enough to create practical code-reuse attack…

   - How to trigger an arbitrary signal handler?

   - • How to control the register arguments inside the handler?

## Slide 61

###### **Is This Enough?**

• Unprotected branches are not enough to create practical code-reuse attack…

- How to trigger an arbitrary signal handler?

- How to control the register arguments inside the handler?

- How to execute multiple arbitrary function calls?

## Slide 62

**Late Kernel Safety Checks**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Late Kernel Safety Checks |
FSR restorer
Sigframe
last return address
-
Userspace ! Kernel
Prepare
mov r8, 0x0 sigframe
mov 19, [r8]
signal !
XZ as V state
restorer } Restore
SSP
```

## Slide 63

###### **Late Kernel Safety Checks**

• The kernel restores the sigframe _before_ checking SSP

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Late Kernel Safety Checks |
¢ The kernel restores the sigframe checking SSP
Userspace : Kernel
Ts restorer ; >
normal
execution ! —————
CORRUPTED ! !
SIGFRAME ! —_
fe) return address
6} return address
®) return address rb ae
```

## Slide 64

###### **Late Kernel Safety Checks**

• At this point we control the pt_regs in the Kernel

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Late Kernel Safety Checks |
¢ At this point we control the pt_regs in the Kernel
Userspace : Kernel
Restore
normal Gs state
execution X 7
Lsor |
return address
return address
return address
```

## Slide 65

###### **Late Kernel Safety Checks**

• Oh no !! Kernel throws catchable Sigsegv

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Late Kernel Safety Checks |
¢ Oh no!! Kernel throws catchable Sigsegv
Userspace : Kernel
| 3™ Restore
normal Y State
execution \ 7
Restore
: SSP
return address ae
return address
```

## Slide 66

###### **Late Kernel Safety Checks**

• What if we already registered a signal handler ?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Late Kernel Safety Checks |
¢ What if we already registered a signal handler ?
SA Userspace : Kernel
restorer SNirestore!
Restore
normal Y state
execution N 7
restorer CORRUPTED Restore
SIGFRAME Ee | SSP
return address Prepare
sigframe
return address x, |
```

## Slide 67

###### **Late Kernel Safety Checks**

• We got our corrupted sigframe back

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Late Kernel Safety Checks |
¢ We got our corrupted sigframe back
Userspace : Kernel
restorer Restore
Restore
normal Y state
execution N 7
restorer CORRUPTED Restore
SIGFRAME signal : SSP
handler VW
@) return address VW Prepare
@) return address rN !
```

## Slide 68

###### **Late Kernel Safety Checks**

• We send our corrupted sigframe back for sigreturn

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Late Kernel Safety Checks |
¢ Wesend our corrupted sigframe back for sigreturn
Userspace : Kernel
restorer SNiRestore|
Restore
normal Y state
execution N 7
restorer CORRUPTED estore
SIGFRAME signal : SSP
handler
return address \Z Prepare
restorer sigframe
return address SN =)
```

## Slide 69

###### **Late Kernel Safety Checks**

• And we bypass the sigreturn shadow stack check

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Late Kernel Safety Checks |
¢ And we bypass the sigreturn shadow stack check
Userspace : Kernel
| 3™ Restore
normal Y state
execution \ 7
Restore
signal | | SSP
handler
WZ : Prepare
Restore
| SSP
return address
return address
van.
```

## Slide 70

###### **User Kernel Data Collision**

• Kernel sets the registers before signal delivery :

- $RDI = signal_no

- $RSI = SIGINFO_location

- $RDX = ucontext_location

- $RSP = sigframe

- $RIP = signal_handler

- $RAX = 0  (can be ignored)

## Slide 71

###### **User Kernel Data Collision**

• Kernel sets the registers before signal delivery :

- $RDI = signal_no

- $RSI = SIGINFO_location

- $RDX = ucontext_location

- $RSP = sigframe

- $RIP = signal_handler

- $RAX = 0  (can be ignored)

- And doesn’t modify any other registers, which can be pass on from previous context to signal handler

## Slide 72

###### **User Kernel Data Collision**

• Kernel sets the registers before signal delivery :

- $RDI = signal_no

- $RSI = SIGINFO_location

- $RDX = ucontext_location

- $RSP = sigframe

- $RIP = signal_handler

- $RAX = 0  (can be ignored)

- And doesn’t modify any other registers, which can be pass on from previous context to signal handler

- What if we set sigaction function as a signal handler ?

## Slide 73

###### **User Kernel Data Collision**

- Data from the kernel is incorrectly used in userland

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
User Kernel Data Collision _
Data from the kernel is In userland
signal handler
<  rdi=signum >
<  rsi=siginfo >
<  rdx=ucontext >
```

## Slide 74

###### **User Kernel Data Collision**

- Data from the kernel is incorrectly used in userland

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
User Kernel Data Collision _
Data from the kernel is In userland
signal handler libc sigaction
cC  rdi=signumn > Cc rdi= signum___>
—————————
<C  rsi=siginfo > C rsi = sigaction ion act{} >
ee
<  rdx=ucontext > dx = sigaction yn oldac>
```

## Slide 75

###### **User Kernel Data Collision**

- Libc sigaction will interpret _rsi_ as act{}… but it is siginfo!

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
User Kernel Data Collision ©
¢ Libc sigaction will interpret {}... but
signal handler = libc sigaction
<— rdi = signum = signum >
<< rsi = siginfo = sigaction act{} _>
a rdx = ucontext = sigaction oldact _>
```

## Slide 76

###### **SIGINFO rsi bug**

## Slide 77

###### **SIGINFO rsi bug**

If we registered a Signal Handler with SA_SIGINFO Flag, then Kernel will fill the siginfo area and rsi will point to that location

## Slide 78

###### **SIGINFO rsi bug**

If we registered a Signal Handler with SA_SIGINFO Flag, then Kernel will fill the siginfo area and rsi will point to that location What if we don’t register with SA_SIGINFO Flag?

## Slide 79

###### **fSFOP: Early Kill**

• We want to register a signal _and_ trigger a SIGSEGV

pthread_once_slow

+

obstack_newchunk

Stack memory controlled + Forward pointer hijacked

Call sigaction(rdi, rsi, rdx) rdi = SIGSEGV (0xb) rsi = act{handler,…} rdx = early kill trigger

## Slide 80

###### **fSFOP: Early Kill**

• We trigger a SIGSEGV _inside_ sigaction() after the signal is already registered

sigaction(rdi, rsi, rdx) rdi = SIGSEGV rsi = act{handler,…} rdx = invalid memory

## Slide 81

###### **fSFOP: Sigframe Pivoting**

• Sigframe Pivoting allows controlling the sigframe from within a signal handler

###### **CLASSIC** Sigframe Pivoting **UNWINDING BASED** Sigframe Pivoting **DOUBLE PARTIAL** Sigframe Pivoting

## Slide 82

###### **fSFOP: Classic Sigframe Pivoting**

1. Register _sigaction_ as SIGSEGV handler, trigger Early Kill

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fSFOP: Classic Sigframe Pivoting
|. Register as handler, trigger
libc sigaction
_ SIGSEGV
sigaction |handler=| handler: sigaction 2a
Tap | —) leave rbp La
ret ss S
rbp value
> 4\,
__restore_rt .
y FAKE ‘
\SIGFRAME,, ,
ret orrupted
memory
```

## Slide 83

###### **fSFOP: Classic Sigframe Pivoting**

###### 2. Signal handler is triggered, sigframe is created

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fSFOP: Classic Sigframe Pivoting
2. Signal handler is triggered, sigframe is created
handler: sigaction
~
ret
¥.
sigreturn
ss
__restore_rt }
Sigframe
rbp value
__restore_rt
FAKE
SIGFRAME @
L
b 4
rake
S
.
.
Written
by the
kernel
Corrupted
memory
```

## Slide 84

###### **fSFOP: Classic Sigframe Pivoting**

###### 3. Stack pivoting gadget moves rsp to fake sigframe

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fSFOP: Classic Sigframe Pivoting
4. Stack pivoting gadget moves to
__restore_rt [}
(USE by
handler: sigaction Sigframe the kernel
| leave
ss J
|
¥ t rbp value ;
sigreturn
> 4
__restore_rt Jeenlnee
7 FAKE meme
\ SIGFRAME / |
```

## Slide 85

###### **fSFOP: Classic Sigframe Pivoting**

4. Sigreturn is called using the fake sigframe

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fSFOP: Classic Sigframe Pivoting
is called using the
__restore_rt j
| Written by
handler: sigaction Sigframe the kernel
leave
ret J
a
~~ rbp ~ rbp value
) r t ~ C ted
restore orrupte
haa FAKE F memory
\SIGFRAME, |
```

## Slide 86

###### **fSFOP: Classic Sigframe Pivoting**

###### 5. Arbitrary function call

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fSFOP: Classic Sigframe Pivoting
5. Arbitrary function call
__restore_rt \)
Written by
handler: sigaction Sigframe [MRA
leave
ret J ss
+ a
sigreturn rbp value
__restore_rt | Corrupted
[ ARBITRARY = RKE memory
“Ss TARGET
. \ SIGFRAME J
```

## Slide 87

###### **fSFOP: Infnite Segfault i Looping**

SIGSEGV triggers the next pivot, achieving infinite function calls

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
fSFOP: Infinite Segfault Looping
triggers the next pivot, achieving
= (om
ict stere byl
handler: sigaction Sigframe [TMAAMURIEE = Sigframe
si
=> L
ret rbp
¥. ~
A
sigreturn robp value
__restore_ | Corrupted 4 __restore_rt
ARBITRARY memory
| TARGET FAKE FAKE
SIGFRAM u SIGFRAME /
```

## Slide 88

###### **Some Hints that something is Fishy**

- During the signal handler execution, the Shadow Stack Pointer (SSP) is saved with MSB=1

   - Is this even good enough?

## Slide 89

###### **Some Hints that something is Fishy**

- During the signal handler execution, the Shadow Stack Pointer (SSP) is saved with MSB=1

   - Is this even good enough?

- It is a pity we cannot control which restorer is executed after a signal handler

   - Because we cannot. Right? Right?

## Slide 90

(signum=SIGSEGV,

handler

})

**Signal Restorer Hijacking**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Signal Restorer Hijacking _
sigaction(signum=SIGSEGV, ={
h,.})
```

## Slide 91

**Signal Restorer Hijacking**

sigaction

(signum=SIGSEGV, act={handler=h,

flags=f,

restorer

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Signal Restorer Hijacking
rsp
SA
restorer
Sigaction(signum=SIGSEGV, act={handler=h,
flags=f, Sigframe
=r})
```

## Slide 92

###### **Signal Restorer Hijacking**

• Calling sigaction is not enough…

- _libc_ always overwrites the restorer with __restore_rt

• __restore_rt calls _sigreturn_

## Slide 93

###### **Signal Restorer Hijacking**

- Calling sigaction is not enough…

   - _libc_ always overwrites the restorer with __restore_rt

- __restore_rt calls _sigreturn_

## Slide 94

###### **Signal Restorer Hijacking**

• Calling sigaction is not enough…

- _libc_ always overwrites the restorer with __restore_rt

   - __restore_rt calls _sigreturn_

- But we can jump _after_ the overwrite

## Slide 95

###### **Signal Restorer Hijacking**

• We can control the _restorer_ after the signal handler

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Signal Restorer Hijacking
¢ Wecan after the signal handler
Userspace Kernel
r
mR restorer
mov r8, 0x0 {siesecv sigframe
mov 19, [r8]
ssp
SN Sigframe signal i
restorer
handler __ J Restore
XZ sigretu mJ state
: ar
arbitrary Restore
Ry restorer ! SSP
last return address <l rb
```

## Slide 96

###### **Not Enough**

- Controlling the restorer is just one function call • The signal handler clobbers any useful register values

## Slide 97

###### **Not Enough**

- Controlling the restorer is just one function call

   - The signal handler clobbers any useful register values

- After the restorer returns, we do not control execution anymore

## Slide 98

###### **Not Enough**

- Controlling the restorer is just one function call

   - The signal handler clobbers any useful register values

- After the restorer returns, we do not control execution anymore

   - Signal handler with rdi, rsi, rdx controlled

## Slide 99

###### **Not Enough**

- Controlling the restorer is just one function call

   - The signal handler clobbers any useful register values

- After the restorer returns, we do not control execution anymore

   - Signal handler with rdi, rsi, rdx controlled

   - Restorer with no registers controlled

## Slide 100

###### **Not Enough**

- Controlling the restorer is just one function call

   - The signal handler clobbers any useful register values

- After the restorer returns, we do not control execution anymore

   - Signal handler with rdi, rsi, rdx controlled

   - Restorer with no registers controlled

   - The Shadow Stack triggers SIGSEGV after the restorer returns

## Slide 101

###### **Not Enough**

###### **USEFUL**

Signal handler with rdi, rsi, rdx controlled

Restorer without any registers controlled

Shadow Stack triggers SIGSEGV after the restorer returns

## Slide 102

###### **Not Enough**

**USEFUL** Signal handler with rdi, rsi, rdx controlled

**USELESS** Restorer without any registers controlled

Shadow Stack triggers SIGSEGV after the restorer returns

## Slide 103

###### **Not Enough**

**USEFUL** Signal handler with rdi, rsi, rdx controlled

**USELESS** Restorer without any registers controlled

**CRASH** Shadow Stack triggers SIGSEGV after the restorer returns

## Slide 104

###### **The Way Forward**

**USEFUL** Signal handler with rdi, rsi, rdx controlled

**USEFUL** Restorer without any registers controlled

**CRASH** Shadow Stack triggers SIGSEGV after the restorer returns

## Slide 105

###### **The Way Forward**

**USEFUL** Signal handler with rdi, rsi, rdx controlled

**USEFUL** Restorer without any registers controlled

**OK** Shadow Stack triggers SIGSEGV after the restorer returns

## Slide 106

###### **The Way Forward**

**USEFUL** Signal handler with rdi, rsi, rdx controlled

**USEFUL** Restorer without any registers controlled

**OK** Shadow Stack triggers SIGSEGV after the restorer returns

## Slide 107

###### **Shadow Stack Injection**

But how do we get the Shadow Stack not to crash?

Easy: We inject values onto it

## Slide 108

###### **Shadow Stack Injection**

Problem: How to write to the shadow stack?

- The userspace cannot write to it directly

## Slide 109

###### **Shadow Stack Injection**

Problem: How to write to the shadow stack?

- The userspace cannot write to it directly

- Calling functions pushes the return address only

Kinda useless

## Slide 110

###### **Shadow Stack Injection**

Using restorers we have two new alternatives

- Setting a restorer pushes the restorer address

- Triggering a signal pushes the SSP with MSB=1

## Slide 111

###### **Shadow Stack Injection**

We can _confuse_ the shadow stack if:

1. Push a restorer with MSB=1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Shadow Stack Injection
We can confuse the shadow stack If:
1.
with MSB=1
libc sigaction
oN
endbr64
sigaction
ret
```

## Slide 112

###### **Shadow Stack Injection**

We can _confuse_ the shadow stack if:

1. Push a restorer with MSB=1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Shadow Stack Injection
We can confuse the shadow stack If:
1. with MSB=1
Userspace ! Kernel
ee cestorer
~N restorer
mov r8, 0x0
mov r9, [r8]
ssp ;
Sigframe signal :
1 restorer handler !
1 P
```

## Slide 113

###### **Shadow Stack Injection**

We can _confuse_ the shadow stack if:

2. We manage to interpret the restorer as a saved SSP

- Moves the SSP to an arbitrary location

## Slide 114

###### **Shadow Stack Injection**

We tricked the Shadow Stack into accepting a random ROP chain

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Shadow Stack Injection
We tricked the Shadow Stack into accepting a random ROP chain
Userspace ! Kernel
me restorer
IN ~N restorer
ROP Gadget 1
mov r8, 0x0 Jsieseev sigframe
mov r9, [r8]
ROP Gadget 2
ania Sigframe signal a
handler | 3™ Restore
XZ | sigreturn Y state
{Ye
ROP Gadget N restorer
rbp Restore
x - SSP
```

## Slide 115

###### **Shadow Stack Injection**

###### It is _still_ complicated

- If the SSP points outside the shadow stack → SIGSEGV

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Shadow Stack Injection __ Ne
It is sti/] complicated
- Ifthe points the shadow stack >
Userspace ! Kernel
Ss Many restorer
IN ~N restorer ! Prepare
ROP Gadget 1 mov r8, 0x0 || SIGSEGVY |sigframe
mov r9, [r8]
ROP Gadget 2
g Sigframe signal a
handler :_3™ Restore
\ Z__|sigreturn Y\_ state
ROP Gadget N restorer
rbp Restore
```

## Slide 116

###### **Shadow Stack Injection**

###### It is _still_ complicated

- If the SSP points outside the shadow stack → SIGSEGV

- Before interpreting the SSP, we must return to the restorer

## Slide 117

###### **Shadow Stack Injection**

###### It is _still_ complicated

- If the SSP points outside the shadow stack → SIGSEGV

- • How to interpret a restorer as a saved SSP?

## Slide 118

###### **Shadow Stack Injection**

We have a very complicated set of rules…

- Do not write to the shadow stack

- Do not point SSP outside of the shadow stack

- Do not interpret the SSP before returning from the handler

- Do not accept a SSP without MSB=1

## Slide 119

###### **Shadow Stack Injection**

The solution is quite complicated as well :)

- Do not write to the shadow stack

- Do not point SSP outside of the shadow stack

- Do not interpret the SSP before returning from the handler

- Do not accept a SSP without MSB=1

## Slide 120

###### **Recursive Shadow Stack**

- A recursive shadow stack tricks CET to validate sigreturn forever

## Slide 121

###### **bSFOP: Early Kill**

• The signal handler starts right after the restorer is overwritten

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Early Kill
¢ The signal handler starts
libc sigaction
rip
|
- SIGSEGV
sigaction | Nandler =
ret
handler: sigaction
endbr64
mm ovorwnts restorer
leave
ret
```

## Slide 122

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming
Next signal handler: sigskip
Next restorer: __restore_rt
last return address
handler: sigskip
leave
ret
v
sigreturn
rsp
SA
rbp
SA
__restore_rt
Sigframe
rbp value
restore_rt
FAKE
SIGFRAME
i
5
Written by
the kernel
a,
5
| Corru pted
memory
ww,
```

## Slide 123

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming
Next signal handler: rsp
Next restorer: SS )
__restore_rt
handler: sigski
g P | Written by
vee Sigframe the kernel
sigaction
_ J
ret TDP
__restore_rt a
A 4 rbp value
SSP
sigreturn __restore_rt comuplics
memory
last return address FAKE
SIGFRAME I
b
```

## Slide 124

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming
Next signal handler: sigskip
Next restorer: recursive | MSB=1
=
__restore_rt
handler: sigskip
| Written by
wes Sigframe the kernel
sigaction
leave J
re Pe
__restore_rt
Z
¥
| = <
_. wim restore
ast return address , FAKE memory
\SIGFRAME , ,
SSP
```

## Slide 125

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming
Next signal handler: sigskip
Next restorer: recursive | MSB=1 | _restore_rt
__restore_rt
handler: sigskip
Written by
a Sigframe the kernel
sigaction
leave
ret Lo
__restore_rt
v
restore rt BW@@eMityce)
memory
J
5
J.
FAKE \
\SIGFRAME @
arco arse Bl
ast return address
Fake
Sigframe 2
```

## Slide 126

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming
Next signal handler: sigskip
Next restorer: recursive | MSB=1
__restore_rt [)
handler: sigski
g P Written by
_ Sigframe the kernel
OOOO Ko sigaction <
J
eave Fake
1 recursive <——— | Sigframe
. rbp value
: SSP Ss sigreturn __restore_rt {Semple
memo
last return address FAKE y
IGFRAME
__restore_rt S Z
pee NIM. ec cecceeeceeneeeneees ‘
Restor Restore :
state SSP
: Kernel | |
```

## Slide 127

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
\\
bSFOP: Shadow Stack Grooming <—
Next signal handler: sigskip rsp
Next restorer: recursive | MSB=1 SA =
__restore_rt
handler: sigskip
Written by
Sigframe the kernel
SSP leave b J
; ret TDP
recursive SA
bf rbp value
SSP recursive __restore_rt Canmpize
memory
FAKE
SIGFRAM
last return address
```

## Slide 128

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ssp
bSFOP: Shadow Stack Grooming
Next signal handler:
Next restorer:
recursive
SsP
last return address
handler: sigskip
sigaction
ret
v
recursive
rsp
SA
rbp
SS
__restore_
Sigframe
rbp value
__restore_
FAKE
IGFRAM
rt
rt
\\
>
Written by
the kernel
| Corrupted
memory
```

## Slide 129

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming
Next signal handler: leave;ret
Next restorer: _restore_rt
__restore_rt
SSP ¢
<i
sspi]
recursive
last return address
handler: sigskip
sigaction <
leave
ret
_¥
recursive
—f
-
>
__restore_rt
Sigframe
| Written by
the kernel
J
-
rbp value
restore_rt
FAKE
| Corrupted
memory
SIGFRAME @
```

## Slide 130

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming
Next signal handler: leave;ret rsp
Next restorer: _restore_rt SA
handler: sigaction
__restore_rt <> ret
SSP Vv
sigreturn rbp
recursive , < SN
__restore_rt
Sigframe
rbp value
restore_rt
FAKE
SIGFRAM
>
\\
Written by
the kernel
| Corrupted
memory
```

## Slide 131

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming
Next signal handler: leave;ret
Next restorer: _restore_rt
__restore_rt
handler: sigaction
leave
ret
__¥
__restore_
Sigframe
rbp value
restore __
FAKE
IGFRAM
rt
rt
>
Written by
the kernel
| Corrupted
memory
```

## Slide 132

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming | <— .
Next signal handler: leave;ret
rsp
Next restorer: _ restore_rt
handler: sigaction >
leave
ret
¥v
sigreturn
__restore_rt
ers
aN
__restore_rt
```

## Slide 133

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming
Next signal handler: leave;ret
Next restorer: _ restore_rt
Fake
handler: sigaction Sigframe 2
leave
__restore_rt <i ret __restore_rt
A Fake
; Sigframe 3
sigreturn
recursive
__restore_rt
```

## Slide 134

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming P=
Next signal handler: leave;ret
Next restorer: _ restore_rt
Fake
Sigframe 2
handler: sigaction
leave
rsp restore rt
__restore_rt ret — — =
A TPR
sigreturn
recursive
rip
aN
__restore_rt
```

## Slide 135

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming 7?
Next signal handler: leave;ret
Next restorer: _ restore_rt
Fake
handler: sigaction Sigframe 2
leave
__restore_rt ret __restore_rt
A 4 Fake
Sigframe 3
: sigreturn
recursive ,
~ Fake
Sigframe 4
```

## Slide 136

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming
Next signal handler: leave;ret
Next restorer: _ restore_rt
handler: sigaction = +-»
SA
leave
ret
Vv TPR,
sigreturn
rip __restore_rt
Sven
Arbitrary call 2 = execve()
Fake
Sigframe 5
```

## Slide 137

**bSFOP: Shadow Stack Grooming**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bSFOP: Shadow Stack Grooming <—>
Next signal handler: leave;ret
Next restorer: _ restore_rt
handler: sigaction
| on SD
A rbp
aA
sigreturn .,
ye
__restore_rt
rip
```

## Slide 138

## **Patching SFOP**

## Slide 139

###### **Patching SFOP**

###### **bSFOP**

- We have coordinated a patch with the Linux kernel developers to patch the bSFOP attack

###### **fSFOP**

   - Patching fSFOP requires enforcing IBT on user-kernel transitions, which is _hard_

- Prevents restorer and SSP hijacking

   - We patch some weaknesses that make fSFOP easier

- •

- **Fully patches** bSFOP fSFOP partially mitigated

## Slide 140

###### **https://github.com/signal-sfop/sfop**

Marcos Bajo _h3xduck_ Ritvik Goyal _RoYalGamr_ Apostolos Chatzianagnostou Christian Rossow

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
ARTIFACT ARTIFACT ARTIFACT
EVALUATED § EVALUATED § EVALUATED
Marcos Bajo h3xduck
Ritvik Goyal Ro YalGamr
Apostolos Chatzianagnostou
Christian Rossow
```
