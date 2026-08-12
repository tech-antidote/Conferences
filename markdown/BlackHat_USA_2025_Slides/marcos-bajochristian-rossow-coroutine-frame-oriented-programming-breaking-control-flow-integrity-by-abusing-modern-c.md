---
title: "Coroutine Frame-Oriented Programming Breaking Control Flow Integrity by Abusing Modern C++"
speakers: ["Marcos Bajo", "Christian Rossow"]
conference: "Black Hat"
conference_full: "Black Hat USA 2025"
edition: "USA"
year: 2025
source_pdf: "BlackHat_USA_2025_Slides/Marcos Bajo&Christian Rossow_Coroutine Frame-Oriented Programming Breaking Control Flow Integrity by Abusing Modern C++.pdf"
pages: 231
sha256: "1eacf6ab14924583996d9927431cc8b5b1775cb05c5b94509dd0af83905c2aff"
text_chars: 56690
ocr_pages: 40
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T22:59:23Z"
---
# Coroutine Frame-Oriented Programming Breaking Control Flow Integrity by Abusing Modern C++

**Speakers:** Marcos Bajo, Christian Rossow  
**Conference:** Black Hat USA 2025  
**Source:** `BlackHat_USA_2025_Slides/Marcos Bajo&Christian Rossow_Coroutine Frame-Oriented Programming Breaking Control Flow Integrity by Abusing Modern C++.pdf` (231 pages)


## Slide 1

## Coroutine Frame-Oriented Programming Breaking Control Flow Integrity by Abusing Modern C++

Marcos Bajo _h3xduck_ Christian Rossow

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| Ze black hat
EFFINGS
AUGUST 6-7, 2025
MANDALAY BAY / LAS VEGAS
Coroutine Frame-Oriented
Programming
Breaking Control Flow Integrity by Abusing Modem C++
; . > m 7 / —_ _
e . aE ” "9
S ‘
‘ G
LE 77 / ~_
“a —~ NX
4,
; | x
SSN \ 7 y
ee A
:
Marcos Bajo h3xduck
Christian Rossow
```

## Slide 2

##### The Old Ages

1972

Buffer overflows 1<sup>st</sup> mentioned

2020

2000

2010

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
1972
Buffer
overflows
1st mentioned
2000 2010
ESD-TR-73-51, ' Vol. II
COMPUTER SECURITY TECHNOLOGY PLANNING STUDY
James P, Anderson
October 1972
```

## Slide 3

##### The Old Ages

1972

1972 2000 Stack canaries ret2libc Buffer overflows 1<sup>st</sup> mentioned

2010

2020

## Slide 4

1972

The Old Ages 2000

2010

2020

Stack canaries ASLR ret2libc DEP/NX Buffer overflows 1<sup>st</sup> mentioned

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bibekhat The OldAges-
1972 2000 2010
Stack
canaries ASLR
(<)- 8-0-O@—--
l DEP/NX
Buffer ret2libc
overflows
1st mentioned
```

## Slide 5

The Old Ages 1972 2000 2010 Stack canaries ASLR JOP ret2libc DEP/NX ROP DOP Buffer overflows 1<sup>st</sup> mentioned

2020

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
gQ : Z SE ec } ip sl A : —
lack hat The Old “ / a
b ecanae Old Ages
1972 2000 2010 2020
Stack
canaries ASLR JOP
(x)1-_©-©-O€ ®@-@®
DEP/NX
Buffer ret2libc
overflows
1st mentioned
```

## Slide 6

1972

The Modern Ages 2000 2010

2020

2010

CFI 1<sup>st</sup> mentioned

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
1972 2000 2010 2020
black hat ma i es Mf jp Oe
BRIEFINGS Modem Ages :
()1-©-©-€
```

## Slide 7

The Modern Ages 1972 2000 2010

2020

LLVM CFI CFG Intel CET CFI 1<sup>st</sup> mentioned

## Slide 8

Code Reuse

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
h()
JQ)
```

## Slide 9

Code Reuse

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
‘ XS ny exe ; _ A F pe: a | ene »
pisekhat Ws “cance ™ a. “if P=:
BRIEFINGS :
f:
call g()
call h()
execve()
ret
‘calll h()
call i()
| ret ret
call i() “call i()
call j() —<$$>
```

## Slide 10

##### Control Flow Integrity

- “C      ”   f

   - A LR, DEP,     r   …

   - Make exploits harder

- Control Flow Integrity • Construct Control Flow Graph (CFG)

- • Instrumentation to enforce CFG

   - Code-reuse techniques stopped

      - Sorry, yes, ROP is dead

## Slide 11

##### Who We Are

###### **Marcos Bajo** aka **_h3xduck_**

@h3xduck h3xduck@gmail.com

- PhD Student at CISPA (Germany)

- • https://github.com/h3xduck

- • Three things I love:

   - Malware

   - Exploits

   - Ducks

## Slide 12

##### Who We Are

###### **Marcos Bajo** aka **_h3xduck_**

@h3xduck h3xduck@gmail.com

###### **Christian Rossow**

@chrossow

rossow@cispa.de

- PhD Student at CISPA (Germany)

- • https://github.com/h3xduck

- • Three things I love:

   - Faculty at CISPA

   - CS Professor at Saarbrücken & Dortmund

   - Leader of the _Systems Security Group_

- Malware

- Exploits

- Ducks

(We do very cool things, reach out!)

## Slide 13

##### What We Will Learn

###### 1. Userspace CFI defenses _How does CFI look like in an everyday system?_

## Slide 14

##### What We Will Learn

1. Userspace CFI defenses _How does CFI look like in an everyday system?_

2. Bypassing CFI _How can we exploit programs protected by CFI  schemes?_

## Slide 15

##### What We Will Learn

###### 1. Userspace CFI defenses _How does CFI look like in an everyday system?_

2. Bypassing CFI

_How can we exploit programs protected by CFI  schemes?_

3. C++20 Coroutines

_Internals and security of C++ coroutines._

## Slide 16

##### What We Will Learn

###### 1. Userspace CFI defenses _How does CFI look like in an everyday system?_ 2. Bypassing CFI

_How can we exploit programs protected by CFI  schemes?_

3. C++20 Coroutines _Internals and security of C++ coroutines._

4. Coroutine Frame-Oriented Programming _Using coroutines to bypass CFI._

## Slide 17

### Userspace CFI Defenses

## Slide 18

##### CFI Types

###### Backward-edge

```
voidg()
{
```

```
…
}
```

void f()
{
g();
}

## Slide 19

CFI Types

###### Backward-edge

###### Forward-edge

void g()
{
…
void f()
}
{
void *ptr = &g;
void f()
ptr();
{
}
g();
}

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
black hat
BRIEFINGS
Backward-edge Forward-edge
void g()
{
vs void £()
! {
A void *ptr = &@;
void f() ptr();
{ }
gQ);
@0O0O0O
```

## Slide 20

##### CFI Types

###### Coarse-grained CFI

###### Fine-grained CFI

- Security

+ Security

+ Performance

- Performance

## Slide 21

##### Intel CET

##### • Coarse-grained CFI

• Hardware-assisted

- Two protections in one:

   - Backward-edge: Shadow Stack

   - Forward-edge: Indirect Branch Tracking (IBT)

## Slide 22

##### Intel CET (Shadow Stack)

void f() void g() void h() void i()
{ { { {
g(); h(); i(); ret;
}
ret; ret; ret;
} } }

## Slide 23

Intel CET (Shadow Stack) SHSTK

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Debaters — r(s ), SHSTK “
A | A
g()
frame
f() return
address
f
frame f() return
address @000
```

## Slide 24

Intel CET (Shadow Stack) SHSTK

## Slide 25

Intel CET (Shadow Stack) SHSTK

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2) ; eS
Ne FISFINGS Intel
A
@0O0O0O
```

## Slide 26

##### Intel CET (Shadow Stack)

###### SHSTK

void i()
{
ret;
}

## Slide 27

##### Intel CET (Shadow Stack)

###### SHSTK

void h()
{
i();
ret;
}

## Slide 28

##### Intel CET (Shadow Stack)

###### SHSTK

void g()
{
h();
ret;
}

## Slide 29

##### Intel CET (Shadow Stack)

###### SHSTK

void i()
{
ret;
}

## Slide 30

##### Intel CET (Shadow Stack)

- For an application to be SHSTK enabled:

   - CPU Support: Intel 11<sup>th</sup> gen (Tiger Lake)

   - Kernel Support: Linux 6.6, Windows 10 19H1

   - Compiler support:

      - GCC 8.1

      - LLVM 11

      - MSVC 16.7

   - Application must be compiled with –fcf-protection=full (Linux) or /CETCOMPAT (Windows)

<u>https://h3xduck.github.io/cfi/2025/06/26/enabling-intel-cet.html</u>

## Slide 31

##### Intel CET (IBT)

```
main:
```

```
push rbp
mov rbp, rsp
mov rsi, [rdi+0x8]
mov rax, [rbx]
call[rax]
leave
```

```
ret
```

## Slide 32

##### Intel CET (IBT)

```
main:
f1:
push rbp
add rdi, 0x8
mov rbp, rsp
mov rax, 0x10
mov rsi, [rdi+0x8]
lea rdx, [rbp]
mov rax, [rbx]
add rdi, rax
call[rax]
leavemov rax, rdx
ret
ret
```

## Slide 33

##### Intel CET (IBT)

```
main:
f1:
push rbp
endbr64
mov rbp, rsp
add rdi, 0x8
mov rsi, [rdi+0x8]
mov rax, 0x10
mov rax, [rbx]
lea rdx, [rbp]
call[rax]
leaveadd rdi, rax
retmov rax, rdx
ret
```

## Slide 34

##### Intel CET (IBT)

##### • Limited availability

   - Windows: Not implemented

   - Linux: enforcement only in the kernel since 5.18

- Coarse-grained CFI

   - We still can use gadgets starting with endbr64

## Slide 35

##### CFG: Control Flow Guard

• Instrumentation for every indirect call/jmp • Windows substitute for IBT • Coarse-grained

call qword ptr [rdi]

call qword ptr [binary!__guard_dispatch_icall_fptr]

## Slide 36

CFG: Control Flow Guard

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
13
“1
“43
i
“1
“43
i
“1
“43
1s
“1
“44
i
“1
“43
13
1
“43
13
1
‘13
@0OO0O0O
```

## Slide 37

##### CFG: Control Flow Guard

- ___guard_dispatch_icall_fptr_ ensures that the call target is valid

   - If yes, make the call

   - If not, abort the process

- Uses a 2-bit map

Disallowed

## Slide 38

##### CFG: Control Flow Guard

- ___guard_dispatch_icall_fptr_ ensures that the call target is valid

   - If yes, make the call

   - If not, abort the process

• Uses a 2-bit map

Allowed if 16-bit aligned

## Slide 39

##### CFG: Control Flow Guard

- ___guard_dispatch_icall_fptr_ ensures that the call target is valid

   - If yes, make the call

   - If not, abort the process

##### • Uses a 2-bit map

###### Allowed for the whole range

## Slide 40

##### CFG: Control Flow Guard

• ___guard_dispatch_icall_fptr_ ensures that the call target is valid

• If yes, make the call

• If not, abort the process

```
KERNEL32!WinExec:
mov     rax,rsp
mov     qword ptr[rax+10h],rbx
mov     qword ptr[rax+18h],rsi
mov     qword ptr[rax+20h],rdi
push    rbp
lea     rbp,[rax-38h]
```

## Slide 41

##### - LLVM CFI (cfi icall)

• Fine(r)-grade CFI: label based • Flag _–fsanitize=cfi-icall_ in Clang/LLVM • Each function is assigned a dynamic type

```
ind_func();
```

```
int puts(const char* s)
int close(int fd)
int kill(pid_tpid, int sig)
int system(const char* c)
```

## Slide 42

##### - LLVM CFI (cfi icall)

• Fine(r)-grade CFI: label based • Flag _–fsanitize=cfi-icall_ in Clang/LLVM • Each function is assigned a dynamic type

```
ind_func= &close;
ind_func();
```

```
int puts(const char* s)
intclose(intfd)
int kill(pid_tpid, int sig)
int system(const char* c)
```

## Slide 43

##### - LLVM CFI (cfi icall)

- Fine(r)-grade CFI: label based

- Flag _–fsanitize=cfi-icall_ in Clang/LLVM

- Each function is assigned a dynamic type

```
if()
ind_func= &close;
else
ind_func= &kill;
ind_func();
```

```
int puts(const char* s)
intclose(intfd)
int kill(pid_tpid, intsig)
int system(const char* c)
```

## Slide 44

-
LLVM CFI (cfi icall)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
BRIEFINGS
<fl>:
<f1+5>:
<f1+6>:
<f1+7>:
<f3>:
<f3+5>;
<f3+6>:
<f3+7>:
<main>:
<maint5>:
<maint+6>:
<maint7>:
jmp
int3
int3
int3
jmp
int3
int3
int3
jmp
int3
int3
int3
<fl>
<f3>
<main>
@0O0O0O
```

## Slide 45

-
LLVM CFI (cfi icall)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekchat
BRIEFINGS
Ca =. Lf
LLVM CF
<+104>:
<+111>:
<+114>:
<+117>:
<+121>:
<+125>:
<+127>:
Srl ale eos
<+131>:
<+133>:
<+137>:
<+138>:
sh rlele eos
<+149>:
<+152>:
lea rax, Lript ]
mov rex ,rbx
sub rex ,rax
rol rcx,
cmp rex,
jae <main+139>
: Stalemate Cli
RU eax
add rsp,
pop rbx
ret
movabs rdi,
mov rsi,rbx
call
<__cfi_slowpath>
# @x1e080 <f1>
@0O0O0O
```

## Slide 46

-
LLVM CFI (cfi icall)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
<+104>:
<+111>:
<+114>:
<+117>:
<+121>:
<+125>:
<+127>:
Srl ale eos
<+131>:
<+133>:
<+137>:
<+138>:
sh rlele eos
<+149>:
<+152>:
xor
add
pop
ret
movabs
mov
call
rax, Lript
rex ,rbx
rex ,rax
rex,
rex,
<maint+139>
eax, eax
rsp,
rbx
rdi,
rsi,rbx
<__cfi_slowpath>
# @x1e080 <f1>
@0O0O0O
```

## Slide 47

-
LLVM CFI (cfi icall)

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekchat
BRIEFINGS
LVM CFI
<+104>:
<+111>:
<+114>:
<+117>:
<+121>:
<+125>:
<+127>:
Srl ale eos
<+131>:
<+133>:
<+137>:
<+138>:
sh rlele eos
<+149>:
<+152>:
rax, Lript ] # @x1e080 <f1>
rex ,rbx
rex ,rax
rex,
rex,
<main+139>
edi,edi
rbx
eax, eax
rsp,
rbx
rdi,
rsi,rbx
<__cfi_slowpath>
@0O0O0O
```

## Slide 48

##### - LLVM CFI (cfi icall)

- Fine(r)-grade CFI: label based

- Flag _–fsanitize=cfi-icall_ in Clang/LLVM

- Each function is assigned a dynamic type

```
ind_func= &puts;
ind_func();
```

```
intputs(const char* s)
intclose(intfd)
int kill(pid_tpid, int sig)
intsystem(const char* c)
```

## Slide 49

### Bypassing CFI Defenses

## Slide 50

##### Approach

- W  u      …

   - Return to arbitrary gadgets: ROP

   - Jump to arbitrary gadgets: JOP

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
¢ We used to...
¢ Return to arbitrary gadgets: ROP
¢ Jump to arbitrary gadgets: JOP
@@00
```

## Slide 51

##### Approach

- W  u      …

   - Return to arbitrary gadgets: ROP   Backward-edge CFI

   - Jump to arbitrary gadgets: JOP      Forward-edge CFI

- How is a new exploitation technique built?

## Slide 52

##### Approach

###### Gadgets

```
…
incrax
ret
```

```
…
pop rdi
ret
```

```
…
pop rsi
ret
```

```
…
mov rdx, rcx
ret
```

## Slide 53

##### Approach

###### Dispatcher

Gadgets

```
…
incrax
ret
```

```
…
pop rdi
ret
```

```
…
pop rsi
ret
```

```
…
mov rdx, rcx
ret
```

## Slide 54

Dispatcher

Approach

Gadgets

Dispatcher table

```
…
incrax
ret
…
pop rdi
ret
```

```
…
pop rsi
ret
```

```
…
mov rdx, rcx
ret
```

## Slide 55

##### Approach

- Ev r                  h  qu  mu   h v    m  f rm  f…

   - Dispatcher: a loop that iterates over gadgets

   - Dispatcher table: memory containing the gadgets to call

   - Gadgets: code to be executed e.g., set registers, etc

## Slide 56

##### COOP

- Counterfeit Object-Oriented Programming (COOP)

   - Leverage virtual pointers (VPs) in C++

```
class Student {
virtual void study();
}
```

- Dispatcher: a loop that calls VPs

- Dispatcher table: overwritten VPs

```
class Course {
```

- Gagdets: (complete) virtual functions `class Course { Student **students; virtual func(){`

```
for(;;){
students[i]->study();
```

```
}
```

```
}
```

```
}
```

## Slide 57

##### How to bypass CFI

- Bypassing coarse-grained CFI (CET and CFG) requires

   - Not tampering with return addresses

   - Tampering with code pointers in writable memory, but only pointing them to the beginning of functions

- Bypassing fine _r_ -grade CFI (LLVM CFI) requires

   - Finding some useful collision (rare)

   - Otherwise, every pointer is instrumented

## Slide 58

##### How to bypass CFI

- Bypassing coarse-grained CFI (CET and CFG) requires

   - Not tampering with return addresses

   - Tampering with code pointers in writable memory, but only pointing them to the beginning of functions

- Bypassing fine _r_ -grade CFI (LLVM CFI) requires

   - Finding some useful collision (rare)

   - Otherwise, every pointer is instrumented

Is this really true though?

## Slide 59

### C++20 Coroutines

## Slide 60

##### What is a Coroutine

• TL;DR: A coroutine is a function that can suspend and resume

```
void foo()
{
```

```
void bar()
{
```

bar();

```
…
```

```
bar();
```

```
}
```

```
}
```

## Slide 61

##### What is a Coroutine

• TL;DR: A coroutine is a function that can suspend and resume

Function
void foo() void bar()
{ {
bar();
…
bar();
} }

## Slide 62

##### What is a Coroutine

###### • TL;DR: A coroutine is a function that can suspend and resume

Function
void foo() void bar()
{ {
bar();
…
bar();
} }

## Slide 63

##### What is a Coroutine

• TL;DR: A coroutine is a function that can suspend and resume

###### Coroutine

void foo() void coro()
{ {
coro();
<suspend>;
coro(); Suspension
} }
point (SP)

## Slide 64

##### What is a Coroutine

• TL;DR: A coroutine is a function that can suspend and resume

Coroutine
void foo() void coro()
{ {
coro();
<suspend>;
coro();
} }

## Slide 65

##### The Coroutine (task) Object

• Every coroutine returns a _task_ object, that describes its state

```
void foo()
{
taskt = coro();
}
```

```
taskcoro()
{
```

```
...
<suspend>;
```

```
...
}
```

## Slide 66

##### Coroutine Handle

• The coroutine handle refers to an instance of a coroutine

```
void foo()
{
```

```
task t1 = coro();
coroutine_handle<> h1 = t1.handle;
}
```

```
taskcoro()
{
```

```
...
<suspend>;
...
}
```

## Slide 67

##### Coroutine Handle

• The coroutine handle refers to an instance of a coroutine

```
void foo()
{
```

```
coroutine_handle<> h1 = coro().handle;
coroutine_handle<> h2 = coro().handle;
}
```

```
taskcoro()
{
```

```
...
<suspend>;
```

```
...
```

```
}
```

## Slide 68

##### Coroutine Handle

• The coroutine handle allows _resuming_ & _destroying_ a coroutine

```
void foo()
{
```

```
coroutine_handle<> h1 = coro().handle;
coroutine_handle<> h2 = coro().handle;
h1.resume();
```

```
taskcoro()
{
```

`...` h1 `<suspend>; ... }`

```
}
```

## Slide 69

##### Coroutine Handle

• The coroutine handle allows _resuming_ & _destroying_ a coroutine

```
void foo()
{
```

```
coroutine_handle<> h1 = coro().handle;
coroutine_handle<> h2 = coro().handle;
h1.resume();
h2.resume();
```

```
taskcoro()
{
```

`...` h1&h2 `<suspend>;`

```
...
```

```
}
```

```
}
```

## Slide 70

##### Coroutine Handle

• The coroutine handle allows _resuming_ & _destroying_ a coroutine

```
void foo()
{
```

```
coroutine_handle<> h1 = coro().handle;
coroutine_handle<> h2 = coro().handle;
h1.destroy();
```

```
taskcoro()
{
```

```
...
<suspend>;
```

```
...
```

```
}
```

```
}
```

## Slide 71

##### What is a Coroutine

• The compiler treats a function as a coroutine whenever one of the three coroutine keywords appear:

`void coro() {` co_await `<suspend>;` co_yield `}` co_return

## Slide 72

##### What is a Coroutine

- _co_yield_ suspends and returns a value

`task fib() void main() { { int a=0, b=1; handle coro = fib().handle; for(;;){ co_yield a+b; coro.resume(); int temp = b;` _returns 1_ `coro.resume(); b = a+b; coro.resume(); a = temp; } } }`

## Slide 73

##### What is a Coroutine

• _co_yield_ suspends and returns a value

task fib()
void main()
{
{
int a=0, b=1;
handle coro = fib().handle;
for(;;){
co_yield a+b;
coro.resume();
int temp = b;
coro.resume();
b = a+b;
returns 2
coro.resume();
a = temp;
}
}
}

## Slide 74

##### What is a Coroutine

• _co_yield_ suspends and returns a value

task fib()
void main()
{
{
int a=0, b=1;
handle coro = fib().handle;
for(;;){
co_yield a+b;
coro.resume();
int temp = b;
coro.resume();
b = a+b;
coro.resume();
a = temp;
returns 3
}
}
}

## Slide 75

##### What is a Coroutine

• _co_return_ suspends and returns a value

`void main() { handle coro = fib().handle; coro.resume();` _returns for_ `coro.resume();` _the final time_ `coro.resume(); }`

```
task fib()
{
```

```
int a=0, b=1;
for(int i=0; i<10; i++){
co_yielda+b;
int temp = b;
b = a+b;
a = temp;
```

```
}
co_returna+b;
}
```

## Slide 76

##### Returning a value

• Coroutines return values by storing them in the promise object

```
void main()
task coro()
{
{
handle coro= coro().handle;
co_return42;
}
coro.resume();
int res = coro.promise().value;
}
```

## Slide 77

##### (Basic) Coroutine Lifetime

Creation stub

```
void foo()
{
coroutine_handle<> h = coro().handle;
h.resume();
h.destroy();
}
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
EQ j Be: Wines” = y gy so / J J »>—
Nene (Basic) Coroutine Lifetime -
void foo()
{
coroutine_handle<> h = .handle;
h.resume();
h.destroy();
}
@@@0
```

## Slide 78

##### (Basic) Coroutine Lifetime

Creation
stub

Resume stub

```
void foo()
{
```

```
coroutine_handle<> h = coro().handle;
h.resume();
h.destroy();
}
```

## Slide 79

##### (Basic) Coroutine Lifetime

Creation
stub

Resume
stub

Destroy
stub

```
void foo()
{
coroutine_handle<> h = coro().handle;
h.resume();
h.destroy();
}
```

## Slide 80

##### (Basic) Coroutine Lifetime

```
task coro()
{
co_return42;
}
```

```
task
{
```

```
}
```

```
void foo()
{
```

```
handle h = coro().h;
h.resume();
h.destroy();
}
```

## Slide 81

##### (Basic) Coroutine Lifetime

```
task coro()
{
co_return42;
}
```

```
task
{
handle h;
struct promise_type{};
}
```

```
void foo()
{
```

```
handle h = coro().h;
h.resume();
h.destroy();
}
```

## Slide 82

##### (Basic) Coroutine Lifetime

```
task coro()
{
```

```
co_return42;
}
```

```
task
{
```

```
handle h;
struct promise_type
{
```

```
void foo()
{
```

```
handle h = coro().h;
}
h.resume();
h.destroy();
}
```

```
int return_value;
suspend_alwaysinitial_suspend();
suspend_alwaysfinal_suspend();
};
```

## Slide 83

##### (Basic) Coroutine Lifetime

```
task coro()
{
co_return42;
}
```

```
task
{
```

```
handle h;
struct promise_type
{
```

```
void foo()
{
```

```
handle h = coro().h;
h.resume();
h.destroy();
}
```

```
}
```

```
int return_value;
suspend_alwaysinitial_suspend();
suspend_alwaysfinal_suspend();
};
```

Resume Destroy stub stub

Creation stub

## Slide 84

##### (Basic) Coroutine Lifetime

###### function foo()

coroutine coro()

```
task
{
handle h;
struct promise_type
{
int return_value;
suspend_alwaysinitial_suspend();
suspend_alwaysfinal_suspend();
};
}
void foo()task coro()
{ {
handle h = coro().h;co_return42;
h.resume();}
h.destroy();
```

Creation Stub Create & Initialize ?

Creation Stub coro() Create & Initialize ? returns Initial_suspend() _task_ ( _lazy start_ )

```
}
```

## Slide 85

(Basic) Coroutine Lifetime function foo() coroutine coro() Creation Stub coro() Create & Initialize ? returns Initial_suspend() `initial_suspend();` _task_ ( _lazy start_ ) `final_suspend();;` Resume Stub h.resume() Resume ? coroutine `task coro()` co_return `{` final_suspend()

```
task
{
handle h;
struct promise_type
{
```

```
int return_value;
suspend_alwaysinitial_suspend();
suspend_alwaysfinal_suspend();;
};
}
```

```
void foo()task coro()
{ {
handle h = coro().h;co_return42;
h.resume();}
h.destroy();
```

```
}
```

## Slide 86

(Basic) Coroutine Lifetime function foo() coroutine coro() `task` Creation Stub coro() `{` Create & Initialize `handle h;` ? `struct promise_type {` returns `int return_value;` Initial_suspend() `suspend_always initial_suspend();` _task_ ( _lazy start_ ) `suspend_always final_suspend(); };` Resume Stub `}` h.resume() Resume ? coroutine `void foo() task coro()` co_return `{ {` final_suspend() `handle h = coro().h; co_return 42; h.resume(); }` Destroy Stub `h.destroy();` h.destroy() `}` Destroys ?

## Slide 87

##### The Coroutine Frame

- Coroutines in C++ are stackless

   - Can only be suspended from the coroutine itself (you cannot call another function and suspend from there)

   - Other stackless coroutines: C#, JS, Python, Rust, Swift

## Slide 88

##### The Coroutine Frame

- Coroutines in C++ are stackless

   - Can only be suspended from the coroutine itself (you cannot call another function and suspend from there)

   - Other stackless coroutines: C#, JS, Python, Rust, Swift

- The coroutine is stored in a heap-allocated coroutine frame

      - `void foo() {`

```
coroutine_handle<> h1 = coro().handle;
coroutine_handle<> h2 = coro().handle;
}
```

2 allocated frames

## Slide 89

handle

##### The Coroutine Frame

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
lackhat wy Y
blackiat The Coroutine Frame -~
handle
resume pointer | destroy pointer
@@@0
```

## Slide 90

The Coroutine Frame
handle

###### handle

handle.resume()
handle
call [rdi]
resume ptr

• Points to the resume stub

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
resume pointer
The Co
destroy pointer
Co utine Arr , if
call [rdil]
¢ Points to the
handle.resume()
@@@0
```

## Slide 91

##### The Coroutine Frame

###### handle

handle.destroy()

handle
call [rdi+0x8]
destroy ptr

• Points to the destroy stub

## Slide 92

##### The Coroutine Frame

###### handle

```
handle.destroy()
```

handle
call [rdi+0x8]
destroy ptr

```
void resume() const{
coro_resume(pointer_to_frame);
}
void destroy() const{
coro_destroy(pointer_to_frame);
}
```

## Slide 93

The Coroutine Frame

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
resume pointer
destroy pointer
resume pointer
destroy pointer
resume pointer
destroy pointer
resume pointer
destroy pointer
@@@0
```

## Slide 94

##### The Coroutine Frame

###### handle

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2) 7 y ga uf A
lackhat ina A
blackhat The Coroutine Frame
resume pointer | destroy pointer
promise object
?
@@@0
```

## Slide 95

handle

##### The Coroutine Frame

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
lackhat we Y ,
mache The Coroutine @ Frathe -
destroy pointer
promise object
parameters
?
@@@0
```

## Slide 96

##### The Coroutine Frame

```
void main()
{
coro(42);
}
```

```
task coro(int arg)
{
co_return;
}
```

## Slide 97

##### The Coroutine Frame

```
void main()
{
string s = “hello”;
coro(s);
}
task coro(string arg)
{
```

```
co_return;
}
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Ni Y er > ———_
I t A ae / 4 vy
blackhat The Coroutine Frame -~
{
string s = “hello”:
coro(s);
:
task coro(string )
Pe
co_return;
@@@0
```

## Slide 98

##### The Coroutine Frame

```
void main()
{
char* buf;
coro(buf);
}
task coro(char* arg)
{
co_return;
}
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
void main()
{
char* buf;
coro(buf);
} arg = <ptr to buf>
task coro(char*
{
co_return;
5
@@@0
```

## Slide 99

##### The Coroutine Frame

###### handle

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Q
| handle |
destroy pointer
promise object
parameters
local variables
lackhat a re
blackhat The Coroutine Frame
@@@0
```

## Slide 100

##### The Coroutine Frame

###### Stack

```
task coro()
{
int var1,var2,var3,var4;
}
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
o aS Za if! A > ee
blackhat The Coroutine Frame -
Stack
* task coro()
t
int varl1,var2,var3,var4,;
5
@@@0
```

## Slide 101

##### The Coroutine Frame

###### Heap

```
task coro()
{
```

```
int var1,var2,var3,var4;
}
```

- Stack-based vars → heap-based vars

- Heap-based vars → heap-based vars

###### Stack

## Slide 102

##### The Coroutine Frame

Heap

```
task coro()
{
```

```
Object *obj= new Object();
}
```

- Stack-based vars → heap-based vars

- Heap-based vars → heap-based vars

## Slide 103

##### The Coroutine Frame

###### Heap

```
task coro()
{
char buffer[];
int var1,var2,var3;
}
```

- Compiler _sometimes_ reorders “stack-based” buffers to safer positions (we will see when) Stack

## Slide 104

##### The Coroutine Frame

###### handle

CI = 0 `task coro() {` CI = 1 `co_yield` CI = 2 `co_yield`

```
co_yield“one”;
co_yield“two”;
co_return“three”;
}
```

CI = 3

## Slide 105

##### The Stubs in Depth

Creation stub

Resume stub

Destroy stub

```
coroframecreation_stub()
{
coroframe= new()
coroIndex= 0;
resumePtr= &resume_stub
destroyPtr= &destroy_stub
return coroframe;
}
```

## Slide 106

##### The Stubs in Depth

Creation stub Resume stub

```
void resume_stub(coroFrame)
{
switch(coroFrame.coroIndex)
{
```

```
case 0:
//first suspension point
case 1:
//second SP
default:
//err
}
}
```

Destroy stub

## Slide 107

##### The Stubs in Depth

```
void resume_stub(coroFrame)
{
switch(coroFrame.coroIndex)
{
```

Creation `{` stub `switch(coroFrame.coroIndex) { case 0: cout << “Hello”;` Resume `case 1:` stub `cout << “Bye”; default: //err }` Destroy `}` stub

```
task coro()
{
cout<< “Hello”;
<SP>
cout<< “Bye”;
}
```

## Slide 108

##### The Stubs in Depth

`void resume_stub(coroFrame) {` Creation `switch(coroFrame.coroIndex)` stub `{ case 0: initial_suspend(); cout << “Hello”;` Resume `case 1:` stub `cout << “Bye”; final_suspend(); default: { //err` Destroy `}` stub `}`

```
task coro()
{
cout<< “Hello”;
<SP>
cout<< “Bye”;
}
```

## Slide 109

##### The Stubs in Depth

Creation
stub

Resume stub

```
void destroy_stub(coroFrame)
{
deletecoroFrame;
}
```

Destroy stub

## Slide 110

##### What is a Coroutine

• The compiler treats a function as a coroutine whenever one of the three coroutine keywords appear:

`void coro() {` co_await

```
<suspend>;
}
```

co_yield

co_return

## Slide 111

##### Coroutine Awaiting

- _co_await_ evaluates an awaitable

- Use cases:

   - Asynchronous jobs

   - Awaitable coroutines

   - Cooperative multitasking

## Slide 112

##### Coroutine Awaiting

```
void func()
{
//Execute async
result= async_task();
//Do something else meanwhile
meanwhile();
```

```
...
```

```
//When result is ready, do sth
something(result);
}
```

## Slide 113

##### Coroutine Awaiting

• Without coroutines, callbacks would typically be used `void func() {`

```
//Read the length, then read the buffer
async_read(len, when_done={
async_read(buf, when_done={
process_buffer(buf());
```

```
}
```

```
}
```

```
}
```

## Slide 114

##### Coroutine Awaiting

• Without coroutines, callbacks would typically be used `void func() { //Read the length, then read the buffer async_read(len, when_done={ async_read(buf, when_done={ process_buffer(buf()); async_other(…, when_done={ process_buffer(buf());`

```
}
```

```
…
```

```
}
```

```
}
}
```

## Slide 115

##### Coroutine Awaiting

- With coroutines, code looks synchronous but is actually not

- • In simple terms, _co_await_ suspends the coroutine and does something else

```
task coro()
{
len= co_awaitasync_read();
buf= co_awaitasync_task();
...
}
```

## Slide 116

##### Coroutine Awaiting

- _co_await_ evaluates an awaitable

```
task coroutine()
{
```

```
co_awaitAwaitable{};
}
```

co_await

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
3 yy / “* i 4 > SZ >
+) is eae — v7, Y i >. ‘ lf 2 fi’ i, 5S
blackhat Covbuthes Awaiting yp
° evaluates an awaitable
task coroutine()
{
5
Awaitable{};
@@@0
```

## Slide 117

##### Coroutine Awaiting

- _co_await_ evaluates an awaitable

```
task coroutine()
{
```

```
co_awaitAwaitable{};
}
```

```
struct Awaitable
{
```

```
Awaiteroperator co_await()
{
```

```
return{};
}
```

```
}
```

co_await Awaitable

## Slide 118

##### Coroutine Awaiting

- The _awaiter_ controls what happens at the co_await point

   - Maybe it suspends, or it executes something else…

```
struct Awaitable
{
```

```
Awaiteroperator co_await()
{
```

```
return{};
}
```

```
}
```

```
struct Awaiter()
{
```

```
bool await_ready();
```

```
void await_suspend(…);
```

```
void await_resume();
```

```
}
```

co_await Awaitable

Awaiter

## Slide 119

##### Coroutine Awaiting

- The _awaiter_ controls what happens at the co_await point

   - Maybe it suspends, or it executes something else…

```
task coroutine()
{
```

```
co_awaitAwaiter{};
}
```

```
struct Awaiter()
{
```

```
bool await_ready();
```

```
void await_suspend(…);
```

```
void await_resume();
```

- `}`

co_await Awaiter

## Slide 120

Coroutine Awaiting

```
struct Awaiter()
{
bool await_ready();
void await_suspend(…);
void await_resume();
}
```

Do we need to suspend the coroutine?

## Slide 121

##### Coroutine Awaiting

###### `struct Awaiter() {`

```
bool await_ready();
void await_suspend(…);
void await_resume();
}
```

The coroutine is now suspended. Do you want to do something with the suspended coroutine?

co_await

Awaiter

## Slide 122

##### Coroutine Awaiting

```
void await_suspend(coroutine_handlesuspended_coro)
{
```

```
//coroutine suspended, return to the caller of the coroutine
}
```

co_await Awaiter

## Slide 123

##### Coroutine Awaiting

```
void await_suspend(coroutine_handlesuspended_coro)
{
```

- `Execute async code`

- • `Start new threads`

- `Resume the coroutine: suspended_coro.resume()`

```
//coroutine suspended, return to the caller of the coroutine
```

```
}
```

## Slide 124

##### Coroutine Awaiting

```
struct Awaiter()
{
```

```
bool await_ready();
void await_suspend(…);
void await_resume();
}
```

Anything to do before resuming the coroutine?

co_await

Awaiter

## Slide 125

##### co_await Example

```
task coro()
{
```

```
//
co_awaitAwaiter{};
//
}
```

```
void func()
{
```

```
handler h = coro();
h.resume();
```

```
struct Awaiter
{
```

```
bool await_ready(){}
void await_suspend(h)
{
```

```
std::thread((){
```

```
<time expensive work>
handle.resume();
}).detach();
}
void await_resume(){};
}
```

```
...
}
```

## Slide 126

co_await Example

```
task coro()
{
```

```
//
co_awaitAwaiter{};
//
}
```

```
void func()
{
```

```
handler h = coro();
h.resume();
```

```
struct Awaiter
{
```

```
bool await_ready(){}
void await_suspend(h)
{
```

```
std::thread((){
<time expensive work>
handle.resume();
}).detach();
```

```
}
void await_resume(){};
}
```

```
...
```

```
}
```

## Slide 127

co_await Example

```
task coro()
{
```

```
//
co_awaitAwaiter{};
//
}
```

```
void func()
{
```

```
handler h = coro();
h.resume();
```

```
struct Awaiter
{
```

```
bool await_ready(){}
void await_suspend(h)
{
```

```
std::thread((){
<time expensive work>
handle.resume();
}).detach();
}
void await_resume(){};
}
```

```
...
}
```

## Slide 128

co_await Example

```
task coro()
{
```

```
//
co_awaitAwaiter{};
//
}
```

```
void func()
{
```

```
handler h = coro();
h.resume();
```

```
struct Awaiter
{
```

```
bool await_ready(){}
void await_suspend(h)
{
```

```
std::thread((){
<time expensive work>
handle.resume();
}).detach();
}
void await_resume(){};
}
```

```
...
}
```

## Slide 129

##### co_await Example

```
task coro()
{
//
co_awaitAwaiter{};
//
}
```

```
void func()
{
handler h = coro();
h.resume();
<something else>
}
```

```
struct Awaiter
{
```

`bool await_ready(){} void await_suspend(h) {` THREAD 1

`std::thread((){` t1 `<time expensive work handle.resume(); }).detach(); } void await_resume(){};`

```
}
```

## Slide 130

##### co_await Example

```
task coro()
{
//
co_awaitAwaiter{};
//
}
void func()
{
```

`handler h = coro(); h.resume();` t2 `<something else> }`

```
struct Awaiter
{
```

`bool await_ready(){} void await_suspend(h) {` THREAD 1

`std::thread((){ <time expensive work>` t1 `handle.resume(); }).detach(); } void await_resume(){}; }`

## Slide 131

##### co_await Example

```
task coro()
{
//
co_awaitAwaiter{};
//
}
void func()
{
```

`handler h = coro(); h.resume();` t2 `<something else> }`

```
struct Awaiter
{
```

```
bool await_ready(){}
void await_suspend(h)
{
```

```
std::thread((){
<time expensive work>
handle.resume();
}).detach();
```

`}` t1 `void await_resume(){}; }`

## Slide 132

##### co_await Example

```
struct Awaiter
{
```

`struct Awaiter task coro() { { // bool await_ready(){} void await_suspend(h) co_await Awaiter{}; { // std::thread((){ } <time expensive work> void func() handle.resume(); { }).detach(); handler h = coro(); } h.resume(); void await_resume(){}; }` t2 `<something else> }`

## Slide 133

co_await Example

```
task coro()
{
//
co_awaitAwaiter{};
//
}
void func()
{
```

`handler h = coro(); h.resume();` t2 t1 `<join> }`

```
struct Awaiter
{
```

```
bool await_ready(){}
void await_suspend(h)
{
```

```
std::thread((){
<time expensive work>
handle.resume();
}).detach();
}
void await_resume(){};
}
```

## Slide 134

##### Co_awaiting Coroutines

```
task
{
```

```
handle h;
struct promise_type
{
```

```
int return_value;
suspend_alwaysinitial_suspend();
suspend_alwaysfinal_suspend();
};
```

```
}
```

## Slide 135

##### Co_awaiting Coroutines

```
task
{
```

```
handle h;
struct promise_type
{
```

```
int return_value;
suspend_alwaysinitial_suspend();
suspend_alwaysfinal_suspend();
};
struct awaiter
{
bool await_ready();
void await_suspend();
void await_resume();
```

```
}
```

```
}
```

## Slide 136

##### Co_awaiting Coroutines

```
task
```

```
{
```

```
task coro2()
{
co_return;
}
```

```
co_return;
```

```
task coro1()
{
```

```
co_awaitcoro2();
```

}

```
handle h;
struct promise_type
{
```

```
int return_value;
suspend_alwaysinitial_suspend();
suspend_alwaysfinal_suspend();
```

```
};
struct awaiter
{
```

```
bool await_ready();
void await_suspend();
void await_resume();
```

```
}
```

```
}
```

## Slide 137

Use Cases

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Se si ZG f°
piStichat Nuts SS ZA
BRIEFINGS ;
coro’
LLLLMWLLLLLLLLL LLLLLLA
@@@0
```

## Slide 138

Use Cases

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
LLLLLLA
coro2
@@@0
```

## Slide 139

CFOP

## Slide 140

##### Threat model

###### • CFI threat model:

- ASLR bypassed

- Infinite number of arbitrary memory writes

## Slide 141

##### Threat model

- CFI threat model:

   - ASLR bypassed

   - Infinite number of arbitrary memory writes

- Our threat model:

   - ASLR bypassed

   - Attacker can leverage a single memory corruption vulnerability

   - At lease one coroutine in the code

   - CFI is in place

## Slide 142

Threat model
LLVM
Intel LLVM Safe
CFI
CET KCFI Dispatch
(icall)
Control
MCFI/ Path
Flow ReCFI VfGuard
piCFI Armor
Guard
CFIXX PittyPat VTrust Typro

## Slide 143

##### Observations

• The coroutine handles and frames are writable

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
+) 7% Sie “ y ~~ \ 1 y a (f oassee
black hat x
BRIEFINGS Oo
¢« The coroutine and are writable
destroy pointer
promise object
parameters
local variables
coroutine index
coroutine
handle
```

## Slide 144

##### Attack primitives

###### FRAME MANIPULATION

• Modifying existing frames

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
FRAME
¢ Modifying frames
destroy pointer
promise object
parameters
local variables
coroutine index
```

## Slide 145

##### Attack primitives

###### FRAME MANIPULATION

###### FRAME INJECTION

- Modifying existing frames

- Inserting new frames

FAKE
FRAME

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
gQ se hy : | =
Blackhat A mitives -
FRAME MANIPULATION FRAME
Modifying existing frames ¢ Inserting frames
resume pointer | destroy pointer
destroy pointer
promise object
parameters
resume pointer | destroy pointer
promise object
coroutine pointer . .
promise object
coroutine index
parameters
parameters
coroutine pointer
FA K E coroutine index
local variables
FRAME
coroutine index
```

## Slide 146

##### DOA: Data Only Attack

• Modifying the runtime data of a program can lead to arbitrary code execution

• Data-Only Attacks (DOA) use frame manipulation

## Slide 147

##### DOA: Data Only Attack

```
task coro(char* arg)
{
```

```
co_awaitsome_task;
co_awaitsome_task;
system(arg);
}
```

## Slide 148

##### DOA: Data Only Attack

Creation
Resume stub
Stub
(SP0) SP1 SP2 SP3

```
task coro(char* arg)
{
//SP1//
co_awaitsome_task;
//SP2//
co_awaitsome_task;
//SP3//
system(arg);
}
```

## Slide 149

##### DOA: Data Only Attack

Creation Resume stub Stub (SP0) SP1 SP2 SP3 Init Vuln Vuln Vuln arg

```
task coro(char* arg)
{
//SP1//
co_awaitsome_task;
//SP2//
co_awaitsome_task;
//SP3//
system(arg);
}
```

1. Arguments are copied in the frame during the creation stub

## Slide 150

##### DOA: Data Only Attack

Creation
Resume stub
Stub
(SP0) SP1 SP2 SP3
task coro(char* arg)
{
Init Vuln Vuln Vuln
arg
//SP1//
co_await some_task;
//SP2//
co_await some_task;
//SP3//
system(arg);
}
1. Arguments are copied in the frame
during the creation stub

## Slide 151

##### DOA: Data Only Attack

arg

Creation
Resume stub
Stub
(SP0) SP1 SP2 SP3
Init Vuln Vuln Vuln

Init

```
task coro(char* arg)
{
//SP1//
char arr[10];
co_awaitsome_task;
//SP2//
co_awaitsome_task;
//SP3//
getline(arr);
}
```

## Slide 152

##### DOA: Data Only Attack

Creation
Resume stub
Stub
(SP0) SP1 SP2 SP3
Init Vuln Vuln Vuln
arg
— — —
arr Init

```
task coro(char* arg)
{
```

```
//SP1//
char arr[10];
co_awaitsome_task;
//SP2//
co_awaitsome_task;
//SP3//
getline(arr);
}
```

2. Local variables are copied to the frame on the same SP where they are first **initialized** .

## Slide 153

##### DOA: Data Only Attack

Creation
Resume stub
Stub
(SP0) SP1 SP2 SP3
Init Vuln Vuln Vuln
arg
— — —
arr Init
— —
arr2 Init Vuln

```
task coro(char* arg)
{
//SP1//
co_awaitsome_task;
//SP2//
chararr2 = “hello”;
co_awaitsome_task;
//SP3//
puts(arr2);
}
```

2. Local variables are copied to the frame on the same SP where they are first initialized.

## Slide 154

##### DOA: Data Only Attack

Creation
Resume stub
Stub
(SP0) SP1 SP2 SP3
Init Vuln Vuln Vuln
arg
— — —
arr Init
— —
arr2 Init Vuln

```
task coro(char* arg)
{
//SP1//
co_awaitsome_task;
//SP2//
void *ptr;
for(int ii=0; ii<3; ii++)
{
```

```
co_awaitsome_task;
//SP3//
write(ptr, 100);
}
}
```

## Slide 155

##### DOA: Data Only Attack

Creation Resume stub Stub (SP0) SP1 SP2 SP3 Init Vuln Vuln Vuln arg — — — arr Init — — arr2 Init Vuln — — ii Init Vuln — — — ptr Vuln

TIP:  Local variables used inside a loop are always hijackable at some SP.

```
task coro(char* arg)
{
//SP1//
co_awaitsome_task;
//SP2//
void *ptr;
for(int ii=0; ii<3; ii++)
{
```

```
co_awaitsome_task;
//SP3//
write(ptr, 100);
}
}
```

## Slide 156

##### DOA: Data Only Attack

Creation Resume stub Stub (SP0) SP1 SP2 SP3 Init Vuln Vuln Vuln arg — — — arr Init — — arr2 Init Vuln — — ii Init Vuln — — — ptr Vuln

```
task coro(char* arg)
{
//SP1//
co_awaitsome_task;
//SP2//
co_awaitsome_task;
//SP3//
int value = 0;
value++;
}
```

## Slide 157

##### DOA: Data Only Attack

Creation Resume stub Stub (SP0) SP1 SP2 SP3 Init Vuln Vuln Vuln arg — — — arr Init — — arr2 Init Vuln — — ii Init Vuln — — — ptr Vuln value (stack based local variable)

```
task coro(char* arg)
{
//SP1//
co_awaitsome_task;
//SP2//
```

```
co_awaitsome_task;
//SP3//
int value = 0;
value++;
}
```

## Slide 158

##### Advanced DOAs

```
task coro(char* arg)
{
//SP1//
vector<int> vec;
vec.push_back(1);
co_awaitsome_task;
//SP2//
co_awaitsome_task;
//SP3//
}
```

## Slide 159

##### Advanced DOAs

```
task coro(char* arg)
{
//SP1//
initial_suspend();
vector<int> vec;
vec.push_back(1);
co_awaitsome_task;
//SP2//
co_awaitsome_task;
//SP3//
<FREE ALL VARIABLES>
final_suspend();
}
```

## Slide 160

##### Advanced DOAs

- Arbitrarily free() chunks

- Need to prepare chunk metadata

```
free(vec)
```

freed
chunk

```
task coro(char* arg)
{
```

```
//SP1//
initial_suspend();
vector<int> vec;
vec.push_back(1);
co_awaitsome_task;
//SP2//
```

```
co_awaitsome_task;
//SP3//
<FREE ALL VARIABLES>
final_suspend();
}
```

## Slide 161

##### Advanced DOAs

g++-14 _-O0_ No reordering clang++-19

```
task coro(char* arg)
{
```

```
//SP1//
char arr[10];
vector<int> vec;
co_awaitsome_task;
//SP2//
```

```
}
```

• Some compilers do variable reordering at –O3, but they do it funny

## Slide 162

##### Advanced DOAs

g++-14 _-O0_ No reordering clang++-19

```
task coro(char* arg)
{
```

```
//SP1//
vector<int> vec;
char arr[10];
```

```
co_awaitsome_task;
//SP2//
```

```
}
```

## Slide 163

##### Advanced DOAs

#### g++-14 _-O3_ No reordering

```
task coro(char* arg)
{
//SP1//
char arr[10];
vector<int> vec;
co_awaitsome_task;
//SP2//
```

```
}
```

## Slide 164

##### Advanced DOAs

#### g++-14 _-O3_ No reordering

```
task coro(char* arg)
{
//SP1//
vector<int> vec;
char arr[10];
co_awaitsome_task;
//SP2//
```

```
}
```

## Slide 165

##### Advanced DOAs

clang++-19 _-O3_ Safe reordering

```
task coro(char* arg)
{
```

```
//SP1//
char arr[10];
int value;
co_awaitsome_task;
//SP2//
```

```
}
```

## Slide 166

##### Advanced DOAs

clang++-19 _-O3_

Ok, that was weird

```
task coro(char* arg)
{
//SP1//
vector<int> vec;
vector<int> vec2;
char arr[10];
co_awaitsome_task;
//SP2//
}
```

- The reordering rules for clang are a bit messed up

## Slide 167

##### Advanced DOAs

clang++-19 _-O3_

#### Ok, that was weird

```
task coro(char* arg)
{
```

```
//SP1//
int value;
char arr[10];
co_awaitsome_task;
//SP2//
```

```
}
```

- The reordering rules for clang are a bit messed up

## Slide 168

##### Advanced DOAs

- The compiler saves space in the frame by reusing addresses for SP-exclusive variables.

- r  b        b  ‘r u   ’ wr  g        h r  P .

```
task coro(char* arg)
{
```

```
//SP1//
int val1;
co_awaitsome_task;
//SP2//
int val2;
```

```
}
```

## Slide 169

##### Revisiting the Threat model

• Launching a DOA (and other CFOP attacks) requires either frame manipulation or frame injection

- Options:

1. Arbitrary memory write

## Slide 170

##### Revisiting the Threat model

• Launching a DOA (and other CFOP attacks) requires either frame manipulation or frame injection • Options:

1. Arbitrary memory write

2. Stack-based overflow overwriting handles

## Slide 171

##### Revisiting the Threat model

- Launching a DOA (and other CFOP attacks) requires either frame manipulation or frame injection

- • Options:

   1. Arbitrary memory write

   2. Stack-based overflow overwriting handles

      - The new frame could even be in the stack

## Slide 172

##### Revisiting the Threat model

- Launching a DOA (and other CFOP attacks) requires either frame manipulation or frame injection

- • Options:

   1. Arbitrary memory write

   2. Stack-based overflow overwriting handles

   3. Stack-based overflow inside the coroutine

      - L v r g     r  r  r  g…            k     r   !! :)

      - Parameters can always overflow almost the whole frame

      - At a minimum, you can always overwrite the coroutine index

      - In ptmalloc, you can overwrite frames further down the heap

## Slide 173

##### Revisiting the Threat model

• Launching a DOA (and other CFOP attacks) requires either frame manipulation or frame injection • Options:

1. Arbitrary memory write

2. Stack-based overflow overwriting handles

3. Stack-based overflow inside the coroutine

4. Heap-based overflow overwriting subsequent frames

## Slide 174

##### Revisiting the Threat model

• Launching a DOA (and other CFOP attacks) requires either frame manipulation or frame injection • Options:

1. Arbitrary memory write

2. Stack-based overflow overwriting handles

3. Stack-based overflow inside the coroutine

4. Heap-based overflow overwriting subsequent frames

5. Any combination of the previous or other bugs

   - DOAs -> arbitrary free() -> allocate one frame on top of the next one

## Slide 175

##### Observations

- The resume and destroy pointers in the frame can be hijacked

handle.resume()
handle
call [rdi]
resume ptr

handle.destroy()

handle
call [rdi+0x8]
destroy ptr

## Slide 176

Threat model
LLVM
Intel LLVM Safe
CFI
CET KCFI Dispatch
(icall)
Control
MCFI/ Path
Flow ReCFI VfGuard
piCFI Armor
Guard
CFIXX PittyPat VTrust Typro

## Slide 177

CFI Defenses in place
Coarse-grained
Finer-grained
LLVM
Intel LLVM Safe
CFI
CET KCFI Dispatch
(icall)
Control
MCFI/ Path
Flow ReCFI VfGuard
piCFI Armor
Guard
CFIXX PittyPat VTrust Typro
(Disclaimer: This classification is a bit subjective)

## Slide 178

##### Threat model

Restrictions
introduced
LLVM
Intel LLVM Safe • No return address
CFI
CET KCFI Dispatch hijacking
(icall)
Control
MCFI/ Path
Flow ReCFI VfGuard
piCFI Armor
Guard
CFIXX PittyPat VTrust Typro

## Slide 179

##### Threat model

LLVM
Intel LLVM Safe
CFI
CET KCFI Dispatch
(icall)
Control
MCFI/ Path
Flow ReCFI VfGuard
piCFI Armor
Guard
CFIXX PittyPat VTrust Typro

Restrictions introduced

- No return address

- hijacking

• No vptr hijacking

## Slide 180

##### Threat model

…Bu  f   -grained schemes will protect every indirect jump, right?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat — . UG,
BRIEFINGS hreat model
...But fine-grained schemes will
protect , right?
\Yy
```

## Slide 181

##### Threat model

- The two problems with fine-grained CFI:

   1. Most fine-grained schemes are academic, and do not support modern features (like coroutines)

## Slide 182

Threat model
Breaks with
LLVM
coroutines Intel LLVM Safe
CFI
CET KCFI Dispatch
(icall)
Control
MCFI/ Path
Flow ReCFI VfGuard
piCFI Armor
Guard
CFIXX PittyPat VTrust Typro

## Slide 183

##### Threat model

- The two problems with fine-grained CFI:

   1. Most fine-grained schemes are academic, and do not support modern features (like coroutines)

   2. New programming languages features break CFI, for which they were not prepared to deal with

## Slide 184

##### Threat model

Failed to keep up-to-date with coroutines
LLVM
Control
Intel LLVM Safe
CFI
Flow
CET KCFI Dispatch
Guard (icall)

- These fine-grained schemes do not generate instrumentation code for coroutine _resume_ and _destroy_ pointers.

(To be fair, SafeDispatch is for virtual calls, so unlike LLVM CFI, that was kinda expected)

## Slide 185

##### Threat model

- The two problems with fine-grained CFI:

   1. Most fine-grained schemes are academic, and do not support modern features (like coroutines)

   2. New programming languages features break CFI, for which they were not prepared to deal with

- In the future, new programming features may be added that break CFI as well. New possibilities :)

- CFI cannot be static, it needs to evolve

## Slide 186

##### Threat model

LLVM
Intel LLVM Safe
CFI
CET KCFI Dispatch
(icall)
Control
MCFI/ Path
Flow ReCFI VfGuard
piCFI Armor
Guard
CFIXX PittyPat VTrust Typro

Restrictions introduced

- No return address

- hijacking

- No vptr hijacking

- • Only jump to the beginning of functions

## Slide 187

##### Control Flow Hijacking

- What we have right now:

   - 1 arbitrary call with 0 arguments

- What we wish to have:

   - Infinitely many arbitrary calls with arbitrary arguments

## Slide 188

Dispatcher

Approach

Gadgets

Dispatcher table

```
…
incrax
ret
…
pop rdi
ret
```

```
…
pop rsi
ret
```

```
…
mov rdx, rcx
ret
```

## Slide 189

##### Control Flow Hijacking

• You do not need to overwrite the pointers for control flow hijacking! Just a _CFP_ .

- A _Controlled Frame Pointer_ (CFP) is any program pointer that indirectly or directly leads to control flow hijacking

• Also! There could be function pointers inside the frame, go for DOAs :)

## Slide 190

##### Control Flow Hijacking

• Sources of CFPs

1. Overwriting the _resume_ or _destroy_ pointers

## Slide 191

##### Control Flow Hijacking

- Sources of CFPs

1. Overwriting the _resume_ or _destroy_ pointers

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a ENeS Flow Hijacking -~
¢ Sources of CFPs
1.
resume pointer | destroy pointer
promise object
parameters
local variables
coroutine index
```

## Slide 192

##### Control Flow Hijacking

###### • Sources of CFPs

1. Overwriting the _resume_ or _destroy_ pointers

2. Overwriting a coroutine handle. But where?

- Schedulers

   - Look for databases

- Or browsers

<u>https://issues.chromium.org/issues/40251667 https://groups.google.com/a/chromium.org/g/cxx/c/ehMerLApxr8</u>

## Slide 193

##### Control Flow Hijacking

- Sources of CFPs

   1. Overwriting the _resume_ or _destroy_ pointers

   2. Overwriting a coroutine frame. But where?

3. Overwriting internal frame coroutine pointers

## Slide 194

##### The awesome world of Continuations

###### • Coroutines need to know how to resume the next coroutine

We know this
task c1() task c2()
{ {
co_await c2(); co_return;
} }
HOW??

## Slide 195

##### The awesome world of Continuations

• Coroutines need to know how to resume the next coroutine • Coroutines set continuation points for the next coroutine

continuation = c1
task c1() task c2()
{ {
co_await c2(); co_return;
} }
continuation.resume()

## Slide 196

##### The awesome world of Continuations

coroutine c1()

`task c1()` RP `{ //SP1` Resume Stub `co_await c2(); //SP2` //SP1 `}` co_await c2 //SP2 `task c2() {` final_suspend() `co_return; }` DP Destroy Stub Destroys F

## Slide 197

##### The awesome world of Continuations

coroutine c1()

```
task c1()
{
```

```
task
{
```

RP

`//SP1` Resume Stub `co_await c2(); //SP2` //SP1 `}` co_await c2 //SP2

```
handle h;
struct promise_type
{
```

```
int return_value;
suspend_alwaysinitial_suspend();
suspend_alwaysfinal_suspend();
};
struct awaiter
{
```

```
task c2()
{
co_return;
}
```

final_suspend()
DP
Destroy Stub
}
Destroys F

```
bool await_ready();
void await_suspend(h);
void await_resume();
```

```
}
```

## Slide 198

The awesome world of Continuations coroutine c1() coroutine c2() `task c1()` RP RP `{ //SP1` Resume Stub Resume Stub `co_await c2();` //SP1 `//SP2` //SP1 _await_suspend_ `}` final_suspend() c2.pms. **cont** =c1 c2.resume() DP `task c2() {` //SP2 Destroy Stub `co_return;` final_suspend() Destroys F `}` DP Destroy Stub Destroys F

## Slide 199

The awesome world of Continuations
coroutine c1() coroutine c2()
task c1()
RP RP
{
//SP1
Resume Stub
Resume Stub
co_await c2();
//SP1
//SP2 //SP1
await_suspend
} final_suspend
c2.pms.cont=c1
cont .resume()
c2.resume()
task c2()
{ //SP2 DP
co_return;
final_suspend()
Destroy Stub
}
Destroys F
DP
Destroy Stub
Destroys F

## Slide 200

##### The awesome world of Continuations

```
task
```

```
task c1()
{
```

```
//SP1
co_awaitc2();
//SP2
}
```

```
task c2()
{
```

```
co_return;
}
```

```
{
```

```
handle coro;
struct promise_type
{
```

```
int return_value;
suspend_alwaysinitial_suspend();
final_awaiterfinal_suspend();
```

```
};
struct awaiter
```

```
{
```

```
bool await_ready();
void await_suspend(h)
{
coro.continuation= h;
```

```
}
```

```
void await_resume();
```

```
}
```

```
struct final_awaiter
```

```
{
```

```
bool await_ready();
void await_suspend(h)
{
if(continuation) continuation.resume();
```

```
}
void await_resume()
```

```
}
```

```
}
```

## Slide 201

##### The awesome world of Continuations

• Wait, where is c2() destroyed?

```
task c1()task c2()
{{
co_awaitc2();co_return;
}}
```

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
x tN SE a 7 Yl > -. A y y “4 yy Tip ree8
blackhat ‘The awesome world of Continuations
¢ Wait, where is c2() destroyed?
task ci() task c2()
{ {
co_await c2(); co_return;
} }
```

## Slide 202

##### The awesome world of Continuations

- Wait, where is c2() destroyed?

   - Implicitly, right after co_await, as c2 goes out of scope

```
~task()
task c1()task c2()
{
{{
if(coro)
co_awaitc2();co_return;
c2.destroy();}coro.destroy();
}
}
```

## Slide 203

The awesome world of Continuations
coroutine c1() coroutine c2()
task c1()
RP RP
{
//SP1
Resume Stub
Resume Stub
co_await c2();
//SP1
//SP2 //SP1
await_suspend
} final_suspend
c2.pms. cont =c1
cont .resume()
c2.resume()
task c2() c2.destroy()
{ //SP2 DP
co_return; final_suspend
Destroy Stub
no continuation
}
Destroys F
DP
Destroy Stub
Destroys F

## Slide 204

The awesome world of Continuations

## Slide 205

##### Infinite Coroutine Chaining

- Infinite Coroutine Chaining (ICC) allows you to call arbitrary functions while maintaining control flow control

- If you have 2 CFPs, you can do ICC

   - First CFP: continuation point

   - Second CFP: task destroy

## Slide 206

Infinite Coroutine Chaining

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
biSekhat
BRIEFINGS
C1 c1' c1"
resume pointer resume pointer resume pointer
parameters parameters parameters
trampoline frame 4 ~—sttrampoline frame 3. ~—s trampoline frame 2 ~‘trampoline frame 1
Toe CTO
```

## Slide 207

Infinite Coroutine Chaining
coroutine c1() coroutine c1’() coroutine c1’’()
RP RP RP
c1
Resume Stub Resume Stub Resume Stub
//SP1 //SP1 //SP1
await_suspend await_suspend await_suspend
c2.destroy() c2.destroy() c2.destroy()
//SP2 //SP2 //SP2
final_suspend final_suspend final_suspend
DP DP DP
Destroy Stub Destroy Stub Destroy Stub
Destroys F Destroys F Destroys F

## Slide 208

Infinite Coroutine Chaining
coroutine c1() coroutine c1’() coroutine c1’’()
c1
RP RP RP
Resume Stub Resume Stub Resume Stub
//SP1 //SP1 //SP1
await_suspend await_suspend await_suspend
c2.destroy() c2.destroy() c2.destroy()
c1' //SP2 //SP2 //SP2
final_suspend final_suspend final_suspend
DP DP DP
Destroy Stub Destroy Stub Destroy Stub
Destroys F Destroys F Destroys F

## Slide 209

Infinite Coroutine Chaining
coroutine c1() coroutine c1’() coroutine c1’’()
c1'
RP RP RP
Resume Stub Resume Stub Resume Stub
//SP1 //SP1 //SP1
await_suspend await_suspend await_suspend
c2.destroy() c2.destroy() c2.destroy()
c1’’
//SP2 //SP2 //SP2
final_suspend final_suspend final_suspend
DP DP DP
Destroy Stub Destroy Stub Destroy Stub
Destroys F Destroys F Destroys F

## Slide 210

c1'

c1’’

Infinite Coroutine Chaining coroutine c1() coroutine c1’() RP RP Resume Stub Resume Stub //SP1 //SP1 _await_suspend await_suspend c2.destroy() c2.destroy()_

//SP2 _final_suspend_

//SP2 _final_suspend_

coroutine c1’’() RP

Resume Stub //SP1 _await_suspend_

c2.destroy()

//SP2
final_suspend

ARBITRARY CALL 1

## Slide 211

Infinite Coroutine Chaining
coroutine c1() coroutine c1’() coroutine c1’’()
c1'
RP RP RP
Resume Stub Resume Stub Resume Stub
//SP1 //SP1 //SP1
await_suspend await_suspend await_suspend
c2.destroy() c2.destroy() c2.destroy()
c1’’
//SP2 //SP2 //SP2
final_suspend final_suspend final_suspend
cont.resume()
ARBITRARY  ARBITRARY
CALL 2 CALL 1

## Slide 212

Infinite Coroutine Chaining
coroutine c1() coroutine c1’() coroutine c1’’()
c1'
RP RP RP
Resume Stub Resume Stub Resume Stub
//SP1 //SP1 //SP1
await_suspend await_suspend await_suspend
c2.destroy() c2.destroy() c2.destroy()
c1’’
//SP2 //SP2 //SP2
final_suspend final_suspend final_suspend
cont.resume() cont.resume()
ARBITRARY  ARBITRARY  ARBITRARY
CALL 3 CALL 2 CALL 1

## Slide 213

Infinite Coroutine Chaining
coroutine c1() coroutine c1’() coroutine c1’’()
c1
RP RP RP
Resume Stub Resume Stub Resume Stub
//SP1 //SP1 //SP1
await_suspend await_suspend await_suspend
c2.destroy() c2.destroy() c2.destroy()

Resume Stub
//SP1
await_suspend
c2.destroy()
//SP2
final_suspend
cont.resume()

c1'

//SP2 //SP2
final_suspend final_suspend
cont.resume() cont.resume()
ARBITRARY  ARBITRARY  ARBITRARY
CALL 4 CALL 3 CALL 2

ARBITRARY  ARBITRARY
CALL 2 CALL 1

## Slide 214

##### Argument Passing

- We now have infinite arbitrary calls

• What about setting arbitrary arguments in the registers?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
y/ u ; i
I kh “ | Ph Ii 2
black hat Anvinaag Passing yp
¢ We now have infinite arbitrary calls
¢ What about setting arbitrary in the registers?
```

## Slide 215

Argument Passing

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
QQ eae y
; : |
blackhat ment’
rdi
resume()
-
resume ptr. destroy ptr.
rdi
destroy()
argdata
-
resume ptr. destroy ptr.
call [rdi] = call [call target]
argO = rdi = pointer to call target
call [rdi+Ox8] = call [call target]
argO = rdi = pointer to argdata
```

## Slide 216

##### Argument Passing

- So, _resume_ and _destroy_ have _rdi_ =frame

- • Is there anything else where _rdi_ is always used?

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
y/ u ; i
EQ : ass tne rg : y " | 3 7 4 a
| kh : y | > ih y 4
blackhat Anvinaag Passing
¢ So, resume and destroy have
¢ Is there anything else where rdi is always used?
```

## Slide 217

##### Argument Passing

- So, _resume_ and _destroy_ have _rdi_ =frame

- Is there anything else where _rdi_ is always used?

   - Member functions address member variables as _rdi_ offsets

```
class A:
char[] buf;
char* name;
char* surname;
void operate()
{
```

```
char* a = this.name;
char* b = this.surname;
```

```
operate:
```

```
endbr64
mov rsi, [rdi+0x80]
mov rdx, [rdi+0x88]
...
```

```
...
func(a,b);
}
```

## Slide 218

##### Argument Passing

• Coroutine frame & class collision

```
operate:
```

```
endbr64
mov rsi, [rdi+0x80]
mov rdx, [rdi+0x88]
```

```
...
```

## Slide 219

##### Argument Passing

• Coroutine frame & class collision

```
operate:
```

```
endbr64
mov rsi, [rdi+0x80]
mov rdx, [rdi+0x88]
```

```
...
```

## Slide 220

##### Argument Passing

• Golden gadget

   - Silver gadget

- Sets registers and controlled call

- Only sets registers and returns, needs to leverage another CFP for the call

```
endbr64
mov rax, rsi
mov rcx, [rdi+0x90] ;ctrl rcx
mov esi, [rdi+0x80] ;ctrl rsi
mov edx, [rdi+0x98] ;ctrl rdx
mov rdi,rax;ctrl rdi
jmprcx;arbitrary call
```

## Slide 221

##### Argument Passing

• Golden gadget

   - Silver gadget

- Sets registers and controlled call

- Only sets registers and returns, needs to leverage another CFP for the call

```
endbr64
mov rax, rsi
mov rcx, [rdi+0x90] ;ctrl rcx
mov esi, [rdi+0x80] ;ctrl rsi
mov edx, [rdi+0x98] ;ctrl rdx
mov rdi,rax;ctrl rdi
ret
```

## Slide 222

# DEMO TIME

## Slide 223

##### CFOP in Windows

- MSVC supports coroutines from MSVC 19 (and Clang8, gcc 10)

- • The coroutine frame, handler and every other internal also exists

   - Still subject to frame manipulation and frame injection

## Slide 224

##### CFOP in Windows

- MSVC supports coroutines from MSVC 19

- The coroutine frame, handler and every other internal also exists

   - Still subject to frame manipulation and frame injection

- Frame injection harder than ptmalloc, LFH chunks are randomized • But if you find one frame, you can overwrite its inner CFPs, or overwrite a handler in the stack, and point to known locations

## Slide 225

##### CFOP in Windows

- MSVC supports coroutines from MSVC 19

- The coroutine frame, handler and every other internal also exists

   - Still subject to frame manipulation and frame injection

- Frame injection harder than ptmalloc, LFH chunks are randomized

   - But if you find one frame, you can overwrite its inner CFPs, or overwrite a handler in the stack, and point to known locations

- Bypassing CET SHSTK and CFG is parallel to SHSTK & IBT

## Slide 226

##### CFOP in Windows

- MSVC supports coroutines from MSVC 19

- The coroutine frame, handler and every other internal also exists

   - Still subject to frame manipulation and frame injection

- Frame injection harder than ptmalloc, LFH chunks are randomized

   - But if you find one frame, you can overwrite its inner CFPs, or overwrite a handler in the stack, and point to known locations

- Bypassing CET SHSTK and CFG is parallel to SHSTK & IBT

- The _rdi = this_ convention turns into _rcx_ = _this_ , account for other regs

## Slide 227

##### Defense Proposal

• Move the _resume_ and _destroy_ pointers to read-only memory • Add a new _coroutine identifier_ to search the corresponding pointers

## Slide 228

##### Heap Allocation Elision Optimization

• Heap Allocation Elision Optimization (HALO) moves the coroutines from the heap to the stack

• As an accidental byproduct, it also stops using the _resume_ and _destroy_ pointers completely. DOAs still good ( _megaframes_ )

## Slide 229

##### Heap Allocation Elision Optimization

- Heap Allocation Elision Optimization (HALO) moves the coroutines from the heap to the stack

- As an accidental byproduct, it also stops using the _resume_ and _destroy_ pointers completely. DOAs still good ( _megaframes_ )

- • In practice, getting HALO on your coroutines is _hard_

   - The compiler must be sure that the coroutine is created and destroyed in a certain scope (e.g., a function). Therefore:

      - All boilerplate needs to be inlinable (await_suspend, constructors, etc…)

      - Not possible if code is at different translation units (no LTO)

      - Indirect calls inside the coroutine may break HALO

      - Accessing coroutine objects outside the the coroutine (e.g., return value)

      - Works well if program is simple and/or you prepare the program for HALO, otherwise it is almost guaranteed you will not get it

## Slide 230

##### Heap Allocation Elision Optimization

Does my compiler support HALO at all?

- GCC

   - No.

- Clang

   - Yes (with the mentioned restrictions), but Clang 19 and 20 are slightly broken – this is a bug, HALO was not discarded

- MSVC

   - Since MSVC 19.43, from VS 17.13, dating February 2025 (after our report)

   - However, requires compiling without exception support (EHsc), which is enabled by default in VS

## Slide 231

https://github.com/coroutine-cfop/cfop

Marcos Bajo _h3xduck_ Christian Rossow

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
7% Way ss Nan A SS
Se ti
black hat
EFINGS
AUGUST - 2025
MANDALAY BAY / LAS VEGAS
https://github.com/coroutine-cfop/cfop
Marcos Bajo h3xduck
Christian Rossow
```
