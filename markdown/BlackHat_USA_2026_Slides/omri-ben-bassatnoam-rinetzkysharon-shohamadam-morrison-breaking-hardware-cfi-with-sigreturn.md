---
title: "Breaking Hardware CFI with Sigreturn"
speakers: ["Omri Ben-Bassat", "Noam Rinetzky", "Sharon Shoham", "Adam Morrison"]
conference: "Black Hat"
conference_full: "Black Hat USA 2026"
edition: "USA"
year: 2026
source_pdf: "BlackHat_USA_2026_Slides/Omri Ben-Bassat&Noam Rinetzky&Sharon Shoham&Adam Morrison_Breaking Hardware CFI with Sigreturn.pdf"
pages: 68
sha256: "d99ad79a3965701e0b31055aeef512b5202c11278371427ac69574e177e7798b"
text_chars: 20262
ocr_pages: 19
has_ocr: true
redacted_secrets: 0
ocr_confidence: 82.6
ocr_unreliable_blocks: 7
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T05:40:55Z"
---
# Breaking Hardware CFI with Sigreturn

**Speakers:** Omri Ben-Bassat, Noam Rinetzky, Sharon Shoham, Adam Morrison  
**Conference:** Black Hat USA 2026  
**Source:** `BlackHat_USA_2026_Slides/Omri Ben-Bassat&Noam Rinetzky&Sharon Shoham&Adam Morrison_Breaking Hardware CFI with Sigreturn.pdf` (68 pages)


## Slide 1

# Breaking Hardware CFI with Sigreturn

_<u>Omri Ben-Bassat</u> , Prof. Noam Rinetzky, Prof. Sharon Shoham, Prof. Adam Morrison Tel Aviv University_

Information Classification: General

## Slide 2

### $ whoami

Omri Ben-Bassat _Vulnerability Researcher & MSc Candidate_

Prof. Sharon Shoham Buchbinder

Prof. Noam Rinetzky

Prof. Adam Morrison

Information Classification: General

## Slide 3

## SROP/BTI

●A novel ARM64 hardware-CFI bypass ●Breaks BTI even with PAC enabled ●Demonstrated on Ubuntu 26.04 and Android 17

Information Classification: General

## Slide 4

### Control Flow Integrity (CFI)

●Modern class of mitigations ●Restricts a program’s execution ●Only intended control-flow paths

Information Classification: General

## Slide 5

### ARM64 _Pointer Authentication Code (PAC)_

●ARM mechanism for authenticating pointers ●Can protect both forward and backward edges ●Linux deploys PAC as backward-edge CFI ●Signs return addresses (pac-ret)

●Aims to mitigate ROP

Information Classification: General

## Slide 6

### PACIxSP + AUTIxSP

gcc … -mbranch-protection=pac-ret

Information Classification: General


> Recovered by OCR — confidence 90/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PACIxS
disas main
P + AUTIXSP
Dump of assembler code for function main:
End of assembler dump.
gcc .. -mbranch-protection=pac-ret
<+8>:
<+12>:
<+16>:
<+20>:
<+28>:
<+32>:
<+36>:
<+40>:
<+44>:
paciasp
stp
mov
str [sp, J
[
str
adrp
bl ) <printfa@plt>
mov
autiasp
ret
#0
```

## Slide 7

### PACIxSP + AUTIxSP

gcc … -mbranch-protection=pac-ret

Information Classification: General


> Recovered by OCR — confidence 87/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
PACIxS
disas main
P + AUTIXSP
Dump of assembler code for function main:
End of assembler dump.
gcc .. -mbranch-protection=pac-ret
<+8>:
<+12>:
<+16>:
<+20>:
<+28>:
<+32>:
<+36>:
<+40>:
<+44>:
paciasp <—
stp
mov
str [sp, ]
str [
adrp
bl ) <printfa@plt>
mov .
autiasp <—
ret
#0
```

## Slide 8

### ARM64 _Branch Target Identification (BTI)_

●Aims to mitigate JOP ●Forward-edge CFI ●Compiler plants _Landing Pads (LP)_ ●LPs are the only valid branch targets

●Enforced in HW

Information Classification: General

## Slide 9

### Threat Model

●Target is Linux user mode program

●Latest OS on ARMv8.5-A+

- -mbranch-protection=standard (bti+pac-ret) => No ROP / JOP

- ●Memory corruption

●ASLR derandomization

Information Classification: General

## Slide 10

### BTI implementation

blr xN pstate.btype := 0b11

// func A bti // _Landing Pad_ ... // JOP gadget1 add x0, x1, x2 br xN ... ret

<u>https://developer.arm.com/documentation/102433/0200/Jump-oriented-programming</u>

Information Classification: General

## Slide 11

### BTI implementation

// func A bti // _Landing Pad_ blr xN ... // JOP gadget1 add x0, x1, x2 pstate.btype := 0b11 br xN ... ● bti ret ○ pstate.btype := 0b00 ● add x0, x1, x2 ○ pstate.btype != 0 => Branch Target Exception

<u>https://developer.arm.com/documentation/102433/0200/Jump-oriented-programming</u>

Information Classification: General

## Slide 12

### BTI implementation

blr xN

pstate.btype := 0b11 ● bti

// func A bti // _Landing Pad_ ... // JOP gadget1 add x0, x1, x2 br xN ... ret

○ pstate.btype := 0b00 ● add x0, x1, x2

- pstate.btype != 0 => Branch Target Exception

<u>https://developer.arm.com/documentation/102433/0200/Jump-oriented-programming</u>

Information Classification: General

## Slide 13

Information Classification: General

## Slide 14

### No JOP? Just Ask the Kernel!

● rt_sigreturn

●POSIX signal-resumption mechanism ○x0–x30, SP, PC, …

○PSTATE

●Resumes execution at the restored PC

●No BTI landing-pad validation

Information Classification: General

## Slide 15

### Sigreturn: A BTI Bypass by Design 🔮

    user kernel
// func A
...
// JOP gadget1
add x0, x1, x2
br xN

Information Classification: General

## Slide 16

### Sigreturn: A BTI Bypass by Design 🔮

user kernel

Crafted rt_sigframe … regs[31] sp pc = &gadget1 pstate.btype=0

// func A ... // JOP gadget1 add x0, x1, x2 br xN

Information Classification: General

## Slide 17

### Sigreturn: A BTI Bypass by Design 🔮

user kernel

Crafted rt_sigframe

… // func A regs[31] ... // JOP gadget1 sp add x0, x1, x2 br xN pc = &gadget1 pstate.btype=0

Information Classification: General

## Slide 18

### Sigreturn: A BTI Bypass by Design 🔮

user

kernel

Crafted rafted __kernel_rt_sigreturn rt_sigframe … // func A regs[31] ... // JOP gadget1 sp add x0, x1, x2 br xN pc = &gadget1 pstate.btype=0

Crafted rafted rt_sigframe

Information Classification: General

## Slide 19

### Sigreturn: A BTI Bypass by Design 🔮

user

kernel

Crafted rafted __kernel_rt_sigreturn rt_sigframe rt_sigreturn … // func A regs[31] ... // JOP gadget1 sp add x0, x1, x2 br xN pc = &gadget1 pstate.btype=0

Crafted rafted rt_sigframe

Information Classification: General

## Slide 20

### Sigreturn: A BTI Bypass by Design 🔮

user

kernel

Crafted rafted __kernel_rt_sigreturn rt_sigframe rt_sigreturn … // func A ... ERET regs[31] // JOP gadget1 sp add x0, x1, x2 br xN pc = &gadget1 pstate.btype=0

Crafted rafted rt_sigframe

Information Classification: General

## Slide 21

### Sigreturn: A BTI Bypass by Design 🔮

user

kernel

Crafted __kernel_rt_sigreturn rt_sigframe rt_sigreturn … // func A ... ERET regs[31] // JOP gadget1 sp add x0, x1, x2 br xN pc = &gadget1 ✅ pc == &gadget1 pstate.btype=0

Information Classification: General

## Slide 22

### Sigreturn: A BTI Bypass by Design 🔮

user

kernel

Crafted rafted __kernel_rt_sigreturn rt_sigframe rt_sigreturn … // func A ... ERET regs[31] // JOP gadget1 sp add x0, x1, x2 br xN pc = &gadget1 ✅ pc == &gadget1 ✅ pstate.btype == 0 pstate.btype=0

Crafted rafted rt_sigframe

Information Classification: General

## Slide 23

### Sigreturn: A BTI Bypass by Design 🔮

user

kernel

Crafted rafted __kernel_rt_sigreturn rt_sigframe rt_sigreturn … // func A ... ERET regs[31] // JOP gadget1 sp add x0, x1, x2 br xN pc = &gadget1 ✅ pc == &gadget1 ✅ pstate.btype == 0 pstate.btype=0 ✅ BTI BYPASSED

Crafted rafted rt_sigframe

Information Classification: General

## Slide 24

### From Super Gadget to BTI Bypass

Sigreturn Oriented Programming BTI  Support (SROP) CET BTI In Ubuntu Bosman & Bos PAC ARMv8.5-A (25.04) _*SROP/BTI*_ 2014 2016 2018 2025 2026 NO HW CFI

Information Classification: General

## Slide 25

### Bootstrapping SROP/BTI

● rt_sigreturn takes sigframe from stack pointer

● pac-ret ⇒ No more (exploitable) stack overflows

●BTI ⇒ Can’t jump to ROP/JOP stack pivot

…
LR
Crafted
rt_sigframe
…

Information Classification: General

## Slide 26

### Bootstrapping SROP/BTI

● rt_sigreturn takes sigframe from stack pointer
● pac-ret ⇒ No more (exploitable) stack overflows
●BTI ⇒ Can’t jump to ROP/JOP stack pivot
…
LR __kernel_rt_sigreturn
SP
Crafted
rt_sigframe
…

Information Classification: General

## Slide 27

### SROP/BTI CFI-Safe Stack Pivots

1. bti

2. sp := xN // xN=&frame_1

3. br xM    // xM=__kernel_rt_sigreturn

Information Classification: General

## Slide 28

Glibc CFI Safe Pivot

Information Classification: General


> Recovered by OCR — confidence 75/100 on the text kept, 61/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
0013ec7F d5
Glibc
undefined
stone ah a CFI Safe Pivot
0013ec80
0013ec84 e'
0013ec88 4
0013ec8c
0013ec90
0013ec94
0013ec98 e
0013ec9c
0013eca4 FUN_00123120
0013ecac FUN_001#8840
0013ecbO
0013ecb4
0013ecb8
0013eccO
0013ecc4
0013ecc8
0013eccc
0013ecd8
LAB_0013ed90 X ] 00 A
0013ed98 4 ldp
```

## Slide 29

Landing Pad
LR
SP
PC

Glibc
CFI Safe Pivot

Information Classification: General


> Recovered by OCR — confidence 79/100 on the text kept, 65/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
0013ec80
0013ec84
0013ec88
0013ec8c
0013ec90
0013ec94
0013ec98
0013ec9c
0013eca4
0013ecbO
0013ecb4
0013ecb8
0013eccO
0013ecc4
0013ecc8
0013eccc
0013ecd4
0013ecdc
0013ed90
0013ed94
0013eda0
0013eda4
undefined
SSIGNED
ldr
ldp
br
FUN_00123120
FUN_0018840
Glibc
CFI Safe Pivot
openSUSE ,
```

## Slide 30

### Caveats

Information Classification: General


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
71 SYM_CODE_START(__kernel_rt_sigreturn)
mov x8, NR_rt_stgreturn
svc #0
SYM_CODE_END(__kernel_rt_sigreturn)
emit_aarch64_feature_1_and
```

## Slide 31

### Caveats

Information Classification: General


> Recovered by OCR — confidence 93/100 on the text kept, 93/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
71 SYM_CODE_START(__kernel_rt_sigreturn)
mov x8,
svc #0
SYM_CODE_END(__kernel_rt_sigreturn)
emit_aarch64_feature_1_and
```

## Slide 32

### Caveats

Most Linux Distros

Information Classification: General


> Recovered by OCR — confidence 87/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
fil SYM_CODE_START(__| Most
mov x Linux
SYM_CODE_END(__kernel_rt_sigre
emit_aarch64_feature_1_and
g ARM64_BTI_KERNEL
y
ARM64_PTR_AUTH_KERNEL
CC_HAS_BRANCH_PROT_PAC_RET_BTI
CC_IS_GCC || GCC_VERSION >= 100100
cc_Is_Gcc
```

## Slide 33

### Forward-to-Backward Edge Gadget

setcontext( &pivot_ctx ) Magical Gadget
bti
… // no side effects
ucontext_t  pivot_ctx
ret __kernel_rt_sigreturn
…
x0 = x1 = 1
pc = Magical Gadget
sp = fake_sigframe
lr = __kernel_rt_sigreturn
…
ret
br x16

Information Classification: General

## Slide 34

### Forward-to-Backward Edge Gadget

setcontext( &pivot_ctx ) Magical Gadget
bti
… // no side effects
ucontext_t  pivot_ctx
ret __kernel_rt_sigreturn
…
x0 = x1 = 1
pc = Magical Gadget
sp = fake_sigframe
lr = __kernel_rt_sigreturn
…
ret
br x16

Information Classification: General

## Slide 35

Bionic (/ llvm-libunwind) CFI Safe Pivot

Source: Google.

Information Classification: General


> Recovered by OCR — confidence 70/100 on the text kept, 56/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
001f4190 df bti
001F4194 02 dp
001f4198 04 dp
001F419c 06 dp
001f41a8 Oc dp
001f41b0 12 4c 4 dp
001f41b8 16 dp
001f41bc 18 dp
001f41d0 02 dp
001f41ec 10 44 dp
001F4218 mov
001F421c mov
0014220 hint
0014228 sys
Lnoges
Eeniatie eet Source: Google. black hat
```

## Slide 36

Bionic (/ llvm-libunwind)
CFI Safe Pivot
Landing Pad
SP
Source: Google.

Source: Google.

Information Classification: General


> Recovered by OCR — confidence 70/100 on the text kept, 51/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
inet le in CFI Safe Pivo
001f4190 df bti
001F4198 04 ldp
001f41b4 14 dp
001f41e8 ldp
001f41ec 10 44 ldp
001F41f0 ldp
0014204 ldp
0014214 dp
001f4218 mov
001f421c mov
0014224 cbnz
Lnoges )
Eeniatie eet Source: Google. black hat
```

## Slide 37

Bionic (/ llvm-libunwind)
CFI Safe Pivot
Landing Pad
LR
SP
Return to __kernel_rt_sigreturn Source: Google.
Information Classification: General

Information Classification: General

## Slide 38

### Infinite SROP/BTI Chaining

setcontext (CFI Safe Pivot)

__kernel_rt_sigreturn JOP Gadget #1 (Step #1)

__kernel_rt_sigreturn (Step #2)

Information Classification: General

## Slide 39

#### Infinite SROP/BTI Chaining

setcontext __kernel_rt_sigreturn JOP Gadget #1 __kernel_rt_sigreturn
(CFI Safe Pivot) (Step #1) (Step #2)
ucontext_t pivot_ctx
…
pc =
__kernel_rt_sigreturn
sp = &frame_1
…

Information Classification: General

## Slide 40

#### Infinite SROP/BTI Chaining

setcontext __kernel_rt_sigreturn JOP Gadget #1 __kernel_rt_sigreturn
(CFI Safe Pivot) (Step #1) (Step #2)
ucontext_t pivot_ctx rt_sigframe frame_1 Gadget 1
(mem-store)
… …
str w2, [x0]
pc =  x16 =  br x16
__kernel_rt_sigreturn __kernel_rt_sigreturn
sp = &frame_1 pc = &gadget_1
… sp = &frame_2
pstate = 0

Information Classification: General

## Slide 41

#### Infinite SROP/BTI Chaining

setcontext __kernel_rt_sigreturn JOP Gadget #1 __kernel_rt_sigreturn
(CFI Safe Pivot) (Step #1) (Step #2)
ucontext_t pivot_ctx rt_sigframe frame_1 Gadget 1
(mem-store)
… …
str w2, [x0]
pc =  x16 =  br x16
__kernel_rt_sigreturn __kernel_rt_sigreturn
sp = &frame_1 pc = &gadget_1
… sp = &frame_2
pstate = 0

Information Classification: General

## Slide 42

#### Infinite SROP/BTI Chaining

setcontext __kernel_rt_sigreturn JOP Gadget #1 __kernel_rt_sigreturn
(CFI Safe Pivot) (Step #1) (Step #2)
ucontext_t pivot_ctx rt_sigframe frame_1 Gadget 1
(mem-store)
… …
str w2, [x0]
pc =  x16 =  br x16
__kernel_rt_sigreturn __kernel_rt_sigreturn
rt_sigframe frame_2
sp = &frame_1 pc = &gadget_1
…
… sp = &frame_2
pc = &gadget_2
pstate = 0
sp = &frame_3
pstate = 0
Information Classification: General

Information Classification: General

## Slide 43

#### Infinite SROP/BTI Chaining

setcontext __kernel_rt_sigreturn JOP Gadget #1 __kernel_rt_sigreturn
(CFI Safe Pivot) (Step #1) (Step #2)
ucontext_t pivot_ctx rt_sigframe frame_1 Gadget 1
(mem-store)
… …
str w2, [x0]
pc =  x16 =  br x16
__kernel_rt_sigreturn __kernel_rt_sigreturn
rt_sigframe frame_2
sp = &frame_1 pc = &gadget_1
…
… sp = &frame_2
pc = &gadget_2
pstate = 0
sp = &frame_3
pstate = 0
Information Classification: General

Information Classification: General

## Slide 44

### PoC #1

<u>https://github.com/betab0t/srop-bti</u>

Information Classification: General

## Slide 45

### Turing Completeness

1. Instruction pointer

2. State propagation

3. Operations (load, store, etc’)

Information Classification: General

## Slide 46

### Instruction Pointer

●Instructions encoded as rt_sigframes

- sp points to next instruction

●TM steps with __kernel_rt_sigreturn

Information Classification: General

## Slide 47

### State Propagation

((void (*)(int))target)(*(int *)p);

**rt_sigframe frame_1** … sp = &frame_2 pc = &gadget_1 x1 = __kernel_rt_sigreturn x19 = src ptr x20 = offsetof(rt_sigframe, x[7]) _Gadget #1 (mem-load-store)_ x21 = &frame_2 ldr x2, [x19, #0x18] // src … str x2, [x21, x20]   // dstblr x1 // back to __kernel_rt_sigreturn pstate = 0

rt_sigframe frame_2
…
x7
…
sp = &frame_3
pc = &gadget_2
pstate = 0

Information Classification: General

## Slide 48

### State Propagation

##### ((void (*)(int))target)(*(int *)p);

rt_sigframe frame_2
…
Gadget #2 (func-call)
x1 = &target
mov x0, x7
x7 = *p
blr x1 // target
…
Gadget #1 (mem-load-store) sp = &frame_3
ldr x2, [x19, #0x18] // src pc = &gadget_2
str x2, [x21, x20]   // dst
blr x1 // back to __kernel_rt_sigreturn pstate = 0
Information Classification: General

Information Classification: General

## Slide 49

### State Propagation

##### -= ((void (*)(int))target)(*(int *)p);

rt_sigframe frame_2
…
Gadget #2 (func-call)
x1 = &target
mov x0, x7
x7 = *p
blr x1 // target
…
Gadget #1 (mem-load-store) sp = &frame_3
ldr x2, [x19, #0x18] // src pc = &gadget_2
str x2, [x21, x20]   // dst
blr x1 // back to __kernel_rt_sigreturn pstate = 0
Information Classification: General

Information Classification: General

## Slide 50

### Operations

●mem-load/store

●Arithmetics

●Goto

○Loops

●Conditional branching

Information Classification: General

## Slide 51

### Arithmetics

1. Load

2. Calculate

3. Store

4. Sigreturn

Information Classification: General

## Slide 52

### Arithmetics

_SROP/BTI Gadget (madd)_

1. Load

2. Calculate

_ROP Gadget (madd-gadget-1)_ madd x0, x10, x8, x9 // x0 = (x10 * x8) + x9 ret // return to gadget #2

3. Store

4. Sigreturn

_JOP Gadget (madd-gadget-2)_ str w0, [x21, #0x10] mov x0, x19 blr x20 // back to __kernel_rt_sigreturn

Information Classification: General

## Slide 53

<u>https://developer.arm.com/documentation/102433/0200/Return-oriented-programming</u>

Information Classification: General


> Recovered by OCR — confidence 92/100 on the text kept, 92/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
arm Developer Develop Blogs Community CPU &Hardware Support
Pointer authentication
Armv8.3-A introduces the option of pointer authentication, FEAT_PAC. Pointer authentication can mitigate against ROP attacks.
Pointer authentication takes advantage of the fact that pointers are stored in a 64-bit format, but not all those bits are needed to represent the addr
virtual address space layout:
https://developer.arm.com/documentation/102433/0200/Return-oriented-programming
```

## Slide 54

Ubuntu GLIBC 2.43

pac

-fschedule-insns2

aut

Information Classification: General


> Recovered by OCR — confidence 72/100 on the text kept, 65/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Ubuntu GLIBC 2.43
-fschedule-insns2
Information Classification: General
@043afc4 stp fp, 1r, [sp, #-@x16]! {__saved_fp} {__saved_1r}
@043afc8 mov fp, sp {__saved_fp}
@043afd@ cbz w2, @x43b014
@043b014 mov x3, #0xe66d @043afd4 ldr x3, [x1, #0x10]
@043b018 mov w2, #0xb @043afd8 I1drh w4, [x1, #@xc]
@043b024 movk x3, #0x5, lsl #@x2@ {@xSdeece66d}
@043b028 mov x4, #@xb
@043b02c_ str w2, [x1, #@xc] {@x1@@@b}
@043b036 str x3, [x1, #0x10] {@x5deece66d}
le
@043afe@ Idrh wi, [x@, #0x4]
@043afe4 ldp fp, lr, [sp], #0x18 {__saved_fp} {__saved_1r}
aut —P | 6043afe8 autiasp
@043afec orr x1, x2, x1, 1lsl #0x2e
e043aff4 Isl w2, w2, #0x10
@043aff8 orr x1, x1, x2
@043b004 Isr x1, x1, #0x20
@043b00c mov wo, #0
@043b018 ret
```

## Slide 55

Ubuntu GLIBC 2.43

pac

-fschedule-insns2

aut

gadget

Information Classification: General


> Recovered by OCR — confidence 71/100 on the text kept, 65/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Ubuntu GLIBC 2.43
-fschedule-insns2
Information Classification: General
@043afc4 stp fp, 1r, [sp, #-@x16]! {__saved_fp} {__saved_1r}
@043afc8 mov fp, sp {__saved_fp}
@043afd@ cbz w2, @x43b014
@043b014 mov x3, #0xe66d @043afd4 ldr x3, [x1, #0x10]
@043b018 mov w2, #0xb @043afd8 I1drh w4, [x1, #@xc]
@043b024 movk x3, #0x5, lsl #@x2@ {@xSdeece66d}
@043b028 mov x4, #@xb
@043b02c_ str w2, [x1, #@xc] {@x1@@@b}
@043b036 str x3, [x1, #0x10] {@x5deece66d}
le
@043afe@ Idrh wi, [x@, #0x4]
@043afe4 ldp fp, lr, [sp], #0x18 {__saved_fp} {__saved_1r}
aut —P | 6043afe8 autiasp
@043afec orr x1, x2, x1, 1lsl #0x2e
e043aff4 Isl w2, w2, #0x10
0043aff8 orr x1, x1, x2
@043b004 Isr x1, x1, #0x20
@043b00c mov wo, #0
@043b018 ret
```

## Slide 56

Ubuntu GLIBC 2.43

pac

-fschedule-insns2 pac-ret[+leaf]

aut

gadget

Information Classification: General


> Recovered by OCR — confidence 76/100 on the text kept, 62/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Ubuntu GLIBC 2.43
-fschedule-insns2
pac-ret[+leaf]
Information Classification: General
pac —>
paciasp
stp fp, 1r, [sp, #-@x16]! {__saved_fp} {__saved_1r}
mov fp, sp {__saved_fp}
1drh w2, [x1, #@xe]
cbz w2, @x43b014
——
mov xo;
mov w2,
movk x3,
movk w2,
movk x3,
mov x4,
str w2,
#0x1, 1sl #@x1@ {@x1@@@b}
[x1, #@xc] {@x1@@@b}
[x1, #0x10] {@x5deece66d}
@043afd4 ldr x3, [x1, #0x10]
@043afd8 I1drh w4, [x1, #@xc]
le
0043afdc
0043afec
1dp fp, 1r, [sp], #0x1@ {__saved_fp} {__saved_1r}
autiasp
orr x1, x2, x1, 1lsl #0x20
e043aff4 Isl w2, w2, #0x10
0043aff8 orr x1, x1, x2
@043b004 Isr x1, x1, #0x20
@043b00c mov wo, #0
@043b018 ret
gadget
```

## Slide 57

### Conditional Branching

●If x Then sp = cond_true Else sp = cond_false ● next_sp =

= cond_true + (ind(x) * sizeof(rt_sigframe))

Information Classification: General

## Slide 58

### Conditional Branching

●If x Then sp = cond_true Else sp = cond_false

● sp =

= cond_true + (ind(x) * sizeof(rt_sigframe))

rt_sigframe frame_branch sp = ? pc = __kernel_rt_sigreturn pstate = 0 rt_sigframe cond_true rt_sigframe cond_false

Information Classification: General

## Slide 59

### Conditional Branching

●If x Then sp = cond_true Else sp = cond_false

● sp =

- = cond_true + (ind(x) * sizeof(rt_sigframe))

rt_sigframe frame_branch // ind(x) sp = ? ldr w1, [x2] cmp w1, #0 pc = __kernel_rt_sigreturn cset x1, ne pstate = 0 str x1, [sp, #0x10] rt_sigframe cond_true // … rt_sigframe cond_false blr x0

Information Classification: General

## Slide 60

### PoC #2

<u>https://github.com/betab0t/srop-bti</u>

Information Classification: General

## Slide 61

Information Classification: General


> Recovered by OCR — confidence 91/100 on the text kept, 90/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Linus Torvalds
the original email to the arm64 maii
> wrote.
p this seems to not be a very effective attack vector and is not
actically fixable, be
gnals by *design* have to be able to
return anywhere
5 would seem to require tha
be able to change
e signal
Stack in a very particular
y, SO you probably already
ity complete control of the program you're attacking
*design* have to be able to
spect this can be dis: ed publicly, ar
signal returr
has - as you poi
- already beer
arious other
contexts, but I th S is just how signals work
BTI isn't some kind of absolute shield. It's
st one layer of black hat
n among mz
```

## Slide 62

### OpenBSD

Information Classification: General


> Recovered by OCR — confidence 88/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= we) openbsd / src ~
Commit 7730d1d
deraadt
SROP mitigation. sendsig() stores a (per-process
inside the s
exact
40 files changed
A &sigcontext) cookie
```

## Slide 63

### OpenBSD

Information Classification: General


> Recovered by OCR — confidence 88/100 on the text kept, 78/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= we) openbsd / src ~
Commit 7730d1d
deraadt
SROP mitigation. sendsig() stores a (per-process
inside the s
exact
40 files changed
A &sigcontext) cookie
```

## Slide 64

XNU

<u>https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/status.c#L1060</u>

Information Classification: General


> Recovered by OCR — confidence 79/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
ser land_diversifier
discriminator traut d t land, sifier, = es) apple-oss-distributions xnu +
Code ©) Securityand quality |“ Insights
Commit a5e7219
@ AppleOssDistributions
xnu-6153.11.26
ntptr.
key_process ep ent_code, d at od > xnu-12377.121.6 «+:
3,016 files changed
(uintptr
key_proces
tps://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/status.c#L1060 Black hat
```

## Slide 65

XNU

<u>https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/status.c#L1060</u>

Information Classification: General


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= ptrauth_strir
user land_diversifier
= (uintptr_t)
t64_t discriminator
(uintptr_t)
key_proces:
tps://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/status.c#L1060
= es) apple-oss-distributions / xnu ~
Code Security and quality l¥ Insights
Commit a5e7219
@ AppleOssDistributions
xnu-6153.11.26
xnu-12377.121.6 ***
3,016 files changed
```

## Slide 66

XNU

<u>https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/status.c#L1060</u>

Information Classification: General


> Recovered by OCR — confidence 84/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
= ptrauth_strir
user land_diversifier
= (uintptr_t)
t64_t discriminator
(uintptr_t)
key_proces:
tps://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/status.c#L1060
= es) apple-oss-distributions / xnu ~
Code Security and quality l¥ Insights
Commit a5e7219
@ AppleOssDistributions
xnu-6153.11.26
xnu-12377.121.6 ***
3,016 files changed
```

## Slide 67

XNU

PRACTICALLY FIXABLE

<u>https://github.com/apple-oss-distributions/xnu/blob/main/osfmk/arm64/status.c#L1060</u>

Information Classification: General

## Slide 68

##### Omri Ben-Bassat “beta_b0t” <u>beta_b0t@yahoo.com https://www.linkedin.com/in/omri-ben-bassat</u>

# Thank You

<u>https://hackertracker.app/defcon34/content/66610</u>

Information Classification: General
