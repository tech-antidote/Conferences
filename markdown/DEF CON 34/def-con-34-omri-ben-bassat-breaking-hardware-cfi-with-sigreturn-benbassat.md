---
title: "Breaking Hardware CFI with Sigreturn"
speakers: ["Omri Ben Bassat"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: null
source_pdf: "DEF CON 34/DEF CON 34 - Omri Ben Bassat - Breaking Hardware CFI with Sigreturn - BENBASSAT.pdf"
pages: 51
sha256: "eba69e32a4a9842c49f4f87cf3760482778e3a213042ac3ad5302e447c530b74"
text_chars: 13676
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:25:48Z"
---
# Breaking Hardware CFI with Sigreturn

**Speakers:** Omri Ben Bassat  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Omri Ben Bassat - Breaking Hardware CFI with Sigreturn - BENBASSAT.pdf` (51 pages)


## Slide 1

# **Breaking Hardware CFI with Sigreturn**

_<u>Omri Ben-Bassat , Prof. Noam Rinetzky, Prof. Sharon Shoham, Prof. Adam Morrison</u> Tel Aviv University_

## Slide 2

### **Branch Target Identification (BTI)**

● ARMv8.5-A+

● Hardware Enforced Control Flow Integrity (CFI) _○ Pointer Authentication Code (PAC)_

_○ Guarded Control Stack (GCS)_

● Mitigates Jump Oriented Programing (JOP)

## Slide 3

### **Branch Target Identification (BTI)**

// func A
bti //  Landing Pad
blr xN ...
// JOP gadget1
add x0, x1, x2
br xN
...
ret

<u>https://developer.arm.com/documentation/102433/0200/Jump-oriented-programming</u>

## Slide 4

### **Branch Target Identification (BTI)**

// func A
bti //  Landing Pad
blr xN ...
// JOP gadget1
add x0, x1, x2
br xN
...
ret

<u>https://developer.arm.com/documentation/102433/0200/Jump-oriented-programming</u>

## Slide 5

### **Branch Target Identification (BTI)**

// func A
bti //  Landing Pad
...
// JOP gadget1
add x0, x1, x2
br xN
...
ret

blr xN

<u>https://developer.arm.com/documentation/102433/0200/Jump-oriented-programming</u>

## Slide 6

### **Branch Target Identification (BTI)**

blr xN pstate.btype := 0b11

// func A
bti //  Landing Pad
...
// JOP gadget1
add x0, x1, x2
br xN
...
ret

<u>https://developer.arm.com/documentation/102433/0200/Jump-oriented-programming</u>

## Slide 7

### **Branch Target Identification (BTI)**

blr xN pstate.btype := 0b11 ● bti

// func A bti // _Landing Pad_ ... // JOP gadget1 add x0, x1, x2 br xN ... ret

○ pstate.btype := 0b00 ● add x0, x1, x2 ○ pstate.btype != 0 => Branch Target Exception

<u>https://developer.arm.com/documentation/102433/0200/Jump-oriented-programming</u>

## Slide 8

### **Branch Target Identification (BTI)**

- blr xN

- pstate.btype := 0b11

- ● bti

// func A bti // _Landing Pad_ ... // JOP gadget1 add x0, x1, x2 br xN ... ret

- pstate.btype := 0b00

- ● add x0, x1, x2

   - pstate.btype != 0 => Branch Target Exception

<u>https://developer.arm.com/documentation/102433/0200/Jump-oriented-programming</u>

## Slide 9

rt_sigreturn

● Handlers signal resumption ● Restore full machine context ○ Including pstate

● _Signal frames_ taken from user space stack

## Slide 10

user
BTI Bypass by Design

kernel

// func A
...
// JOP gadget1
add x0, x1, x2
br xN

## Slide 11

BTI Bypass by Design
sp points to
crafted
rt_sigframe
…
regs[31]
sp
pc = &gadget1
pstate.btype=0

user

// func A
...
// JOP gadget1
add x0, x1, x2
br xN

kernel

## Slide 12

user
BTI Bypass by Design
sp points to
crafted
rt_sigframe
… // func A
regs[31] ...
// JOP gadget1
sp add x0, x1, x2
br xN
pc = &gadget1
pstate.btype=0

kernel

## Slide 13

user
BTI Bypass by Design
sp points to
__kernel_rt_sigreturn
crafted
rt_sigframe
… // func A
regs[31] ...
// JOP gadget1
sp add x0, x1, x2
br xN
pc = &gadget1
pstate.btype=0

kernel

## Slide 14

kernel

**BTI Bypass by Design** sp points to crafted rt_sigframe … regs[31] sp pc = &gadget1 pstate.btype=0

user

__kernel_rt_sigreturn
rt_sigreturn
// func A
...
// JOP gadget1
add x0, x1, x2
br xN

## Slide 15

kernel

### **BTI Bypass by Design**

user

sp points to crafted rt_sigframe … regs[31] sp pc = &gadget1 pstate.btype=0

__kernel_rt_sigreturn rt_sigreturn // func A ... ERET // JOP gadget1 add x0, x1, x2 br xN

## Slide 16

user kernel
BTI Bypass by Design
sp points to
__kernel_rt_sigreturn
crafted
rt_sigframe
rt_sigreturn
… // func A
...  ERET
regs[31]
// JOP gadget1
sp add x0, x1, x2
br xN
pc = &gadget1
pstate.btype=0
pc == &gadget1
✅
pstate.btype == 0b00
✅

## Slide 17

### **Attack Flow**

setcontext (bootstrap) _ucontext_t pivot_ctx_

… pc = __kernel_rt_sigreturn sp = &frame_1 …

__kernel_rt_sigreturn __kernel_rt_sigreturn (step #1) (step #2)

## Slide 18

### **Attack Flow**

setcontext __kernel_rt_sigreturn
(bootstrap) (step #1) (step #2)
ucontext_t pivot_ctx rt_sigframe frame_1
… …
pc =  x16 =
__kernel_rt_sigreturn __kernel_rt_sigreturn
sp = &frame_1 pc = &gadget_1
… sp = &frame_2
pstate = 0

__kernel_rt_sigreturn (step #2)

## Slide 19

Attack Flow
setcontext __kernel_rt_sigreturn __kernel_rt_sigreturn
(bootstrap) (step #1) (step #2)
ucontext_t pivot_ctx rt_sigframe frame_1 Gadget 1
… …
str w2, [x0]
br x16
pc =  x16 =
__kernel_rt_sigreturn __kernel_rt_sigreturn
sp = &frame_1 pc = &gadget_1
… sp = &frame_2
pstate = 0

## Slide 20

__kernel_rt_sigreturn
(step #2)
Gadget 1
str w2, [x0]
br x16
rt_sigframe frame_2
…
pc = &gadget_2
sp = &frame_3
pstate = 0

### **Attack Flow**

setcontext __kernel_rt_sigreturn
(bootstrap) (step #1)
ucontext_t pivot_ctx rt_sigframe frame_1
… …
pc =  x16 =
__kernel_rt_sigreturn __kernel_rt_sigreturn
sp = &frame_1 pc = &gadget_1
… sp = &frame_2
pstate = 0

## Slide 21

Attack Flow
setcontext __kernel_rt_sigreturn __kernel_rt_sigreturn
(bootstrap) (step #1) (step #2)
ucontext_t pivot_ctx rt_sigframe frame_1 Gadget 1
… …
str w2, [x0]
br x16
pc =  x16 =
__kernel_rt_sigreturn __kernel_rt_sigreturn
rt_sigframe frame_2
sp = &frame_1 pc = &gadget_1
…
… sp = &frame_2
pc = &gadget_2
pstate = 0
sp = &frame_3
pstate = 0

## Slide 22

## **PoC #1**

<u>https://github.com/betab0t/srop-bti</u>

## Slide 23

**From Super Gadget to BTI Bypass** Sigreturn Oriented Programming BTI  Support (SROP) CET BTI In Ubuntu Bosman & Bos PAC ARMv8.5-A (25.04) _*SROP/BTI*_ 2014 2016 2018 2025 2026 NO HW CFI

## Slide 24

**From Super Gadget to BTI Bypass** Sigreturn Oriented Programming BTI  Support (SROP) CET BTI In Ubuntu Bosman & Bos PAC ARMv8.5-A (25.04) _*SROP/BTI*_ 2014 2016 2018 2025 2026 NO HW CFI

<u>https://blackhat.com/us-26/briefings/schedule/index.html#breaking-hardware-cfi-with-sigreturn-52333</u>

## Slide 25

### **Real-World Applicability**

We’d like to -

1. Relax attack assumptions a. setcontext(&pivot_ctx) b. Implies Control Flow Hijack w/ *arbitrary argument* 2. Save on aux memory space

a. sizeof(ucontext_t) ≈ 500 bytes

b. sizeof(rt_sigframe) ≈ 600 bytes

## Slide 26

### **Real-World Applicability**

We’d like to -

1. Relax attack assumptions a. setcontext(&pivot_ctx)

b. Implies Control Flow Hijack w/ *arbitrary argument*

2. Save on aux memory space

   - a. sizeof(ucontext_t) ≈ 500 bytes

   - b. sizeof(rt_sigframe) ≈ 600 bytes

## Slide 27

### **Counterfeit Object-oriented Programming (COOP)**

class Container { private: Item **items; Main size_t nItems; public: Loop // ... virtual ~Course() { for (size_t i=0; i < nItems; i++) **items[i]->unref(); // virt func** delete items; }};

## Slide 28

Counterfeit Object-oriented Programming (COOP)
class Container {
private:
X::vtable
Item **items;
Main
size_t nItems;
public: Loop 1st entry
// ...
virtual ~Course() {
2 nd entry
for (size_t i=0; i < nItems; i++)
items[i]->unref(); // virt func
delete items; …
}};
Counterfeit
items
Object #1
1st item vptr
2nd item
1st field
… …

## Slide 29

Counterfeit Object-oriented Programming (COOP)
class Container {
private:
X::vtable
Item **items;
Main
size_t nItems;
public: Loop 1st entry
// ...
virtual ~Course() {
2 nd entry
for (size_t i=0; i < nItems; i++)
items[i]->unref(); // virt func
delete items; …
}};
Counterfeit
items
Object #1 Only valid func entrypoints
1st item vptr
2nd item
1st field
… …

## Slide 30

### **Counterfeit Object-oriented Programming (COOP)**

items

1st item

Nth item

items[n]->unref() =>

setcontext((ucontext_t *)overlay_counterfeit_obj)

## Slide 31

### **Counterfeit Object-oriented Programming (COOP)**

#### items

##### **Overlay Counterfeit Object**

1st item
uc_link vptr
…
…
Nth item
pc=
…
&__kernel_rt_sigretrun
sp=&frame_1
…

items[n]->unref() =>

setcontext((ucontext_t *)overlay_counterfeit_obj)

## Slide 32

### **Counterfeit Object-oriented Programming (COOP)**

items
Overlay
Overlay vtable
Counterfeit Object
1st item
…
uc_link vptr
…
setcontext unref
…
Nth item
pc= …
…
&__kernel_rt_sigretrun
sp=&frame_1
…

items[n]->unref() =>

setcontext((ucontext_t *)overlay_counterfeit_obj)

## Slide 33

### **Coroutine Frame-Oriented Programming (CFOP)**

● Abuses _C++ 20’ Coroutines Frames_

● Functions that pause and resume

● Bypass lots of Fine Grained CFIs

● CFOP *dosen’t bypass* ARM64 BTI

● Extend with SROP/BTI

## Slide 34

### **Coroutine Frame-Oriented Programming (CFOP)**

● Abuses _C++ 20’ Coroutines Frames_

● Functions that pause and resume

● Bypass lots of Fine Grained CFIs

● CFOP *dosen’t bypass* ARM64 BTI

● Extend with SROP/BTI

## Slide 35

### **Coroutine Frame-Oriented Programming (CFOP)**

● Abuses _C++ 20’ Coroutines Frames_

● Functions that pause and resume

● Bypass lots of Fine Grained CFIs ● CFOP *dosen’t bypass* ARM64 BTI

● Extend with SROP/BTI

## Slide 36

### **Coroutine Frame-Oriented Programming (CFOP)**

● Abuses _C++ 20’ Coroutines Frames_ ● Functions that pause and resume

● Bypass lots of Fine Grained CFIs ● CFOP *dosen’t bypass* ARM64 BTI ● Extend with SROP/BTI

## Slide 37

### **Coroutine Frame-Oriented Programming (CFOP)**

● Abuses _C++ 20’ Coroutines Frames_ ● Functions that pause and resume

● Bypass lots of Fine Grained CFIs

● CFOP *dosen’t bypass* ARM64 BTI

● Extend with SROP/BTI

## Slide 38

### **Coroutine Frame-Oriented Programming (CFOP)**

● Abuses _C++ 20’ Coroutines Frames_ ● Functions that pause and resume ● Bypass lots of Fine Grained CFIs ● CFOP *dosen’t bypass* ARM64 BTI ● Extend with SROP/BTI

## Slide 39

### **Coroutine Frame-Oriented Programming (CFOP)**

handle.resume() resume ptr destroy ptr promise object parameters local variables coroutine index

_*coroutines frame on the heap_

## Slide 40

### **Coroutine Frame-Oriented Programming (CFOP)**

// func A
b ti
handle.resume()
// …
add x0, x1, x2
// …
ret
resume ptr destroy ptr
promise object
// func B
parameters b ti
local variables // …
sub x0, x1, x2
coroutine index
// …
ret
*coroutines frame on the heap

## Slide 41

user kernel
Overlay // setcontext
b ti
// …
ldr x16, [x0, #0x1b8]
handle.resume()
br  x16
resume ptr destroy ptr
promise object
// func A
parameters bti
local variables // …
// JOP  ga dget1
coroutine index
add x0, x1, x2
br xN
*coroutines frame on the heap

## Slide 42

user kernel
Overlay // setcontext
b ti
???
// …
ldr x16, [x0, #0x1b8]
handle.resume()
br  x16
resume ptr destroy ptr
promise object
// func A
parameters bti
local variables // …
// JOP  ga dget1
coroutine index
add x0, x1, x2
br xN
*coroutines frame on the heap

## Slide 43

user kernel
Overlay // setcontext
b ti
???
// …
ldr x16, [x0, #0x1b8]
handle.resume()
br  x16
resume ptr destroy ptr
promise object
// func A
parameters bti
local variables // …
// JOP  ga dget1
coroutine index
add x0, x1, x2
br xN
*coroutines frame on the heap

## Slide 44

user kernel
Overlay // setcontext
b ti
???
// …
ldr x16, [x0, #0x1b8]
handle.resume()
br  x16
resume ptr destroy ptr
pivot_ctx
pc =&__kernel_rt_sigreturn // func A
sp = &frame_1 bti
// …
frame_1
pc=&gadget_1 // JOP  ga dget1
pstate.btype = 0
add x0, x1, x2
br xN
*coroutines frame on the heap

## Slide 45

user kernel
Overlay // setcontext
b ti
???
// …
ldr x16, [x0, #0x1b8]
handle.resume()
br  x16
resume ptr destroy ptr __kernel_rt_sigreturn
rt_sigreturn
pivot_ctx
pc =&__kernel_rt_sigreturn // func A
sp = &frame_1 bti
// …
frame_1
pc=&gadget_1 // JOP  ga dget1
pstate.btype = 0
add x0, x1, x2
br xN
*coroutines frame on the heap

## Slide 46

user kernel
Overlay // setcontext
b ti
???
// …
ldr x16, [x0, #0x1b8]
handle.resume()
br  x16
resume ptr destroy ptr __kernel_rt_sigreturn
rt_sigreturn
pivot_ctx
pc =&__kernel_rt_sigreturn // func A
sp = &frame_1 bti
// …
frame_1
pc=&gadget_1 // JOP  ga dget1
pstate.btype = 0
add x0, x1, x2
br xN
*coroutines frame on the heap

## Slide 47

user kernel
Overlay // setcontext
b ti
???
// …
ldr x16, [x0, #0x1b8]
handle.resume()
br  x16
resume ptr destroy ptr __kernel_rt_sigreturn
rt_sigreturn
pivot_ctx
pc =&__kernel_rt_sigreturn // func A
sp = &frame_1 bti
// …
frame_1
pc=&gadget_1 // JOP  ga dget1
pstate.btype = 0
add x0, x1, x2
br xN
*coroutines frame on the heap
pc == &gadget1
✅
pstate.btype == 0b00
✅

## Slide 48

user kernel
Overlay // setcontext
b ti
???
// …
ldr x16, [x0, #0x1b8]
handle.resume()
br  x16
resume ptr destroy ptr __kernel_rt_sigreturn
rt_sigreturn
pivot_ctx
pc =&__kernel_rt_sigreturn // func A
sp = &frame_1 bti
// …
frame_1
pc=&gadget_1 // JOP  ga dget1
pstate.btype = 0
add x0, x1, x2
br xN
*coroutines frame on the heap
No g++/clang++
mitigations
pc == &gadget1
✅
pstate.btype == 0b00
✅

## Slide 49

## **PoC #2**

<u>https://github.com/betab0t/srop-bti</u>

## Slide 50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
& Linus Torvalds
ind t y@k and t I 1 t8
| have forwarded the original email to the arm64 maintainers, also cc’d here.
But
On Mon, 26 Jan
26 at 09:37, beta bot <beta_b0t@yahoo.com> wrote
So this seems to not be a very effective attack vector and is not
practically fixable, because signals by *design* have to be able to
return anywhere
This would seem to require that you be able to change the signal
return stack in a very particular way, so you probably already had
pretty complete control of the program you're attacking
So this seems to not be a very effective attack vector and is not
practically fixable, because signals by *design* have to be able to
return anywhere.
| suspect this can be discussed publicly, and the signal return path
has - as you point out - already been discussed in various other
contexts, but | think this is just how signals work
BTI isn't some kind of absolute shield. It's just one layer of
security protection among many others.
```

## Slide 51

Omri Ben-Bassat _<u>beta_b0t@yahoo.com</u>_

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Omri Ben-Bassat
& Linus Torvalds
na it y . i } t t 1
I have for
yarded the original email to the arm64 maintainers, also cc’d here.
But
On Mon, 26 Jan 2026 at 09:37, beta bot <beta_b0t@yahoo.com> wrote:
So this seems to not be a very effective attack vector and is not
practically fixable, because signals by *design* have to be able to
return anywhere
This would seem to require that you be able to change the signal
ack in a very particular way, so you probably already had
ity complete control of the program you're attacking
So this seems to not be a very effective attack vector and is not
practically fixable, because signals by *design* have to be able to
ret
n anyv
pect this can be discussed publicly, and the signal return path
has
contexts, but | think this is just how signals work
as you point out - already been discussed in various other
BTI isn't some kind of absolute shield. It's just one layer of
security protection among many others.
```
