---
title: "Crashing the Party Pwning Control-Flow Integrity with Segmentation Fault-Oriented Programming"
speakers: ["Marcos Bajo", "Ritvik Goyal"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Marcos Bajo, Ritvik Goyal - Crashing the Party Pwning Control-Flow Integrity with Segmentation Fault-Oriented Programming - Crashingthe.pdf"
pages: 140
sha256: "ec375e413944ef9a14c44bd246fb5a266201c8a683cf114552fd5480d991ff51"
text_chars: 28733
ocr_pages: 60
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.2
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 125
vision_verified_pages: 140
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:39:49Z"
---
# Crashing the Party Pwning Control-Flow Integrity with Segmentation Fault-Oriented Programming

**Speakers:** Marcos Bajo, Ritvik Goyal  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Marcos Bajo, Ritvik Goyal - Crashing the Party Pwning Control-Flow Integrity with Segmentation Fault-Oriented Programming - Crashingthe.pdf` (140 pages)


## Slide 1

#### **Crashing the Party: Pwning Control-Flow Integrity with _SFOP_**

_Segmentation Fault-Oriented Programming_

**Marcos Bajo (_h3xduck_) | Ritvik Goyal (_RoYalGamr_)**

_CISPA Helmholtz Center for Information Security_

## Slide 2

###### **The Old Ages**

###### **1972**

Buffer overflows 1<sup>st</sup> mentioned

Scanned cover of the report:

```text
ESD-TR-73-51, Vol. II

COMPUTER SECURITY TECHNOLOGY PLANNING STUDY

James P. Anderson

October 1972

DEPUTY FOR COMMAND AND MANAGEMENT SYSTEMS
HQ ELECTRONIC SYSTEMS DIVISION (AFSC)
L. G. Hanscom Field, Bedford, Massachusetts  01730
```

The USAF emblem at the top right of the cover is ringed with the words ELECTRONIC SYSTEMS DIVISION.

## Slide 3

###### **The Old Ages**

###### **1972**

Buffer overflows 1<sup>st</sup> mentioned

The timeline labels **2000**, **2010** and **2020** run along the top of the panel, which covers the timeline with:

### **MEMORY CORRUPTION** → **CODE EXECUTION**

(a downward arrow from MEMORY CORRUPTION to CODE EXECUTION)

## Slide 4

###### **The Old Ages**

**1972**    **2000**    **2010**    **2020**

Timeline. Under **1972**: an attack marker labelled

Buffer overflows 1<sup>st</sup> mentioned

Then a break in the line, and a second attack marker just before the **2000** tick, labelled

ret2libc

## Slide 5

###### **The Old Ages**

**1972**    **2000**    **2010**    **2020**

Timeline. Under **1972**: an attack marker labelled

Buffer overflows 1<sup>st</sup> mentioned

Then a break in the line, and four markers clustered around the **2000** tick, in order along the line:

- ret2libc (attack marker)

- Stack canaries (shield marker)

- DEP/NX (shield marker)

- ASLR (shield marker)

## Slide 6

###### **The Old Ages**

**1972**    **2000**    **2010**    **2020**

Timeline. Under **1972**: an attack marker labelled

Buffer overflows 1st mentioned

Then a break in the line, and four markers clustered around the **2000** tick, in order along the line:

- ret2libc (attack marker)

- Stack canaries (shield marker)

- DEP/NX (shield marker)

- ASLR (shield marker)

The line continues toward **2010** and **2020** with three more attack markers, in order:

- ROP

- JOP

- DOP

## Slide 7

**Code Reuse**

Call graph diagram with five boxes, **f()**, **g()**, **h()**, **i()**, **j()**, arranged with f() at top, g() and i() in a middle row, h() and j() in a bottom row. Arrows:

- f() → g()

- f() → h() (curved, routed down the left side)

- g() → h()

- g() → i()

- h() → i() (diagonal)

- h() → j()

- j() → i() (curved, routed up the right side)

## Slide 8

**Vulnerability Exploitation: Code Reuse**

Same call graph as the previous slide (f, g, h, i, j), redrawn with each function's body split into its call instructions plus a separately-outlined ".... / ret" line, and a new **execve()** box at top right. Node contents:

- **f:** call g() / call h() / .... / ret

- **g:** call h() / call i() / .... / ret

- **h:** call i() / call j() / .... / ret

- **i:** (no body) / .... / ret

- **j:** call i() / .... / ret

Every function's "...."/ret line is boxed in red. The white call-graph arrows from the previous slide are unchanged: f→g, f→h (curved, left side), g→h, g→i, h→i (diagonal), h→j, j→i (curved, right side).

A thick red arrow chain is overlaid on top, tracing a hijacked return path from ret to ret, independent of the white call edges:

f:ret → g:ret → i:ret → j:ret → execve()

## Slide 9

###### **Code-Reuse attacks**

- Code-Reuse uses small code pieces: gadgets

- **ROP** gadgets:

   - End with a _ret_ instruction

```text
pop rax
ret
```

- **JOP** gadgets:

   - End with a jmp instruction

```text
mov rax, [rsp]
mov rdi, [rsp+0x8]
jmp rdi
```

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

Same call graph as the earlier Code Reuse slides (f, g, h, i, j), with a padlock icon on every edge: f→g, f→h (curved, left side), g→h, g→i, h→i (diagonal), h→j, j→i (curved, right side).

## Slide 11

# **SFOP**

**S**egmentation **F**ault-**O**riented **P**rogramming

## Slide 12

# **SFOP**

###### **Segmentation Fault-Oriented Programming**

- Bypasses Intel CET

_…unlike ROP, JOP, SROP_

## Slide 13

# **SFOP**

###### **Segmentation Fault-Oriented Programming**

- Bypasses Intel CET

_…unlike ROP, JOP, SROP_

- Does not require C++ programming paradigms

_…unlike COOP, CFOP, CHOP_

## Slide 14

# **SFOP**

###### **Segmentation Fault-Oriented Programming**

- Bypasses Intel CET

_…unlike ROP, JOP, SROP_

- Does not require C++ programming paradigms

_…unlike COOP, CFOP, CHOP_

- Does not require specific program gadgets

_…unlike FOP_

## Slide 15

# **SFOP**

###### **Segmentation Fault-Oriented Programming**

Works **by default** in any **x86_64 Linux** program with **Intel CET** enabled

_Unlike ROP, JOP, SROP, COOP, CFOP, FOP, CHOP…_

## Slide 16

###### **What We Will Learn**

###### 1. Control-Flow Integrity

_The defenses bypassed by SFOP._

## Slide 17

###### **What We Will Learn**

###### 1. Control-Flow Integrity

_The defenses bypassed by SFOP._

###### 2. Linux Signals

_The mechanism behind SFOP._

## Slide 18

###### **What We Will Learn**

###### 1. Control-Flow Integrity

_The defenses bypassed by SFOP._

###### 2. Linux Signals

_The mechanism behind SFOP._

###### 3. Segmentation Fault-Oriented Programming

_Using bSFOP and fSFOP to exploit programs protected by CET._

## Slide 19

###### **What We Will Learn**

###### 1. Control-Flow Integrity

_The defenses bypassed by SFOP._

###### 2. Linux Signals

_The mechanism behind SFOP._

###### 3. Segmentation Fault-Oriented Programming

_Using bSFOP and fSFOP to exploit programs protected by CET._

###### 4. Patching SFOP

_Patching the Linux Kernel to stop SFOP._

## Slide 20

**1**

### **Userspace CFI Defenses**

Four progress dots beneath a red rule: the first (this section) filled red, the remaining three outlined white.

## Slide 21

###### **Intel CET**

- SFOP bypasses Intel CET

   - Most widespread CFI scheme in modern x86

   - Linux and Windows

   - Intel 11th generation (Tiger Lake) processors Onwards

- CET composed of two techniques:

   - Shadow Stack (SHSTK)

   - Indirect Branch Tracking (IBT)

## Slide 22

**Intel CET (Shadow Stack)**

Four snippets left to right, each connected to the next by a red arrow (f() → g() → h() → i()):

```text
void f()
{
    g();
    ret;
}

void g()
{
    h();
    ret;
}

void h()
{
    i();
    ret;
}

void i()
{
    ret;
}
```

## Slide 23

**Intel CET (Shadow Stack)**

Two vertical stack diagrams side by side, both growing upward.

Left, the regular stack, entries bottom to top:

- f() frame

- f() return address (highlighted red)

- g() frame

- g() return address (dimmed)

- h() frame (dimmed)

- h() return address (dimmed)

- i() frame (dimmed, top)

**rsp** points at the top of the stack, just above g() frame.

Right, the shadow stack, holding only:

- f() return address (highlighted red)

**ssp** points just above it, at the top of the shadow stack.

## Slide 24

**Intel CET (Shadow Stack)**

Left, the regular stack, entries bottom to top:

- f() frame

- f() return address (red)

- g() frame

- g() return address (red)

- h() frame

- h() return address (dimmed)

- i() frame (dimmed, top)

**rsp** points at the top of the stack, just above h() frame.

Right, the shadow stack, entries bottom to top:

- f() return address (red)

- g() return address (red)

**ssp** points just above g() return address, at the top of the shadow stack.

## Slide 25

**Intel CET (Shadow Stack)**

Left, the regular stack, now fully solid (nothing dimmed), entries bottom to top:

- f() frame

- f() return address (red)

- g() frame

- g() return address (red)

- h() frame

- h() return address (red)

- i() frame (top)

**rsp** points at the top of the stack, just above i() frame.

Right, the shadow stack, entries bottom to top:

- f() return address (red)

- g() return address (red)

- h() return address (red)

**ssp** points just above h() return address, at the top of the shadow stack.

## Slide 26

**Intel CET (Shadow Stack)**

```text
void i()
{
    ret;
}
```

The `ret;` line is boxed in red (currently executing).

Left, the regular stack, entries bottom to top: f() frame, f() return address (red), g() frame, g() return address (red), h() frame, h() return address (red), i() frame (top). **rsp** points at h() return address.

Right, the shadow stack, entries bottom to top: f() return address (red), g() return address (red), h() return address (red). **ssp** points at h() return address.

Two arrows, one from each stack's h() return address entry, converge on a green checkmark, showing the two addresses match.

## Slide 27

**Intel CET (Shadow Stack)**

```text
void h()
{
    i();
    ret;
}
```

The `ret;` line is boxed in red (currently executing).

Left, the regular stack, entries bottom to top: f() frame, f() return address (red), g() frame, g() return address (red, rsp here), h() frame, h() return address (red), i() frame (top).

Right, the shadow stack, entries bottom to top: f() return address (red), g() return address (red, ssp here), h() return address (red, top).

Two arrows, one from each stack's g() return address entry, converge on a green checkmark, showing the two addresses match.

## Slide 28

**Intel CET (Shadow Stack)**

```text
void g()
{
    h();
    ret;
}
```

The `ret;` line is boxed in red (currently executing).

Left, the regular stack, entries bottom to top: f() frame, f() return address (red, rsp here), g() frame, g() return address (red), h() frame, h() return address (red), i() frame (top).

Right, the shadow stack, entries bottom to top: f() return address (red, ssp here), g() return address (red), h() return address (red, top).

Two arrows, one from each stack's f() return address entry, converge on a green checkmark, showing the two addresses match.

## Slide 29

**Intel CET (Shadow Stack)**

```text
void i()
{
    ret;
}
```

The `ret;` line is boxed in red (currently executing).

Left, the regular stack, entries bottom to top: f() frame, f() return address (red), g() frame, g() return address (red), h() frame, **system()** (red, in place of h() return address, rsp here), i() frame (top).

Right, the shadow stack, unchanged, entries bottom to top: f() return address (red), g() return address (red), h() return address (red, ssp here).

Two arrows, one from system() on the regular stack and one from h() return address on the shadow stack, converge on a red X, showing the two addresses do not match.

## Slide 30

###### **Intel CET (Shadow Stack)**

- Processes allocate a dedicated memory region before calling _main_

   - Function _​_dl_cet_setup_features_

   - Instructs the kernel to allocate a shadow stack

arch_prctl ➡️ do_arch_prctl_64 ➡️ shstk_prctl ➡️ shstk_setup ➡️ alloc_shstk

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

Meme image captioned **PERFECTLY SECURED** (imgflip.com): a man carefully closing a small decorative gate set in a low fence, while the adjacent house wall has an open doorway right next to it with no gate or barrier at all.

## Slide 33

###### **Intel CET (IBT)**

```text
main:
 push rbp
 mov rbp, rsp
 mov rsi, [rdi+0x8]
 mov rax, [rbx]
 call [rax]
 leave
 ret
```

The `call` mnemonic is highlighted red.

## Slide 34

###### **Intel CET (IBT)**

```text
main:
 push rbp
 mov rbp, rsp
 mov rsi, [rdi+0x8]
 mov rax, [rbx]
 call [rax]
 leave
 ret

f1:
 add rdi, 0x8
 mov rax, 0x10
 lea rdx, [rbp]
 add rdi, rax
 mov rax, rdx
 ret
```

The `call` mnemonic is highlighted red. Two red arrows branch from `call [rax]`: one to the top of f1 (`add rdi, 0x8`), one to the bottom (`ret`); both are marked with a green checkmark.

## Slide 35

###### **Intel CET (IBT)**

```text
main:
 push rbp
 mov rbp, rsp
 mov rsi, [rdi+0x8]
 mov rax, [rbx]
 call [rax]
 leave
 ret

f1:
 endbr64
 add rdi, 0x8
 mov rax, 0x10
 lea rdx, [rbp]
 add rdi, rax
 mov rax, rdx
 ret
```

The `call` and `endbr64` mnemonics are highlighted red. Two red arrows branch from `call [rax]`: one to `endbr64` at the top of f1, marked with a green checkmark; one to `ret` at the bottom of f1, marked with a red X.

## Slide 36

###### **Intel CET (IBT)**

- Limited availability

   - Windows: Not implemented

   - Linux: enforcement only in the kernel since 5.18

- Coarse-grained CFI

   - We still can use gadgets starting with endbr64

## Slide 37

###### **Intel CET (IBT)**

- Coarse-grained CFI still prevents classic code-reuse

- ROP

```text
pop rax
ret
```

- JOP

```text
mov rax, [rsp]
mov rdi, [rsp+0x8]
jmp rdi
```

## Slide 38

**2**

### **Linux Signals**

Four progress dots beneath a red rule: the first two (sections 1–2) filled red, the remaining two outlined white.

## Slide 39

###### **Linux Signals**

- Signals are asynchronous inter-process notifications

SIGKILL → Killing a process

SIGSEGV → Inaccessible memory location

## Slide 40

###### **Linux Signals**

- Signals can be handled registering a signal handler

signal(signum=SIGSEGV, handler=h)

sigaction(signum=SIGSEGV, act={handler=h,…})

## Slide 41

**Linux Signals**

A vertical dashed line divides **Userspace** (left) from **Kernel** (right).

On the userspace side, a boxed code snippet:

```text
mov r8, 0x0
mov r9, [r8]
```

The second line, `mov r9, [r8]`, is highlighted red.

Below it, a small stack diagram: **rsp** and **rbp** both point at the same box, labelled "…".

## Slide 42

**Linux Signals**

A vertical dashed line divides **Userspace** (left) from **Kernel** (right).

On the userspace side, the same boxed code snippet as before:

```text
mov r8, 0x0
mov r9, [r8]
```

A red **SIGSEGV** banner arrows from that code, across the divider, into a kernel box labelled _Prepare sigframe_. A white arrow leads back from _Prepare sigframe_ down to the stack diagram on the left.

Stack diagram: **rsp** now points at the top of a new red block pushed above the old frame, made of two parts stacked together — **restorer** (top) and **Sigframe** (below it) — with **rbp** still pointing at the old "…" frame beneath them.

## Slide 43

**Linux Signals**

Memory layout of the signal frame pushed onto the stack, as a byte-offset table with two fields per row (left column, right column):

| Offset | Left column | Right column |
|---|---|---|
| 0x0 | (blank) | restorer ptr. |
| 0x10 | uc_flags | uc_link |
| 0x20 | uc_stack.ss_sp | uc_stack.ss_flags |
| 0x30 | uc_stack.ss_size | r8 |
| 0x40 | r9 | r10 |
| 0x50 | r11 | r12 |
| 0x60 | r13 | r14 |
| 0x70 | r15 | rdi |
| 0x80 | rsi | rbp |
| 0x90 | rbx | rdx |
| 0xA0 | rax | rcx |
| 0xB0 | rsp | rip |
| 0xC0 | rflags | cs/gs/fs/pad |
| 0xD0 | err | trapno |
| 0xE0 | oldmask | cr2 |
| 0xF0 | fpstate ptr. | (blank) |
| 0x100 | _reserved | (the lower right portion of _reserved is carved out and labelled **sigmask**) |
| 0x140 | siginfo (spans both columns) | |
| 0x1B0 | 64B Align | |
| — | xstate (≈0xA8C bytes) | |
| — | 16B Align | |
| ~0xD00 | redzone (0x80 bytes) | |

Top annotations: an arrow labelled **restorer rsp** points at the 0x0/0x10 boundary of the left column; an arrow labelled **handler rsp** points at the 0x0 row of the right column (restorer ptr.). At the bottom, an arrow labelled **old rsp** points at the bottom edge of the redzone.

Three braces on the right margin mark nested regions by size:

- **sigcontext** (size=0xD0) — top aligned with the r8 row (offset 0x30)

- **ucontext** (size=0x100) — top aligned with the uc_link row (offset 0x10)

- **sigframe** (size=0x1B8) — top aligned with the very first row (offset 0x0)

## Slide 44

**Linux Signals**

A vertical dashed line divides **Userspace** (left) from **Kernel** (right).

On the userspace side, the boxed code snippet:

```text
mov r8, 0x0
mov r9, [r8]
```

A red **SIGSEGV** banner arrows from that code, across the divider, into a kernel box labelled _Prepare sigframe_. A large red arrow now leads back from _Prepare sigframe_, across the divider, into a new box labelled **signal handler** (red text, below the code snippet).

Stack diagram, unchanged from the previous slide: **rsp** points at the top of a red block made of two parts — **restorer** (top) and **Sigframe** (below it) — with **rbp** pointing at the old "…" frame beneath them.

## Slide 45

**Linux Signals**

A vertical dashed line divides **Userspace** (left) from **Kernel** (right).

```text
mov r8, 0x0
mov r9, [r8]
```

The SIGSEGV banner and the arrow between _Prepare sigframe_ (kernel) and **signal handler** (userspace) are unchanged. New: a black arrow leads down from **signal handler** to a new box, **restorer** (red text).

Stack diagram, unchanged: **rsp** points at the top of a red block made of two parts — **restorer** (top) and **Sigframe** (below it) — with **rbp** pointing at the old "…" frame beneath them.

## Slide 46

**Linux Signals**

Same layout as before, with the SIGSEGV path now shown in black (de-emphasized). New: a red **sigreturn** banner arrows from the **restorer** box, across the divider, into a new kernel box labelled _Restore state_.

Stack diagram, unchanged: **rsp** points at the top of a red block made of two parts — **restorer** (top) and **Sigframe** (below it) — with **rbp** pointing at the old "…" frame beneath them.

## Slide 47

**Linux Signals**

Same right-side diagram as before: the **Userspace** / **Kernel** divide, the `mov r8, 0x0` / `mov r9, [r8]` code, the SIGSEGV banner into _Prepare sigframe_, the arrow back into **signal handler**, the arrow down into **restorer**, and the red **sigreturn** banner into _Restore state_.

Stack diagram, reverted: the red restorer/Sigframe block is gone — **rsp** and **rbp** both point at the single "…" box, as before the fault.

## Slide 48

###### **Shadow Stack with Signals**

- The Shadow Stack Pointer (SSP) marks the top of the Shadow Stack

Small stack diagram: two empty dashed rows above a red row labelled **last return address**. **SSP** points at the top of the red row.

## Slide 49

###### **Shadow Stack with Signals**

- The Shadow Stack Pointer (SSP) marks the top of the Shadow Stack

   - The SSP is saved onto the Shadow Stack when a signal is triggered. The MSB is set to 1 to distinguish it

Two small stack diagrams side by side.

Left (unchanged from the previous slide): two empty dashed rows above a red row labelled **last return address**; **SSP** points at the top of the red row.

Right (new): **SSP** points at the top of a row labelled **restorer**; below it, a row split into a small **1** cell and a red **SSP** cell; below that, a row labelled **last return address**. A white arrow loops from the **SSP** cell around to the right and back into the **last return address** cell.

## Slide 50

###### **Shadow Stack with Signals**

- The SSP is checked during _sigreturn_

   - If MSB=1, the SSP is restored to the saved value

   - If MSB≠1 a SIGSEGV is triggered

Same two stack diagrams as the previous slide, unchanged: left, two empty dashed rows above a red **last return address** row with **SSP** pointing at its top; right, **SSP** pointing at a **restorer** row, above a row split into **1** and **SSP**, above a **last return address** row, with a white arrow looping from the **SSP** cell back into **last return address**.

## Slide 51

###### **SROP is Dead**

- In the SROP attack, the attacker:

   - Forges a fake sigframe in memory

   - Calls sigreturn directly

Three diagrams:

Left, the shadow stack: three rows, all labelled **return address**, each with a red **0** sub-cell on the left (MSB=0). **ssp** points at the top row. A white loop connects the second row to the third row, arrowhead at the third row.

Middle, the regular stack: **rsp** points at the top of a row labelled **restorer**, below it a red block labelled **CORRUPTED SIGFRAME**, below that **rbp** points at a row labelled "…".

Right, the Userspace/Kernel flow: a **normal execution** box, a red **sigreturn** banner arrowing across the divider into a kernel box _Restore state_, and below it a second kernel box _Restore SSP_.

## Slide 52

###### **SROP is Dead**

- In modern Linux, the kernel checks MSB=1

   - No return address in the shadow stack has MSB=1 naturally

   - Check always failed → SIGSEGV

Same three diagrams as the previous slide (forged shadow stack with MSB=0 entries; regular stack with a CORRUPTED SIGFRAME; Userspace/Kernel flow through sigreturn into _Restore state_ then _Restore SSP_). New: a red arrow leads down from _Restore SSP_ to a new box, **SIGSEGV**.

## Slide 53

###### **Is It The End?**

ROP → Prevented by Shadow Stacks

JOP → Prevented by IBT

SROP → Prevented by MSB check on Shadow Stack

## Slide 54

**3**

### **SFOP**

Four progress dots beneath a red rule: the first three (sections 1–3) filled red, the fourth outlined white.

## Slide 55

**Missing IBT Checks**

A vertical dashed line divides **Userspace** (left) from **Kernel** (right).

```text
mov r8, 0x0
mov r9, [r8]
```

A **SIGSEGV** banner arrows from that code, across the divider, into a kernel box labelled _Prepare sigframe_. An arrow leads back into a **signal handler** box, then down into a **restorer** box. A **sigreturn** banner arrows from **restorer**, across the divider, into a kernel box labelled _Restore state_.

## Slide 56

**Missing IBT Checks**

Same diagram as the previous slide, with a translucent red banner overlaid across the top (covering the `mov r8, 0x0`/`mov r9, [r8]` code, the SIGSEGV banner, and the _Prepare sigframe_ box, all still faintly visible beneath it), captioned in bold white:

NO IBT CHECKS
SIGNAL DELIVERY

## Slide 57

**Missing IBT Checks**

Same diagram as before, now with a second translucent red banner added beneath the first, covering the **signal handler**/**restorer** boxes and the sigreturn/_Restore state_ path, captioned:

NO IBT CHECKS
SIGNAL DELIVERY

NO IBT CHECKS
SIGNAL RETURN

## Slide 58

###### **Is This Enough?**

- Unprotected branches are not enough to create practical code-reuse attack…

## Slide 59

###### **Is This Enough?**

- Unprotected branches are not enough to create practical code-reuse attack…

   - How to trigger an arbitrary signal handler?

## Slide 60

###### **Is This Enough?**

- Unprotected branches are not enough to create practical code-reuse attack…

   - How to trigger an arbitrary signal handler?

   - How to control the register arguments inside the handler?

## Slide 61

###### **Is This Enough?**

- Unprotected branches are not enough to create practical code-reuse attack…

   - How to trigger an arbitrary signal handler?

   - How to control the register arguments inside the handler?

   - How to execute multiple arbitrary function calls?

## Slide 62

**Late Kernel Safety Checks**

Three diagrams:

Left, the shadow stack: **ssp** points at a row labelled **restorer**; below it, a row split into a red **1** cell and a red **SSP** cell; below that, a row labelled **last return address**. A white loop connects the **SSP** cell around to the right and back into **last return address**.

Middle, the regular stack: **rsp** points at a row labelled **restorer**, below it a red block labelled **Sigframe**, below that **rbp** points at a row labelled "…".

Right, the Userspace/Kernel flow:

```text
mov r8, 0x0
mov r9, [r8]
```

A **SIGSEGV** banner arrows from that code, across the divider, into a kernel box _Prepare sigframe_. An arrow leads back into **signal handler**, then down into **restorer**. A red **sigreturn** banner arrows from **restorer** into a kernel box _Restore state_, above a second kernel box _Restore SSP_.

## Slide 63

###### **Late Kernel Safety Checks**

- The kernel restores the sigframe _before_ checking SSP

Three diagrams, continuing from the previous slide:

Left, the shadow stack: three "return address" rows (each with a red **0** cell), **ssp** at the top row, the white loop from row 2 to row 3 now marked with a red X.

Middle, the regular stack: **rsp** points at **restorer**, below it a red block now labelled **CORRUPTED SIGFRAME**, below that **rbp** points at "…".

Right, the Userspace/Kernel flow, simplified to: a **normal execution** box, a **sigreturn** banner arrowing into kernel box _Restore state_, and below it _Restore SSP_ — now marked with a red X.

## Slide 64

###### **Late Kernel Safety Checks**

- At this point we control the pt_regs in the Kernel

Two diagrams:

Left, the shadow stack: same three "return address" rows (each with a red **0** cell), **ssp** at the top row, the white loop from row 2 to row 3 marked with a red X. **rsp** and **rbp** now both point at a single plain box beside it (the sigframe has been popped).

Right, the Userspace/Kernel flow: a **normal execution** box, a red **sigreturn** banner arrowing into kernel box _Restore state_, and below it a red arrow down into _Restore SSP_ — marked with a red X.

## Slide 65

###### **Late Kernel Safety Checks**

- Oh no !! Kernel throws catchable Sigsegv

Two diagrams:

Left, the shadow stack, unchanged: three "return address" rows (each with a red **0** cell), **ssp** at the top row, the white loop from row 2 to row 3 marked with a red X. **rsp** and **rbp** both point at a single plain box beside it.

Right, the Userspace/Kernel flow: **normal execution** → red **sigreturn** banner → _Restore state_ → _Restore SSP_ → a red arrow down to a new box **SIGSEGV** → a red arrow down to a new kernel box _Prepare sigframe_.

## Slide 66

###### **Late Kernel Safety Checks**

- What if we already registered a signal handler ?

Three diagrams, continuing:

Left, the shadow stack: **ssp** now points at a new top row, **restorer** (plain), above a red **1 | SSP** row (with a white loop arrow to the row below), above two **0 | return address** rows.

Middle, unchanged: **rsp** → restorer / CORRUPTED SIGFRAME, **rbp** → "…".

Right, the Userspace/Kernel flow: **normal execution** → **sigreturn** → _Restore state_ → _Restore SSP_ → **SIGSEGV** → _Prepare sigframe_ → a black arrow into **signal handler**.

## Slide 67

###### **Late Kernel Safety Checks**

- We got our corrupted sigframe back

Same three diagrams. Left, the shadow stack now has only one **0 | return address** row left below the **restorer** / **1 | SSP** rows. Right, new: a red arrow leads down from **signal handler** into a new box, **restorer** (red text).

## Slide 68

###### **Late Kernel Safety Checks**

- We send our corrupted sigframe back for sigreturn

Same diagrams, unchanged left and middle. Right, new: a red **sigreturn** banner arrows from **restorer**, across the divider, directly into a new kernel box, _Restore SSP_.

## Slide 69

###### **Late Kernel Safety Checks**

- And we bypass the sigreturn shadow stack check

Three diagrams:

Left, the shadow stack, back to two plain **0 | return address** rows, **ssp** pointing at the top one.

Middle, **rsp** and **rbp** both point at a single plain "…" box.

Right, the Userspace/Kernel flow: **normal execution** → **sigreturn** → _Restore state_ → _Restore SSP_ → **SIGSEGV** → _Prepare sigframe_ → **signal handler** → **restorer** → a second **sigreturn** banner → _Restore SSP_ → a thick red arrow into a new box, **ARBITRARY TARGET** (red text).

## Slide 70

###### **User Kernel Data Collision**

- Kernel sets the registers before signal delivery :

   - $RDI = signal_no

   - $RSI = SIGINFO_location

   - $RDX = ucontext_location

   - $RSP = sigframe

   - $RIP = signal_handler

   - $RAX = 0  (can be ignored)

## Slide 71

###### **User Kernel Data Collision**

- Kernel sets the registers before signal delivery :

   - $RDI = signal_no

   - $RSI = SIGINFO_location

   - $RDX = ucontext_location

   - $RSP = sigframe

   - $RIP = signal_handler

   - $RAX = 0  (can be ignored)

   - And doesn’t modify any other registers, which can be pass on from previous context to signal handler

## Slide 72

###### **User Kernel Data Collision**

- Kernel sets the registers before signal delivery :

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

_signal handler_

Diagram: one oval labelled **rdi = signum**, above an empty box labelled "…".

## Slide 74

###### **User Kernel Data Collision**

- Data from the kernel is incorrectly used in userland

Two diagrams side by side.

Left, _signal handler_: three ovals, **rdi = signum**, **rsi = siginfo**, **rdx = ucontext**, above an empty box labelled "…".

Right, _libc sigaction_: three ovals, **rdi = signum**, **rsi = sigaction act{}**, **rdx = sigaction oldact{}**, above an empty box labelled "…".

## Slide 75

###### **User Kernel Data Collision**

- Libc sigaction will interpret _rsi_ as act{}… but it is siginfo!

**signal handler = libc sigaction**

Diagram: three ovals, **rdi = signum = signum**, **rsi = siginfo = sigaction act{}**, **rdx = ucontext = sigaction oldact**, above an empty box labelled "…".

## Slide 76

###### **SIGINFO rsi bug**

Stack diagram: a box divided into rows, top to bottom: **restorer** (plain), **ucontext** (red, tall), **Siginfo** (red), **…** (plain). **rdx** points at the top of the **ucontext** row; **rsi** points at the top of the **Siginfo** row.

## Slide 77

###### **SIGINFO rsi bug**

If we registered a Signal Handler with SA_SIGINFO Flag, then Kernel will fill the siginfo area and rsi will point to that location

Same stack diagram as the previous slide: **restorer** (plain), **ucontext** (red, tall), **Siginfo** (red), **…** (plain). **rdx** points at the top of **ucontext**; **rsi** points at the top of **Siginfo**.

## Slide 78

###### **SIGINFO rsi bug**

If we registered a Signal Handler with SA_SIGINFO Flag, then Kernel will fill the siginfo area and rsi will point to that location

What if we don’t register with SA_SIGINFO Flag?

Same stack diagram as the previous slides: **restorer** (plain), **ucontext** (red, tall), **Siginfo** (red), **…** (plain). **rdx** points at the top of **ucontext**; **rsi** points at the top of **Siginfo**.

## Slide 79

###### **fSFOP: Early Kill**

- We want to register a signal _and_ trigger a SIGSEGV

__pthread_once_slow  +  __obstack_newchunk

Stack memory controlled + Forward pointer hijacked

Call sigaction(rdi, rsi, rdx)
   rdi = SIGSEGV (0xb)
   rsi = act{handler,…}
   rdx = early kill trigger

## Slide 80

###### **fSFOP: Early Kill**

- We trigger a SIGSEGV _inside_ sigaction() after the signal is already registered

sigaction(rdi, rsi, rdx)
   rdi = SIGSEGV
   rsi = act{handler,…}
   rdx = invalid memory

_libc sigaction_

```text
mov r8, rdx
...
sigaction
...
mov [r8], rax
...
ret
```

The `mov [r8], rax` line is marked with a red X.

## Slide 81

###### **fSFOP: Sigframe Pivoting**

- Sigframe Pivoting allows controlling the sigframe from within a signal handler

**CLASSIC** Sigframe Pivoting

**UNWINDING-BASED** Sigframe Pivoting

**DOUBLE-PARTIAL** Sigframe Pivoting

## Slide 82

###### **fSFOP: Classic Sigframe Pivoting**

1. Register _sigaction_ as SIGSEGV handler, trigger Early Kill

_libc sigaction_

```text
...
sigaction
...
mov [r8], rax
...
ret
```

**rip** points at `mov [r8], rax`, annotated: **SIGSEGV handler = sigaction**. A white arrow leads from there into a new box, **handler: sigaction**:

```text
leave
ret
```

Stack diagram on the right: **rsp** and **rbp** both point at a plain "…" row, below which three red rows are labelled **Corrupted memory**: **rbp value**, **__restore_rt**, **FAKE SIGFRAME**.

## Slide 83

###### **fSFOP: Classic Sigframe Pivoting**

2. Signal handler is triggered, sigframe is created

_handler: sigaction_

```text
leave
ret
```

**rip** points at `leave`. A white arrow leads down from this box into a new box:

```text
sigreturn
```

Stack diagram on the right: **rsp** points at a new red block written by the kernel — **__restore_rt** (top) and **Sigframe** (below it, tall) — labelled **Written by the kernel**. Below that, **rbp** points at a plain "…" row, below which three rows are labelled **Corrupted memory**: **rbp value** (red), **__restore_rt** (white), **FAKE SIGFRAME** (white).

## Slide 84

###### **fSFOP: Classic Sigframe Pivoting**

3. Stack pivoting gadget moves rsp to fake sigframe

_handler: sigaction_

```text
leave
ret
```

**rip** points at `ret`. A white arrow leads down into a new box:

```text
sigreturn
```

Stack diagram on the right: **__restore_rt** and **Sigframe** (plain, labelled **Written by the kernel**), then a plain "…" row, then **rsp** and **rbp** both point at the top of a red block labelled **Corrupted memory**: **rbp value**, **__restore_rt**, **FAKE SIGFRAME**.

## Slide 85

###### **fSFOP: Classic Sigframe Pivoting**

4. Sigreturn is called using the fake sigframe

_handler: sigaction_

```text
leave
ret
```

A white arrow leads down into a new box, now pointed at by **rip**:

```text
sigreturn
```

Stack diagram on the right: **__restore_rt** and **Sigframe** (plain, **Written by the kernel**), then a plain "…" row, then the **Corrupted memory** block: **rbp** points at **rbp value** (plain), **rsp** points at **__restore_rt** (plain), below which **FAKE SIGFRAME** is still red.

## Slide 86

###### **fSFOP: Classic Sigframe Pivoting**

5. Arbitrary function call

_handler: sigaction_

```text
leave
ret
```

A white arrow leads down into:

```text
sigreturn
```

Below it, **rip** now points at a separate red box, **ARBITRARY TARGET**.

Stack diagram on the right, all plain/white now (nothing highlighted): **__restore_rt** and **Sigframe** (**Written by the kernel**), a plain "…" row, then the former **Corrupted memory** block, now also plain: **rbp value**, **__restore_rt**, **FAKE SIGFRAME**. **rsp** and **rbp** both point at a new plain "…" row past it.

## Slide 87

###### **fSFOP: Infinite Segfault Looping**

SIGSEGV triggers the next pivot, achieving infinite function calls

_handler: sigaction_, now outlined in red, pointed at by **rip**:

```text
leave
ret
```

A white arrow leads down into:

```text
sigreturn
```

Below that, a plain box, **ARBITRARY TARGET**, connects by a red line to a new box, **SIGSEGV**, from which a thick red arrow loops back up into **handler: sigaction**.

Two identical stack diagrams side by side: **__restore_rt** and **Sigframe** (**Written by the kernel**), a plain "…" row, then **Corrupted memory**: **rbp value**, **__restore_rt**, **FAKE SIGFRAME**. **rsp** and **rbp** point at the top of the right-hand copy.

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

Meme image, bottom right: SpongeBob SquarePants smirking suspiciously with narrowed eyes.

## Slide 90

**Signal Restorer Hijacking**

sigaction(signum=SIGSEGV, act={handler=h,…})

## Slide 91

**Signal Restorer Hijacking**

sigaction(signum=SIGSEGV, act={handler=h,
             flags=f,
             restorer=r})

Stack diagram: **rsp** points at a red row labelled **restorer**, above a plain row labelled **Sigframe**, above a plain "…" row pointed at by **rbp**.

## Slide 92

###### **Signal Restorer Hijacking**

- Calling sigaction is not enough…

   - _libc_ always overwrites the restorer with __restore_rt

   - __restore_rt calls _sigreturn_

## Slide 93

###### **Signal Restorer Hijacking**

- Calling sigaction is not enough…

   - _libc_ always overwrites the restorer with __restore_rt

   - __restore_rt calls _sigreturn_

_libc sigaction_

```text
endbr64
...
overwrite restorer
...
sigaction
...
ret
```

The `overwrite restorer` line is highlighted red.

## Slide 94

###### **Signal Restorer Hijacking**

- Calling sigaction is not enough…

   - _libc_ always overwrites the restorer with __restore_rt

   - __restore_rt calls _sigreturn_

- But we can jump _after_ the overwrite

_libc sigaction_

```text
endbr64
...
overwrite restorer
...
sigaction
...
ret
```

The `overwrite restorer` line is highlighted red. A red arrow points at the `...` line just below it (between `overwrite restorer` and `sigaction`).

## Slide 95

###### **Signal Restorer Hijacking**

- We can control the _restorer_ after the signal handler

Three diagrams:

Left, the shadow stack: **ssp** points at a red row, **restorer**, above a row split into a red **1** cell and **SSP**, above a row **last return address**. A white loop connects the **SSP** cell around to the right and back into **last return address**.

Middle, the regular stack: **rsp** points at a red row, **restorer**, above a plain **Sigframe** block, above a plain "…" row pointed at by **rbp**.

Right, the Userspace/Kernel flow:

```text
mov r8, 0x0
mov r9, [r8]
```

A **SIGSEGV** banner arrows from that code, across the divider, into a kernel box _Prepare sigframe_, which arrows back into **signal handler**, then down into a red box, **arbitrary restorer**. A **sigreturn** banner arrows from **arbitrary restorer** into kernel boxes _Restore state_ and _Restore SSP_.

## Slide 96

###### **Not Enough**

- Controlling the restorer is just one function call

   - The signal handler clobbers any useful register values

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

**USEFUL**
Signal handler with rdi, rsi, rdx controlled

A red arrow points down.

**USELESS**
Restorer without any registers controlled

Shadow Stack triggers SIGSEGV after the restorer returns

## Slide 103

###### **Not Enough**

**USEFUL**
Signal handler with rdi, rsi, rdx controlled

**USELESS**
Restorer without any registers controlled

A red arrow points down.

**CRASH**
Shadow Stack triggers SIGSEGV after the restorer returns

A red X mark.

## Slide 104

###### **The Way Forward**

**USEFUL** Signal handler with rdi, rsi, rdx controlled

**USEFUL** Restorer without any registers controlled

**CRASH** Shadow Stack triggers SIGSEGV after the restorer returns

## Slide 105

###### **The Way Forward**

**USEFUL**
Signal handler with rdi, rsi, rdx controlled

**USEFUL**
Restorer without any registers controlled

A red arrow points down.

**OK**
Shadow Stack triggers SIGSEGV after the restorer returns

## Slide 106

###### **The Way Forward**

**USEFUL**
Signal handler with rdi, rsi, rdx controlled

**USEFUL**
Restorer without any registers controlled

**OK**
Shadow Stack triggers SIGSEGV after the restorer returns

A long red arrow runs up the left margin from **OK** back to the first **USEFUL**.

## Slide 107

###### **Shadow Stack Injection**

But how do we get the Shadow Stack not to crash?

Easy: We inject values onto it

Meme image, bottom right: Mr. Burns (The Simpsons) being injected with a syringe labelled "MEMES".

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

Stack diagram: **ssp** points at a red row, **custom restorer**, above a row split into a red **1** cell and **SSP**, above a row, **last return address**. A white loop connects the **SSP** cell around to the right and back into **last return address**.

## Slide 111

###### **Shadow Stack Injection**

We can _confuse_ the shadow stack if:

1. Push a restorer with MSB=1

_libc sigaction_

```text
endbr64
...
overwrite restorer
...
sigaction
...
ret
```

A red arrow points at the `overwrite restorer` line, which is highlighted red.

## Slide 112

###### **Shadow Stack Injection**

We can _confuse_ the shadow stack if:

1. Push a restorer with MSB=1

Three diagrams:

Left, the shadow stack: **ssp** points at a row split into a red **1** cell and **restorer**, above a row split into a red **1** cell and **SSP**, above a row, **last return address**. A white loop connects the **SSP** cell around to the right and back into **last return address**.

Middle, the regular stack: **rsp** points at a plain row, **restorer**, above a plain **Sigframe** block, above a plain "…" row pointed at by **rbp**.

Right, the Userspace/Kernel flow:

```text
mov r8, 0x0
mov r9, [r8]
```

A **SIGSEGV** banner arrows from that code, across the divider, into a kernel box _Prepare sigframe_, which arrows back into **signal handler**.

## Slide 113

###### **Shadow Stack Injection**

We can _confuse_ the shadow stack if:

2. We manage to interpret the restorer as a saved SSP

   - Moves the SSP to an arbitrary location

Three diagrams:

Far left, a new red box, **ARBITRARY MEMORY**, now pointed at by **ssp**.

Left, the shadow stack (unchanged): a row split into a red **1** cell and **restorer**, above a row split into a red **1** cell and **SSP**, above a row, **last return address**. A white loop connects the **SSP** cell around to the right and back into **last return address**.

Middle, the regular stack: **rsp** points at a plain row, **restorer**, above a plain **Sigframe** block, above a plain "…" row pointed at by **rbp**.

Right, the Userspace/Kernel flow:

```text
mov r8, 0x0
mov r9, [r8]
```

A **SIGSEGV** banner arrows from that code, across the divider, into a kernel box _Prepare sigframe_, which arrows back into **signal handler**, then down into **restorer**. A red **sigreturn** banner arrows from **restorer** into kernel boxes _Restore state_ and _Restore SSP_.

## Slide 114

###### **Shadow Stack Injection**

We tricked the Shadow Stack into accepting a random ROP chain

Three diagrams:

Left, the shadow stack, now four red rows: **ssp** points at **ROP Gadget 1**, then **ROP Gadget 2**, then "…", then **ROP Gadget N**.

Middle, the regular stack: **rsp** points at a plain row, **restorer**, above a plain **Sigframe** block, above a plain "…" row pointed at by **rbp**.

Right, the Userspace/Kernel flow:

```text
mov r8, 0x0
mov r9, [r8]
```

A **SIGSEGV** banner arrows from that code, across the divider, into a kernel box _Prepare sigframe_, which arrows back into **signal handler**, then down into **restorer**. A **sigreturn** banner arrows from **restorer** into kernel boxes _Restore state_ and _Restore SSP_.

## Slide 115

###### **Shadow Stack Injection**

###### It is _still_ complicated

- If the SSP points outside the shadow stack → SIGSEGV

Same three diagrams as before. Left, the ROP-gadget shadow stack is now dimmed/outlined in red (de-emphasized): **ssp** → **ROP Gadget 1**, **ROP Gadget 2**, "…", **ROP Gadget N**.

## Slide 116

###### **Shadow Stack Injection**

It is _still_ complicated

- If the SSP points outside the shadow stack → SIGSEGV

- Before interpreting the SSP, we must return to the restorer

Same three diagrams. Left, the ROP-gadget shadow stack is plain again. Right, the **signal handler** / **restorer** boxes are now outlined in red for emphasis.

## Slide 117

###### **Shadow Stack Injection**

It is _still_ complicated

- If the SSP points outside the shadow stack → SIGSEGV

- How to interpret a restorer as a saved SSP?

Same three diagrams as slide 113: **ARBITRARY MEMORY** (red, pointed at by ssp), the shadow stack (1|restorer, 1|SSP with loop to last return address), the regular stack (rsp→restorer/Sigframe, rbp→"…"), and the Userspace/Kernel flow ending in a red sigreturn arrow into Restore state and Restore SSP.

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

Meme image overlaid across the middle of the slide, partly covering the bullets: Dave Chappelle captioned "Modern problems require modern solutions".

## Slide 120

###### **Recursive Shadow Stack**

- A recursive shadow stack tricks CET to validate sigreturn forever

Memory layout, offsets down the left:

- 0x0: __restore_rt (plain)
- 0x10: a row split into a red **1** cell and **0x20**
- 0x20: a row split into a red **1** cell and **0x0**

Two white arrows on the right: one from the **0x20** value (row 0x10) looping down into the row at offset 0x20; another from the **0x0** value (row 0x20) looping further out and up into the **__restore_rt** row at offset 0x0.

## Slide 121

###### **bSFOP: Early Kill**

- The signal handler starts right after the restorer is overwritten

_libc sigaction_

```text
...
sigaction
...
mov [r8], rax
...
ret
```

**rip** points at `mov [r8], rax`, annotated: **SIGSEGV handler = sigaction**. A red arrow leads from there into a new box, **handler: sigaction**:

```text
endbr64
...
overwrite restorer
...
sigaction syscall
...
leave
ret
```

## Slide 122

**bSFOP: Shadow Stack Grooming**

Next signal handler: sigskip
Next restorer: __restore_rt

Three diagrams:

Left, the shadow stack: **ssp** points at a row, **__restore_rt**, above a row split into a red **1** cell and **SSP**, above a row, **last return address**. A white loop connects the **SSP** cell around to the right and back into **last return address**.

Middle, _handler: sigskip_, **rip** points at `sigaction` (red):

```text
...
sigaction
...
leave
ret
```

A white arrow leads down into a new box, **sigreturn**.

Right, the regular stack: **rsp** points at **__restore_rt**, above a plain **Sigframe** block (labelled **Written by the kernel**), above a plain "…" row pointed at by **rbp**, above **Corrupted memory**: **rbp value**, **__restore_rt**, **FAKE SIGFRAME**.

## Slide 123

**bSFOP: Shadow Stack Grooming**

Next signal handler: sigskip
Next restorer: recursive | MSB=1

Three diagrams, same as before. Middle: **rip** now points at `leave` (red) in _handler: sigskip_. Right: unchanged (rsp → __restore_rt / Sigframe / Written by the kernel, rbp → "…" / Corrupted memory: rbp value, __restore_rt, FAKE SIGFRAME).

## Slide 124

**bSFOP: Shadow Stack Grooming**

Next signal handler: sigskip
Next restorer: recursive | MSB=1

Three diagrams. Middle: **rip** now points at **sigreturn** (red). Right: **rsp** and **rbp** now both point together at **FAKE SIGFRAME**, now highlighted red (skipping past the plain "…" row); above it, unchanged: rbp value, __restore_rt, and above that __restore_rt / Sigframe (Written by the kernel).

## Slide 125

**bSFOP: Shadow Stack Grooming**

Next signal handler: sigskip
Next restorer: recursive | MSB=1

Three diagrams. Middle: below **sigreturn**, a new red-outlined box, **__restore_rt**, now pointed at by **rip**. Right: **rsp** and **rbp** now point at a new separate red box, **Fake Sigframe 2**, to the right of the original stack (which still shows __restore_rt / Sigframe / Written by the kernel, "…", and Corrupted memory: rbp value, __restore_rt, FAKE SIGFRAME).

## Slide 126

**bSFOP: Shadow Stack Grooming**

Next signal handler: sigskip
Next restorer: recursive | MSB=1

Left, the shadow stack: a dimmed gray region above the existing rows; **ssp** points at **recursive** (red **1** cell), above **SSP** (red **1** cell), above **last return address**.

Middle, _handler: sigskip_ (rip at `leave`, red); below it a white arrow into **sigreturn**, then a further arrow into a box **__restore_rt**, then into a dotted-outline **Kernel** box containing **Restore state** → **Restore SSP** and a red **SIGSEGV** box. A thick red arrow leads from **SIGSEGV** back up into `sigaction` inside _handler: sigskip_.

Right: **rsp** and **rbp** point at a separate red box, **Fake Sigframe**, to the right of the original stack (__restore_rt / Sigframe / Written by the kernel, "…", Corrupted memory: rbp value, __restore_rt, FAKE SIGFRAME).

## Slide 127

**bSFOP: Shadow Stack Grooming**

Next signal handler: sigskip
Next restorer: recursive | MSB=1

Left, the shadow stack: the dimmed gray region, **ssp** at **recursive** (red **1** cell), above **SSP** (red **1** cell) with a black loop arrow to **last return address**.

Middle, _handler: sigskip_, **rip** at `sigaction` (red); white arrow down into a new box, **recursive**.

Right: **rsp** and **rbp** point together at **__restore_rt** / **Sigframe** (Written by the kernel), above "…", above Corrupted memory: rbp value, __restore_rt, FAKE SIGFRAME.

## Slide 128

**bSFOP: Shadow Stack Grooming**

Next signal handler: leave;ret
Next restorer: __restore_rt

Left, the shadow stack: the dimmed gray region, **ssp** at **recursive** (red **1** cell), above **SSP** (red **1** cell) with a black loop arrow to **last return address**.

Middle, _handler: sigskip_, **rip** now at `leave` (red); white arrow down into a box, **recursive**.

Right: **rsp** and **rbp** point together at **__restore_rt** / **Sigframe** (Written by the kernel), above "…", above Corrupted memory: rbp value, __restore_rt, FAKE SIGFRAME.

## Slide 129

**bSFOP: Shadow Stack Grooming**

Next signal handler: leave;ret
Next restorer: __restore_rt

Left, the shadow stack, now five rows: **__restore_rt** (red) — **ssp** points here — then **SSP** (red **1** cell), **recursive** (**1** cell), **SSP** (**1** cell), **last return address**.

Middle, _handler: sigskip_; **rip** points at a box, **recursive**, now containing a red **SIGSEGV** label. A thick red arrow loops from there back up into `sigaction`.

Right: **rsp** and **rbp** point at **__restore_rt** inside Corrupted memory (above **FAKE SIGFRAME**, below **rbp value**), below the standard __restore_rt / Sigframe (Written by the kernel) / "…" stack.

## Slide 130

**bSFOP: Shadow Stack Grooming**

Next signal handler: leave;ret
Next restorer: __restore_rt

Left, the shadow stack: **ssp** points at **__restore_rt** (red), above **SSP** (red **1** cell), above **recursive** (red **1** cell); below that, grayed out: **SSP** (**1** cell) and **last return address**.

Middle, now relabelled _handler: sigaction_; **rip** points at `leave` (red), above `ret`. A white arrow leads down into **sigreturn**.

Right: **rsp** points at **__restore_rt** (top), **rbp** points at "…", above Corrupted memory: rbp value, __restore_rt, FAKE SIGFRAME.

## Slide 131

**bSFOP: Shadow Stack Grooming**

Next signal handler: leave;ret
Next restorer: __restore_rt

Left, the shadow stack: **ssp** points at **__restore_rt** (white), above **SSP** (red **1** cell), above **recursive** (**1** cell); below that, a plain gray region with no labels.

Middle, _handler: sigaction_: `leave` / `ret`, white arrow down into **sigreturn**, now pointed at by **rip** (red).

Right: **rsp** and **rbp** point together at **__restore_rt** inside Corrupted memory (above **FAKE SIGFRAME**, below **rbp value**), below the standard __restore_rt / Sigframe (Written by the kernel) / "…" stack.

## Slide 132

**bSFOP: Shadow Stack Grooming**

Next signal handler: leave;ret
Next restorer: __restore_rt

Left, the shadow stack, unchanged from the previous slide.

Middle, _handler: sigaction_: `leave` / `ret`, white arrow down into **sigreturn**, then down into a new box, **__restore_rt** (red).

Right: **rsp** and **rbp** point together at a new box, **Fake Sigframe 2**.

## Slide 133

**bSFOP: Shadow Stack Grooming**

Next signal handler: leave;ret
Next restorer: __restore_rt

Left, the shadow stack, unchanged.

Middle, _handler: sigaction_: `leave` / `ret` → **sigreturn** → **__restore_rt** → **rip** now points at a new red box, **Arbitrary call 1 = system()**.

Right: **rsp** points at **Fake Sigframe 2**, containing a red **__restore_rt** pill; **rbp** points at a new box below it, **Fake Sigframe 3**.

## Slide 134

**bSFOP: Shadow Stack Grooming**

Next signal handler: leave;ret
Next restorer: __restore_rt

Left, the shadow stack, unchanged.

Middle, _handler: sigaction_: `leave` / `ret` → **sigreturn** → **rip** points at a red box, **__restore_rt**.

Right: **rsp** points at a red-outlined **__restore_rt** pill inside **Fake Sigframe 2**; **rbp** points at **Fake Sigframe 3**, now highlighted red.

## Slide 135

**bSFOP: Shadow Stack Grooming**

Next signal handler: leave;ret
Next restorer: __restore_rt

Left, the shadow stack, unchanged.

Middle, _handler: sigaction_: `leave` / `ret` → **sigreturn** → **rip** points at **__restore_rt**.

Right, stacked top to bottom: **Fake Sigframe 2**, **__restore_rt** pill, **Fake Sigframe 3**; **rsp** and **rbp** point at a new box below, **Fake Sigframe 4** (red).

## Slide 136

**bSFOP: Shadow Stack Grooming**

Next signal handler: leave;ret
Next restorer: __restore_rt

No shadow-stack diagram on this slide.

Middle, _handler: sigaction_: `leave` / `ret` → **sigreturn** → **__restore_rt** → **rip** points at a new red box, **Arbitrary call 2 = execve()**.

Right: **rsp** points at a red **__restore_rt** pill; **rbp** points at **Fake Sigframe 5** below it.

## Slide 137

**bSFOP: Shadow Stack Grooming**

Next signal handler: leave;ret
Next restorer: __restore_rt

Left, the shadow stack, unchanged.

Middle, _handler: sigaction_: `leave` / `ret` → **sigreturn** → **rip** points at **__restore_rt**.

Right: **rsp** points at a **__restore_rt** pill; **rbp** points at **Fake Sigframe 5** (red) below it.

## Slide 138

**4**

### **Patching SFOP**

Four progress dots beneath a red rule, all four filled red.

## Slide 139

###### **Patching SFOP**

**bSFOP**

- We have coordinated a patch with the Linux kernel developers to patch the bSFOP attack

- Prevents restorer and SSP hijacking

- **Fully patches** bSFOP

**fSFOP**

- Patching fSFOP requires enforcing IBT on user-kernel transitions, which is _hard_

- We patch some weaknesses that make fSFOP easier

- fSFOP partially mitigated

## Slide 140

### **https://github.com/signal-sfop/sfop**

Marcos Bajo _h3xduck_

Ritvik Goyal _RoYalGamr_

Apostolos Chatzianagnostou

Christian Rossow

Top right: three "ARTIFACT EVALUATED — IEEE S&P" badges (each with a horse-head logo), labelled **AVAILABLE** (green), **FUNCTIONAL** (blue), **REPRODUCED** (purple).

Bottom right: a QR code with the CISPA Helmholtz Center for Information Security logo at its center.

