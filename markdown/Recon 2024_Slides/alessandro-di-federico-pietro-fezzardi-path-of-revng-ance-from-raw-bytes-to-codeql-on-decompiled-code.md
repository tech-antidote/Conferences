---
title: "Path of rev.ng-ance from raw bytes to CodeQL on decompiled code"
speakers: ["Alessandro Di Federico", "Pietro Fezzardi"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Alessandro Di Federico & Pietro Fezzardi_Path of rev.ng-ance from raw bytes to CodeQL on decompiled code.pdf"
pages: 74
sha256: "e3f3780b354d16cd5ab3b9754ebf33c6d680ff1deaf3be82085f39a3d32c1fb3"
text_chars: 12720
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:27:18Z"
---
# Path of rev.ng-ance from raw bytes to CodeQL on decompiled code

**Speakers:** Alessandro Di Federico, Pietro Fezzardi  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Alessandro Di Federico & Pietro Fezzardi_Path of rev.ng-ance from raw bytes to CodeQL on decompiled code.pdf` (74 pages)

## Slide 1

## **The binary analysis framework**

2

## Slide 2

This presentation is available at:

All the demos are available at:

3

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
This presentation is available at:
rev.ng/presentation
All the demos are available at:
github.com/revng/demos
```

## Slide 3

#### 1. 10 people 2. Partly in Milan, Italy, partly in rest of Europe 3. Compiler engineers/security researchers 4. We worked with

4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
rev.ng Labs
1. 10 people
2. Partly in Milan, Italy, partly in rest of Europe
3. Compiler engineers/security researchers
4. We worked with
Qualcown HUAWEI
```

## Slide 4

# **Outline**

1. rev overview .ng 2. Demo: with rev .ng 3. Let’s put our hands into 4. Demo: automatic bug finding 5. Automated recovery 6. The

5

## Slide 5

## **rev.ng**

6 . 1

## Slide 6

**rev.ng is an binary analysis framework and decompiler for native code**

6 . 2

## Slide 7

### **This is a**

#### **LLVM**

clang
C ARM
-O2
clang++
C++ LLVM IR MIPS
rustc
rust x86-64

6 . 3

## Slide 8

## Slide 9

### **This is a**

#### **QEMU**

ARM ARM
-O2
MIPS Tiny code MIPS
x86-64 x86-64

6 . 4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
This is a dynamic binary translator
QEMU
ARM -02 ARM
™a A”
MIPS MIPS
ZA Ny
x86-64 x86-64
```

## Slide 10

## Slide 11

### **This is a**

#### **rev.ng**

ARM
-O2
MIPS Tiny code LLVM IR C
x86-64

6 . 5

## Slide 12

## Slide 13

# **Using**

7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
¢e
Using QEMU as a lifter
```

## Slide 14

**We use QEMU but we run any code We just use it as a lifter**

8

## Slide 15

### **Writing an**

### **is hard**

9

## Slide 16

#### QEMU Advent Calendar

10 . 1

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
QEMU Advent Calendar 2023+ Finalday Jumptoday~ About —Contact
FROM QEMU TO YOU
HAPPY HOLIDAYS???
Day 1 - TinyCore Linux Day 2 - Bootable PDF holiday card Day 3 - Bootable Assembly word
TinyCore linux Bootable PDF holiday card game: FLORDLE
Size of download Is 22M bytes. Size of download is 8M bytes. Bootable Assembly word game: FLORDLE
"Download Size of download Is 2.5k bytes.
QEMU Advent Calendar
10.
```

## Slide 17

**Supporting is hard** QEMU supports: Alpha, , CRIS, HPPA, , Hexagon, LatticeMico32, 68K, MicroBlaze, , Moxie, Nios2, OpenRISC, PowerPC, RISC-V, SH4, Sparc, , TileGX, TriCore, Unicore32, Xtensa

10 . 2

## Slide 18

### **QEMU is for:**

- a ccuracy

- s upporting many architectures

- • l ifting

- d ynamic binary translation

10 .

3

## Slide 19

### **QEMU is for:**

• a nything else

10 . 4

## Slide 20

Tiny code

LLVM IR

10 . 5

## Slide 21

## **Here be dragons**

10 .

6

## Slide 22

- E nable us to focus on building a , not a compiler framework

- • W ell known and big community

- • W ell defined semantics

- KLEE Phasar

- M any tools build on top of it ( , , …)

- • H igh performance (C++)

10 . 7

## Slide 23

### **A note on**

We do not use symbolic execution in the pipeline. However, we deem it appropriate for bug hunting!

10 .

8

## Slide 24

**A note on** We’ve done it. We’re no longer focused on it. There are a lot of effective alternative approaches.

10 .

9

## Slide 25

## **How do I with rev.ng?**

11 .

1

## Slide 26

# **The**

• b asically rev.ng’s project file • a YAML document

• c ontains everything the user can customize

11 .

2

## Slide 27

# **Example**

Architecture: x86_64 DefaultABI: SystemV_x86_64 Segments: - StartOffset: 0 FileSize: 7 StartAddress: "0x400000:Generic64" Functions: - Entry: "0x400000:Code_x86_64" Types: - Kind: StructType ID: 1 Size: 8 Fields: - Offset: 4 Type: ...

11 . 3

## Slide 28

#### Interaction option #1: the

revng \ artifact \ --analyze \ decompile-to-single-file \ /bin/df

#### Interaction option #2: the

Python
revng-daemon
HTTP
... API rev.ng core
UI TypeScript

11 . 4

## Slide 29

## Slide 30

### **tl;dr: stay** They can:

- u se any language having YAML + HTTP /system

- • u se any version of the language they want

- • u se a different version of LLVM

- b e on a different machine

- c rash independently from rev.ng

11 . 5

## Slide 31

### **No more**

11 . 6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
No more
hex rays Products > Solutions Partners Shop Support > Company >
IDAPython and Python 3
As of now (IDA version 7.3), IDA ships with an IDAPython plugin, that is compiled against, and compatible with Pyt!
The Python ai that Python 3 has been available for long enough, to drop support for Pyt!
That effectively means that since Python 2.x will be unmaintained, it will gradually disappear from the landscape.
Work has begun (in fact, work is even finished) here at Hex-Rays to make IDAPython compilable, and compatible with Pyt
11.
```

## Slide 32

**Wrappers** In practice, we make things easier for and users with wrappers.

11 . 7

## Slide 33

### **stay**

11 . 8

## Slide 34

**stay** They have to buy into our dev stack (docs)

11 . 9

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
developers stay in-process
They have to buy into our dev stack (docs)
```

## Slide 35

## **Demo time!**

12

## Slide 36

tl;dr there are only two types of actions: 1. Request an (LLVM IR, valid C, …) 2. Run an /make changes to the model

13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
tl;dr there are only two types of actions:
1. Request an artif
2. Run an anal
(LLVM IR, valid C, ...)
/make changes to the model
13
```

## Slide 37

## **It’s time!**

14

## Slide 38

**Example program** long myfunction(long value) { long result = value; result = result * 2 ; return result; }

15 . 1

## Slide 39

# **Disassembly**

1 myfunction: 2 push rbp 3 mov rbp,rsp - 4 mov QWORD PTR [rbp 0x8],rdi - 5 mov rax,QWORD PTR [rbp 0x8] - 6 mov QWORD PTR [rbp 0x10],rax - 7 mov rax,QWORD PTR [rbp 0x10] 8 shl rax,0x1 - 9 mov QWORD PTR [rbp 0x10],rax - 10 mov rax,QWORD PTR [rbp 0x10] 11 pop rbp 12 ret

15 . 2

## Slide 40

.

15

3

## Slide 41

15 . 4

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CALL Prempctptr nena # remy
ptr met, ptr meth)
15.4
```

## Slide 42

15 . 5

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Gefine 164 Plocal_myfunction(i64 Srdi_xB6_64) {
NO = call 164 @_init_rdpt)
Call Bnewpe(ptr nonnull @"revng. const .0x481130
ptr null, ptr nuit)
Sl = Load 164, ptr @rsp
S2 = add 164 &
SS = inttoptr 164 <2 te ptr
Store 164 8, ptr %
Store 164 82, ptr @rsp
call Bnewpe(ptr nonnull @"revng. const .6x481131:
ptr null, pte mult)
4 = Load 164, ptr @rsp
call @nenpe(ptr nonnull @"revng. const .0x401134
ptr null, pte mull)
SS = add 166 %4
SO © Anttoptr 164 85 te ptr
Store 164 Srdi_x86_64, ptr \s
call @nenpe(ptr mennult 5 0x401138
ptr null, pte mull)
7 = Load 164, ptr %
call @neape(ptr nonnull @"revng. const .6x48115¢
ptr null, ptr mutt)
NO = add 166 %4, -1
SP © Anttoptr 164 X8 te ptr
store 164 7, ptr so
call Bnespe(ptr monnull @*revng. .0x401140
ptr null, pte mull)
X10 = load 466, ptr ®
call @neape(ptr nonnull @"revng. const .6x481144
ptr null, ptr nuit)
Sli = shi 466 %2
COLL Bnewpe(ptr nonnull B"revng. const.0x401148
ptr null, pte mull)
store 164 X11, ptr %9
call Bnenpe(ptr nonnull @* sonst .Ox48114¢
ptr null, ptr nuit)
S12 = load 164, ptr x9
call Brewpe(ptr nonnull @*revng. const 0401150:
ptr mult, ptr mutt)
S15 © Load 466, ptr @rsp
S14 = add 466 S15, |
store 164 X14, ptr @rsp
CALL Bnenpe(pte monnuLt ; 0x401151
ptr mult, ptr mutt)
15 = load 164, ptr @rsp
S16 = add 166 %2
store 164 X16, ptr @rsp
ret 166 &
}
Code_x86_64"
Code_x86_64"
Code_x86_64",
Code_x86_64",
Code_x86_64"
Code _«86_64"
Code_x86_64"
‘Code_«86_64"
Code_x86_64"
15.5
```

## Slide 43

.

15

6

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
164 @local_myfunction(i64 %0) {
call i64 @revng_stack_frame(i64 24)
call i64 @AddressOf(ptr nonnull
.const.c10d6afb753dc601da714646784a7e4040e86F7b, 164 %1)
add i64 %2, 8
inttoptr i64 %5 to ptr
call ptr @stack_offset(ptr %4, i64 -16, i64 -7)
store i164 %0, ptr %5
%6 = inttoptr i64 %2 to ptr
%7 shl i164 %0, 1
%8 = call ptr @stack_offset(ptr %6, i64 -24, i164 -15)
store i164 %7, ptr %8
ret i164 %7
15.
```

## Slide 44

15 . 7

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
define i64 @local_myfunction(i64 %0) {
%1 = shl i164 %0, 1
ret 164 %1
15.
```

## Slide 45

**A couple of demos** 1. Write a small ( ) 2. Collect some information about ( )

16 . 1

## Slide 46

## **-ENOTIME You can check them out at**

16 . 2

## Slide 47

**Things you can do in LLVM** • G raph theory ▪ B uild the ▪ I dentify ▪ P erform (depth first, topological…) • M anipulate functions ▪ I nline ▪ O utline ▪ S pecialize

17

## Slide 48

# **Let’s find some bugs!**

- U se for revng

- or

- W ith static analysis tools for

- • D emo on LLVM IR:

• W e’ve got offline demos on C with ▪ C lang Static Analyzer ▪ C odeQL

18

## Slide 49

### **What is**

• engine for LLVM • W orks on vanilla LLVM IR • H as a builtin set of states known as bugs: ▪ fail

▪ v arious classes of

• R egular use from source code

19

## Slide 50

### **Demo time!**

20

## Slide 51

### **Bug-finding ?**

- T ake the same input program

- • D ecompile it with revng

- F eed it into source-level static analysis tools ▪ C lang Static Analyzer

- ▪ C odeQL

- P rofit!

21

## Slide 52

### **Clang static analyzer ( )**

##### Original C

Clang Static Analyzer Report

void my_free(void *p) { free(p); } int do_stuff(int condition) { int *p = malloc(sizeof(int)); if (condition > 4) my_free(p); *p = 3; int result = *p; my_free(p); return result; }

22

## Slide 53

### **CodeQL ( )** Original C CodeQL Report

int do_stuff(int condition) { _ABI(SystemV_x86_64) int *p = malloc(sizeof(int)); generic64_t do_stuff(generic64_t _argument0) { if (condition > 4) void *_var_0; free(p); _var_0 = malloc((size_t) 4); *p = 3; if ((int32_t) (generic32_t) _argument0 > (int32_t) 4) { int result = *p; // BUG 1: call to free free(p); // BUG 2: call to free return result; free((generic32_t *) _var_0); // line 69 } } // BUG 1: Potential use after free // An allocated memory block is used after it has been freed. // Behavior in such cases is undefined and can cause memory corruption. // Memory may have been previously freed by call to free at line 69. *(generic32_t *) _var_0 = 3; // BUG 2: Potential double free // Behavior in such cases is undefined and can cause memory corruption. // Memory may already have been freed by call to free at line 69. free((generic32_t *) _var_0); return 3; }

23

## Slide 54

- **Automated bug-finding with** • revng output quality plays well with tooling • D ifferent levels of abstraction: LLVM IR or C • L LVM: crossroad of project for static analysis

- • C : has a huge base of analysis tools

24

## Slide 55

25

## Slide 56

### **No type recovery**

generic64_t sum(generic64_t _argument0) { generic64_t _var_0 = 0, _var_1 = 0 ; do { _var_1 = _var_1 + *(generic64_t *) ((_var_0 << 3) + _argument0); _var_0 = _var_0 + 1; } while (_var_0 != 5); return _var_1; } generic64_t compute(generic64_t _argument0) { generic64_t _var_0 = _argument0, _var_1 = 0; generic64_t _var_2; do { gen_var_2 = sum(_var_0); _var_1 = _var_1 + _var_2; _var_0 = *(generic64_t *) (_var_0 + 40); } while (_var_0); return _var_1; }

26

## Slide 57

### **With automated type recovery**

typedef struct _PACKED _struct_61 { generic64_t _offset_0[5]; _struct_61 *_offset_40; } _struct_61; generic64_t sum(_struct_61 *_argument0) { generic64_t _var_0 = 0, _var_1 = 0 do { _var_0 = _var_0 + _argument0->_offset_0[_var_1]; _var_1 = _var_1 + 1; } while (_var_1 != 5); return _var_0; } generic64_t compute(_struct_61 *_argument0) { _struct_61 *_var_0 = _argument0 generic64_t _var_1 = 0, _var_2; do { _var_2 = sum(_var_0); _var_1 = _var_1 + _var_2; _var_0 = _var_0->_offset_40; } while (_var_0); return _var_1; }

27

## Slide 58

28

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
sum() compute ()
Prototype Prototype
_cabifunction_78 _cabifunction_79
_cabifunction_78 (size: 0) _cabifunction_79 (size: 0)
Return Types Arguments Return Types Arguments
generic64_t * struct_6l1 generic64_t * struct_61
\
SC Pointer (8 bytes) _- Pointer (8 bytes)
vy
_struct_61 (size: 48)
Offset Size Name
Pointer (8 bytes)
40 generic64_t [5]
* struct_61
```

## Slide 59

## **The**

## **of rev.ng**

29 . 1

## Slide 60

# **Supported**

- x 86 • x 86-64 • A RM

- A Arch64 • M IPS

- S ystemZ

29 . 2

## Slide 61

• E LF

• D WARF • P E/COFF • C odeView (.pdb) • M ach-O

#### • I DA Pro

29 .

3

## Slide 62

**does rev.ng run?** • D aemon ▪ L inux x86-64 natively ▪ m acOS via Docker ▪ W indows via WSL • C lients can run anywhere

30

## Slide 63

**Recently, we released the pipeline as open source. We’re now focusing on and .**

31

## Slide 64

We currently produce IR for GCC in 18 minutes.

- N ew argument detection analysis: 2.1x

- • R educe invalidation: ~1.7x (10min expected)

- • O ther low effort fixes: ~2x (5min expected)

32

## Slide 65

# **Goal: with Ghidra and IDA**

1min 30sec and 40sec

33

## Slide 66

# **Next up:**

• D ecompile all binaries on: ▪ U buntu x86-64 ▪ W indows x86-64 ▪ A ndroid AArch64

• F ocus on:

▪ o ptimizing performance of bottlenecks ▪ s quashing bugs

34

## Slide 67

#### In short,

#### • i s FLOSS

- i s declarative in user interactions • h as a modern design

- u ses a “standard” IR and emits valid C • i nteracts with existing tools

- h as a nice (commercial) UI

35

## Slide 68

• B ased on , mostly a plugin • C onnects to • R uns as a app or in the • just works out of the box • A lso, (think GitHub for reversers) • C loud version will be

36

## Slide 69

### **Final note** We’re and we do

37

## Slide 70

0:00 / 2:03

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
1) EXPLORER
, UNTITLED (WORKSPACE)
\/) ~ linked_list (on rev.ng cloud)
> binary
> function
> type
! model.yml
» OUTLINE
@
pe
Questions?
) Untitled (Workspace)
= Overview: linked_list (on rev.ng cloud) x
Upload Binary
No file chosen
@ Upload & Analyze Binary
Segments:
Start address End address
> 0x400000 0x400b98
> 0x401d98 ‘)
>
O80
O
Information
Architecture: x86_64
DefaultABI: SystemV_x86_64
Entrypoint: unreserved__start (0x4007c0:Code_x86_64)
Size File Offset uci aos) Permissions
ize
2968 1°) @ r-x
657 3480 1 rw-
0:00/2:03 wW §2
38
```

## Slide 71

## **Backup slides**

39 . 1

## Slide 72

# **frontends?**

-O2
ARM ???
LLVM IR C
MIPS Tiny code
x86-64

39 . 2

## Slide 73

## Slide 74

# **Idea**

typedef struct { uint32_t rax; uint32_t rdi; // ... } CPUState; void add(CPUState *state) { state->rax = state->rax + state->rdi; }

WIP, particularly interesting for WebAssembly

39 . 3
