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
text_chars: 35912
ocr_pages: 19
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:05:38Z"
---
# PLaTypus Eliminating Code-Reuse at the Module Boundary

**Speakers:** Apostolos Chatzianagnostou, Marcos Bajo, Christian Rossow  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Apostolos Chatzianagnostou&Marcos Bajo&Christian Rossow_PLaTypus Eliminating Code-Reuse at the Module Boundary.pdf` (130 pages)

## Slide 1

## Slide 2

PLaTypus: Killing Code-Reuse at the Module Boundary

Speaker: Apostolos Chatzianagnostou Collaborators: Marcos Bajo, Christian Rossow

2

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

3

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

4

## Slide 5

## Memory War: Chronicles

Ret2libc (1997)

• _And so it begins..._

ROP (2007)

main:
call  f()
...
system:
f:
...
ret

JOP (2011)

SROP (2014)

5

## Slide 6

## Memory War: Chronicles

Stack canaries (~2000)

ASLR (2003)

DEP/NX (2004)

6

## Slide 7

## Memory War: Chronicles

Stack canaries (~2000)

ASLR (2003)

Control Flow Integrity (2005)

- Control Flow Guard (2014)

- • LLVM CFI (2015)

- Intel CET (2020)

DEP/NX (2004)

Powerful in theory, hard to enforce…

7

## Slide 8

## Memory War: Chronicles

COOP (2015)

FOP (2018)

CFOP (2024)

SFOP (2026)

8

## Slide 9

## Memory War: Chronicles

COOP (2015)

FOP (2018)

Code-reuse attacks still an issue…

CFOP (2024)

SFOP (2026)

9

## Slide 10

## Memory War: Chronicles

COOP (2015)

FOP (2018)

Code-reuse attacks still an issue…

But they all share one thing:

CFOP (2024)

Cross-module transitions!

SFOP (2026)

10

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

11

## Slide 12

## Agenda

1.Userspace CFI and debloating approaches

- 2.Motivation and goals of PLaTypus

- 3.Design, methodology and challenges

- 4.Evaluation and discussion

12

## Slide 13

# BACKGROUND

13

## Slide 14

## Control Flow Integrity (CFI)

• Creation (statically) of Control Flow Graph (CFG) Which indirect transitions are expected/benign?

- Enforcement of CFG through code instrumentation

• Code-reuse: solved Well…

14

## Slide 15

## CFI Taxonomy

Based on the protected edges:

1. Backward-edge CFI

main:
void (* func )() = &f;
func ();
…
f:
...
ret

### 2.  Forward-edge CFI

main:
void (* func )() = &f;
func ();
…
g:
f:
...
...
ret

15

## Slide 16

## CFI Taxonomy

Based on security:

**Coarse-grained**

**Fine-grained**

Weaker Security

Stronger Security

16

## Slide 17

## CFI Taxonomy

Based on security:

**Coarse-grained Fine-grained** Weaker Stronger Security Security Better Worse Performance Performance

17

## Slide 18

## CFI Limitations

- Accurate CFG construction is hard

Static analysis limitations              Overapproximation

- Incomplete, leaving pointers unprotected

- Example: C++ coroutines

- Protected/unprotected interop is hard

Needed for third-party libraries/modules

Fine-grained CFI: limited deployment

18

## Slide 19

## CFI Limitations

- Accurate CFG construction is hard

#### Deployed schemes in practice:

Static analysis limitations              Overapproximation

   - Intel CET (coarse-grained)

- Incomplete, leaving pointers unprotected

- Example: C++ coroutines

   - ARM BTI (coarse-grained)

   - Control Flow Guard (coarse-grained)

- Protected/unprotected interop is hard

- Needed for third-party libraries/modules

- LLVM CFI (fine(r)-grained)

Fine-grained CFI: limited deployment

19

## Slide 20

## Intel CET

- Hardware-enforced CFI

- Two main components:

1.  Shadow Stack for backward edges

2.  Indirect Branch Tracking (IBT) for forward edges

- Supported on Intel 11<sup>th</sup> Gen and later

- Available on both Windows and Linux

20

## Slide 21

## Intel CET – Shadow Stacks

#### **Regular Stack**

t() return
address
g() return
address
f() return
address
h() return
address

#### **Shadow Stack**

t() return
address
g() return
address
f() return
address
h() return
address

21

## Slide 22

## Intel CET – Shadow Stacks

#### **Regular Stack**

t() return address

g() return address

f() return address h() return address

match

#### **Shadow Stack**

t() return
address
g() return
address

f() return address h() return address

22

## Slide 23

## Intel CET – Shadow Stacks

#### **Regular Stack**

execve() mismatch g() return address f() return address SIGSEGV h() return address

SIGSEGV

#### **Shadow Stack**

t() return
address
g() return
address
f() return
address
h() return
address

23

## Slide 24

## Intel CET – Shadow Stacks

#### **Regular Stack**

execve()
g() return
address
f() return
address
h() return
address

**ROP mitigated**

#### **Shadow Stack**

t() return
address
g() return
address
f() return
address
h() return
address

24

## Slide 25

## Intel CET – IBT

g():

f():

endbr 64

mov    rdi

Ptr rax
, Qword  [ ]
, [rip+ 0xdd 3]
rdx
rax

push

lea    rsi

mov

xor

rdx
,

sub

call

mov

mov

…

pop

jmp

rbx

rsp

0
,

20

rax

25

## Slide 26

## ARM BTI

- Protects forward edges

- Similar to Intel’s IBT but in ARM hardware

- Can differentiate between _call targets_ and _jump targets_

- Available on Apple, Android, Linux and Windows systems

26

## Slide 27

## Control Flow Guard

- Protects forward edges

- Microsoft’s implementation of Intel IBT

- Software-enforced

- A bitmap marks valid indirect call/jump targets

27

## Slide 28

## LLVM CFI

- Type-based CFI

- Software-enforced

- Applicable also to virtual calls in C++

void

(*

func_ptr ();

void =  &funcA
)( ) ;

void

void )

int

funcB (

const char* s )

void

funcC (

char* t )

int

funcD (

long )

28

## Slide 29

## LLVM CFI

- Supports modularity ( _cross-DSO_ mode)

- Transitions to uninstrumented libraries are allowed

- Cannot compile glibc

void

(*

func_ptr ();

void =  &funcA
)( ) ;

void

int

void

int

void )

const char* s )

(char* t)

(long)

29

## Slide 30

## Debloating

- Remove code that is not needed E.g., dead code

- Available gadgets are reduced

- Attack surface shrinks

- Especially useful in libraries

- Plethora of gadgets and unused code

main:
call  f()
...
f:
...
ret

:
unused_func
...

30

## Slide 31

## Debloating

- Remove code that is not needed E.g., dead code

- Available gadgets are reduced

- Attack surface shrinks

- Especially useful in libraries

- Plethora of gadgets and unused code

main:
call  f()
...
f:
...
ret

:
unused_func
...

31

## Slide 32

## Library Debloaters

- Nibbler: debloats libraries per _set of binaries_ . Inserting new ones?

- Piece-Wise compilation: modifies library pages _per application_ at load time

- BlankIt: copies library code at runtime to enable/disable functions

32

## Slide 33

## Library Debloaters

• Nibbler: debloats libraries per _set of binaries_ . Inserting new ones?

- Piece-Wise compilation: modifies library pages _per application_ at load time

• BlankIt: copies library code at runtime to enable/disable functions

Need for recompilation

COW - Sharing property undermined

COW - Sharing property undermined

33

## Slide 34

## Library Debloaters

• Nibbler: debloats libraries per _set of binaries_ . Inserting new ones?

• Piece-Wise compilation: modifies library pages **Not practical for general-purpose systems** _per application_ at load time

• BlankIt: copies library code at runtime to enable/disable functions

Need for recompilation

COW - Sharing property undermined

COW - Sharing property undermined

34

## Slide 35

## Where we stand

- Fine(r)-grained CFI schemes not yet mature enough for widespread adoption

- Debloating not practical: unused library/module code remains exposed in applications

35

## Slide 36

## Where we stand

• Fine(r)-grained CFI schemes not yet mature enough for widespread adoption

• Debloating not practical: unused library/module code remains exposed in applications

• Intel CET is the current and foreseeable main line of defense on x86

Is this that bad though?

36

## Slide 37

# MOTIVATION

37

## Slide 38

## CET Limitation

• Arbitrary cross-Dynamic Shared Objects (DSO) / cross-module indirect transitions are allowed

- Leveraged by nearly every attack

- Libraries are rich in gadgets (e.g., syscalls, sensitive functions)

Development of specialized attacks

38

## Slide 39

## Function-Oriented Programming (FOP)

### Class of attacks:

- Evading schemes like CET/BTI

- Entire functions as gadgets

39

## Slide 40

## Function-Oriented Programming (FOP)

### Class of attacks:

### Documented attacks:

- Evading schemes like CET/BTI

   - Loop-Oriented Programming (2015)

- Entire functions as gadgets

- FOP (2018)

- Phrack’s FOP (2024)

40

## Slide 41

## Function-Oriented Programming (FOP)

Class of attacks:

Documented attacks:

- Evading schemes like CET/BTI

   - Loop-Oriented Programming (2015)

- Entire functions as gadgets How do they control arguments?

- FOP (2018)

- Phrack’s FOP (2024)

41

## Slide 42

## Dispatcher Gadget

#### **Attacker-controlled**

- Orchestrator for FOP attacks

- Calls subsequent gadgets in a loop Retrieved from attacker-controlled memory

gadget 1
Dispatcher
gadget 2
Gadget
gadget 3

- Conservative register usage between loops

42

## Slide 43

## Dispatcher Gadget

#### **Attacker-controlled**

- Orchestrator for FOP attacks

- Calls subsequent gadgets in a loop Retrieved from attacker-controlled memory

gadget 1
Dispatcher
gadget 2
Gadget
gadget 3

- Conservative register usage between loops

43

## Slide 44

## Dispatcher Gadget

#### **Attacker-controlled**

- Orchestrator for FOP attacks

- Calls subsequent gadgets in a loop Retrieved from attacker-controlled memory

gadget 1
Dispatcher
gadget 2
Gadget
gadget 3

- Conservative register usage between loops

44

## Slide 45

## Dispatcher Gadget

#### **Attacker-controlled**

• Orchestrator for FOP attacks

• Calls subsequent gadgets in a loop Retrieved from attacker-controlled memory

gadget 1 Dispatcher gadget 2 Gadget gadget 3

### • Conservative register usage between **Normally cross-DSO transition** loops

45

## Slide 46

## Dispatcher Gadget

dispatcher loop

46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Dispatcher Gadget
void
_dl_call_fini (void *closure_map)
{
struct link_map *map closure_map;
Make sure nothing happens
map->1l_init_called = @;
ElfW(Dyn) *fini_array = map->1_info[DT_FINI_ARRAY];
if (fini_array NULL)
Volume @x1@, Issue @x47, Phile #0x@7 of @x11 {
ElfW(Addr) *array = (ElfW(Addr) *) (map->l_addr
==Phrack Inc.==
fini_array->d_un.d_ptr)3
size_t sz (map->1_info[DT_FINI_ARRAYSZ]->d_un.d_val
sizeof (ElfW(Addr)));
while (sz @)
((fini_t) array[sz]) ()3
* Next try t 2
ElfW(Dyn) *fini = map->1_info[DT_FINI];
if (fini NULL)
DL_CALL_DT_FINI (map, ((void *) map->l_addr + fini->d_un.d_ptr));
black hat
2026 46
```

## Slide 47

## Dispatcher Gadget

- __dl_call_fini_ : part of glibc loader

- Called gadgets: part of libc

dispatcher loop

47

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Dispatcher Gadget
void
_dl_call_fini (void *closure_map)
° _dl_call_fini: part e)i glibc loader struct link_map *map closure_map;
sure nothing happens
map->1l_init_called = @;
if we
ElfW(Dyn) *fini_array = map->1_info[DT_FINI_ARRAY];
¢ Called gadgets: part of libc “array [= NULL)
ElfW(Addr) *array = (ElfW(Addr) *) (map->l_addr
fini_array->d_un.d_ptr)3
size_t sz (map->1_info[DT_FINI_ARRAYSZ]->d_un.d_val
sizeof (ElfW(Addr)));
11. Appendix B: Intel "/bin/sh" in memory chain
tener nnn nnn ene n een e eee tenn c renee n eee e eee -- +
Function Name Equivalent Operation
while (sz @)
((fini_t) array[sz]) ()3
_nss_files_endpwent
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
_d1_mcount_wrapper...
ElfW(Dyn) *fini
if (fini NULL)
DL_CALL_DT_FINI (map, ((void *) map->l_addr + fini->d_un.d_ptr));
try th
black hat
2026 47
```

## Slide 48

## Dispatcher Gadgets

- Rare and hard to find

- Most of them not exploitable

- Exploitable ones are related to initialization and finalization routines

   - LOOP attack: __initterm()_ in _msvcrt.dll_ Phrack attack: __dl_call_fini()_ in _ld-linux_

48

## Slide 49

## Dispatcher Gadgets

- Rare and hard to find

- Most of them not exploitable

• Exploitable ones are related to initialization and finalization routines LOOP attack: __initterm()_ in _msvcrt.dll_ Phrack attack: __dl_call_fini()_ in _ld-linux_

We will revisit this later

49

## Slide 50

### How does Linux handle cross-DSO transitions?

50

## Slide 51

## Procedure Linkage Table (PLT)

- Code stubs dispatching cross-DSO calls in ELFs

- Efficient and robust With Full RELRO mitigation

f():

:
puts@plt

lea    rdi

,[rip+ 0

endbr 64

xd 95 ]
0xdd 3]

lea    rsi

jmp

Qword

puts@plt

nop

pop

…

…

[rip+ 0

x 2

e6

]

51

## Slide 52

## Motivation

### **Why then should cross-DSO transfers be allowed outside of PLTs?**

52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Motivation
Main Binary Libc
pues Sa
Why then should cross-DSO lg ~
transfers be allowed outside callrax === =){---1 >| exeove |< +=) -imp rox
of PLTs? mprotect
malloc@PLT malloc@PLT
el
black hat
2026 52
```

## Slide 53

## PLaTypus Goals

- Support both libraries and applications Even complex ones like _glibc_ and _OpenSSL_

- Secure even when some DSOs remain uninstrumented

   - Avoid library recompilation

   - Retain the sharing property of libraries

- Third-party libraries

53

## Slide 54

# DESIGN – METHODOLOGY - CHALLENGES

54

## Slide 55

## Threat Model

- Memory corruption vulnerabilities Arbitrary reads/writes

- Function pointers can be overwritten

- Vulnerabilities can be triggered multiple times

- Intel CET in place

- Operating system enforces DEP

- Full RELRO is enabled

55

## Slide 56

## PLaTypus Design

- Each DSO can only reach external functions for which it possesses PLT stubs

- Per-DSO granularity of enforcement

56

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
PLaTypus Design _. SS
¢ Each DSO can only reach external Main Binary
functions for which it possesses PLT puts@PLT
“4
stubs
call rax -- - -\K- - -- > execve |\<- -X- -jmp rbx
mprotect
malloc@PLT malloc@PLT
¢ Per-DSO granularity of enforcement
black hat
2026 56
```

## Slide 57

## PLaTypus Design

- Each DSO can only reach external functions for which it possesses PLT stubs

- Per-DSO granularity of enforcement

57

## Slide 58

## PLaTypus Design

- Each DSO can only reach external functions for which it possesses PLT stubs

- Per-DSO granularity of enforcement

58

## Slide 59

## Terminology

• Intra-DSO transition: _caller_ and _callee_ in the same module

• Inter-DSO transition: _caller_ and _callee_ in different modules

59

## Slide 60

## Execution Jails (EJ)

• Each DSO is restricted in its EJ Subset of DSO’s address range

60

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Execution Jails (EW)
¢ Each DSO is restricted in its EJ
Subset of DSO’s address range
28 bits
——_
Ox7fff20000000
Oley Me!) a0 DSOA
LY or 1 we mappings Execution
DSOA r-xX mappings Jail
prefix :
Other r-- / rw- mappings
Ox7fff3000000
Execution
Other r-- / rw- mappings DSO B
Jail
r-x Mappings
Other r-- / rw- mappings
black hat
2026 60
```

## Slide 61

## Execution Jails (EJ)

- Each DSO is restricted in its EJ

Subset of DSO’s address range

### • DSO’s indirect branches cannot escape the EJ

Exception? PLT stubs

61

## Slide 62

## Execution Jails (EJ) - Enforcement

### • Enforced with two bitmasks

; Original         ; Execution Jail

...                or

ormask

...                and

andmask

call

rax

62

## Slide 63

## Execution Jails (EJ) - Enforcement

### • Enforced with two bitmasks

; Original         ; Execution Jail
...                or    rax ormask
,
...                and   rax andmask
,
call  rax call  rax

63

## Slide 64

## Execution Jails (EJ) - Enforcement

### • Enforced with two bitmasks

; Original         ; Execution Jail
...                or    rax ormask
,
...                and   rax andmask
,
call  rax call  rax

64

## Slide 65

## Execution Jails (EJ)

### • Enforced with two bitmasks

; Original         ; Execution Jail

...                or

ormask

...                and

andmask

call

rax

65

## Slide 66

## Execution Jails (EJ)

66

## Slide 67

Execution Jails (EJ)

### Inter-DSO transitions are transformed to intra-DSO

67

## Slide 68

## Non-PLT Relocations

- Not all imports go through the PLT…

68

## Slide 69

## Non-PLT Relocations

• Not all imports go through the PLT… _Address-taken_ symbols

int

main (

void )

{

fp )(

int

const

char

*)

=

fp ("

hello ");

}

-O0

puts ;

69

## Slide 70

## Non-PLT Relocations

70

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Non-PLT Relocations
Dump of assembler code for function main:
<+0>: push rbp
<+1>: mov rbp,rsp
<+U>; sub rsp,
<+8>: mov DWORD PTR [rbp ],
<+15>: rax,QWORD PTR [ript+ # 0x555555557Fc8
<+22>: QWORD PTR [rbp ],rax
<+26>: rdi, [rip+ J # 0x555555556004
<+33>: QWORD PTR [rbp ]
<+36>: xor eax, eax
<+38>: add rsp,
<+U2>: pop rbp
<+U3>: ret
black hat
2026 70
```

## Slide 71

## Non-PLT Relocations

### Instrumentation here would corrupt the cross-DSO pointer…

71

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Non-PLT Relocations
Dump of assembler code for function main:
<+0>: push
<+1>: mov ;
<+U>; sub 1
<+8>: mov DWORD PTR [ ],
<+15>: ,QWORD PTR
<+22>: QWORD PTR [
I
QWORD PTR [
xor 1
add 1
pop
ret
Instrumentation here would corrupt the cross-DSO pointer...
black hat
2026 71
```

## Slide 72

## Fake PLTs

For such symbols:

1. Emit PLT stubs

New section: _.fakeplt.sec_

2. Redirect associated relocations to point to these stubs

72

## Slide 73

## Fake PLTs

For such symbols:

1. Emit PLT stubs New section: _.fakeplt.sec_

int

main (

void )

{

fp )(

int

const

char

*)

=

fp ("

hello ");

}

puts ;

2. Redirect associated relocations to point to these stubs

:
puts@plt

0x

:   endbr 64

Qword

[rip+ 0

2e

6]

73

## Slide 74

## Fake PLTs

For such symbols:

1. Emit PLT stubs New section: _.fakeplt.sec_

2. Redirect associated relocations to point to these stubs

:
puts@plt

0x

:   endbr 64

Qword

[rip+ 0

2e

6]

int

main (

void )

{

fp )(

puts ;

int

const

char

*)

=

fp ("

hello ");

}

74

## Slide 75

## Fake PLTs

For such symbols:

int

main (

void )

{

1. Emit PLT stubs New section: _.fakeplt.sec_

}

fp )(

int

fp ("

hello ");

const

char

*)

=

puts ;

2. Redirect associated relocations to point to these stubs

:
puts@plt

0x

:   endbr 64

Qword

[rip+ 0

2e6]

75

## Slide 76

## Fake PLTs

76

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fake PLTs
endbr64
push rbp
mov rbp,rsp
sub rsp,
mov DWORD PTR [rbp ],
mov rax,QWORD PTR [rip+ ]
mov QWORD PTR [rbp ],rax
mov rax,QWORD PTR [rbp
rcx,QWORD PTR [ript+ # 0x555545550ef0
rax ,rcx
rcex,QWORD PTR [rip+ # 0x555545550ef8
rax ,rcx
rdi, [rip+ # 0x55554554ea2c
rax
xor eax , eax
add rsp,
pop rbp
ret
black hat
2026 76
```

## Slide 77

## Fake PLTs

77

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fake PLTs
endbr64
push rbp
mov rbp,rsp
sub rsp,
mov DWORD PTR [rbp ],
mov rax,QWORD PTR [rip+ ]
mov QWORD PTR [rbp ],rax
mov rax,QWORD PTR [rbp ]
7 ript
ee PTR Lrip # 0x555545550ef0 gef> x/9x 6x555545550ee8
rcex,QWORD PTR [ript # 0x555545550ef8 : @x0Q0055554554F cd
rax ,rcx
rdi, [rip+ # 0x55554554ea2c
rax
xor eax , eax
add rsp,
pop rbp
ret
black hat
2026 77
```

## Slide 78

## Fake PLTs

78

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Fake PLTs
endbr64
push rbp
mov rbp,rsp
sub rsp,
mov DWORD PTR [rbp ],
mov rax,QWORD PTR [rip+ ]
mov QWORD PTR [rbp ],rax
mov rax,QWORD PTR [rbp
7 ript
eee PTR Lrip # 0x555545550ef0 gef> x/gx ©x555545550¢0e8
rex,QWORD PTR [rip+ # 0x555545550ef8 >: 0x000055554554F cdo
rax ,rcx
rdi, [rip+ # 0x55554554ea2c
rax
xor eax , eax
add rsp,
pop rbp
ret
gef> x/3i 0x000055554554FcdO
: endbr64
jmp  QWORD PTR [rip+ ] # 0x555545550£28
nop WORD PTR [raxtrax*1+0x0]
black hat
2026 78
```

## Slide 79

## Fake vs Normal PLTs

- Normal PLTs are reached through **direct** calls

- Fake PLTs are reached through **indirect** calls

79

## Slide 80

## Fake vs Normal PLTs

- Normal PLTs are reached through **direct** calls

- Fake PLTs are reached through **indirect** calls

### We can place Normal PLTs **outside** each DSO’s Execution Jail

80

## Slide 81

## Final Design

81

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Final Design
28 bits
—
Ox7fff20000000
Other r-- / rw- j DSO A
Lo er r-- / rw- mappings Exewution
DSOA .fakeplt.sec / r-x mappings Jail
prefix
Other r-- / rw- mappings
.plt / .plt.sec sections
Ox7f ff 30000000
Ox7fff32000000
fr Other r-- / rw- mappings DSO B
fakeplt.sec / r-x mappings Pxecttion
Ox7FFFS7FFFFFFFE vat
Other r-- / rw- mappings
.plt / .plt.sec sections
black hat
2026 81
```

## Slide 82

## Quick Summary

### Hijacked pointers can reach:

1. Intra-module functions

2. Only the Fake PLT stubs of the module

82

## Slide 83

## Quick Summary

Hijacked pointers can reach:

1. Intra-module functions

2. Only the Fake PLT stubs of the module

Possible cross-DSO targets

83

## Slide 84

## Tooling

LLVM toolchain (20.1.0)

- Modifications to the compiler and the linker

- • Instrumentation through compiler passes

- Glibc (2.41)

- Modifications to the loader

84

## Slide 85

## Challenges

### • Callbacks

85

## Slide 86

## Challenges

- Callbacks

- Dynamically loaded modules (via _dlopen_ )

86

## Slide 87

## Callbacks

### **Module A**

void f 1

()

{

...

qsort (

arr,n,sizeof

(int),compare)

...

}

void compare (

...
)

...

}

{

87

## Slide 88

## Callbacks

void f 1

()

{

void compare (

...
)

{

### **Module A**

...

...

qsort ( arr,n,sizeof (int),compare) }
...
}
:
qsort

### **Libc**

...

rcx,ormask

rcx,andmask

call

...

88

## Slide 89

## Callbacks

### **Module A**

### **Libc**

void f 1

()

{

...

qsort (

arr,n,sizeof

(int),compare)

...

rcx,ormask

rcx,andmask

call

...

void compare (

...
)

...

}

{

89

## Slide 90

## Callbacks

### **Module A**

**Libc**

void f 1

()

{

void compare (

...
)

...

...

}

qsort (

arr,n,sizeof

(int),compare)

...

Cannot escape
the Execution Jail

}

:
qsort

...

or

and

call

...

{

90

## Slide 91

## Handling Callbacks

1. Collect callback symbols (per module)

2. Instrument callback sites with extended masking

Places where callbacks are invoked

91

## Slide 92

## Symbol Gathering

• Leverage 2 compiler passes Examining Intermediate Representation

void f1 ()

{

...

qsort (

arr,n,sizeof

qsort (

arr,n,sizeof

...

}

compare1 )

compare2 )

92

## Slide 93

## Symbol Gathering

- Leverage 2 compiler passes Examining Intermediate Representation

- Create callback tables

- One for each DSO dependency

void f 1

()

{

...

qsort (

arr,n,sizeof

1
compare

)

qsort (

arr,n,sizeof

2
compare

)

...

}

{

“

libc ”

: [compare 1

2
, compare

],

“

libcrypto ”

: [...],

...

}

93

## Slide 94

## Symbol Gathering

• Leverage 2 compiler passes Examining Intermediate Representation

• Create callback tables One for each DSO dependency

void f 1

()

{

...

qsort (

arr,n,sizeof

1
compare

)

qsort (

arr,n,sizeof

2
compare

)

...

}

If the current module is used, then _libc_ may need to call _compare1_ and _compare2_

{

“

libc ”

: [compare 1

2
, compare

],

“

libcrypto ”

: [...],

...

}

94

## Slide 95

## Extended Masking

- Instrument callback sites

:
; Original

call

:
; Extended Masking

mov   r11,rax

rax,ormask

rax,andmask

cmp

r11,rax

jne

call_target

call

jmp

after_call

:
call_target

DSO_callback_table

:
after_call

...

95

## Slide 96

## Extended Masking

- Instrument callback sites

If not equal, then target outside the Execution Jail

; Original:

call

:
; Extended Masking

mov   r 11

,rax

rax,ormask

rax,andmask

cmp

r 11

,rax

jne

call_target

call

jmp

after_call

:
call_target

DSO_callback_table

:
after_call

...

96

## Slide 97

## Extended Masking

- Instrument callback sites

If not equal, then target outside the Execution Jail

Search target inside the callback table of the DSO

; Original:

call

:
; Extended Masking

mov   r 11

,rax

rax,ormask

rax,andmask

cmp

r 11

,rax

jne

call_target

call

jmp

after_call

:
call_target

DSO_callback_table

:
after_call

...

97

## Slide 98

## Extended Masking

- Instrument callback sites

If not equal, then target outside the Execution Jail

Search target inside the callback table of the DSO Not found? Halt execution

; Original:

call

:
; Extended Masking

mov   r 11

,rax

rax,ormask

rax,andmask

cmp

r 11

,rax

jne

call_target

call

jmp

after_call

:
call_target

DSO_callback_table

:
after_call

...

98

## Slide 99

## Special Callbacks

1. main()

Called by libc

2. Initialization and finalization routines

_.init, .fini, .init_array, .fini_array_ sections

3. Exit handlers

Registered via _atexit()_

99

## Slide 100

## Special Callbacks

1. main() Called by libc

2. Initialization and finalization routines

_.init, .fini, .init_array, .fini_array_ sections

3. Exit handlers

Complete set of these callback routines known after compilation and linking

Create callback tables just for them

Registered via _atexit()_

100

## Slide 101

## Dynamically Loaded Modules

Typical approaches:

- On-the-fly call target recalculation

- Rewriting of code pages

- Profiling applications with benchmarks

101

## Slide 102

## Dynamically Loaded Modules

Typical approaches:

- On-the-fly call target recalculation

- Rewriting of code pages

• Profiling applications with benchmarks

102

## Slide 103

## Dynamically Loaded Modules

- Preload necessary modules at startup

- Generate appropriate PLT stubs for _dlsym-ed_ symbols

- Most libraries do not use _dlopen()_ Libc frequently loads NSS libraries

103

## Slide 104

# EVALUATION

104

## Slide 105

## Evaluation Metrics

1. Correctness

Does PLaTypus instrumentation preserve program behavior?

2. Security guarantees What is the reduction in cross-DSO gadgets? Are state-of-the-art CET bypass attacks mitigated?

3. Performance

What is the runtime overhead introduced by PLaTypus?

105

## Slide 106

## Correctness

• No failures observed in test suites of 19 real-world applications

106

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Correctness
¢ No failures observed in test suites of 19 real-world applications
Table 1. BENCHMARK SUITE. EVERY BENCHMARK IS FOLLOWED BY ITS VERSION NUMBER.
black hat
2026 106
```

## Slide 107

## Correctness

• No failures observed in test suites of 19 real-world applications

• 16 libraries were instrumented as well

Including complex ones like _glibc, OpenSSL_

107

## Slide 108

## Cross-DSO Gadget Reduction

108

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Cross-DSO Gadget Reduction
Table 2. NUMBER OF INDIRECTLY ACCESSIBLE CROSS-DSO En8R64
PADS UNDER CET (COL. 3) AND PLATYPUS (COL. 4-6), FROM THE
PERSPECTIVE OF THE RESPECTIVE MODULE. CT = CALLBACK TABLE.
Module CET
PLAT YPU Red
ec erver 3739
libc.so 4961
99.37
99.96
99.96
99.96
99.75
| Module | CET | PLaTypus | CT | Red. (%) _
vise [el & (8) ay
|
8
100.00
| itibeso | 4472, || 40 | 40 | 99
|
|
|
|
|
|
—_| libeso | 16533 | = 166 =| 166 | ~— 98.99
libreadline.so 7452
libtinfo.so 7856
libncurses.so 7347
libm.so
libz.so
libc.so 99.1]
99.97
99.99
99.12
99, 97
nginx 17986
libpere2-8.so | 20124
liberypto.so 9551
libz.so 20085
libssl.so 17182
libcrypt. 80 20171
ibe 16533
sqlite3 6873
98.99
black hat
2026 108
```

## Slide 109

## Cross-DSO Gadget Reduction

109

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Cross-DSO Gadget Reduction
Table 2. NUMBER OF INDIRECTLY ACCESSIBLE CROSS-DSO En8R64
PADS UNDER CET (COL. 3) AND PLATYPUS (COL. 4-6), FROM THE
PERSPECTIVE OF THE RESPECTIVE MODULE. CT = CALLBACK TABLE.
Module Red
erver
libc.so
99.37
99.96
99.96
99.96
99.75
[|| ose
|
8
100.00
|
|
|
|
|
|
6 |
| Module || CET |] PLatypus | CT | Red. (%) _
|} ;
|| 4
sqlite3 |
libreadline.so
libtinfo.so
libncurses.so |
libm.so
libz.so
libc.so 99.1]
|
|
|
|
—__| libeso | L16533}] — 166 | 166 | ~— 98.99
17986
20124
9551
20085
17182
20171
16533
99.97
99.99
99.12
99, 97
nginx
libpcre2-8.so
liberypto.so
libz.so
libssl.so
libcrypt. so
98.99
black hat
2026 109
```

## Slide 110

## Cross-DSO Gadget Reduction

110

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Cross-DSO Gadget Reduction
Table 2. NUMBER OF INDIRECTLY ACCESSIBLE CROSS-DSO En8R64
PADS UNDER CET (COL. 3) AND PLATYPUS (COL. 4-6), FROM THE
PERSPECTIVE OF THE RESPECTIVE MODULE. CT = CALLBACK TABLE.
Module CET | PLAT YPUS| YPU
Red
ec erver 4g | redis-server | 3739 ||
libc.so 4961
99.37
99.96
99.96
99.96
99.75
| Module | CET |[PLaTyus]| CT | Red. (%) _
i ay
|
8
100.00
| 40 | 99.11 |
|
|
|
|
|
|
—__| libeso | 16533 |[|_ 166 i} 166 | = 98.99
libreadline.so 7452
libtinfo.so 7856
libncurses.so 7347
libm.so
libz.so
libc.so 99.1]
99.97
99.99
99.12
99, 97
nginx | nginx «sd: 7986
libpere2-8.so | 20124
liberypto.so 9551
libz.so 20085
libssl.so 17182
libcrypt. 80 20171
ibe 16533
| gglites «| 6873. 6873
98.99
black hat
2026 110
```

## Slide 111

## Cross-DSO Gadget Reduction

111

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Cross-DSO Gadget Reduction
Table 2. NUMBER OF INDIRECTLY ACCESSIBLE CROSS-DSO En8R64
PADS UNDER CET (COL. 3) AND PLATYPUS (COL. 4-6), FROM THE
PERSPECTIVE OF THE RESPECTIVE MODULE. CT = CALLBACK TABLE.
| Module | CET | PLaTypus |) CT]] Red. (%) CET PLATYPU
ec erver 4g -| redis-server | 3739 | 6. ||
libc.so 4961
| sglites—ti‘(g;S«OS73 «| (COSY; 6873 43 ) 99.37
99.96
99.96
99.96
99.75
100.00
99.11
libreadline.so 7452
libtinfo.so 7856
libncurses.so 7347
libm.so
libz.so
libc.so
99.97
99.99
99.12
99, 97
nginx It nginx =—st—=‘;«d‘T9BO | COCSYS;
libpere2-8.so | 20124
liberypto.so 9551
libz.so 20085
libssl.so 17182
libcrypt. 80 20171
___| libeso | 16533 | 166 || 166)| 98.99 98.99
black hat
2026 111
```

## Slide 112

## Cross-DSO Gadget Reduction

### > 98% gadget reduction per module

112

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Cross-DSO Gadget Reduction
Table 2. NUMBER OF INDIRECTLY ACCESSIBLE CROSS-DSO ENBR
PADS UNDER CET (COL. 3) AND PLATYPUS (COL. 4-6), FROM THE
PERSPECTIVE OF THE RESPECTIVE MODULE. CT = CALLBACK TABLE.
Module
redis-server
libc.so
| sglites—ti‘(;:S«‘OS73 «| BS:C“‘“;;C SLOT
libreadline.so
libtinfo.so
libncurses.so
libm.so
libz.so
libc.so
nginx
libpcre2-8.so
liberypto.so
libz.so
libssl.so
liberypt.so
—_ tibeso | 16533 | 166 | 166 | 98.99 80
CET
3739
496]
6873
7452
7856
7347
7242
8064
4472
nginx si‘; «d‘TOBO | COCS:~*~<~:C<i SYST
201 24
201 71
16533
PLATYPUS | Module | CET | PLaTypus | CT | Red. (%) _ CT
0
52
0
?
0
0
18
0
99.84
98.95
99.37
99.96
99.96
99.96
99.75
100.00
99.11
99.97
99.99
99. 12
98.99
64
> 98% gadget
reduction per
module
black hat
2026 112
```

## Slide 113

## FOP Attacks Mitigation

- __dl_call_fini_ : part of glibc loader

- Called gadgets: part of libc

dispatcher loop

113

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
FOP Attacks Mitigation
“Gi call fini (void *closure_map)
¢ _dl_call_fini: part of glibc loader struct Link map *nap = closure_maps
sure nothing happens
map->1l_init_called = @;
if we
ElfW(Dyn) *fini_array = map->1_info[DT_FINI_ARRAY];
_array NULL)
¢ Called gadgets: part of libc
ElfW(Addr) *array = (ElfW(Addr) *) (map->l_addr
fini_array->d_un.d_ptr)3
size_t sz (map->1_info[DT_FINI_ARRAYSZ]->d_un.d_val
sizeof (ElfW(Addr)));
11. Appendix B: Intel "/bin/sh" in memory chain
tener nnn nnn ene n een e eee tenn c renee n eee e eee -- +
Function Name Equivalent Operation
while (sz @)
((fini_t) array[sz]) ()3
_nss_files_endpwent
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
__cache_sysconf
_d1_mcount_wrapper...
ElfW(Dyn) *fini
if (fini NULL)
DL_CALL_DT_FINI (map, ((void *) map->l_addr + fini->d_un.d_ptr));
try th
black hat
2026 113
```

## Slide 114

## FOP Attacks Mitigation

- __dl_call_fini_ : part of glibc loader

- Called gadgets: part of libc

dispatcher loop

No PLTs for them inside the loader

114

## Slide 115

## FOP Attacks Mitigation

- __dl_call_fini_ : part of glibc loader

- Called gadgets: part of libc

dispatcher loop

No PLTs for Transitions them inside impossible the loader

115

## Slide 116

## FOP Attacks Mitigation

- Rare and hard to find

- Most of them not exploitable

• Exploitable ones are related to initialization and finalization routines LOOP attack: __initterm()_ in _msvcrt.dll_ Phrack attack: __dl_call_fini()_ in _ld-linux_

We will revisit this later

116

## Slide 117

## FOP Attacks Mitigation

- Rare and hard to find

- Most of them not exploitable

• Exploitable ones are related to initialization and finalization routines LOOP attack: __initterm()_ in _msvcrt.dll_ Phrack attack: __dl_call_fini()_ in _ld-linux_

Dedicated callback tables at call sites

117

## Slide 118

## Intra-DSO Protection

### • Normal PLTs are not reachable indirectly

118

## Slide 119

## Intra-DSO Protection

### • Normal PLTs are not reachable indirectly

int

DSOA_f 1

()

{

fp )(

void

...

...

();

}

void );

void

DSOA_f 2

()

{

...

(...);

...

}

119

## Slide 120

## Intra-DSO Protection

### • Normal PLTs are not reachable indirectly

int

DSOA_f 1

()

{

fp )( void );

void

...

=

...

();

}

void

DSOA_f 2

()

{

...

(...);

...

}

120

## Slide 121

## Intra-DSO Protection

- Normal PLTs are not reachable indirectly

- Isolate _DSOA_f2_ outside the EJ of DSO A

int

DSOA_f 1

()

{

fp )( void );

void

...

=

...

();

}

void

DSOA_f2 ()

{

...

(...);

...

}

If _DSOA_f2_ is never called indirectly (static analysis)

121

## Slide 122

## Intra-DSO Protection

• Normal PLTs are not reachable indirectly

- Isolate _DSOA_f2_ outside the EJ of DSO A If _DSOA_f2_ is never called indirectly (static analysis)

int

DSOA_f1 ()

void

...

=

...

();

}

{

fp )( void );

void

DSOA_f 2

()

{

...

(...);

...

}

Works for sensitive functions such as _system()_ in libc

122

## Slide 123

Performance

#### Overhead (%)

2
1,5
1
0,5
0

123

## Slide 124

# DISCUSSION

124

## Slide 125

## Modular Support

Interoperability with unprotected modules is supported.

• Unprotected modules can reach arbitrary functions within the address space

- Protected modules can only reach unprotected functions for which they possess PLT stubs

125

## Slide 126

## Modular Support

Interoperability with unprotected modules is supported.

• Unprotected modules can reach arbitrary functions within the address space

• Protected modules can only reach unprotected functions for which they possess PLT stubs

Reachability of in third-party code is limited

126

## Slide 127

## General Applicability

### ARM

- ARM BTI ≈ Intel IBT

- Methodology and design remain the same

- Need for backward-edge protection No shadow stack… use PAC

127

## Slide 128

## General Applicability

ARM

- ARM BTI ≈ Intel IBT

- Methodology and design remain the same

- Need for backward-edge protection No shadow stack… use PAC

### Microsoft Windows

- CFG ≈ Intel IBT

- Leverage IAT instead of PLTs

- Possible modifications to OSspecific code paths

E.g., loader, system libraries

128

## Slide 129

## PLaTypus: Conclusion

• Closes the gap of arbitrary cross-DSO transitions

- Mitigates state-of-the-art FOP attacks

- Supports interoperability between protected and unprotected code

- Incurs negligible overhead while handling complex corner cases

129

## Slide 130

## Interested in more?

- IEEE S&P paper here

- Code here

130

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Interested in more?
¢ IEEE S&P paper here
¢ Code here
PLATYPUs: Restricting
Apostolos Chatzianagnostou
CISPA Helmholtz Center
for Information Security
Abstract—Numerous techniques have been proposed to thwart
code reuse attacks, yet practical adoption remains limited due
to compatibility and deployment challenges. In the current
and foreseeable Intel architecture landscape, the main line
of defense against such attacks is Intel CET—a hardware-
enforced control-flow integrity mechanism integrated into re-
cent Intel x86-64 CPUs. However, despite its hardware-backed
ms and widespread adoption, CET still provides only
it continues to allow hijacked function pointers
to invoke arbitrary functions across module boundaries, a
capability that remains fundamental to many modern exploits.
This paper proposes PLATYPU novel defense on top
of Intel CET to address this limitation. PLATYPuUs enforces
execution jails using lightweight address masking to ensure
indirect control transfers remain within module boundaries.
on calls are only permitted via necessary PLT
stubs specific to each DSO. The evaluation on our LLVM-based
prototype, spanning 19 applications and 16 shared libraries (in-
cluding glibc), demonstrates that PLAT YPUS reduces indirectly
accessible cross-DSO functions by over 98%. Performance
testing with complex applications like Nginx and Redis shows
that PLATyPUs incurs no more than 0.5% overhead.
ARTIFACT ARTIFACT ARTIFACT
EVALUATED EVALUATED EVALUATED
FUNCTIONAL REPRODUCED
s-Module Transitions to Mitigate Code-Reuse Attacks
Marcos Bajo Christian Rossow
CISPA Helmhol:
for Information §
CISPA Helmholtz Center
for Information Security
legitimate, precomputed transfers at runtime. Numerous CFI
schemes have been proposed in recent years. These schemes
are typically categorized based on the strictness of their
CFGs as either coarse-grained or fine-grained, with the
latter raising the bar for successful exploitation consider-
ably. Despite extensive academic efforts to develop fine-
grained CFI techniques, their adoption in practice remains
notably limited [15]. core reason for this is their lack
of robust support for interoperability between protected and
unprotected code [10], [46], a c al requirement in real-
world environments where instrumented applications must
frequently interact with third-party libraries.
Therefore, the vast majority of modern software relies
on coarse-grained CFI schemes as the primary line of de-
fense. The prevailing solutions, whose adoption is steadily
increasing and is expected to become the default for fu-
ture systems on the two most popular architectures are In-
tel’s Control-Flow Enforcement Technology (CET) [40] and
Arm’s Branch Target Identification (BTI) [11], resp
Both restrict the modularity of code-reuse gadgets to entire
functions. This restriction is significant, as it complicates an
attacker’s ability to set up the necessary function arguments
despite successfully hijacking control flow. Nonetheless,
black hat
2026
130
```
