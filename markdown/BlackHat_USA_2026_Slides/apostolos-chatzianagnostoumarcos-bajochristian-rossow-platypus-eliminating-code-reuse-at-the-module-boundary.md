---
title: "PLaTypus Eliminating Code-Reuse at the Module Boundary"
speakers: ["Apostolos Chatzianagnostou", "Marcos Bajo", "Christian Rossow"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Apostolos Chatzianagnostou&Marcos Bajo&Christian Rossow_PLaTypus Eliminating Code-Reuse at the Module Boundary.pdf"
pages: 130
sha256: "7f4af7214730e9fcbe6d2ee9f1160004faa72df9eade78dde856d9b7120ab8e8"
text_chars: 33251
ocr_pages: 19
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.7
ocr_unreliable_blocks: 0
vision_verified_pages_changed: 130
vision_verified_pages: 130
vision_verified_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:28:22Z"
---
# PLaTypus Eliminating Code-Reuse at the Module Boundary

**Speakers:** Apostolos Chatzianagnostou, Marcos Bajo, Christian Rossow  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Apostolos Chatzianagnostou&Marcos Bajo&Christian Rossow_PLaTypus Eliminating Code-Reuse at the Module Boundary.pdf` (130 pages)


## Slide 1

This slide carries no title or text of its own.

## Slide 2

# PLaTypus: Killing Code-Reuse at the Module Boundary

Speaker: Apostolos Chatzianagnostou

Collaborators: Marcos Bajo, Christian Rossow

## Slide 3

## Memory War: Chronicles

Ret2libc (1997)

• _And so it begins..._

main:
call  f()
...
f:
...
ret

## Slide 4

## Memory War: Chronicles

Ret2libc (1997)

• _And so it begins..._

main:
call  f()
...
system:
f:
...
ret

## Slide 5

## Memory War: Chronicles

- Ret2libc (1997)
  - _And so it begins..._
- ROP (2007)
- JOP (2011)
- SROP (2014)

```
main:
    call  f()
    ...

system:

f:
    ...
    ret
```

## Slide 6

## Memory War: Chronicles

Stack canaries (~2000)

ASLR (2003)

DEP/NX (2004)

## Slide 7

## Memory War: Chronicles

- Stack canaries (~2000)
- ASLR (2003)
- DEP/NX (2004)
- Control Flow Integrity (2005)
  - Control Flow Guard (2014)
  - LLVM CFI (2015)
  - Intel CET (2020)

Powerful in theory, hard to enforce…

## Slide 8

## Memory War: Chronicles

COOP (2015)

FOP (2018)

CFOP (2024)

SFOP (2026)

## Slide 9

## Memory War: Chronicles

- COOP (2015)
- FOP (2018)
- CFOP (2024)
- SFOP (2026)

Code-reuse attacks still an issue…

## Slide 10

## Memory War: Chronicles

- COOP (2015)
- FOP (2018)
- CFOP (2024)
- SFOP (2026)

Code-reuse attacks still an issue…

But they all share one thing:

Cross-module transitions!

## Slide 11

## Who We Are

#### **Apostolos Chatzianagnostou** apostolos.chatzianagnostou@cispa.de

- PhD student at CISPA

#### **Marcos Bajo** aka **_h3xduck_** h3xduck@gmail.com

- PhD student at CISPA

- _<u>https://h3xduck.github.io</u>_

#### **Christian Rossow**

rossow@cispa.de

- Faculty at CISPA

- CS Professor at TU Dortmund

- Leader of the _Systems Security Group_

We build, break, and explore. Reach out!

## Slide 12

## Agenda

1. Userspace CFI and debloating approaches
2. Motivation and goals of PLaTypus
3. Design, methodology and challenges
4. Evaluation and discussion

## Slide 13

# BACKGROUND

## Slide 14

## Control Flow Integrity (CFI)

- Creation (statically) of Control Flow Graph (CFG)
  - Which indirect transitions are expected/benign?
- Enforcement of CFG through code instrumentation
- Code-reuse: solved
  - Well…

CFG diagram: nodes f(), g(), h(), i(), j(), and a malicious execve() 👿 (magenta box); the attempted transition from i() to execve() is blocked (❌).

## Slide 15

## CFI Taxonomy

Based on the protected edges:

### 1. Backward-edge CFI

```
main:
    void (*func)() = &f;
    func();
    …

f:
    …
    ret
```

### 2. Forward-edge CFI

```
main:
    void (*func)() = &f;
    func();
    …

f:
    …
    ret

g:
    …
```

## Slide 16

## CFI Taxonomy

Based on security:

**Coarse-grained**

**Fine-grained**

Weaker Security

Stronger Security

## Slide 17

## CFI Taxonomy

Based on security:

**Coarse-grained**   **Fine-grained**

Weaker Security   Stronger Security

Better Performance   Worse Performance

## Slide 18

## CFI Limitations

- Accurate CFG construction is hard
  - Static analysis limitations → Overapproximation
- Incomplete, leaving pointers unprotected
  - Example: C++ coroutines
- Protected/unprotected interop is hard
  - Needed for third-party libraries/modules

Fine-grained CFI: limited deployment

## Slide 19

## CFI Limitations

- Accurate CFG construction is hard
  - Static analysis limitations → Overapproximation
- Incomplete, leaving pointers unprotected
  - Example: C++ coroutines
- Protected/unprotected interop is hard
  - Needed for third-party libraries/modules

Fine-grained CFI: limited deployment

#### Deployed schemes in practice:

- Intel CET (coarse-grained)
- ARM BTI (coarse-grained)
- Control Flow Guard (coarse-grained)
- LLVM CFI (fine(r)-grained)

## Slide 20

## Intel CET

- Hardware-enforced CFI

- Two main components:

1.  Shadow Stack for backward edges

2.  Indirect Branch Tracking (IBT) for forward edges

- Supported on Intel 11<sup>th</sup> Gen and later

- Available on both Windows and Linux

## Slide 21

## Intel CET – Shadow Stacks

**Regular Stack**

- t() return address
- g() return address
- f() return address
- h() return address

**Shadow Stack**

- t() return address
- g() return address
- f() return address
- h() return address

## Slide 22

## Intel CET – Shadow Stacks

**Regular Stack**

- t() return address
- g() return address
- f() return address
- h() return address

match ✓

**Shadow Stack**

- t() return address
- g() return address
- f() return address
- h() return address

## Slide 23

## Intel CET – Shadow Stacks

**Regular Stack**

- execve()
- g() return address
- f() return address
- h() return address

mismatch (❌) → SIGSEGV

**Shadow Stack**

- t() return address
- g() return address
- f() return address
- h() return address

## Slide 24

## Intel CET – Shadow Stacks

**Regular Stack**

- execve()
- g() return address
- f() return address
- h() return address

**ROP mitigated**

**Shadow Stack**

- t() return address
- g() return address
- f() return address
- h() return address

## Slide 25

## Intel CET – IBT

g():

```
mov    rdi, Qword Ptr[rax]
lea    rsi, [rip+0xdd3]
xor    rdx, rdx
call   rcx
mov    rcx, rax
pop    rbp
jmp    rbx
```

f():

```
endbr64
push   rbp
mov    rbp, rsp
sub    rsp, 0x20
mov    rcx, rax
…
```

- call rcx → endbr64 (function entry): allowed ✓
- jmp rbx → middle of f() (push rbp / mov rbp, rsp / sub rsp, 0x20 / mov rcx, rax): blocked ❌

## Slide 26

## ARM BTI

- Protects forward edges

- Similar to Intel’s IBT but in ARM hardware

- Can differentiate between _call targets_ and _jump targets_

- Available on Apple, Android, Linux and Windows systems

## Slide 27

## Control Flow Guard

- Protects forward edges

- Microsoft’s implementation of Intel IBT

- Software-enforced

- A bitmap marks valid indirect call/jump targets

## Slide 28

## LLVM CFI

- Type-based CFI
- Software-enforced
- Applicable also to virtual calls in C++

```
void (*func_ptr)(void)= &funcA;
func_ptr();
```

```
void funcA(void)
int  funcB(const char* s)
void funcC(char* t)
int  funcD(long)
```

func_ptr() (type void(void)) → funcA(void): allowed; funcB / funcC / funcD: blocked ❌ (type mismatch).

## Slide 29

## LLVM CFI

- Supports modularity (_cross-DSO_ mode)
- Transitions to uninstrumented libraries are allowed
- Cannot compile glibc

```
void (*func_ptr)(void)= &funcA;
func_ptr();
```

```
void funcA(void)
int  system(const char* s)
void funcC(char* t)
int  funcD(long)
```

func_ptr() → funcA(void) and system(const char* s): allowed; funcC / funcD: blocked ❌.

## Slide 30

## Debloating

- Remove code that is not needed
  - E.g., dead code
- Available gadgets are reduced
  - Attack surface shrinks
- Especially useful in libraries
  - Plethora of gadgets and unused code

```
main:
    call  f()
    ...

f:
    ...
    ret

unused_func:
    ...
```

## Slide 31

## Debloating

- Remove code that is not needed
  - E.g., dead code
- Available gadgets are reduced
  - Attack surface shrinks
- Especially useful in libraries
  - Plethora of gadgets and unused code

```
main:
    call  f()
    ...

f:
    ...
    ret

unused_func:
    ...
```

unused_func is crossed out (❌) — removed by debloating.

## Slide 32

## Library Debloaters

- Nibbler: debloats libraries per _set of binaries_ . Inserting new ones?

- Piece-Wise compilation: modifies library pages _per application_ at load time

- BlankIt: copies library code at runtime to enable/disable functions

## Slide 33

## Library Debloaters

- Nibbler: debloats libraries per _set of binaries_. Inserting new ones? → Need for recompilation
- Piece-Wise compilation: modifies library pages _per application_ at load time → COW - Sharing property undermined
- BlankIt: copies library code at runtime to enable/disable functions → COW - Sharing property undermined

## Slide 34

## Library Debloaters

- Nibbler: debloats libraries per _set of binaries_. Inserting new ones? → Need for recompilation
- Piece-Wise compilation: modifies library pages _per application_ at load time → COW - Sharing property undermined
- BlankIt: copies library code at runtime to enable/disable functions → COW - Sharing property undermined

**Not practical for general-purpose systems**

## Slide 35

## Where we stand

- Fine(r)-grained CFI schemes not yet mature enough for widespread adoption

- Debloating not practical: unused library/module code remains exposed in applications

## Slide 36

## Where we stand

• Fine(r)-grained CFI schemes not yet mature enough for widespread adoption

• Debloating not practical: unused library/module code remains exposed in applications

• Intel CET is the current and foreseeable main line of defense on x86

Is this that bad though?

## Slide 37

# MOTIVATION

## Slide 38

## CET Limitation

- Arbitrary cross-Dynamic Shared Objects (DSO) / cross-module indirect transitions are allowed
  - Leveraged by nearly every attack
  - Libraries are rich in gadgets (e.g., syscalls, sensitive functions)

Development of specialized attacks

Diagram: Main Binary (call rax) → Libc functions puts, system, execve (each an attacker-controlled 👿 indirect call).

## Slide 39

## Function-Oriented Programming (FOP)

### Class of attacks:

- Evading schemes like CET/BTI

- Entire functions as gadgets

## Slide 40

## Function-Oriented Programming (FOP)

Class of attacks:

- Evading schemes like CET/BTI
- Entire functions as gadgets

Documented attacks:

- Loop-Oriented Programming (2015)
- FOP (2018)
- Phrack’s FOP (2024)

## Slide 41

## Function-Oriented Programming (FOP)

Class of attacks:

- Evading schemes like CET/BTI
- Entire functions as gadgets
  - How do they control arguments?

Documented attacks:

- Loop-Oriented Programming (2015)
- FOP (2018)
- Phrack's FOP (2024)

## Slide 42

## Dispatcher Gadget

- Orchestrator for FOP attacks
- Calls subsequent gadgets in a loop
  - Retrieved from attacker-controlled memory
- Conservative register usage between loops

Dispatcher Gadget

**Attacker-controlled**

- gadget 1
- gadget 2
- gadget 3

## Slide 43

## Dispatcher Gadget

- Orchestrator for FOP attacks
- Calls subsequent gadgets in a loop
  - Retrieved from attacker-controlled memory
- Conservative register usage between loops

Dispatcher Gadget

**Attacker-controlled**

- gadget 1
- gadget 2
- gadget 3

## Slide 44

## Dispatcher Gadget

- Orchestrator for FOP attacks
- Calls subsequent gadgets in a loop
  - Retrieved from attacker-controlled memory
- Conservative register usage between loops

Dispatcher Gadget

**Attacker-controlled**

- gadget 1
- gadget 2
- gadget 3

## Slide 45

## Dispatcher Gadget

- Orchestrator for FOP attacks
- Calls subsequent gadgets in a loop
  - Retrieved from attacker-controlled memory
- Conservative register usage between loops

Dispatcher Gadget

**Attacker-controlled**

- gadget 1
- gadget 2
- gadget 3

**Normally cross-DSO transition**

## Slide 46

## Dispatcher Gadget

```
==Phrack Inc.==

Volume 0x10, Issue 0x47, Phile #0x07 of 0x11

|=-------------------------------------------------------------------=|
|=-----=[ Bypassing CET & BTI With Functional Oriented Programming ]=-----=|
|=-------------------------------------------------------------------=|
|=------------------------------=[ LMS ]=----------------------------=|
|=-------------------------------------------------------------------=|
```

```c
void
_dl_call_fini (void *closure_map)
{
  struct link_map *map = closure_map;

  /* Make sure nothing happens if we are called twice.  */
  map->l_init_called = 0;

  ElfW(Dyn) *fini_array = map->l_info[DT_FINI_ARRAY];
  if (fini_array != NULL)
    {
      ElfW(Addr) *array = (ElfW(Addr) *) (map->l_addr
                                          + fini_array->d_un.d_ptr);
      size_t sz = (map->l_info[DT_FINI_ARRAYSZ]->d_un.d_val
                   / sizeof (ElfW(Addr)));

      while (sz-- > 0)
        ((fini_t) array[sz]) ();
    }

  /* Next try the old-style destructor.  */
  ElfW(Dyn) *fini = map->l_info[DT_FINI];
  if (fini != NULL)
    DL_CALL_DT_FINI (map, ((void *) map->l_addr + fini->d_un.d_ptr));
}
```

_dispatcher loop_ (annotation on the boxed `while (sz-- > 0)` loop)

## Slide 47

## Dispatcher Gadget

- `_dl_call_fini`: part of glibc loader
- Called gadgets: part of libc

```
----|  11. Appendix B: Intel "/bin/sh" in memory chain

+---------------------------+--------------------------+
|       Function Name       |   Equivalent Operation   |
+---------------------------+--------------------------+
| _nss_files_endpwent       | MOV RDI, 0x6             |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| _dl_mcount_wrapper...     | MOV RSI, RDI             |
```

```c
void
_dl_call_fini (void *closure_map)
{
  struct link_map *map = closure_map;

  /* Make sure nothing happens if we are called twice.  */
  map->l_init_called = 0;

  ElfW(Dyn) *fini_array = map->l_info[DT_FINI_ARRAY];
  if (fini_array != NULL)
    {
      ElfW(Addr) *array = (ElfW(Addr) *) (map->l_addr
                                          + fini_array->d_un.d_ptr);
      size_t sz = (map->l_info[DT_FINI_ARRAYSZ]->d_un.d_val
                   / sizeof (ElfW(Addr)));

      while (sz-- > 0)
        ((fini_t) array[sz]) ();
    }

  /* Next try the old-style destructor.  */
  ElfW(Dyn) *fini = map->l_info[DT_FINI];
  if (fini != NULL)
    DL_CALL_DT_FINI (map, ((void *) map->l_addr + fini->d_un.d_ptr));
}
```

_dispatcher loop_ (annotation on the boxed `while (sz-- > 0)` loop)

## Slide 48

## Dispatcher Gadgets

- Rare and hard to find
- Most of them not exploitable
- Exploitable ones are related to initialization and finalization routines
  - LOOP attack: `_initterm()` in _msvcrt.dll_
  - Phrack attack: `_dl_call_fini()` in _ld-linux_

## Slide 49

## Dispatcher Gadgets

- Rare and hard to find
- Most of them not exploitable
- Exploitable ones are related to initialization and finalization routines
  - LOOP attack: `_initterm()` in _msvcrt.dll_
  - Phrack attack: `_dl_call_fini()` in _ld-linux_

We will revisit this later

## Slide 50

## How does Linux handle cross-DSO transitions?

## Slide 51

## Procedure Linkage Table (PLT)

- Code stubs dispatching cross-DSO calls in ELFs
- Efficient and robust
  - With Full RELRO mitigation

```
f():

    lea    rdi,[rip+0xd95]
    lea    rsi, [rip+0xdd3]
    call   puts@plt
    pop    rbp
    …
```

```
puts@plt:

    endbr64
    jmp    Qword Ptr[rip+0x2e6]
    nop
    …
```

(`call puts@plt` jumps into the `puts@plt` stub)

## Slide 52

## Motivation

**Why then should cross-DSO transfers be allowed outside of PLTs?**

Diagram:

- **Main Binary**: puts@PLT, malloc@PLT; `call rax`
- **Libc**: puts; system / execve / mprotect / …; malloc
- **DSO A**: malloc@PLT; `jmp rbx`

PLT paths are allowed (puts@PLT → puts, malloc@PLT → malloc). The direct `call rax` and `jmp rbx` transitions into libc's system/execve/mprotect are blocked (✗).

## Slide 53

## PLaTypus Goals

- Support both libraries and applications
  - Even complex ones like _glibc_ and _OpenSSL_
- Secure even when some DSOs remain uninstrumented
  - Third-party libraries
- Avoid library recompilation
- Retain the sharing property of libraries

## Slide 54

# DESIGN — METHODOLOGY - CHALLENGES

## Slide 55

## Threat Model

- Memory corruption vulnerabilities
  - Arbitrary reads/writes
- Function pointers can be overwritten
- Vulnerabilities can be triggered multiple times
- Intel CET in place
- Operating system enforces DEP
- Full RELRO is enabled

## Slide 56

## PLaTypus Design

- Each DSO can only reach external functions for which it possesses PLT stubs
- Per-DSO granularity of enforcement

Diagram:

- **Main Binary**: puts@PLT, malloc@PLT; `call rax`
- **Libc**: puts; system / execve / mprotect / …; malloc
- **DSO A**: malloc@PLT; `jmp rbx`

PLT paths are allowed (puts@PLT → puts, malloc@PLT → malloc); direct `call rax` and `jmp rbx` into libc's system/execve/mprotect are blocked (✗).

## Slide 57

## PLaTypus Design

- Each DSO can only reach external functions for which it possesses PLT stubs
- Per-DSO granularity of enforcement

Diagram:

- **Main Binary**: puts@PLT, malloc@PLT; `call rax`
- **Libc**: puts, malloc

`call rax` routes through the PLT stubs: puts@PLT → puts and malloc@PLT → malloc.

## Slide 58

## PLaTypus Design

- Each DSO can only reach external functions for which it possesses PLT stubs
- Per-DSO granularity of enforcement

Diagram:

- **Libc**: malloc
- **DSO A**: malloc@PLT; `jmp rbx`

`jmp rbx` routes through DSO A's malloc@PLT stub → malloc in Libc.

## Slide 59

## Terminology

- Intra-DSO transition: _caller_ and _callee_ in the same module
- Inter-DSO transition: _caller_ and _callee_ in different modules

## Slide 60

## Execution Jails (EJ)

- Each DSO is restricted in its EJ
  - Subset of DSO's address range

Diagram (memory layout):

- 28 bits (the low part of the address)
- `0x7fff20000000` — DSO A prefix is `0x7fff2`
- **DSO A Execution Jail:**
  - Other r-- / rw- mappings
  - r-x mappings
  - Other r-- / rw- mappings
  - (hatched region)
- `0x7fff3000000`
- **DSO B Execution Jail:**
  - Other r-- / rw- mappings
  - r-x mappings
  - Other r-- / rw- mappings
  - (hatched region)

## Slide 61

## Execution Jails (EJ)

- Each DSO is restricted in its EJ
  - Subset of DSO's address range
- DSO's indirect branches cannot escape the EJ
  - Exception? PLT stubs

Diagram (memory layout):

- 28 bits (the low part of the address)
- `0x7fff20000000` — DSO A prefix is `0x7fff2`
- **DSO A Execution Jail:**
  - Other r-- / rw- mappings
  - r-x mappings (highlighted)
  - Other r-- / rw- mappings
  - (hatched region)
- `0x7fff3000000`
- **DSO B Execution Jail:**
  - Other r-- / rw- mappings
  - r-x mappings (highlighted)
  - Other r-- / rw- mappings
  - (hatched region)

## Slide 62

## Execution Jails (EJ) - Enforcement

- Enforced with two bitmasks

```
; Original          ; Execution Jail

...                 or    rax, ormask
...                 and   rax, andmask
call rax            call  rax
```

Memory layout (right): `0x7fff20000000` — DSO A prefix `0x7fff2`, low 28 bits; **DSO A Execution Jail** (Other r-- / rw- mappings; r-x mappings [highlighted]; Other r-- / rw- mappings; hatched region). `0x7fff3000000` — **DSO B Execution Jail** (same structure).

## Slide 63

## Execution Jails (EJ) - Enforcement

- Enforced with two bitmasks

```
; Original          ; Execution Jail

...                 or    rax, ormask
...                 and   rax, andmask
call rax            call  rax
```

(`ormask` is highlighted; a white arrow points to DSO A's r-x mappings.)

Memory layout (right): `0x7fff20000000` — DSO A prefix `0x7fff2`, low 28 bits; **DSO A Execution Jail** (Other r-- / rw- mappings; r-x mappings [highlighted]; Other r-- / rw- mappings; hatched region). `0x7fff3000000` — **DSO B Execution Jail** (same structure).

## Slide 64

## Execution Jails (EJ) - Enforcement

- Enforced with two bitmasks

```
; Original          ; Execution Jail

...                 or    rax, ormask
...                 and   rax, andmask
call rax            call  rax
```

(`andmask` is highlighted; a white arrow points to DSO A's r-x mappings.)

Memory layout (right): `0x7fff20000000` — DSO A prefix `0x7fff2`, low 28 bits; **DSO A Execution Jail** (Other r-- / rw- mappings; r-x mappings [highlighted]; Other r-- / rw- mappings; hatched region). `0x7fff3000000` — **DSO B Execution Jail** (same structure).

## Slide 65

## Execution Jails (EJ)

- Enforced with two bitmasks

```
; Original          ; Execution Jail

...                 or    rax, ormask
...                 and   rax, andmask
call rax            call  rax
```

Relocation types:

```
R_X86_64_ORMASK
R_X86_64_ANDMASK
```

Memory layout (right): `0x7fff20000000` — DSO A prefix `0x7fff2`, low 28 bits; **DSO A Execution Jail** (Other r-- / rw- mappings; r-x mappings [highlighted]; Other r-- / rw- mappings; hatched region). `0x7fff3000000` — **DSO B Execution Jail** (same structure).

## Slide 66

## Execution Jails (EJ)

```
0x0000555555555dd1 <+81>:    mov    rcx,QWORD PTR [rip+0x12a0]        # 0x555555557078
0x0000555555555dd8 <+88>:    or     rax,rcx
0x0000555555555ddb <+91>:    mov    rcx,QWORD PTR [rip+0x129e]        # 0x555555557080
0x0000555555555de2 <+98>:    and    rax,rcx
0x0000555555555de5 <+101>:   call   rax
0x0000555555555de7 <+103>:   xor    eax,eax
```

## Slide 67

## Execution Jails (EJ)

Inter-DSO transitions are transformed to intra-DSO

## Slide 68

## Non-PLT Relocations

- Not all imports go through the PLT…

## Slide 69

## Non-PLT Relocations

- Not all imports go through the PLT…
  - _Address-taken_ symbols

```c
int main(void) {

    int (*fp)(const char *) = &puts;

    fp("hello");
}
```

Compiled with `-O0`, this yields the relocation:

```
R_X86_64_GLOB_DAT   puts@GLIBC_2.2.5 + 0
```

## Slide 70

## Non-PLT Relocations

```
Dump of assembler code for function main:
   0x0000555555555130 <+0>:     push   rbp
   0x0000555555555131 <+1>:     mov    rbp,rsp
   0x0000555555555134 <+4>:     sub    rsp,0x10
   0x0000555555555138 <+8>:     mov    DWORD PTR [rbp-0x4],0x0
   0x000055555555513f <+15>:    mov    rax,QWORD PTR [rip+0x2e82]        # 0x555555557fc8
   0x0000555555555146 <+22>:    mov    QWORD PTR [rbp-0x10],rax
   0x000055555555514a <+26>:    lea    rdi,[rip+0xeb3]                   # 0x555555556004
   0x0000555555555151 <+33>:    call   QWORD PTR [rbp-0x10]
   0x0000555555555154 <+36>:    xor    eax,eax
   0x0000555555555156 <+38>:    add    rsp,0x10
   0x000055555555515a <+42>:    pop    rbp
   0x000055555555515b <+43>:    ret
```

## Slide 71

## Non-PLT Relocations

```
Dump of assembler code for function main:
   0x0000555555555130 <+0>:     push   rbp
   0x0000555555555131 <+1>:     mov    rbp,rsp
   0x0000555555555134 <+4>:     sub    rsp,0x10
   0x0000555555555138 <+8>:     mov    DWORD PTR [rbp-0x4],0x0
   0x000055555555513f <+15>:    mov    rax,QWORD PTR [rip+0x2e82]        # 0x555555557fc8
   0x0000555555555146 <+22>:    mov    QWORD PTR [rbp-0x10],rax
   0x000055555555514a <+26>:    lea    rdi,[rip+0xeb3]                   # 0x555555556004
   0x0000555555555151 <+33>:    call   QWORD PTR [rbp-0x10]
   0x0000555555555154 <+36>:    xor    eax,eax
   0x0000555555555156 <+38>:    add    rsp,0x10
   0x000055555555515a <+42>:    pop    rbp
   0x000055555555515b <+43>:    ret
```

(The boxed instructions `<+15>`–`<+33>` are highlighted, with an arrow pointing to them.)

Instrumentation here would corrupt the cross-DSO pointer…

## Slide 72

## Fake PLTs

For such symbols:

1. Emit PLT stubs
   - New section: _.fakeplt.sec_
2. Redirect associated relocations to point to these stubs

## Slide 73

## Fake PLTs

For such symbols:

1. Emit PLT stubs
   - New section: _.fakeplt.sec_
2. Redirect associated relocations to point to these stubs

```c
int main(void) {

    int (*fp)(const char *) = &puts;

    fp("hello");
}
```

```
puts@plt:

0x1860:    endbr64
           jmp    Qword Ptr[rip+0x2e6]
           nop
```

## Slide 74

## Fake PLTs

For such symbols:

1. Emit PLT stubs
   - New section: _.fakeplt.sec_
2. Redirect associated relocations to point to these stubs

```c
int main(void) {

    int (*fp)(const char *) = &puts;

    fp("hello");
}
```

Relocations:

```
Type                Symbol's Value
R_X86_64_RELATIVE   1860
```

```
puts@plt:

0x1860:    endbr64
           jmp    Qword Ptr[rip+0x2e6]
           nop
```

## Slide 75

## Fake PLTs

For such symbols:

1. Emit PLT stubs
   - New section: _.fakeplt.sec_
2. Redirect associated relocations to point to these stubs

```c
int main(void) {

    int (*fp)(const char *) = &puts;

    fp("hello");
}
```

Relocations:

```
Type                Symbol's Value
R_X86_64_RELATIVE   1860
R_X86_64_JUMP_SLOT  puts@GLIBC_2.2.5 + 0
```

```
puts@plt:

0x1860:    endbr64
           jmp    Qword Ptr[rip+0x2e6]
           nop
```

## Slide 76

## Fake PLTs

```
0x55554554fbf0:    endbr64
0x55554554fbf4:    push   rbp
0x55554554fbf5:    mov    rbp,rsp
0x55554554fbf8:    sub    rsp,0x10
0x55554554fbfc:    mov    DWORD PTR [rbp-0x4],0x0
0x55554554fc03:    mov    rax,QWORD PTR [rip+0x12de]      # 0x555545550ee8
0x55554554fc0a:    mov    QWORD PTR [rbp-0x10],rax
0x55554554fc0e:    mov    rax,QWORD PTR [rbp-0x10]
0x55554554fc12:    mov    rcx,QWORD PTR [rip+0x12d7]      # 0x555545550ef0
0x55554554fc19:    or     rax,rcx
0x55554554fc1c:    mov    rcx,QWORD PTR [rip+0x12d5]      # 0x555545550ef8
0x55554554fc23:    and    rax,rcx
0x55554554fc26:    lea    rdi,[rip+0xffffffffffffedff]    # 0x55554554ea2c
0x55554554fc2d:    call   rax
0x55554554fc2f:    xor    eax,eax
0x55554554fc31:    add    rsp,0x10
0x55554554fc35:    pop    rbp
0x55554554fc36:    ret
```

## Slide 77

## Fake PLTs

```
0x55554554fbf0:    endbr64
0x55554554fbf4:    push   rbp
0x55554554fbf5:    mov    rbp,rsp
0x55554554fbf8:    sub    rsp,0x10
0x55554554fbfc:    mov    DWORD PTR [rbp-0x4],0x0
0x55554554fc03:    mov    rax,QWORD PTR [rip+0x12de]      # 0x555545550ee8
0x55554554fc0a:    mov    QWORD PTR [rbp-0x10],rax
0x55554554fc0e:    mov    rax,QWORD PTR [rbp-0x10]
0x55554554fc12:    mov    rcx,QWORD PTR [rip+0x12d7]      # 0x555545550ef0
0x55554554fc19:    or     rax,rcx
0x55554554fc1c:    mov    rcx,QWORD PTR [rip+0x12d5]      # 0x555545550ef8
0x55554554fc23:    and    rax,rcx
0x55554554fc26:    lea    rdi,[rip+0xffffffffffffedff]    # 0x55554554ea2c
0x55554554fc2d:    call   rax
0x55554554fc2f:    xor    eax,eax
0x55554554fc31:    add    rsp,0x10
0x55554554fc35:    pop    rbp
0x55554554fc36:    ret
```

```
gef➤  x/gx 0x555545550ee8
0x555545550ee8: 0x000055554554fcd0
```

## Slide 78

## Fake PLTs

```
0x55554554fbf0:    endbr64
0x55554554fbf4:    push   rbp
0x55554554fbf5:    mov    rbp,rsp
0x55554554fbf8:    sub    rsp,0x10
0x55554554fbfc:    mov    DWORD PTR [rbp-0x4],0x0
0x55554554fc03:    mov    rax,QWORD PTR [rip+0x12de]      # 0x555545550ee8
0x55554554fc0a:    mov    QWORD PTR [rbp-0x10],rax
0x55554554fc0e:    mov    rax,QWORD PTR [rbp-0x10]
0x55554554fc12:    mov    rcx,QWORD PTR [rip+0x12d7]      # 0x555545550ef0
0x55554554fc19:    or     rax,rcx
0x55554554fc1c:    mov    rcx,QWORD PTR [rip+0x12d5]      # 0x555545550ef8
0x55554554fc23:    and    rax,rcx
0x55554554fc26:    lea    rdi,[rip+0xffffffffffffedff]    # 0x55554554ea2c
0x55554554fc2d:    call   rax
0x55554554fc2f:    xor    eax,eax
0x55554554fc31:    add    rsp,0x10
0x55554554fc35:    pop    rbp
0x55554554fc36:    ret
```

```
gef➤  x/gx 0x555545550ee8
0x555545550ee8: 0x000055554554fcd0
```

```
gef➤  x/3i 0x000055554554fcd0
   0x55554554fcd0:      endbr64
   0x55554554fcd4:      jmp    QWORD PTR [rip+0x124e]        # 0x555545550f28
   0x55554554fcda:      nop    WORD PTR [rax+rax*1+0x0]
```

## Slide 79

## Fake vs Normal PLTs

- Normal PLTs are reached through **direct** calls
- Fake PLTs are reached through **indirect** calls

## Slide 80

## Fake vs Normal PLTs

- Normal PLTs are reached through **direct** calls
- Fake PLTs are reached through **indirect** calls

We can place Normal PLTs **outside** each DSO's Execution Jail

## Slide 81

## Final Design

Diagram (memory layout, top to bottom):

- 28 bits (the low part of the address)
- `0x7fff20000000` (DSO A prefix `0x7fff2`)
- **DSO A** (the top two rows form the DSO A Execution Jail):
  - Other r-- / rw- mappings
  - .fakeplt.sec / r-x mappings
  - Other r-- / rw- mappings
  - .plt / .plt.sec sections
  - (hatched region)
- `0x7fff30000000`
- `0x7fff32000000`
- **DSO B** (the top two rows form the DSO B Execution Jail):
  - Other r-- / rw- mappings
  - .fakeplt.sec / r-x mappings
  - Other r-- / rw- mappings
  - .plt / .plt.sec sections
  - (hatched region)
- `0x7fff37ffffff`

## Slide 82

## Quick Summary

Hijacked pointers can reach:

1. Intra-module functions
2. Only the Fake PLT stubs of the module

## Slide 83

## Quick Summary

Hijacked pointers can reach:

1. Intra-module functions
2. Only the Fake PLT stubs of the module

Possible cross-DSO targets

## Slide 84

## Tooling

LLVM toolchain (20.1.0)

- Modifications to the compiler and the linker
- Instrumentation through compiler passes

Glibc (2.41)

- Modifications to the loader

## Slide 85

## Challenges

- Callbacks

## Slide 86

## Challenges

- Callbacks
- Dynamically loaded modules (via _dlopen_)

## Slide 87

## Callbacks

**Module A**

```c
void f1() {

    ...
    qsort(arr,n,sizeof(int),compare)
    ...
}
```

```c
void compare(...) {

    ...
}
```

## Slide 88

## Callbacks

**Module A**

```c
void f1() {

    ...
    qsort(arr,n,sizeof(int),compare)
    ...
}
```

```c
void compare(...) {

    ...
}
```

**Libc**

```
qsort:

    ...
    or   rcx,ormask
    and  rcx,andmask
    call rcx
    ...
```

## Slide 89

## Callbacks

**Module A**

```c
void f1() {

    ...
    qsort(arr,n,sizeof(int),compare)
    ...
}
```

```c
void compare(...) {

    ...
}
```

**Libc**

```
qsort:

    ...
    or   rcx,ormask
    and  rcx,andmask
    call rcx
    ...
```

## Slide 90

## Callbacks

**Module A**

```c
void f1() {

    ...
    qsort(arr,n,sizeof(int),compare)
    ...
}
```

```c
void compare(...) {

    ...
}
```

**Libc**

```
qsort:

    ...
    or   rcx,ormask
    and  rcx,andmask
    call rcx
    ...
```

**Cannot escape the Execution Jail** (✗ — the masked `call rcx` cannot reach `compare` in Module A)

## Slide 91

## Handling Callbacks

1. Collect callback symbols (per module)
2. Instrument callback sites with extended masking
   - Places where callbacks are invoked

## Slide 92

## Symbol Gathering

- Leverage 2 compiler passes
  - Examining Intermediate Representation

```c
void f1() {
    ...
    qsort(arr,n,sizeof(int),compare1)
    qsort(arr,n,sizeof(int),compare2)
    ...
}
```

## Slide 93

## Symbol Gathering

- Leverage 2 compiler passes
  - Examining Intermediate Representation
- Create callback tables
  - One for each DSO dependency

```c
void f1() {
    ...
    qsort(arr,n,sizeof(int),compare1)
    qsort(arr,n,sizeof(int),compare2)
    ...
}
```

```
{
  “libc”: [compare1, compare2],
  “libcrypto”: [...],
  ...
}
```

## Slide 94

## Symbol Gathering

- Leverage 2 compiler passes
  - Examining Intermediate Representation
- Create callback tables
  - One for each DSO dependency

```c
void f1() {
    ...
    qsort(arr,n,sizeof(int),compare1)
    qsort(arr,n,sizeof(int),compare2)
    ...
}
```

```
{
  “libc”: [compare1, compare2],
  “libcrypto”: [...],
  ...
}
```

If the current module is used, then _libc_ may need to call _compare1_ and _compare2_

## Slide 95

## Extended Masking

- Instrument callback sites

```
; Original:
    call  rax

; Extended Masking:
    mov   r11,rax
    or    rax,ormask
    and   rax,andmask
    cmp   r11,rax
    jne   call_target
    call  rax
    jmp   after_call

call_target:
    call  DSO_callback_table

after_call:
    ...
```

## Slide 96

## Extended Masking

- Instrument callback sites

If not equal, then target **outside** the Execution Jail

```
; Original:
    call  rax

; Extended Masking:
    mov   r11,rax
    or    rax,ormask
    and   rax,andmask
    cmp   r11,rax
    jne   call_target
    call  rax
    jmp   after_call

call_target:
    call  DSO_callback_table

after_call:
    ...
```

## Slide 97

## Extended Masking

- Instrument callback sites

If not equal, then target **outside** the Execution Jail

Search target inside the callback table of the DSO

```
; Original:
    call  rax

; Extended Masking:
    mov   r11,rax
    or    rax,ormask
    and   rax,andmask
    cmp   r11,rax
    jne   call_target
    call  rax
    jmp   after_call

call_target:
    call  DSO_callback_table

after_call:
    ...
```

## Slide 98

## Extended Masking

- Instrument callback sites

If not equal, then target **outside** the Execution Jail

Search target inside the callback table of the DSO

Not found? **Halt** execution 😈😈

```
; Original:
    call  rax

; Extended Masking:
    mov   r11,rax
    or    rax,ormask
    and   rax,andmask
    cmp   r11,rax
    jne   call_target
    call  rax
    jmp   after_call

call_target:
    call  DSO_callback_table

after_call:
    ...
```

## Slide 99

## Special Callbacks

1. main()
   - Called by libc
2. Initialization and finalization routines
   - _.init, .fini, .init_array, .fini_array_ sections
3. Exit handlers
   - Registered via _atexit()_

## Slide 100

## Special Callbacks

1. main()
   - Called by libc
2. Initialization and finalization routines
   - _.init, .fini, .init_array, .fini_array_ sections
3. Exit handlers
   - Registered via _atexit()_

Complete set of these callback routines known after compilation and linking

Create callback tables just for them

## Slide 101

## Dynamically Loaded Modules

Typical approaches:

- On-the-fly call target recalculation
- Rewriting of code pages
- Profiling applications with benchmarks

## Slide 102

## Dynamically Loaded Modules

Typical approaches:

- On-the-fly call target recalculation
- Rewriting of code pages
- Profiling applications with benchmarks

## Slide 103

## Dynamically Loaded Modules

- Preload necessary modules at startup
- Generate appropriate PLT stubs for _dlsym-ed_ symbols
- Most libraries do not use _dlopen()_
  - Libc frequently loads NSS libraries

## Slide 104

# EVALUATION

## Slide 105

## Evaluation Metrics

1. Correctness
   - Does PLaTypus instrumentation preserve program behavior?
2. Security guarantees
   - What is the reduction in cross-DSO gadgets?
   - Are state-of-the-art CET bypass attacks mitigated?
3. Performance
   - What is the runtime overhead introduced by PLaTypus?

## Slide 106

## Correctness

- No failures observed in test suites of 19 real-world applications

Table 1. Benchmark Suite. Every benchmark is followed by its version number.

| | | | | |
|---|---|---|---|---|
| rm v9.7 | mkdir v9.7 | gzip v1.14 | make v4.4.1 | Nginx v1.28.0 |
| date v9.7 | sort v9.7 | grep v3.12 | lighttpd v1.4.79 | Redis v8.2.0 |
| uniq v9.7 | tar v1.35 | objdump v2.44 | wget v1.25.0 | SQLite v3.50.4 |
| chown v9.7 | bzip2 v1.0.8 | bftpd v6.3 | memcached v1.6.38 | |

## Slide 107

## Correctness

- No failures observed in test suites of 19 real-world applications
- 16 libraries were instrumented as well
  - Including complex ones like _glibc, OpenSSL_

Table 1. Benchmark Suite. Every benchmark is followed by its version number.

| | | | | |
|---|---|---|---|---|
| rm v9.7 | mkdir v9.7 | gzip v1.14 | make v4.4.1 | Nginx v1.28.0 |
| date v9.7 | sort v9.7 | grep v3.12 | lighttpd v1.4.79 | Redis v8.2.0 |
| uniq v9.7 | tar v1.35 | objdump v2.44 | wget v1.25.0 | SQLite v3.50.4 |
| chown v9.7 | bzip2 v1.0.8 | bftpd v6.3 | memcached v1.6.38 | |

## Slide 108

## Cross-DSO Gadget Reduction

Table 2. Number of indirectly accessible cross-DSO ENBR64 pads under CET (col. 3) and PLaTypus (col. 4-6), from the perspective of the respective module. CT = Callback Table.

| Group | Module | CET | PLaTypus | CT | Red. (%) |
|---|---|---|---|---|---|
| Redis | redis-server | 3739 | 6 | 0 | 99.84 |
|  | libc.so | 4961 | 52 | 52 | 98.95 |
| SQLite | sqlite3 | 6873 | 43 | 0 | 99.37 |
|  | libreadline.so | 7452 | 3 | 2 | 99.96 |
|  | libtinfo.so | 7856 | 3 | 0 | 99.96 |
|  | libncurses.so | 7347 | 3 | 0 | 99.96 |
|  | libm.so | 7242 | 18 | 18 | 99.75 |
|  | libz.so | 8064 | 0 | 0 | 100.00 |
|  | libc.so | 4472 | 40 | 40 | 99.11 |
| Nginx | nginx | 17986 | 6 | 0 | 99.97 |
|  | libpcre2-8.so | 20124 | 2 | 2 | 99.99 |
|  | libcrypto.so | 9551 | 84 | 83 | 99.12 |
|  | libz.so | 20085 | 6 | 6 | 99.97 |
|  | libssl.so | 17182 | 31 | 14 | 99.82 |
|  | libcrypt.so | 20171 | 21 | 0 | 99.90 |
|  | libc.so | 16533 | 166 | 166 | 98.99 |

## Slide 109

## Cross-DSO Gadget Reduction

Table 2. Number of indirectly accessible cross-DSO ENBR64 pads under CET (col. 3) and PLaTypus (col. 4-6), from the perspective of the respective module. CT = Callback Table.

| Group | Module | CET | PLaTypus | CT | Red. (%) |
|---|---|---|---|---|---|
| Redis | redis-server | 3739 | 6 | 0 | 99.84 |
|  | libc.so | 4961 | 52 | 52 | 98.95 |
| SQLite | sqlite3 | 6873 | 43 | 0 | 99.37 |
|  | libreadline.so | 7452 | 3 | 2 | 99.96 |
|  | libtinfo.so | 7856 | 3 | 0 | 99.96 |
|  | libncurses.so | 7347 | 3 | 0 | 99.96 |
|  | libm.so | 7242 | 18 | 18 | 99.75 |
|  | libz.so | 8064 | 0 | 0 | 100.00 |
|  | libc.so | 4472 | 40 | 40 | 99.11 |
| Nginx | nginx | 17986 | 6 | 0 | 99.97 |
|  | libpcre2-8.so | 20124 | 2 | 2 | 99.99 |
|  | libcrypto.so | 9551 | 84 | 83 | 99.12 |
|  | libz.so | 20085 | 6 | 6 | 99.97 |
|  | libssl.so | 17182 | 31 | 14 | 99.82 |
|  | libcrypt.so | 20171 | 21 | 0 | 99.90 |
|  | libc.so | 16533 | 166 | 166 | 98.99 |

## Slide 110

## Cross-DSO Gadget Reduction

Table 2. Number of indirectly accessible cross-DSO ENBR64 pads under CET (col. 3) and PLaTypus (col. 4-6), from the perspective of the respective module. CT = Callback Table.

| Group | Module | CET | PLaTypus | CT | Red. (%) |
|---|---|---|---|---|---|
| Redis | redis-server | 3739 | 6 | 0 | 99.84 |
|  | libc.so | 4961 | 52 | 52 | 98.95 |
| SQLite | sqlite3 | 6873 | 43 | 0 | 99.37 |
|  | libreadline.so | 7452 | 3 | 2 | 99.96 |
|  | libtinfo.so | 7856 | 3 | 0 | 99.96 |
|  | libncurses.so | 7347 | 3 | 0 | 99.96 |
|  | libm.so | 7242 | 18 | 18 | 99.75 |
|  | libz.so | 8064 | 0 | 0 | 100.00 |
|  | libc.so | 4472 | 40 | 40 | 99.11 |
| Nginx | nginx | 17986 | 6 | 0 | 99.97 |
|  | libpcre2-8.so | 20124 | 2 | 2 | 99.99 |
|  | libcrypto.so | 9551 | 84 | 83 | 99.12 |
|  | libz.so | 20085 | 6 | 6 | 99.97 |
|  | libssl.so | 17182 | 31 | 14 | 99.82 |
|  | libcrypt.so | 20171 | 21 | 0 | 99.90 |
|  | libc.so | 16533 | 166 | 166 | 98.99 |

## Slide 111

## Cross-DSO Gadget Reduction

Table 2. Number of indirectly accessible cross-DSO ENBR64 pads under CET (col. 3) and PLaTypus (col. 4-6), from the perspective of the respective module. CT = Callback Table.

| Group | Module | CET | PLaTypus | CT | Red. (%) |
|---|---|---|---|---|---|
| Redis | redis-server | 3739 | 6 | 0 | 99.84 |
|  | libc.so | 4961 | 52 | 52 | 98.95 |
| SQLite | sqlite3 | 6873 | 43 | 0 | 99.37 |
|  | libreadline.so | 7452 | 3 | 2 | 99.96 |
|  | libtinfo.so | 7856 | 3 | 0 | 99.96 |
|  | libncurses.so | 7347 | 3 | 0 | 99.96 |
|  | libm.so | 7242 | 18 | 18 | 99.75 |
|  | libz.so | 8064 | 0 | 0 | 100.00 |
|  | libc.so | 4472 | 40 | 40 | 99.11 |
| Nginx | nginx | 17986 | 6 | 0 | 99.97 |
|  | libpcre2-8.so | 20124 | 2 | 2 | 99.99 |
|  | libcrypto.so | 9551 | 84 | 83 | 99.12 |
|  | libz.so | 20085 | 6 | 6 | 99.97 |
|  | libssl.so | 17182 | 31 | 14 | 99.82 |
|  | libcrypt.so | 20171 | 21 | 0 | 99.90 |
|  | libc.so | 16533 | 166 | 166 | 98.99 |

## Slide 112

## Cross-DSO Gadget Reduction

Table 2. Number of indirectly accessible cross-DSO ENBR64 pads under CET (col. 3) and PLaTypus (col. 4-6), from the perspective of the respective module. CT = Callback Table.

| Group | Module | CET | PLaTypus | CT | Red. (%) |
|---|---|---|---|---|---|
| Redis | redis-server | 3739 | 6 | 0 | 99.84 |
|  | libc.so | 4961 | 52 | 52 | 98.95 |
| SQLite | sqlite3 | 6873 | 43 | 0 | 99.37 |
|  | libreadline.so | 7452 | 3 | 2 | 99.96 |
|  | libtinfo.so | 7856 | 3 | 0 | 99.96 |
|  | libncurses.so | 7347 | 3 | 0 | 99.96 |
|  | libm.so | 7242 | 18 | 18 | 99.75 |
|  | libz.so | 8064 | 0 | 0 | 100.00 |
|  | libc.so | 4472 | 40 | 40 | 99.11 |
| Nginx | nginx | 17986 | 6 | 0 | 99.97 |
|  | libpcre2-8.so | 20124 | 2 | 2 | 99.99 |
|  | libcrypto.so | 9551 | 84 | 83 | 99.12 |
|  | libz.so | 20085 | 6 | 6 | 99.97 |
|  | libssl.so | 17182 | 31 | 14 | 99.82 |
|  | libcrypt.so | 20171 | 21 | 0 | 99.90 |
|  | libc.so | 16533 | 166 | 166 | 98.99 |

**> 98% gadget reduction per module**

## Slide 113

## FOP Attacks Mitigation

- `_dl_call_fini`: part of glibc loader
- Called gadgets: part of libc

```
----|  11. Appendix B: Intel "/bin/sh" in memory chain

+---------------------------+--------------------------+
|       Function Name       |   Equivalent Operation   |
+---------------------------+--------------------------+
| _nss_files_endpwent       | MOV RDI, 0x6             |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| _dl_mcount_wrapper...     | MOV RSI, RDI             |
```

```c
void
_dl_call_fini (void *closure_map)
{
  struct link_map *map = closure_map;

  /* Make sure nothing happens if we are called twice.  */
  map->l_init_called = 0;

  ElfW(Dyn) *fini_array = map->l_info[DT_FINI_ARRAY];
  if (fini_array != NULL)
    {
      ElfW(Addr) *array = (ElfW(Addr) *) (map->l_addr
                                          + fini_array->d_un.d_ptr);
      size_t sz = (map->l_info[DT_FINI_ARRAYSZ]->d_un.d_val
                   / sizeof (ElfW(Addr)));

      while (sz-- > 0)
        ((fini_t) array[sz]) ();
    }

  /* Next try the old-style destructor.  */
  ElfW(Dyn) *fini = map->l_info[DT_FINI];
  if (fini != NULL)
    DL_CALL_DT_FINI (map, ((void *) map->l_addr + fini->d_un.d_ptr));
}
```

_dispatcher loop_ (annotation on the boxed `while (sz-- > 0)` loop)

## Slide 114

## FOP Attacks Mitigation

- `_dl_call_fini`: part of glibc loader
- Called gadgets: part of libc

No PLTs for them inside the loader

```
----|  11. Appendix B: Intel "/bin/sh" in memory chain

+---------------------------+--------------------------+
|       Function Name       |   Equivalent Operation   |
+---------------------------+--------------------------+
| _nss_files_endpwent       | MOV RDI, 0x6             |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| _dl_mcount_wrapper...     | MOV RSI, RDI             |
```

```c
void
_dl_call_fini (void *closure_map)
{
  struct link_map *map = closure_map;

  /* Make sure nothing happens if we are called twice.  */
  map->l_init_called = 0;

  ElfW(Dyn) *fini_array = map->l_info[DT_FINI_ARRAY];
  if (fini_array != NULL)
    {
      ElfW(Addr) *array = (ElfW(Addr) *) (map->l_addr
                                          + fini_array->d_un.d_ptr);
      size_t sz = (map->l_info[DT_FINI_ARRAYSZ]->d_un.d_val
                   / sizeof (ElfW(Addr)));

      while (sz-- > 0)
        ((fini_t) array[sz]) ();
    }

  /* Next try the old-style destructor.  */
  ElfW(Dyn) *fini = map->l_info[DT_FINI];
  if (fini != NULL)
    DL_CALL_DT_FINI (map, ((void *) map->l_addr + fini->d_un.d_ptr));
}
```

_dispatcher loop_ (annotation on the boxed `while (sz-- > 0)` loop)

## Slide 115

## FOP Attacks Mitigation

- `_dl_call_fini`: part of glibc loader
- Called gadgets: part of libc

No PLTs for them inside the loader → Transitions impossible

```
----|  11. Appendix B: Intel "/bin/sh" in memory chain

+---------------------------+--------------------------+
|       Function Name       |   Equivalent Operation   |
+---------------------------+--------------------------+
| _nss_files_endpwent       | MOV RDI, 0x6             |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| __cache_sysconf           | SUB RDI, 0xB9            |
| _dl_mcount_wrapper...     | MOV RSI, RDI             |
```

```c
void
_dl_call_fini (void *closure_map)
{
  struct link_map *map = closure_map;

  /* Make sure nothing happens if we are called twice.  */
  map->l_init_called = 0;

  ElfW(Dyn) *fini_array = map->l_info[DT_FINI_ARRAY];
  if (fini_array != NULL)
    {
      ElfW(Addr) *array = (ElfW(Addr) *) (map->l_addr
                                          + fini_array->d_un.d_ptr);
      size_t sz = (map->l_info[DT_FINI_ARRAYSZ]->d_un.d_val
                   / sizeof (ElfW(Addr)));

      while (sz-- > 0)
        ((fini_t) array[sz]) ();
    }

  /* Next try the old-style destructor.  */
  ElfW(Dyn) *fini = map->l_info[DT_FINI];
  if (fini != NULL)
    DL_CALL_DT_FINI (map, ((void *) map->l_addr + fini->d_un.d_ptr));
}
```

_dispatcher loop_ (annotation on the boxed `while (sz-- > 0)` loop)

## Slide 116

## FOP Attacks Mitigation

- Rare and hard to find
- Most of them not exploitable
- Exploitable ones are related to initialization and finalization routines
  - LOOP attack: `_initterm()` in _msvcrt.dll_
  - Phrack attack: `_dl_call_fini()` in _ld-linux_

We will revisit this later

## Slide 117

## FOP Attacks Mitigation

- Rare and hard to find
- Most of them not exploitable
- Exploitable ones are related to initialization and finalization routines
  - LOOP attack: `_initterm()` in _msvcrt.dll_
  - Phrack attack: `_dl_call_fini()` in _ld-linux_

Dedicated callback tables at call sites

## Slide 118

## Intra-DSO Protection

- Normal PLTs are not reachable indirectly

## Slide 119

## Intra-DSO Protection

- Normal PLTs are not reachable indirectly

```c
int DSOA_f1() {

    void (*fp)(void);
    ...
    fp = 😈
    ...
    fp();
}
```

```c
void DSOA_f2() {

    ...
    system(...);
    ...
}
```

## Slide 120

## Intra-DSO Protection

- Normal PLTs are not reachable indirectly

```c
int DSOA_f1() {

    void (*fp)(void);
    ...
    fp = 😈
    ...
    fp();
}
```

```c
void DSOA_f2() {

    ...
    system(...);
    ...
}
```

## Slide 121

## Intra-DSO Protection

- Normal PLTs are not reachable indirectly
- Isolate _DSOA_f2_ outside the EJ of DSO A

```c
int DSOA_f1() {

    void (*fp)(void);
    ...
    fp = 😈
    ...
    fp();
}
```

```c
void DSOA_f2() {

    ...
    system(...);
    ...
}
```

If _DSOA_f2_ is never called indirectly (static analysis)

## Slide 122

## Intra-DSO Protection

- Normal PLTs are not reachable indirectly
- Isolate _DSOA_f2_ outside the EJ of DSO A

```c
int DSOA_f1() {

    void (*fp)(void);
    ...
    fp = 😈
    ...
    fp();
}
```

```c
void DSOA_f2() {

    ...
    system(...);
    ...
}
```

If _DSOA_f2_ is never called indirectly (static analysis)

Works for sensitive functions such as _system()_ in libc

## Slide 123

## Performance

Bar chart — legend: **Overhead (%)**

Y-axis (Overhead %): 0, 0,5, 1, 1,5, 2

Benchmarks (x-axis) and their approximate bar heights (bars are unlabeled; all overheads are below 0.5%):

| Benchmark | Overhead (%), approx. |
|---|---|
| Bftpd | ≈0 |
| Memcached | ≈0.2 |
| Lighttpd | ≈0 |
| Redis | ≈0.4 |
| SQLite | ≈0.3 |
| Nginx | ≈0.45 |
| Nginx (ramfs) | ≈0.48 |

## Slide 124

# DISCUSSION

## Slide 125

## Modular Support

Interoperability with unprotected modules is supported.

- Unprotected modules can reach arbitrary functions within the address space
- Protected modules can only reach unprotected functions for which they possess PLT stubs

## Slide 126

## Modular Support

Interoperability with unprotected modules is supported.

- Unprotected modules can reach arbitrary functions within the address space
- Protected modules can only reach unprotected functions for which they possess PLT stubs

Reachability of 🐞 in third-party code is limited

## Slide 127

## General Applicability

**ARM**

- ARM BTI ≈ Intel IBT
- Methodology and design remain the same
- Need for backward-edge protection
  - No shadow stack… use PAC

## Slide 128

## General Applicability

**ARM**

- ARM BTI ≈ Intel IBT
- Methodology and design remain the same
- Need for backward-edge protection
  - No shadow stack… use PAC

**Microsoft Windows**

- CFG ≈ Intel IBT
- Leverage IAT instead of PLTs
- Possible modifications to OS-specific code paths
  - E.g., loader, system libraries

## Slide 129

## PLaTypus: Conclusion

- Closes the gap of arbitrary cross-DSO transitions
- Mitigates state-of-the-art FOP attacks
- Supports interoperability between protected and unprotected code
- Incurs negligible overhead while handling complex corner cases

## Slide 130

## Interested in more?

- IEEE S&P paper here
- Code here

(The slide shows a thumbnail of the IEEE S&P paper "PLaTypus: Restricting Cross-Module Transitions to Mitigate Code-Reuse Attacks" by Apostolos Chatzianagnostou, Marcos Bajo, and Christian Rossow — CISPA Helmholtz Center for Information Security — with ARTIFACT EVALUATED badges: Available, Functional, Reproduced.)

