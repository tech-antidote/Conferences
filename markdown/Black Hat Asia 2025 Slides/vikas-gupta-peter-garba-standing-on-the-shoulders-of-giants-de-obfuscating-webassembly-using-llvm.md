---
title: "Standing on the Shoulders of Giants De-Obfuscating WebAssembly Using LLVM"
speakers: ["Vikas Gupta", "Peter Garba"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Vikas Gupta & Peter Garba_Standing on the Shoulders of Giants De-Obfuscating WebAssembly Using LLVM.pdf"
pages: 80
sha256: "425a31817412c79bd3b686dde7cf103f579e2b60c574392780252aa02bd4d6bf"
text_chars: 39653
ocr_pages: 35
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:09:02Z"
---
# Standing on the Shoulders of Giants De-Obfuscating WebAssembly Using LLVM

**Speakers:** Vikas Gupta, Peter Garba  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Vikas Gupta & Peter Garba_Standing on the Shoulders of Giants De-Obfuscating WebAssembly Using LLVM.pdf` (80 pages)

## Slide 1

**Standing on the Shoulders of Giants** De-Obfuscating WebAssembly Using LLVM

**Vikas Gupta & Peter Garba Thales** Cybersecurity & Digital Identity (CDI)

## Slide 2

Agenda

2

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2\int w2c_squanchy_calc_0(undefined8 param_1,uint param_2)
5) uint uVari;
6) int ivar2;
7) int ivar3;
8
9} wari = param_2 & 3;
10) iVar3 = (param_2 * Oxbaaaddbf) * (param_2 | 4);
12) iVar3 = (param_2 & 5) * (param_2 + Oxbaaadobf);
+
14) ivar2 = (param_2 | Oxbaaaddbf) * (param_2 ~ 2);
15) if (uvar1 Dae
16 ivar2 = (param_2 & @xbaaad@bf) * (param_2 + 3);
+
19) iVar3 = ivar2;
+
21) return iVar3;
```

## Slide 3

##### About Us

- **Vikas Gupta**

   - Senior Security Researcher at _Thales CDI_ , previously with _Google_ .

   - ○ Masters in information security, OSCP Certified

   - ○ Co-Author OWASP Mobile Security Testing Guide (MSTG)

   - Interests: Reverse engineering, mobile security

- **Peter Garba**

   - Principal Software Security Engineer at _Thales CDI, Singapore_

   - ○ Product Owner

   - Author of the Thales internal obfuscation tools

   - Passionate reverse engineer at night.

3

## Slide 4

##### Motivation

4

## Slide 5

##### Problem Statement

1. Is Wasm <u>secure</u> for us?

2. <u>Obfuscate Wasm binaries</u>

3. Lifting Wasm to LLVM IR

4. <u>Deobfuscate Wasm binaries &</u> recover original logic

5

## Slide 6

##### Achievements

- Demonstrating use of existing tooling for Wasm

   - Obfuscation

   - Deobfuscation

- Lifting Wasm to LLVM IR - Squanchy

- Automated deobfuscation of Wasm

6

## Slide 7

## WebAssembly Essentials

7

## Slide 8

##### WebAssembly Essentials

- Announced in 2015, a high-performance, secure, and portable <u>compilation target.</u>

- Binaries that are compact and quick to parse.

- Runs in a stack based virtual machine (think JVM)

   - Communicates with host program using well defined exports and imports

- Wide adoption

   - Games

   - Big web apps - Google Earth

   - Blockchain smart contracts

   - ...

8

## Slide 9

##### WebAssembly Essentials

- Each Wasm program is a single file of code - Module.

- Module is organized in sections. ○ Sections - Export, imports, globals, functions etc.

- Indexed Spaces

   - Items can be accessed by a 0-based integer index

- Code and data spaces are disjoint

   - compiled programs cannot corrupt their execution environment

   - ○ Can not jump to arbitrary locations

   - Perform other undefined behaviour

9

## Slide 10

# WebAssembly Tooling

10

## Slide 11

##### WebAssembly Tooling

- <u>WebAssembly Binary Toolkit</u>

- <u>Wasm-tools</u>

- Ghidra

   - Using a <u>Wasm plugin</u>

- Used to view decompiled Wasm

- ● IDA Pro v9

- It is hit-n-miss with Wasm

- ○ Using to view object files

- ● JEB Pro

11

## Slide 12

### WebAssembly Obfuscation

12

## Slide 13

##### Obfuscation

- <u>Obfuscation: Process of making a program harder to</u> understand while preserving the original program’s behavior.

- To make code unreadable, for reasons...

   - Malware author to avoid reversing

   - ○ In apps, to prevent stealing/reversing of IP

   - ○ Digital Rights Management (DRM)

13

## Slide 14

##### WebAssembly Obfuscation: Approaches

14

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
WebAssembly Obfuscation: Approaches
possssesseeee-- | pessssssseee-- ; poccccccctsen- 1
i]
Source Level ' : IR Level ; = Wasm Level N
- i
C Source P——*+>| C Source P= +>) LLVMIR [—— >] WebAssembly -+— Bi
' Emgcripttn Glan i inary
1 (dlang)t ou 7 "
' Tigress 5 & O-LLVM 4 § wasm-mutate | 1!
14
ASIA 2025
```

## Slide 15

##### Obfuscation Using LLVM

- Open Source Obfuscators: <u>O-LLVM, Hikari, Polaris</u>

- ● Works on the middle-end

- Approach is source language agnostic

15

## Slide 16

##### LLVM Based Obfuscators

###### O-LLVM

- Instruction Substitution

- Control Flow Flattening

- Basic block splitting

- Bogus control flow

###### Hikari

- Bogus control flow

- Control Flow Flattening

- Function call Obfuscate

- Function wrapper

   - Basic block splitting

-

- String encryption

- Instruction Substitution

- Indirect Branching

###### Polaris

- Alias Access

- Flattening

- Indirect Branch

- Indirect Call

- String Encryption

- Bogus Control Flow

- Instruction Substitution

- Merge Function

- Linear MBA

16

## Slide 17

##### Obfuscation: O-LLVM Instruction Substitution

O-LLVM Instruction Substitution (Loop=3)

O-LLVM Instruction Substitution (Loop=1)

17

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bfuscation: O-LLVM Instruction Substitution
. *0O-LLVM Instruction
Substitution (Loop=3)
O-LLVM Instruction
Substitution (Loop=1)
if (iVarl =
local_10
0) {
(paraml & OxbaaadObf | param1 ~ OxbaaadObf) *
(((paraml * Oxffffffff) & Oxbcec65b1 | param1 & 0x43139a4e) * Oxbcec65b3);}
pisex hat
ASIA 2025
tf (tard == 0) {
wVarl0 = paraml & Oxc9e645ce | (param ~ OxfffffFft) & 0x3619ba31
warll = ((uvar1@ ~ 6x3619a31) & OxSc2eaifS | (uVar1 ~ ExcDe645ce) & @xa3d15e0a) ~ Oxf1571094
| ware ~ 6x3619ba31;
warl2 = (param ~ oxtffffftt) & oxad796f68 | param & 0x52864097) ~ oxtffttttt |
paraml * oxtffftttts
wars = uvarli | warl2;
Warll = (wVarl2 ~ OxffFff fff) & wari | (uWarll ~ OxffFFTTFA) & wWari2;
warl2 = wVaril * oxfffftttt;
warll = (ward & Oxaea378C3 | (uVard * OxffFfff ff) & x515CB73C) *
(uVarl2 & Oxaea378c3 | wVarll & 6x515c873c) | (ward | warl2) ~ oxttfftftts
warl2 = ((uvarll ~ Oxffffffft) & Oxcb7321da | Warll & Ox348cdeb5) ~ Oxcb73214a | Ox604afl1c;
warll = uVaril * oxfffffttt | ox9fbS0ee3;
warll = (wvarl2 & 0x5835bf98 | (wWarl2 * Oxtffffftt) & Oxa7ca4067) *
(uVarll & 0x58350f98 | (uVarll ~ oxff fff tft) & Oxa7ca4067) |
(wari2 | warl1) * oxtffffttt;
warll = (warll ~ Oxfffftfft) & 0x88666134 | uVaril & 0x77999ecb;
warl2 = uVarl® ~ 0x3619ba31 | Oxbaaadoof;
warl0 = (uVarle ~ 0x3619ba31) & 0x565b2720 | (uVarle ~ OxcSe645ce) & OxaSa4d85t;
Ward = wWarle * exectf71f;
wVarl2 = (warl2 & OxcdtalS85 | (warl2 > oxtffftftt) & Ox3b0Sea7a) *
(uVard & oxcétal585 | (uVarl® ~ 6x130e08e6) & 6x3b05ea7a) |
(wWari2 | ward) > oxttfftttts
wvarl0 = (((uVari2 * Oxfffffftf) & Oxbe3cBGad | uVari2 & 6x41c37952) * exbe3cBbad | xe6842217)
* Oxtffttttt;
uvari2 = (wVarl2 ~ x197bdde8) & uvari2
Vario = uVar20 & uvari2 | uvarie * wvara2;
warl0 = (warle ~ oxffffffff) & Ox9di1e123 | uVari0 & ox62ee1edc;
warl0 = (uVarle ~ ox846a3ccb) & 0x61675078 | (uVarl@ ~ 0x7b95C334) & Ox9e98atB7;
wVarl0 = (uVarl0 ~ 0x61675078) & 0xa63617bd | (uVar]e ~ 0x9e98af87) & 0x59C9e842;
warl2 = (wVarl1 ~ warl0 ~ 0xa63617bd) & wVarl1;
wVarl0 = ((uvarll ~ oxtffTffFt) & exbccsbddd | wVarl1 & 0x4339422b) *
((uVarl0 ~ 6xa63617bd) & exbccBbdd4 | (uVarlO ~ 6x59c9e842) & 0x4339422b);
Warll = wari2 * oxtfFrttfts
Warl® ~ Oxtffttttts
param ~ Oxffffffff) & 6xaf91567b | param & @x506ea994;
ar5 ~ 0xaf91567b;
1uVar6 & Oxe30d84a7 | (uVarS * 9x506ea984) & Ox1cf27b58) ~ Oxe30d84a5 |
(uvaré | Oxf ffftttay * oxtferteet;
((param. * OxfffffFff) & @x7ceBffb1 | param & 0x831f004e) ~ Oxea109553) & Ox96f06a62;
paraml ~ OxffffttfT | Ox96f06ae2) ~ Oxtfrttttt;
WWar6 * wVar7;
uVarB ~ OxffffFftF) & 0x690f951d | uVar6 & wWar7 | uVar8 & 0x96F06a02;
wVar6 = wWaré & Oxba8cSc70 | (uVaré ~ Oxftffttft) & 0x4573a38F;
1uVar6 ~ 0x4573a38f) & (uVar6 ~ OxbaBc5c72);
juVar5 * @xcb0as819)
‘uVarS | @x34f5a7e6)
ors = (war6 * 0x34f5a7e6) & (uVar6 * Oxtffttftt);
jar2 = (uVar6 * 0x34f5a7e6) & war;
War? & wVar8 | uVar7 ~ uVar8;
war8 = ward ~ oxtfffttft;
war3 = war2 ~ oxtftftttt;
war8 = (uVar8 & Oxd3d541ce | uVar & Ox2c2abe31) * (uVar3 & Oxd3d541ce | UVar2 & @x2c2abe31) |
(uvar8 | wvar3) ~ oxfffftttts
war? = ((uVar? * Oxfffffftt) & Oxefdsab1i | uVar7 & 0x1027b4ee) *
((uVar8 > oxtfftfftt) & exefds4b11 | uVar8 & 0x1027bsee);
wars = ((uVarS * Oxfffffttt) & oxtfb73ee8 | uWarS & x48c117) ~
(uvaré & oxffb73eeB | (uVaré * oxtfftfftt) & Ox48c117) |
(uvars * oxtfffertr | wvar6) > oxtfferttrs
WarS = (uVarS * OxtffTFftt) & Oxa9See2be | WVarS & OxS6al1d41;
War6 = war5 ~ oxa9Sec2be:
war8 = war? ~ oxtfffttft
Local_10 = ((uVari1 & «1098326 | uVari2 & Oxfe167cd9) ~
(uvara & 0x1698326 | wVarl0 & Oxfe167cd9) | (uVari1 | uWara) ~ Oxtffrftet) *
((uVar8 & 9xcBa77567 | wWar7 & 37588098) *
(uWaré & 0xcBa77567 | (uVar5 * GxS6a11d41) & 0x37588298) |
(war8 | war6) ~ Oxffffftft)s
```

## Slide 18

18

##### Obfuscation: Control Flow

## Slide 19

##### Obfuscation: Complexity Increases

- On applying obfuscation multiple times

   - Binary sizes can balloon, e.g to 12MB

   - 2k+ LoC of decompiled code.

   - ○ Tools start to break

19

## Slide 20

#### WebAssembly Deobfuscation

20

## Slide 21

##### Deobfuscation

- Revert the transformations (sometimes impossible)

- ● Simplify the code to facilitate further analysis

- _Classical Obfuscation_

   - Obfuscation patterns, constant unfolding, junk code insertion

- _Classical Deobfuscation_ ○ Pattern matching

- _Modern obfuscation_ ○ Source Code Level ○ Intermediate representation level

- _Modern deobfuscation_

   - Several Intermediate Languages at different abstract layers

   - Based on generic optimization tools

21

## Slide 22

##### SATURN: Compiler Based Deobfuscation

- Generic approach for deobfuscation based on LLVM compiler infrastructure.

- ● Weaken certain obfuscation, and in best case completely remove them.

22

## Slide 23

##### SATURN: Compiler Based Deobfuscation

23

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
SATURN: Compiler Based Deobfuscation
r sree erer2= q PoC 0 SSS SSS S BES SSESSSSS5 S85 S88SS8SSs880° =eeeee = — 7 ee
Input 1 : Deobfuscation ! 1 Output '
| MachO File |! Optimizations "  ——+ Shared Object]!
w
it Pt
i| ELF File : +>] Translation }——»| LLVMIR |—> Brightening = H f
\
i PE File — ' OP Detection Injection —— Patched File
! I
Leneenenene 5 |r 1 ' Leae------- J
Boaaa Ss SOOO SOO OO OOS SOD OSS SUSU OBES SOD BHOeSSOGSd
blackhat
ASIA 2025
23
```

## Slide 24

##### Binaryen

- Binaryen is a compiler and toolchain infrastructure library for Wasm.

- Binaryen's optimizer has many passes that can improve code size and speed.

- Input Wasm, Output Wasm

- <u>Didn’t work - no deobfuscation</u>

24

## Slide 25

25

## Slide 26

# Lifting to LLVM IR

26

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
® Lifting to LLVM IR
poaaaaa se anesecnceeeoone-- 1
t Lifting "
‘ i
' t
Obf. Wasm |_4.. soo i
Binary 1 22? >| LLVMIR [>] Clang Object File
'
i]
```

## Slide 27

##### Why LLVM?

- LLVM - a target-independent optimizer and code generator.

- ● LLVM has a language-independent intermediate representation (IR)

- Advantages of using LLVM IR

   - World Class Optimizations and Analysis Passes

   - Feature rich intermediate language

   - Accessible API

   - Normalization

   - Several backends available for recompilation

   - _○_ _<u>It’s fast!</u>_

27

## Slide 28

##### Challenges of Lifting

- To leverage LLVM optimisation passes, requires lifting Wasm to LLVM IR.

- <u>Challenges</u>

   - Correctness

   - Captures side effects and expressiveness

   - Representation of the runtime environment

   - Stack machine to register machine transformation

28

## Slide 29

##### Wasm Code Lifting to C: Lifting Principles

Wasm Code Wasm Opcode Specification

Lifted C Code

29

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting to C: Lifting Principles
Wasm Code Wasm Opcode Specification Lifted C Code
Get Local
. text
file “add.c" Mnemonic Opcode _—Immediates Signature u32 add(u32 var_p0, u32 var_p1) {
.functype add (132, i32) -> (132) A ~ a ~
aan “text.add,"",@ local.get 0x20 $id: varuint32 © () = ($TI11) u32 var_i0, var_il;
«hidden add . _ .
“globt. add var_i@ = var_pl;
type add, @function var il = var pQ:
add: # @add Integer Add -, —p 2
.functype add (i32, i32) -> (132) var_i@ += var_il;
ree A Mnemonic Opcode Signature var_il = 15u;
local.get 10) i = il:
i32.add i32.add © Ox6a (432, 432) : (432) var_i0 + var_t1;
i32. const 15 return var_i0;
i32.add i64.add Ox7c (4164, 164) : (164) }
end_function
Mnemonic Opcode Immediates Signature
i32.const 0x41 $value : varsint32 (+ (432)
blackhat a)
ASIA 2025
```

## Slide 30

##### Wasm Code Lifting: Using WAMRC

- WebAssembly Micro Runtime (WAMR) ○ Lightweight, standalone Wasm runtime

   - WAMR Compiler (WAMRC)

■ The AOT compiler to compile Wasm file into AOT file

- <u>Shortcomings</u>

   - Symbols information is lost

   - ○ Generated LLVM IR does not contain various tables (global’s table, function table) => LLVM <u>optimisations don’t work</u>

30

## Slide 31

31

## Slide 32

##### Wasm Lifter Problem Persists

32

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Lifter Problem Persists
pono ocnnnnnssscsennnnnn-—- :
: Lifting "
1 u
J "
‘|
Nf W/E 22? ->| LivVMIR | lang -—»| Object File
J
Binary ' | -
i) i)
es eles eee ee eee ene eae ae eee eee ne J
(2)
blackhat
ASIA 2025
32
```

## Slide 33

##### Wasm Code Lifting: Code Lifters Comparison

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: Code Lifters Comparison
_— Instance P
Lifting Language Code Foldin Comments
| _Name | Lifting Language Parameter | Code Folding | Comments
WAMRC LLVM IR yes Partially No tables ( aa
functions...
pifek hat 33
ASIA 2025
```

## Slide 34

##### Wasm Code Lifting: Lifting Idea!

34

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: Lifting Idea!
POT eee 7
penne oan eee 5 pocesssssseaey ee t Pseudo C '
i]
!  Wasm Level c ! Source Level [ IR Level ' dion EB ee " '
LJ ! ' 4 ' " >|Native Object/——__ C Source |,
rT 1 1 ' 1 tl Binary Ninja -_ ~~
u i C Source
u | Wasm Binary R==¥ lang -O0 1 1
Leeense------ 5 bososossesass zi ' jt clang -03 -< —, >| Wasm Object
' ; -target wasm
1 i]
| | Optimisations | !
' Runtime '
Helpers C
a
pif hat 34
ASIA 2025
```

## Slide 35

##### Wasm Tool: wasm2c

- Great tool to lift Wasm to C

- Well defined wasm runtime that helps during deobfuscation ○ Helpers to initialize - Wasm instance and memory ○ Helpers to initialize and modify globals

   - Helpers for load/stores to memory ■ Load/Stores are access through helpers that can be overridden

- Does not modify the original Control Flow Graph

- <u>Shortcomings</u> ○ Runtime information (tables…) not available for each function

- ○ Code doesn’t fold

35

## Slide 36

##### Wasm Code Lifting: Motivating Example

36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: Motivating Example
int add(int a, int b) {
inte ann l= (59253545 55;
int sum = 0;
// Loop to calcuate a constant
Ton (inl W= Os Vv <95s i++) {
sum += arr[i];
}
// MBA based Opaque Predicate
sum += 1911;
} else {
sum += 2102;
}
bisekhat
ASIA 2025
int add(int a, int b) {
return a + b + 1926;
i
36
```

## Slide 37

##### Wasm Code Lifting: wasm2c (O3 Unobfuscated)

**wasm2c clang -O3 clang -c + IDA Pro**

37

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: wasm2c (O3 Unobfuscated)
u32 w2c_squanchy_add_@(w2c_squanchy* instance,
u32 var_p0, u32 var_p1) {
u32 var_i0, var_il;
var_iO = var_p1;
-text var_il = var_p0;
file = "“add.c" var_i0 += var_il;
. functype add (i132, 132) -> (132) var_il = 15u;
.section .text.add,"",@ var_iO += var_il;
hidden add return var_i0;
.globl add t
.type add,@function
add: # @add wasm2c clang -O3
. functype add (i32, i32) -> (132)
# *bb.0: define i32 @add(ptr %0, i32 %1, i32 %2) {
local.get 1 %4 = add i32 %1, 15
coc 2 %5 = add 132 %4, %2
i32.const 15 } Hd
i32.add
end_function clang -c + IDA Pro
int add(void *a1, int a2, int a3) {
+
pif hat 37
ASIA 2025
```

## Slide 38

##### Wasm Code Lifting: wasm2c

u32 w2c_add(w2c* instance, …)

- _w2c_instance_ is passed to all functions

   - Keeps track of execution state between functions

- _w2c_env_instance_ can be freely used to keep track of important values

- ● Memory struct keeps the state of the current initialized memory ○ Will be initialized with table memory

- Function table is used for indirect function calls

- ● Globals will be dynamically generated

38

## Slide 39

##### Wasm Code Lifting: wasm2c

● _w2c_instance_ will be instantiated by helper functions ○ Initialized memory, globals and others

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: wasm2c
e w2c_instance will be instantiated by helper functions
o Initialized memory, globals and others
void wasm2c_instantiate(w2c* instance,
struct w2c_env* w2c_env_instance) {
assert(wasm_rt_is_initialized());
init_instance_import( instance, w2c_env_instance);
init_globals( instance);
init_tables( instance) ;
init_memories( instance);
init_elem_instances( instance);
init_data_instances(instance);
QQ
blackhat
ASIA 2025
39
```

## Slide 40

##### Wasm Code Lifting: Deobfuscation idea!

40

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: Deobfuscation idea!
prosaaecaen a
Ilvm | Pseudo C "
rot !
Wasm Level 1 i 1 IR Level clang -O3-c J 1
oH ro ' ¥|Native Object % C Source |,
Wi tot IDA Pro ! 1
DE f Ghidra H '
; 1 ty Binary Ninja. _.----.---+
Wasm Binary >] C Source tt clang -OG 4 LLVM IR
| tot clang -O3 -c CSCS
H ' target wasm
oot
1 + ! | Optimisations
! rot Runtime H
H SiMBA++ ! +p} Hl
KLEE 1 | 1 Helens td i
H SOUPER t H H
Leese e eesssS=ssee- ba eeeeeeescsesssccsesesessseseees See
pisex hat
ASIA 2025
```

## Slide 41

##### Wasm Code Lifting: Squanchy

- Tool to automate several deobfuscation steps

- Models and injects the runtime

   - Injects runtime helpers into Module/Function

- Inlines functions accordingly

- ● Optimizes the function/module

- Customized optimization pipeline to preserve Control Flow Graph

- ● Removes _wasm2c_ runtime

- Extracts functions and dependencies into new clean module

- ● https://github.com/pgarba/Squanchy

41

## Slide 42

##### Wasm Code Lifting: Squanchy - _Runtime Modeling_

42

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: Squanchy - Runtime Modeling
Runtime
Injection
Inlining
Optimisations
Brightening
bisek hat
ASIA 2025
Wasm function
(W2C *, i32, i32)
! || Lifted Wasm
H Code t
anew enecennnnee-----------
wasm2c Runtime wasm2c/squanchy
Initializer Helpers
| Init Imports Allocate i
j ' memory H
it Init Globals F : Allocate f
i H H FuncRef |}:
i . ; Allocate i
: Init Tables ExternRef if
i nit Elem/Data ; - Load/Stores i
| |Init Memories i ; TableBase i
42
```

## Slide 43

##### Wasm Code Lifting: Squanchy - Runtime Injection

43

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Optimisations
\
Brightening
pisex hat
ASIA 2025
Wasm function
(W2C *, i32, i32)
Allocate w2c
instance
Lifted Wasm
Code
w2c uses
wasm2c Runtime wasm2c/squanchy
Initializer Helpers
(Geran ] Meee]
| | Init Globals Alec :
| Init Tables : fleets f :
nit Elem/Datal Load/Stores |
| Init Memories TableBase
```

## Slide 44

##### Wasm Code Lifting: Squanchy - Runtime Injection

44

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Optimisations
\
Brightening
pisex hat
ASIA 2025
Wasm function
(W2C *, i32, 132)
Allocate w2c
instance
Call Runtime
Initializer
Lifted Wasm
Code
RSIS SS SSO 555)
Create call
wasm2c Runtime wasm2c/squanchy
Initializer Helpers
: | Init Imports |: ! jalesetic
1 | H memory '
: . i Allocate
Init Globals i FuncRef
i Fi i Allocate
Init Tables i | ExternRef
: [nit Elem/Datal || | ‘| Load/Stores | |
F Init Memories i TableBase
Unease sacceecceeeeenenn-----
44
```

## Slide 45

##### Wasm Code Lifting: Squanchy - Inlining

45

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: Squanchy - Inlining
wasm2c Runtime wasm2c/squanchy
Initializer Helpers
Runtime Wasm function
ime _| (W2C *, i32, i32)
v gocnsoonescccecereceeneneg qececsescessssezsssscceeees) 0 pe--ccceeeneeenneeeecee--9
Injection i | Allocate w2c
Init Imports it Allecate F
| instance ' i i
|
/ Init Globale i ft | Allocate
. i Call Runtime /:! F F FuncRe H
i Inlining f Initializer " Mark i H it F
la=saa=s- || Functions | |) Init Tables 7 eecer 4
H ‘| for inlining | i i xternRef i
| optimisations | HI E Tnit Elen/bate F Load/Stores
{ | | Lifted Wasm
| Code i i [Init Meneriee] : | TableBase |:
JRE
Brightening i f { H
blackhat 45
ASIA 2025
```

## Slide 46

##### Wasm Code Lifting: Squanchy - Inlining

46

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: Squanchy - Inlining
Wasm function wasm2c Runtime wasm2c/squanchy
Runtime (W2C *, i32, i32) Tnitializer Helpers
x Allocate w2c Allocate 7
Injection : |__instance} ; i oot memo i
Call Runtime i Allocate
—= = H Initializer i H i FuncRef ;
Inlining : | Init Imports | | Functions: an |WNPAllocaTe i
= J : i Recursively HE |_ExternRef :
i | Init Globals | *——___; i ot
Optimisations E | |i | Load/Stores
[Init Memories} * nt H
Brightening i = i nt
' | Lifted Wasm | } ' fou
blackhat Le eel \eeeeeeeeezeeezsszsszzssseed {neadeeeeeerecsecenccaeecd ts
ASIA 2025
```

## Slide 47

##### Wasm Code Lifting: Squanchy - Runtime Injection

47

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: Squanchy - Runtime Injection
Runtime
Vv
Injection
§| — Inlining 1
leasa=2el
| optimisations |
Brightening
pisex hat
ASIA 2025
i ExternRef
Wasm function
(W2C *, i32, i32)
Allocate w2c
instance
Init Imports
ee
Init Globals
Init Tables
Allocate
memory
Allocate
FuncRef
Allocate
Lifted Wasm
Code
Inline
Functions
i Recursively
‘¢—_—_____
wasm2c Runtime
Tnitializer
wasm2c/squanchy
Helpers
47
```

## Slide 48

##### Wasm Code Lifting: Squanchy - Optimisation

Apply LLVM O3 pipeline and <u>preserve</u> Control Flow Graph

- Obfuscation pipelines are written by humans

   - Control Flow Protection ■ Control Flow Flattening

   - Code Protection

      - Instruction Substitutions

   - Harden Protections

      - Opaque Predicates

      - Mixed Boolean Arithmetics

48

## Slide 49

##### Wasm Code Lifting: Squanchy - Optimizations

###### <u>Override LLVM Thresholds</u>

49

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: Squanchy - Optimizations
Runtime
i
Injection
Inlining
poor)
1 |) Optimisations |
==
!
Brightening
e
9
Py
7
ASIA 2025
Wasm function
(W2C *, i32, i32)
|
w2c instance
Tnitialisation
+
Lifted Wasm
Code
Gesssesscccssssseeene-----7
Override LLVM Thresholds
// DSE
-memdep-block-scan-Limit=1000000
-dse-memoryssa-walkLimit=1000000
-available-lLoad-scan-Limit=1000000
-dse-memoryssa-scanLimit=1000000
// Loop Unrolling
-unroll-threshold=1000000
-unroll-count=64
49
```

## Slide 50

##### Wasm Code Lifting: Squanchy - Brightening

50

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: Squanchy - Brightening
Wasm function
(W2C *, i32, i32)
Wasm function
(W2C *, i32, i32)
i
Injection
Replace w2c reference
" | w2c instance
Ss i
Inlining
Clean Leftover
Initialisation Code
Deobfuscated
Wasm Code
| thitialisati
Optimisations nitialisation
W +
Lifted Wasm
§j Brightening |! : :
black hat | cecenenecsctstenreseeeecd ba ceceseecennsssscraneneed 0
ASIA 2025
```

## Slide 51

##### Wasm Code Lifting: Squanchy - Recompilation

LLVM IR

ARM64

51

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Wasm Code Lifting: Squanchy - Recompilation
Runtime
se
Injection
Inlining
Optimisations
Brightening
bisek hat
ASIA 2025
Wasm function
(W2C *, i32, i32)
Deobfuscated
Wasm Code
Loe eee eee eee ssesssceeeet
LLVM IR
define 132 @add(ptr %0, i132 %1, 132 %2) {
%3 = add i32 %1, 1926
%4 = add i132 %3, %2
ret 132 %4
}
add
add
ret
ARM64
w2c_squanchy_add_0:
w8, wl, #1926
w0, w8, w2
51
```

## Slide 52

##### Deobfuscation

52

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deobfuscation
iatatalaianaiaia eeeceesssSSSseSseeeeeeweene IRE OSS 5
1 '
Lifting Deobfuscation |
Binary | Wasm2C Squanchy | LLVM IR Hie ??7 ra Clang >| Object File
! i:
eee ee a bee wee ------ a
blackhat
ASIA 2025
```

## Slide 53

##### Reminder: Original Input

53

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Reminder: Original Input
eee
1 #include <stdio.h>
int calc(unsigned int n) {
unsigned int mod =n % 4;
unsigned int result = 0;
else if (mod 1) result = (n & OxBAAADOBF) * (3 + n)
else if (mod == 2) result = (n * OxBAAADOBF) * (4 | n);
else result = (n + OxBAAADOBF) * (5 & n);| Of
return result;
20 int main(int argc, char *xargv) {
21 printf("Hello from WebAsm! %d\n", calc(arge + 23));
Q 22, return 0;
blackhat e
ASIA 2025
```

## Slide 54

##### Deobfuscation: LLVM Optimisations

54

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deobfuscation: LLVM Optimisations
if (iVarl == 0) {
local_10 = (paraml & OxbaaadObf | paraml * OxbaaadObf) *
(((paraml * Oxffffffff) & Oxbcec65b1 | paraml & 0x43139a4e) * Oxbcec65b3);
else if (iVarl == 1) {
local_10 = ((paraml * 0x45552f40) & paraml) * (paraml + 3); ia
else if (iVarl == 2) {
local_10 = ((paraml * Oxffffffff) & OxbaaadObf | paraml & 0x45552f40) * a
(paraml & 4 | paraml * 4);
t
else {
local_10 = (paraml + OxbaaadObf) * ((paraml * Oxffffffff | Oxfffffffa) * Oxffffffff);
pisex hat
ASIA 2025
if (iVar] == 0) {
local_24 = (param_2 | OxbaaadObf )
*
(param_2 * 2); a
else if (iVar] == 1) {
local_24 = (param_2 & OxbaaadObf )
*
(param_2 + |
F
local_24 = (param_2 ~ OxbaaadObf )
*
(param_2 | 4); [|
elseLf
local_24 = (param_2 + OxbaaadObf )
*
(param_2 & 5);
y
54
```

## Slide 55

##### Deobfuscation: LLVM Optimisations

55

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deobfuscation: LLVM Optimisations
01) else if (ivari == 2) {
102) [" uVari0 = (parami ~ Oxfffftftt) & paraml;
103] uVar11 = uvario ~ oxffffftfts Ba
104 uVar1@ = (param1 & @x28b159a6 | (paraml ~ Oxffffffff) & Oxd74ea659) ~
105 Unsigned Integer (compiler-specific size) | uVar1@ & Oxd74ea659) | (param1 | uVar11) ~ Oxffffffff;
106 Var Length: 4 & Oxad@2e611 | uVarl@ & Ox52fd19ee;
107 uVarle uVar1@ ~ @x52fd19ee) & @x2d4bd55a | (uVar1@ ~ @xad@2e611) & @xd2b42aa5;
108] uVar10 = (uVarl@ ~ ox2dabd55a) & uVari0; ‘Liv optimised)
109 uVar1l = (param & Ox43df8f | (paraml *~ Oxffffffff) & @xffbc2070) * Oxd2f7f52a |
110 (param1 | @x2d4bd55a) * Oxffffffff;
111)| uvar12 = uVarle ~ exffffffff | uVar11; 20| (IF Tivars = oy T @
122)| wvari0 = (uvarii ~ oxfffffttf) & (uVarie ~ oxfffffttt) | uvarte & uvari1; 21} wWar2 = (((param_2 | Oxbaaaddbf) & Oxc4fai585 | param_2 & 0x1052a40) * param_2 ~ 0x80aa1085) &
113)| uVari1 = wVar10 ~ oxffffffff; 22 (param_2 | @xbaaad@bf | param_2 * 0x45552f40);
114)| uVari0 = (uVar12 & Oxac3e94d1 | (uVar12 * Oxffffffff) & Ox53c16b2e) ~ 23} wari = war2 & (param_2 * Oxbaaaddbt) ;
115 (uVar11 & @xac3e94d1 | uVar1@ & 0x53c16b2e) | (uVar12 | uVar11) ~ Oxffffffft; 24) uvar2
uVar2 * param_2;
116 | uVari1 = uVar10 ~ 0x35ec8eeb; 25} uVar3
((param_2 & Oxfffffffd ~ Oxffffffff) & @x34f5a7e6 | param_2 & @xcb@a5819) ~
uno
117/| varie = wVar10 ~ oxfffftfft | ox35ec8eeb; 26 (param_2 & 2 | Oxdb2dect5);
118) | uVar12 = wVarli & 0x35ecBeeb * Oxf ff ff TTT; 27) ward = ((param_2 & Oxfffffffd * Oxtfffffff) & Ox48c117 | param_2 & Oxffb73ee8) *
119) | uvar10 = (uVar12 & Ox2dSbbaff | uVari1 & 0x10a40400) * ———— 28 (param_2 & 2 | @x48c115) | param_2 * Oxfffffffd;
120) (uVar1@ & Ox2dSbbaff | (uVar10 ~ Oxffffffff) & Oxd2a44500) | 29] ocal_24 = (uVar2 * uVarl ~ Oxbaaaddbf | (uVar2 ~ Oxbaaaddbf) & uVarl) *
121 (uVar12 | uVar10) * Oxffffffff; 30 (uVar3 * uVar4 * @x1027b4ee | (uVar3 ~ @x1027b4ee | uVar4) ~ Oxffffffff);
122 uVaril paraml “ Oxffffffff) & @x733e697e | paraml & Ox8cc19681; an fF
123)|  uvari1 = ((uVari1 * @x8cc19681) & Oxfffffffb | (uVarl1 ~ 0x733e697e) & 4) ~ Oxffffffft | 32( else if (ivars = 1) { a
124 Oxf ff fff tb; 33] local_24 = ((((param_2 | Oxbaaad®bf) & 0x3c966fda | param_2 & 0x41410000) ~ param_2 ~ 0x3882409a
125 uVar12 = (paraml *~ @x55a04b31) & (paraml *~ Oxffffffff); 34 ) & (param_2 | @xbaaad@bf | param_2 ~ @x45552f40)) * (param_2 + 3);
126 uVar4 (param1 * Oxffffffff | @x55a04b31) ~ Oxffffffff; oo
127 uVar12 Warl2 & uVar4 | uVari2 * uVar4; 36{ else if (ivarsS = 2) {
128)| uVari2 = (uVar12 * oxffffffff) & Oxf7e551b4 | uVar12 & Ox8laae4b; 37} wWar2 = (param_2 * Oxfffffffb | param_2 * 4) & (param_2 ~ Ox7eb64781);
129)| wVar4 = (uVar12 * OxSdbaeS7e) & Oxda9fbf90 | (uVar12 * 0xa2451a81) & 0x2560406f; 38} local_24 = (uVar2 & (param_2 & 4 | @x8149b87a) |
130)| uvar5 = (uVar11 * @x8149b87a) & uVar11; x (param_2 & 4 * Ox7eb64785) & (uVar2 * Oxfffffftt)) * (param 2 * Oxbaaaddbf);
131 uVar6 (uVar11 * @x8149b87a) & (uVar1l ~ Oxffffffff); 40}
132 uVar7 (uVar4 * @xa429f815) & (uVar4 * 0x2560406f) #] 41 plse {
133, | uVari2 = (uVar12 * Oxdcf35d04) & (uVar12 ~ 0xa2451a81); 42, [_locat_24 = (paran_2 + @xbaaaddbf) * (paran_2 & 5); |_| ‘Original Expression Recovered,
134] uVar8 = uVar5 * Oxffffffft; 43,
135 | uVar9 = uVar6 * Oxffffffft;
136 | uVar5 = (uVar8 & @xa7224c94 | uVar5 & Ox58ddb36b) ~ (uVar9 & Oxa7224c94 | uVar6 & Ox58ddb36b) |
137 (uVar8 | uVar9) * oxffffffff;
138} uVari2 = wVar7 & uVari2 | uVar7 * uVari2;
139} uVari2 = warl2 & (uVars * Oxffffffff) | uVarS & (uVar12 ~ Oxffffffft);
140] uVari1 = ((uVari1 * oxffffffff) & @x3c7da929 | uVar11 & @xc38256d6) *
141 ((uVar4 * Oxda9fbf90) & @x3c7da929 | (uVar4 ~ 0x2560406F) & Oxc38256d6) |
142 (uvarl1 * Oxffffffff | uVar4 ~ @xda9fbf90) ~ oxfffffftt;
143, | uVarli = (uVarll ~ Oxffffffff) & OxS1a3afbb | uVarl1 & Oxae5c5044;
144} uVar4 = uVarll * Ox51a3afbb;
145] uVar5 = uVarl2 * oxffffffft;
146, | local_10 = (((uVarlo ~ oxffffffff) & @xebfaad8@ | uVar10 & 0x1405527f) * @xb608d971) *
147 ((uVar5 & Oxf368b83d | uVar12 & @xc9747c2) ~
148 (uVar4 & 0xf368b83d | (uVari1 * Oxae5c5044) & Oxc9747c2) |
149 (uVar5 | uVar4) * Oxffffffff); 55
50| -F
```

## Slide 56

##### Deobfuscation: Progress…

56

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deobfuscation: Progress...
Hn UU DUD UE UE ERLE U TUE EEUU LGES === uF eee eee 1
a i)
Lifting i Deobfuscation |
tt
Obf. Wasm |_!. ~ im LLVM ' ; ;
Binary >| Wasm2C |— >| Squanchy LLVM IR iid Optimisations nw Clang Object File
ee Wee eaucceccesuessscceeosoos- }loeeeeannene!
blackhat 56
ASIA 2025
```

## Slide 57

##### Deobfuscation: LLVM Optimisation Shortcomings

- May only weaken some obfuscations

- Some techniques which LLVM cannot outright break

   - Control flow flattening*

   - Bogus control flow

   - Solving complex MBAs ■ Multiple iterations of substitution

   - . . .

57

## Slide 58

58

## Slide 59

##### Beyond LLVM: Solving MBAs

(x ⊕ y) + 2 × (x ∧ y) = x + y

- Mixed Boolean Arithmetic (MBA) expressions ○ Expressions mixing arithmetic operators (+,-,x) with boolean operators (¬, ⊕, ∧, ∨)

○ Difficult to analyze - no general rules for interaction b/w operators (no distributivity, no associativity etc.) ○ With complex MBAs, SMT solvers may not able to solve them.

- Pattern based solving of MBAs can be overcome by chaining the MBAs.

59

## Slide 60

##### Solving MBAs: Tooling

- Specialised tools for solving MBAs

○ <u>SiMBA</u> - For linear MBAs ○ <u>GAMBA</u> - Nonlinear MBA expression

- <u>SiMBA++</u> - For simplifying MBAs in LLVM IR ■ <u>https://github.com/pgarba/SiMBA-</u>

- SiMBA++

   - Detects candidate expressions in LLVM IR

   - ○ Performs simplification using SiMBA or GAMBA

■ Supports calling external simplifiers

○ Replaces expressions with simplifications in LLVM IR

60

## Slide 61

##### Deobfuscation: LLVM Opt + SiMBA + GAMBA

61

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deobfuscation: LLVM Opt + SIMBA + GAMBA
ef (en 06 _ ; Neu "LVM Optimised
aril © (tavern * estlooah) eonse2aHts | (onarid = oxoeeiSe) 6 6a361Se0a) > oxt1S7684 if (iVar5 == 0) {
winsa «lured = TET) & sate | garam &wasztann) = EHF | uVar2 = (((param_2 | OxbaaadObf) & Oxc4fa1585 | param_2 & 0x1052a40) ~ param_2 ~ 0x80aa1085) &
(param_2 | OxbaaadObf | param_2 * 0x45552f40);
5c873c) * uVarl1 = uVar2 & (param_2 * OxbaaadObf );
Warde arstecdebs) ~ xco7azien | 8x60atc; uVar2 = uVar2 * param_2;
LEED e eeateeen uVar3 = ((param_2 & Oxfffffffd * Oxffffffff) & Ox34f5a7e6 | param_2 & Oxcb0a5819) *
SBS6EL34 | Warll & 0%7799Secbs (param_2 & 2 | Oxdb2decf5);
ball (tara = erctevesca}/e eeivetenst —VT uVar4 = ((param_2 & Oxfffffffd * Oxffffffff) & Ox48c117 | param_2 & Oxffb73ee8) ~
EEO Scare (param_2 & 2 | 0x48c115) | param_2 ~ Oxfffffffd;
Arava seme eres c tea eremar tp evaeasleeetiea eeyiol eaten @eesezIn) local_24 = (uVar2 * uVarl1 * Oxbaaad@bf | (uVar2 * OxbaaadObf) & uVarl) *
open w Ble Ste pone (uVar3 * uVar4 * 0x1027b4ee | (uVar3 * 0x1027b4ee | uVar4) ~ Oxf fffffff);
13 }
if (uVar2 == 0) { ‘SIMBA
uVar2 = (param_2 & 0xa81b62f7 | 0x17000408) ~ param_2 & 0x57e49d08;
*xpiVarl = ((uVar2 * Oxadaad4b7) & (param_2 & OxbaaadObf ~ Oxffffffff) |
(uVar2 * 0x12000008) & param_2 & OxbaaadObf) *
(param_2 & Oxfffffffd * (param_2 & 2 | Ox4fa5c831) ~ 0x4fa5c833);
v
if (uVar2 == 0) { Gamba
rr
es een es ac iia ead xpiVarl = ((param_2 & 0x77b39989 | 0x88006252) ~ (param_2 * Oxed32f2d0) & (param_2 ~ 0x9a816b59)
) * (param_2 | OxbaaadObf);
(2) return;
Ip
blackhat ; i 61
ASIA 2025
WWar6 = (ware ~
lars = Wardle
Ware = (uVar
War? = (vars,
£114) & 0x4573038"5
return;
}
19) | (wvard | ward) * oxtrrerreny
8) *
```

## Slide 62

##### Deobfuscation: LLVM Opt + SiMBA + GAMBA

62

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deobfuscation: LLVM Opt + SIMBA + GAMBA
if (warl = 0) {
wari = ((parami * oxfffffftt) & ox19495cff | param & Oxe6d6a300) ~ OxScic73bf;
lomeoncoussa, Wari * paral * Oxfffftfff) & uVarl;
Sawre = aparaml * @x625558ec) & (param ~ Oxfffffttt);
wVar2 = (paraml * 0x625558ec) & paraml}
uVarS = wVar5 & wVar2 | uVar5 * uVar2;
uVarS = (uVarS * Oxffffffff) & OxdBff8853 | uVar5 & 0x270077ac;
uVar2
uVar3
(param & Oxlbad26fa | (paranl * OxfffTTTTT) & Oxed5fd905) ~ oxB60a81e9;
(param * OxfffffFfF) & @x625558ec | paraml ~ @x9daaa713;
wVar3 = (uVar3 * Oxffffffff) & 0x741226bb | uVar3 & OxBbedd944;
wVar2 = (uVar2 * paraml) & wVar2 * Oxfffftttf;
wVar2 = (uVar2 * ((uVar3 * 0x741226bb) & 0x6590700b | (uVar3 ~ OxBbedd944) & OxSa6tBtt4) ~
0x6590700b) & uVar2;
wVar2 = (uVar2 * Oxffffffff) & @xiebasd23 | uVar2 & Oxel45a2dc;
wVarl = (uVar2 * @xlebasd23 | 0x625558ee) * oxfffff fff;
wVarl = (((uVar2 * @xteba5d23) & Ox60b6dt70 | (uVar2 ~ Oxe145a2dc) & Ox9f49208F) ~ 0x2€3879e) &
0x625558ee;
(((uVard * OxfFFFFFFF) & Ox7c83e458 | uVarl & Ox837clba7) * Ox7c83e458 |
((uVar5 * Oxffffffff) & 0x721da317 | uVarS & Ox8de25ce8) ~ 0x721da317) *
(ward & uVarl | uVari * uVar);
local_c =
¥
else if (wari = 1) {
uVarl = (((paraml * Oxffffffff) & OxSfb8011c | param] & Oxa047fee3) ~ OxSfbBO11c | OxBde25ce8) &
(param * @x721da317) & param1 * Oxffffffff);
Warl & Ox8de25ce8 | (uVarl * Oxffffffft) & @x721da317;
((uvarl * Oxfffffftt) & @x53584bcb | uVarl & Oxaca7b434) ~ ax53584bcb | 0x45552140;
Warl * oxffffffft;
= ((uVar5 * Wart) & wars) * -(-3 - param);
uVart
uVar1
uVarS
Vocal
E
else if (wari
uVar1
uVarl = ((uVarl & @x68b867d3 | (uVarl * Oxffffffff) & 0x9747982c) * 0x924@bb4b) & Oxbaaadebf;
uVar5 = ((paraml * Oxffffffff) & 0x368db37e | paraml & @xc9724c81) * Ox8c2763c1;
uVar5 = (uVar5 * paraml * Oxffffffff) & uVars;
uVar2 = (param * Oxffffffff) & Oxfffffffb | paraml & 4;
uVar2 = (uVar2 * oxfffffffb) & uVar2;
uVar3 = (param1 | @xb4a77@ab) & (paraml * Oxffffffff | Ox4bseefs4);
uVar3 = uVar3 & Oxicda0Bec | (uVar3 * Oxffffffff) & Oxe3b5f713;
uVard = (uVar2 * Oxffffffff | uVar3 * @xa8ed7843) ~ oxtfffffft;
uVard
locals
(war2 * oxffffffft) & (uVar3 * 0x571287bc) | uVar2 & (uVar3 * OxaBed7843);
= ((uVarl * Oxfffffftt | wars * Oxffffffff) &
(((uVarl * Oxffffffff) & uVarS | uVarl & (uVarS * Oxffffffft)) * oxfffftttt) *
Oxffffffff) * (ward & wari | uVar4 * uVarl);
else { a
uVarl = ((paraml * Oxffffffff) & 0x769a091f ~ @x769a091f) &
((parami * Oxffffffff) & paraml * Oxfffffftt);
uVar5 = (uVarl * @x8bedd944) & uVarl;
uVarl = (uVari | 0x741226bb) * oxfffftttt;
uVarl = wVar5 & uVarl | uVar5 * uVarl;
Vocal_c = ~(-0x374a3fe6 - (-0x374a3fe6 - (0x45552f41 - paraml))) *
((((uVarl * Oxffffffff) & @x52a311c3 | uVarl & @xadScee3c) ~ 0x26b1377d) & 5:
+
return local_cy
ASIA 2U2Z5
a a
(paraml | Oxfafedc98) & ((param1 * 0x5072367) & paraml * Oxfffffttt);
10
11
12
13
14
| 15
16
17
18
19
20
21
uVar1
param_2 & 3;
1iVar3 =
(param_2 * @xbaaad@bT) * (param_2 | 4);
if_(uVari '= 2) {
iVar3 = (param_2 + Oxbaaad@bf) * (param_2 & 5);
£
iVar2 = (param_2 + 2) * (param_2 | OxbaaadObf);
1t (Vari t= a) +
iVar2 = (param_2 & Oxbaaad@bd) * (param_2 + 3);
}
if (uVarl < 2) {
iVar3 = iVar2;
}
return iVar3;
Cy
```

## Slide 63

##### Deobfuscation: Progress…

63

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deobfuscation: Progress...
; ypc e meses accccssssccceeeess 4
Lifting H Deobfuscation H
i
Bina +4 Wasm2Cc >| Squanchy LLVM IR aa optimisations = SiMBA++ Clang D| Object File
Looe eee eee eee Sloe enone eee 4
pisex hat
ASIA 2025
63
```

## Slide 64

##### SOUPER: Supercharging Deobfuscation

- Souper - a synthesis-based superoptimizer for a domain specific intermediate representation (IR) that resembles a purely functional, control-flow-free subset of LLVM IR

- ● Can run as an LLVM optimization pass

- Synthesise optimisations

   - Counterexample guided inductive synthesis (CEGIS)

■ Multiple RHS generated, cheapest among them is chosen.

   - Dataflow

- Can resolve opaque predicates

- **Good results with control flow obfuscation**

64

## Slide 65

##### Deobfuscation: SOUPER

65

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deobfuscation: SOUPER
if_(uVar2 == @) {
if ((((uRam@@01@ae8 | uRam@@01@aec) * Ox3c2e5570) & Ox97Ff2bd7) + @x64293ba9 < @xe@465c21) {
bVar1 = true;
}
‘ “Opaque Predicate.
else {
bVar1 = false;
}
while( true ) {
while (bVar1) {
bVar1 = false;
}
if (Ox5fd76e94 < ((iRam0001@af@ + iRam@0010af4 ~* Ox410@5e8aU) + Ox63d028ff) * Ox65edfa51)
break;
bVar1 = true;
}
if ((iRam@0010af8 * iRam@@@1@afc + Oxd9ef92c7U | Oxbale4315) + Oxce83d3a0 < Ox8bb488b1) {
do {
} while (((uRam@0010c30 * uURam@0010c34) + Ox6f44ee27 & Ox7ca@3c77) * OxSed@b58a == -0x29120a04
3
+
lio {
local_c = (param1 | @xbaaad@bf) * (param1 * 2); ]
} while (((uRam@0010b00 / uRamd0010b04 | Oxbabf5164) * -Ox32ee4c95 & Ox67c7c119) < @x20a96022);
do {
} while ((uRam0@0010b10 / uRam@0010b14 + @xc8de4516) / @x936b17aa == @xa9fOadac);
AOIA CULO
65
```

## Slide 66

##### Deobfuscation: SOUPER

66

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deobfuscation: SOUPER
10
11
12
13
14
15
16
17
18
19
20
21
22
uVarl = param.2 & 3;
iVar3 = (param_2 *~ @xbaaad@bf) * (param_2 | 4); 4
if (wWarl '=2)T __
| 1Var3 = (param_2 & 5) * (param_2 + Oxbaaadobt);] (ay
[ivar2 = (param 2 | Oxbaaadobt) * (param 2 ~ 2); |p
if_(uVari != @) ¢
iVar2 = (param_2 & @xbaaadO@bf) * (param_2 + 3); &
}
if (uVari < 2) {
iVar3 = iVar2;
}
return iVar3;
66
```

## Slide 67

67

## Slide 68

Deobfuscation: Progress…

68

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deobfuscation: Progress...
pocessssssccssssssssscsssssssseeeeeen-- i etetetetetatetetetetetetet ttt eee tte 1
‘ Lifting i Deobfuscation '
Binary rn Wasm2C Squanchy —D| LLVMIR iti Optimisations >| SiIMBA++ a SOUPER ha Clang ad Object File
t
uw
pif hat 68
ASIA 2025
```

## Slide 69

###### Deobfuscation: Hikari (Sub=1, bogus=1, split=1)

###### **Long complex obfuscated code**

6969

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Deobfuscation: Hikari (Sub=1, bogus=1, split=1)
Long complex
obfuscated code
uVar1 = param_2 & 3;
f (uVar1 < 2) {
iVar2 = (param_2 | @xbaaad@bf) * (param_2 + 2); je
if (uVari != 0) {
iVar2 = (param_2 + 3) * (param 2 & @xbaaadobf) |i
}
return iVar2;
}
if (uVar1 == 3) {
return (param_2 & 5) * (param_2 + OxbaaadQbf); a
return (param_2 & @xbaaad@b8 ~*~ @xbaaad@b9) * (param_2 & @xbaaad@bf) +
(param_2 & @x45552f44 ~ 4) * (param_2 | OxbaaadQbf);
89
```

## Slide 70

# Real World Application

70

## Slide 71

##### WebAssembly Malwares

- Steady increase in usage of Wasm for cryptomining in browsers

   - Compared to JS, Wasm is fast in performing hashing operations

   - Monero is the most used cryptocurrency for cryptomining.

71

## Slide 72

##### Malware Diversification: _wasm-mutate_

- <u>Carbera-Arteaga et. al.</u> demonstrate use of _wasm-mutate_ to evade detection

- _wasm-mutate_ transforms binary into a variant binary program that preserves the original functionality.

- 3 kind of transformations

○ <u>Peephole</u> ■ ~135 rewrite rules. ○ <u>Module structure transformation</u> ■ Add new type, new function, new export etc.

- <u>Control flow graph</u>

   - Loop unrolling, swap conditional branches.

- _wasm-mutate_ output needs to <u>verified with</u> _wasm-validate_ ○ Some transformation <u>break</u> the WASM file

72

## Slide 73

##### DEMO!!

73

## Slide 74

Use Case: wasm-mutate

- wasm-mutate

   - 3000 (real) iterations are applied

   - _<u>100%</u>_ of mutations are removed

   - Code is normalized and matches 100% the original code! ■ <u>Our approach fully recovers the function (and</u> optimizes it!)

74

## Slide 75

##### Use Case: Deobfuscating Malwares

- CryptoNight, CryptoNight Obfuscated

   - Deobfuscated functions by Squanchy match non-obfuscated functions

   - <u>https://www.crowdstrike.com/en-us/blog/ecriminals-increas ingly-use-webassembly-to-hide-malware/</u>

   - <u>https://arxiv.org/abs/2403.15197</u>

75

## Slide 76

##### Use Case: hCaptcha

- hCaptcha uses obfuscated Wasm

- ● Small and medium size obfuscated functions can be simplified in <1-2min.

Unflattens control flow, simplifies and inlines functions.

76

## Slide 77

77

## Slide 78

##### Conclusion

- Wasm obfuscation

   - LLVM IR based tools - O-LLVM, Polaris

- Squanchy: Lifting Wasm to LLVM IR ○ Wasm2c  + Squanchy works great.

- Deobfuscation using LLVM

   - LLVM + SiMBA + GAMBA + SOUPER + …

78

## Slide 79

##### Conclusion

- Real World Application

   - Malware Normalisation

■ Wasm-mutate output can be simplified ■ Cryptonight malware simplified ○ Deobfuscating hCaptcha binary

- Tooling

   - Existing tooling can be reused

- <u>Obfuscation - Polaris, O-LLVM,</u> ~~Wasmixer~~

- <u>Deobfuscation - LLVM, SiMBA++, SOUPER</u>

- Symbolic Execution - KLEE, ~~Manticore, SeeWasm~~

79

## Slide 80

##### Thank You!!

- Slides + Whitepaper - https://github.com/su-vikas/Presentations

- _Squanchy_ - <u>https://github.com/pgarba/Squanchy</u>

80
