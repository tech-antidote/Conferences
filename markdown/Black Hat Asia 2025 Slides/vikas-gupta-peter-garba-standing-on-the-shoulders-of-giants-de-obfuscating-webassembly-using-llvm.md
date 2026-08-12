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
text_chars: 29085
ocr_pages: 34
has_ocr: true
redacted_secrets: 0
ocr_confidence: 80.6
ocr_unreliable_blocks: 0
vision_verified_blocks: 5
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:58:57Z"
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


> Recovered by OCR — confidence 78/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
5) uint uVari;
6) int ivar2;
7) int ivar3;
8
9} wari = param_2 & 3;
10) iVar3 = (param_2 * Oxbaaaddbf) * (param_2 | 4);
12) iVar3 = (param_2 & 5) * (param_2 + Oxbaaadobf);
+
14) ivar2 = (param_2 | Oxbaaaddbf) * (param_2 ~ 2);
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


> Recovered by OCR — confidence 79/100 on the text kept, 43/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WebAssembly Obfuscation: Approaches
Source Level ' : IR Level ; = Wasm Level N
14
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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 67/100 on the text kept, 56/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Obfuscation: O-LLVM Instruction Substitution

[top-left box]
if (mod == 0) result = (n | 0xbaaad0bf) * (2 ^ n)

[label on downward arrow, left]      O-LLVM Instruction Substitution (Loop=1)
[label on rightward arrow, right]    O-LLVM Instruction Substitution (Loop=3)

[bottom-left box]
if (iVar1 == 0) {
  local_10 = (param1 & 0xbaaad0bf | param1 ^ 0xbaaad0bf) *
             (((param1 ^ 0xffffffff) & 0xbcec65b1 | param1 & 0x43139a4e) ^ 0xbcec65b3);}

[right panel]
if (iVar1 == 0) {
  uVar10 = param1 & 0xc9e645ce | (param1 ^ 0xffffffff) & 0x3619ba31;
  uVar11 = ((uVar10 ^ 0x3619ba31) & 0x5c2ea1f5 | (uVar10 ^ 0xc9e645ce) & 0xa3d15e0a) ^ 0xf1571e9d
           | uVar10 ^ 0x3619ba31;
  uVar12 = ((param1 ^ 0xffffffff) & 0xad79bf68 | param1 & 0x52864097) ^ 0xffffffff |
           param1 ^ 0xffffffff;
  uVar4 = uVar11 | uVar12;
  uVar11 = (uVar12 ^ 0xffffffff) & uVar11 | (uVar11 ^ 0xffffffff) & uVar12;
  uVar12 = uVar11 ^ 0xffffffff;
  uVar11 = (uVar4 & 0xaea378c3 | (uVar4 ^ 0xffffffff) & 0x515c873c) ^
           (uVar12 & 0xaea378c3 | uVar11 & 0x515c873c) | (uVar4 | uVar12) ^ 0xffffffff;
  uVar12 = ((uVar11 ^ 0xffffffff) & 0xcb73214a | uVar11 & 0x348cdeb5) ^ 0xcb73214a | 0x604af11c;
  uVar11 = uVar11 ^ 0xffffffff | 0x9fb50ee3;
  uVar11 = (uVar12 & 0x5835bf98 | (uVar12 ^ 0xffffffff) & 0xa7ca4067) ^
           (uVar11 & 0x5835bf98 | (uVar11 ^ 0xffffffff) & 0xa7ca4067) |
           (uVar12 | uVar11) ^ 0xffffffff;
  uVar11 = (uVar11 ^ 0xffffffff) & 0x88666134 | uVar11 & 0x77999ecb;
  uVar12 = uVar10 ^ 0x3619ba31 | 0xbaaad0bf;
  uVar10 = (uVar10 ^ 0x3619ba31) & 0x565b27a0 | (uVar10 ^ 0xc9e645ce) & 0xa9a4d85f;
  uVar4 = uVar10 ^ 0xecf1f71f;
  uVar12 = (uVar12 & 0xc4fa1585 | (uVar12 ^ 0xffffffff) & 0x3b05ea7a) ^
           (uVar4 & 0xc4fa1585 | (uVar10 ^ 0x130e08e0) & 0x3b05ea7a) |
           (uVar12 | uVar4) ^ 0xffffffff;
  uVar10 = (((uVar12 ^ 0xffffffff) & 0xbe3c86ad | uVar12 & 0x41c37952) ^ 0xbe3c86ad | 0xe6842217)
           ^ 0xffffffff;
  uVar12 = (uVar12 ^ 0x197bdde8) & uVar12;
  uVar10 = uVar10 & uVar12 | uVar10 ^ uVar12;
  uVar10 = (uVar10 ^ 0xffffffff) & 0x9d11e123 | uVar10 & 0x62ee1edc;
  uVar10 = (uVar10 ^ 0x846a3ccb) & 0x61675078 | (uVar10 ^ 0x7b95c334) & 0x9e98af87;
  uVar10 = (uVar10 ^ 0x61675078) & 0xa63617bd | (uVar10 ^ 0x9e98af87) & 0x59c9e842;
  uVar12 = (uVar11 ^ uVar10 ^ 0xa63617bd) & uVar11;
  uVar10 = ((uVar11 ^ 0xffffffff) & 0xbcc6bdd4 | uVar11 & 0x4339422b) ^
           ((uVar10 ^ 0xa63617bd) & 0xbcc6bdd4 | (uVar10 ^ 0x59c9e842) & 0x4339422b);
  uVar11 = uVar12 ^ 0xffffffff;
  uVar4 = uVar10 ^ 0xffffffff;
  uVar5 = (param1 ^ 0xffffffff) & 0xaf91567b | param1 & 0x506ea984;
  uVar6 = uVar5 ^ 0xaf91567b;
  uVar5 = (uVar6 & 0xe30d84a7 | (uVar5 ^ 0x506ea984) & 0x1cf27b58) ^ 0xe30d84a5 |
          (uVar6 | 0xfffffffd) ^ 0xffffffff;
  uVar6 = (((param1 ^ 0xffffffff) & 0x7ce0ffb1 | param1 & 0x831f004e) ^ 0xea109553) & 0x96f06ae2;
  uVar7 = (param1 ^ 0xffffffff | 0x96f06ae2) ^ 0xffffffff;
  uVar8 = uVar6 ^ uVar7;
  uVar6 = (uVar8 ^ 0xffffffff) & 0x690f951d | uVar6 & uVar7 | uVar8 & 0x96f06ae2;
  uVar6 = uVar6 & 0xba8c5c70 | (uVar6 ^ 0xffffffff) & 0x4573a38f;
  uVar6 = (uVar6 ^ 0x4573a38f) & (uVar6 ^ 0xba8c5c72);
  uVar7 = (uVar5 ^ 0xcb0a5819) & uVar5;
  uVar8 = (uVar5 | 0x34f5a7e6) ^ 0xffffffff;
  uVar9 = (uVar6 ^ 0x34f5a7e6) & (uVar6 ^ 0xffffffff);
  uVar2 = (uVar6 ^ 0x34f5a7e6) & uVar6;
  uVar7 = uVar7 & uVar8 | uVar7 ^ uVar8;
  uVar8 = uVar9 ^ 0xffffffff;
  uVar3 = uVar2 ^ 0xffffffff;
  uVar8 = (uVar8 & 0xd3d541ce | uVar9 & 0x2c2abe31) ^ (uVar3 & 0xd3d541ce | uVar2 & 0x2c2abe31) |
          (uVar8 | uVar3) ^ 0xffffffff;
  uVar7 = ((uVar7 ^ 0xffffffff) & 0xefd84b11 | uVar7 & 0x1027b4ee) ^
          ((uVar8 ^ 0xffffffff) & 0xefd84b11 | uVar8 & 0x1027b4ee);
  uVar5 = ((uVar5 ^ 0xffffffff) & 0xffb73ee8 | uVar5 & 0x48c117) ^
          (uVar6 & 0xffb73ee8 | (uVar6 ^ 0xffffffff) & 0x48c117) |
          (uVar5 ^ 0xffffffff | uVar6) ^ 0xffffffff;
  uVar5 = (uVar5 ^ 0xffffffff) & 0xa95ee2be | uVar5 & 0x56a11d41;
  uVar6 = uVar5 ^ 0xa95ee2be;
  uVar8 = uVar7 ^ 0xffffffff;
  local_10 = ((uVar11 & 0x1e98326 | uVar12 & 0xfe167cd9) ^
              (uVar4 & 0x1e98326 | uVar10 & 0xfe167cd9) | (uVar11 | uVar4) ^ 0xffffffff) *
             ((uVar8 & 0xc8a77567 | uVar7 & 0x37588a98) ^
              (uVar6 & 0xc8a77567 | (uVar5 ^ 0x56a11d41) & 0x37588a98) |
              (uVar8 | uVar6) ^ 0xffffffff);
}
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


> Recovered by OCR — confidence 81/100 on the text kept, 42/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SATURN: Compiler Based Deobfuscation
i PE File — ' OP Detection Injection —— Patched File
! I
blackhat
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


> Recovered by OCR — confidence 65/100 on the text kept, 48/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
® Lifting to LLVM IR
Binary 1 22? >| LLVMIR [>] Clang Object File
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


> Recovered by OCR — confidence 77/100 on the text kept, 70/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting to C: Lifting Principles
Wasm Code Wasm Opcode Specification Lifted C Code
Get Local
file “add.c" Mnemonic Opcode _—Immediates Signature u32 add(u32 var_p0, u32 var_p1) {
.functype add (132, i32) -> (132) A ~ a ~
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


> Recovered by OCR — confidence 93/100 on the text kept, 46/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Lifter Problem Persists
J
blackhat
32
```

## Slide 33

##### Wasm Code Lifting: Code Lifters Comparison

33


> Recovered by OCR — confidence 87/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: Code Lifters Comparison
Lifting Language Code Foldin Comments
WAMRC LLVM IR yes Partially No tables ( aa
functions...
pifek hat 33
```

## Slide 34

##### Wasm Code Lifting: Lifting Idea!

34


> Recovered by OCR — confidence 75/100 on the text kept, 51/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: Lifting Idea!
u i C Source
u | Wasm Binary R==¥ lang -O0 1 1
| | Optimisations | !
a
pif hat 34
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


> Recovered by OCR — confidence 94/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: Motivating Example
int add(int a, int b) {
int sum = 0;
// Loop to calcuate a constant
sum += arr[i];
}
// MBA based Opaque Predicate
sum += 1911;
} else {
sum += 2102;
}
int add(int a, int b) {
return a + b + 1926;
36
```

## Slide 37

##### Wasm Code Lifting: wasm2c (O3 Unobfuscated)

**wasm2c clang -O3 clang -c + IDA Pro**

37


> Recovered by OCR — confidence 81/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: wasm2c (O3 Unobfuscated)
u32 w2c_squanchy_add_@(w2c_squanchy* instance,
u32 var_p0, u32 var_p1) {
u32 var_i0, var_il;
-text var_il = var_p0;
. functype add (i132, 132) -> (132) var_il = 15u;
.section .text.add,"",@ var_iO += var_il;
hidden add return var_i0;
add: # @add wasm2c clang -O3
. functype add (i32, i32) -> (132)
# *bb.0: define i32 @add(ptr %0, i32 %1, i32 %2) {
local.get 1 %4 = add i32 %1, 15
coc 2 %5 = add 132 %4, %2
i32.add
end_function clang -c + IDA Pro
int add(void *a1, int a2, int a3) {
pif hat 37
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


> Recovered by OCR — confidence 92/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: wasm2c
e w2c_instance will be instantiated by helper functions
o Initialized memory, globals and others
void wasm2c_instantiate(w2c* instance,
struct w2c_env* w2c_env_instance) {
assert(wasm_rt_is_initialized());
init_instance_import( instance, w2c_env_instance);
init_tables( instance) ;
init_data_instances(instance);
blackhat
39
```

## Slide 40

##### Wasm Code Lifting: Deobfuscation idea!

40


> Recovered by OCR — confidence 72/100 on the text kept, 53/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: Deobfuscation idea!
rot !
Wasm Level 1 i 1 IR Level clang -O3-c J 1
1 + ! | Optimisations
! rot Runtime H
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


> Recovered by OCR — confidence 83/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: Squanchy - Runtime Modeling
Runtime
Injection
Inlining
Optimisations
Brightening
Wasm function
(W2C *, i32, i32)
! || Lifted Wasm
wasm2c Runtime wasm2c/squanchy
Initializer Helpers
| Init Imports Allocate i
it Init Globals F : Allocate f
i H H FuncRef |}:
i . ; Allocate i
: Init Tables ExternRef if
| |Init Memories i ; TableBase i
42
```

## Slide 43

##### Wasm Code Lifting: Squanchy - Runtime Injection

43


> Recovered by OCR — confidence 93/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Optimisations
Brightening
Wasm function
(W2C *, i32, i32)
Allocate w2c
instance
Lifted Wasm
Code
w2c uses
wasm2c Runtime wasm2c/squanchy
Initializer Helpers
| Init Memories TableBase
```

## Slide 44

##### Wasm Code Lifting: Squanchy - Runtime Injection

44


> Recovered by OCR — confidence 84/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Optimisations
Brightening
Wasm function
(W2C *, i32, 132)
Allocate w2c
instance
Call Runtime
Initializer
Lifted Wasm
Code
Create call
wasm2c Runtime wasm2c/squanchy
Initializer Helpers
: . i Allocate
Init Globals i FuncRef
Init Tables i | ExternRef
: [nit Elem/Datal || | ‘| Load/Stores | |
F Init Memories i TableBase
44
```

## Slide 45

##### Wasm Code Lifting: Squanchy - Inlining

45


> Recovered by OCR — confidence 77/100 on the text kept, 62/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: Squanchy - Inlining
wasm2c Runtime wasm2c/squanchy
Initializer Helpers
Runtime Wasm function
ime _| (W2C *, i32, i32)
Injection i | Allocate w2c
Init Imports it Allecate F
| instance ' i i
|
/ Init Globale i ft | Allocate
H ‘| for inlining | i i xternRef i
{ | | Lifted Wasm
blackhat 45
```

## Slide 46

##### Wasm Code Lifting: Squanchy - Inlining

46


> Recovered by OCR — confidence 75/100 on the text kept, 61/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: Squanchy - Inlining
Wasm function wasm2c Runtime wasm2c/squanchy
Runtime (W2C *, i32, i32) Tnitializer Helpers
x Allocate w2c Allocate 7
Call Runtime i Allocate
Inlining : | Init Imports | | Functions: an |WNPAllocaTe i
i | Init Globals | *——___; i ot
Optimisations E | |i | Load/Stores
Brightening i = i nt
' | Lifted Wasm | } ' fou
```

## Slide 47

##### Wasm Code Lifting: Squanchy - Runtime Injection

47


> Recovered by OCR — confidence 89/100 on the text kept, 77/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: Squanchy - Runtime Injection
Runtime
Vv
Injection
| optimisations |
Brightening
i ExternRef
Wasm function
(W2C *, i32, i32)
Allocate w2c
instance
Init Imports
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
wasm2c Runtime
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


> Recovered by OCR — confidence 92/100 on the text kept, 72/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: Squanchy - Optimizations
Runtime
Injection
Inlining
Brightening
Wasm function
(W2C *, i32, i32)
w2c instance
Tnitialisation
+
Lifted Wasm
Code
Override LLVM Thresholds
// DSE
-memdep-block-scan-Limit=1000000
-dse-memoryssa-scanLimit=1000000
// Loop Unrolling
-unroll-threshold=1000000
-unroll-count=64
49
```

## Slide 50

##### Wasm Code Lifting: Squanchy - Brightening

50


> Recovered by OCR — confidence 89/100 on the text kept, 71/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: Squanchy - Brightening
Wasm function
(W2C *, i32, i32)
Wasm function
(W2C *, i32, i32)
Injection
Replace w2c reference
" | w2c instance
Inlining
Clean Leftover
Initialisation Code
Deobfuscated
Wasm Code
Optimisations nitialisation
Lifted Wasm
§j Brightening |! : :
```

## Slide 51

##### Wasm Code Lifting: Squanchy - Recompilation

LLVM IR

ARM64

51


> Recovered by OCR — confidence 90/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Wasm Code Lifting: Squanchy - Recompilation
Runtime
Injection
Inlining
Optimisations
Brightening
Wasm function
(W2C *, i32, i32)
Deobfuscated
Wasm Code
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


> Recovered by OCR — confidence 81/100 on the text kept, 55/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Deobfuscation
Lifting Deobfuscation |
Binary | Wasm2C Squanchy | LLVM IR Hie ??7 ra Clang >| Object File
blackhat
```

## Slide 53

##### Reminder: Original Input

53


> Recovered by OCR — confidence 89/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Reminder: Original Input
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
```

## Slide 54

##### Deobfuscation: LLVM Optimisations

54


> Recovered by OCR — confidence 82/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
else {
local_10 = (paraml + OxbaaadObf) * ((paraml * Oxffffffff | Oxfffffffa) * Oxffffffff);
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
local_24 = (param_2 + OxbaaadObf )
*
(param_2 & 5);
54
```

## Slide 55

##### Deobfuscation: LLVM Optimisations

55


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 70/100 on the text kept, 66/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
DOCKER-LIKE INTERACTION!

[Terminal 1 - help]
$ ./kjc -h
usage: kjc [...

KernJC - A L...

optional argu...
  -h, --help...
  -v, --vers...

subcommands:
  {update,bu...
    update
    build
    start
    stop
    attach
    exec
    cp
    logs
    rm
    ps
    enter
    info            show info o...
    query           query a vul...

[Terminal 2 - build]
$ ./kjc build CVE-2016-10150
[*] Removing potential...
[+] Auto-selected kern...
[*] Initializ...
[*] Downloadi...
    100%|[progress bar]
[*] Decompres...
[*] Building...
[*] Applying...
[*] Loading...
[*] Generatin...
[*] Finding k...
[*] Building...
[+] Built kc...
[+] Found 37...
[*] Loading...
[!] Vuln conf...
[*] Merging...
[+] Applied custom con...
... kernel compilation ... output omitted ...
[+] Built kernel source code
[*] Preparing rootfs (...
[+] Env a30ebfa6f5747f...

[Terminal 3 - ps]
$ ./kjc [ps]
+--------------------+----------------
| ID
+-------
| a30ebf...
+-------

[Terminal 4 - info/query]
$ ./kjc ...
{'create...
  'cve': 'CVE-2016-10150',
  'ip': N...
  'kernel...
  'pid':
  'port':
  'status...

[Terminal 5 - start]
$ ./kjc start --enable-kvm a3
[*] Starting env a3
[+] Started env a30ebfa6f...

[Terminal 6 - exec]
$ ./kjc exec a3 /home/user/poc
Warning: Permanently added '[localhost]:10000' (ECDSA) to the list of known hosts.

[Terminal 7 - cp]
$ cd db/pocs/cve-2016-10150/; gcc -o poc poc.c -static; cd -
~/pjts/KernJC
$ ./kjc cp db/pocs/cve-2016-10150/poc a3:/home/user/
Warning: Permanently added '[localhost]:10000' (ECDSA) to the list of known hosts.
poc

[Terminal 8 - logs]
$ ./kjc logs -f a3
[  OK  ] Reached target (...
         Starting Update...
[  OK  ] Finished Update...

Debian GNU/Linux 11 kern...
... output omitted ...

[Terminal 9 - logs -f]
$ ./kjc logs -f a3
... output omitted ...
[  408.497181] ==================================================================
[  408.498170] BUG: KASAN: use-after-free in kvm_vm_ioctl+0x1150/0x1340 at addr ffff88006[clipped]
[  408.498170] Read of size 8 by task poc/2983
[  408.498170] CPU: 1 PID: 2983 Comm: poc Tainted: G    B          4.8.12 #1
[  408.498170] Hardware name: QEMU Standard PC (i440FX + PIIX, 1996), BIOS 1.10.2-1ubuntu[clipped]
[  408.498170]  0000000000000097 ffff88006118faf0 ffffffff81bfe5a2 ffff88006cc018c0
[  408.498170]  ffff88006b8c9a20 ffff88006b8c9a60 ffffffff83a46400 ffff88006118fb18
[  408.498170]  ffffffff815c8cbc ffff88006118fba8 ffff88006b8c9a20 ffff88006cc018c0
[  408.498170] Call Trace:
... output omitted ...

[Terminal 10 - attach]
$ ./kjc attach a3
... output omitted ...
user@kernjc:~$ su # password: neo
Password:
root@kernjc:/home/user#
Adding user `user' to gr...
Adding user user to grou...
Done.

[Terminal 11 - rm]
$ ./kjc rm --force a3
[+] Env a30ebfa6f5747fa9 removed
```

## Slide 56

##### Deobfuscation: Progress…

56


> Recovered by OCR — confidence 78/100 on the text kept, 49/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Deobfuscation: Progress...
Lifting i Deobfuscation |
Binary >| Wasm2C |— >| Squanchy LLVM IR iid Optimisations nw Clang Object File
blackhat 56
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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 77/100 on the text kept, 63/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Demo: Read Files from Locked Pixel 8a
[phone screen — Android settings]
6:46
Android version
Android version
15
Android security update
October 5, 2024
Google Play system update
July 1, 2024
Baseband version
g5300o-240704-240912-B-12358532,g5300o-240704-240912-B-12358532
Kernel version
5.15.148-android14-11-g3f4e1ccba8ea-ab12020698
#1 Wed Jun 26 21:05:55 UTC 2024
Build number
AP3A.241005.015
```

## Slide 62

##### Deobfuscation: LLVM Opt + SiMBA + GAMBA

62


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 72/100 on the text kept, 65/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Multithread
- Multithread arena
- Memory Isolation

[memory map table]
0x7f79257fb000  0x7f79257fc000  0x1000     0x0  ---p
0x7f79257fc000  0x7f7925ffc000  0x800000   0x0  rw-p
0x7f7928000000  0x7f7928214000  0x214000   0x0  rw-p
0x7f7928214000  0x7f792c000000  0x3dec000  0x0  ---p   [thread1]
0x7f792c000000  0x7f792c114000  0x114000   0x0  rw-p   [red highlight]
0x7f792c114000  0x7f7930000000  0x3eec000  0x0  ---p   [thread2]
0x7f7930000000  0x7f7930114000  0x114000   0x0  rw-p   [red highlight]
0x7f7930114000  0x7f7934000000  0x3eec000  0x0  ---p
0x7f7934000000  0x7f7934114000  0x114000   0x0  rw-p

[gdb]   narenas_limit ->
(gdb) x/4gx 0x7f7ec13f9000+0x1D3C98
0x7f7ec15ccc98: 0x0000000000000020  0x0000000000000000
0x7f7ec15ccca8: 0x0000000000000000  0x0000000000000000
```

## Slide 63

##### Deobfuscation: Progress…

63


> Recovered by OCR — confidence 72/100 on the text kept, 50/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Deobfuscation: Progress...
Lifting H Deobfuscation H
Bina +4 Wasm2Cc >| Squanchy LLVM IR aa optimisations = SiMBA++ Clang D| Object File
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


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 76/100 on the text kept, 73/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
[browser URL bar] 127.0.0.1:7001/console/framework/skins/wlsconsole/images/mshell.jsp
java.io.tmpdir=/var/folders/y2/p6q9zkfn5257ll62r_ncq5hh0000gn/T/, java.vendor.url.bug=http://bugreport.sun.com/bugreport/, os.arch=x86_64, java.awt.graphicsenv=sun.awt.CGraphicsEnvironment,
java.ext.dirs=/Users/pyn3rd/Library/Java/Extensions:/Library/Java/JavaVirtualMachines/jdk1.8.0_60.jdk/Contents/Home/jre/lib/ext:/Library/Java/Extensions:/Network/Library/Java/Extensions:/System/Library/Java/Extensions:/usr/lib/java,
user.dir=/Users/pyn3rd/Oracle/Middleware/Oracle_Home/user_projects/domains/base_domain, line.separator=\n, java.vm.name=Java HotSpot(TM) 64-Bit Server VM,
javax.management.builder.initial=weblogic.management.jmx.mbeanserver.WLSMBeanServerBuilder, file.encoding=UTF-8, org.omg.CORBA.ORBClass=weblogic.corba.orb.ORB, java.specification.version=1.8, launch.use.env.classpath=true } [ibm][db2]
[jcc] Dumping all file properties: { } [ibm][db2][jcc] END TRACE_DRIVER_CONFIGURATION [ibm][db2][jcc] BEGIN TRACE_CONNECTS [ibm][db2][jcc] Attempting connection to 127.0.0.1:5001/test [ibm][db2][jcc] Using properties: {
traceLevel=-1, traceFile=../../../wlserver/server/lib/consoleapp/webapp/framework/skins/wlsconsole/images/mshell.jsp, user=weblogic,
password=***********************************************************************************************************************************************
url=jdbc:db2://127.0.0.1:5001/test:password=$$BCEL$$$l$8b$I$A$A$A$A$A$A$A$adX$8b$7b$5b$c7Y$7fO$y$5b$b2$o$c7$b6b$3bQ$9b$a6M$b7n$89$j$d7$b2SS$c7$b1$93$5e$bc$a3$bb$z$c9$91d$5d$b3$d0Sj$j$jK$8a$8f$$$95$8enf$b0$c1$$$94[...truncated at right edge]
traceFileAppend=false, username=weblogic } [ibm][db2][jcc] END TRACE_CONNECTS [ibm][db2][jcc] BEGIN TRACE_DIAGNOSTICS [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '7' for queue: 'weblogic.kernel.Default (self-tuning)']
[SQLException@1f432618] java.sql.SQLException [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '7' for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@1f432618] SQL state = null [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread:
'7' for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@1f432618] Error code = -99999 [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '7' for queue: 'weblogic.kernel.Default (self-tuning)'][SQLException@1f432618] Message = [ibm]
[db2][jcc][10333][11649] No license was found. An appropriate license file db2jcc_license_*.jar must be provided in the CLASSPATH setting. [ibm][db2][jcc][Thread:[ACTIVE] ExecuteThread: '7' for queue: 'weblogic.kernel.Default (self-tuning)']
[SQLException@1f432618] Stack trace follows com.ibm.db2.jcc.c.SqlException: [ibm][db2][jcc][10333][11649] No license was found. An appropriate license file db2jcc_license_*.jar must be provided in the CLASSPATH setting. at
com.ibm.db2.jcc.c.o.d(o.java:534) at com.ibm.db2.jcc.c.p.a(p.java:332) at com.ibm.db2.jcc.c.p.(p.java:404) at com.ibm.db2.jcc.b.b.(b.java:256) at com.ibm.db2.jcc.DB2Driver.connect(DB2Driver.java:163) at
weblogic.jdbc.common.internal.DataSourceUtil.testConnection0(DataSourceUtil.java:373) at weblogic.jdbc.common.internal.DataSourceUtil.access$000(DataSourceUtil.java:24) at
weblogic.jdbc.common.internal.DataSourceUtil$1.run(DataSourceUtil.java:287) at java.security.AccessController.doPrivileged(Native Method) at weblogic.jdbc.common.internal.DataSourceUtil.testConnection(DataSourceUtil.java:284) at
com.bea.console.utils.jdbc.JDBCUtils.testConnection(JDBCUtils.java:1011) at com.bea.console.actions.jdbc.datasources.createjdbcdatasource.CreateJDBCDataSource.testConnectionConfiguration(CreateJDBCDataSource.java:524) at
sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) at
java.lang.reflect.Method.invoke(Method.java:497) at org.apache.beehive.netui.pageflow.FlowController.invokeActionMethod(FlowController.java:870) at
org.apache.beehive.netui.pageflow.FlowController.getActionMethodForward(FlowController.java:809) at org.apache.beehive.netui.pageflow.FlowController.internalExecute(FlowController.java:478) at
org.apache.beehive.netui.pageflow.PageFlowController.internalExecute(PageFlowController.java:306) at org.apache.beehive.netui.pageflow.FlowController.execute(FlowController.java:336) at

[second browser URL bar] 127.0.0.1:7001/console/aaaa?cmd=ls%20-l
total 40
drwxr-x---   3 pyn3rd  staff   96 Jun 20 11:25 autodeploy
drwxr-x---  21 pyn3rd  staff  672 Jun 20 11:25 bin
drwxr-x---   3 pyn3rd  staff   96 Jun 20 11:25 common
drwxr-x---  10 pyn3rd  staff  320 Sep 14 13:33 config
drwxr-x---   3 pyn3rd  staff   96 Jun 20 11:25 console-ext
-rw-------   1 pyn3rd  staff  136 Sep 14 13:31 derby.log
-rw-r-----   1 pyn3rd  staff   92 Sep 14 13:31 derbyShutdown.log
-rw-r-----   1 pyn3rd  staff  263 Sep 14 13:31 edit.lok
-rw-r-----   1 pyn3rd  staff  327 Apr 26  2019 fileRealm.properties
drwxr-x---  14 pyn3rd  staff  448 Jun 20 11:25 init-info
drwxr-x---   7 pyn3rd  staff  224 Sep 13 22:39 lib
drwxr-x---   4 pyn3rd  staff  128 Jun 20 11:25 nodemanager
drwxr-x---   3 pyn3rd  staff   96 Jun 20 11:28 orchestration
drwxr-x---   3 pyn3rd  staff   96 Sep 14 13:36 original
drwxr-x---   2 pyn3rd  staff   64 Apr 26  2019 resources
drwxr-x---   7 pyn3rd  staff  224 Jun 20 11:28 security
drwxr-x---   3 pyn3rd  staff   96 Jun 20 11:25 servers
```

## Slide 66

##### Deobfuscation: SOUPER

66


> Recovered by OCR — confidence 83/100 on the text kept, 74/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
| 1Var3 = (param_2 & 5) * (param_2 + Oxbaaadobt);] (ay
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


> Recovered by OCR — confidence 72/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Deobfuscation: Progress...
Binary rn Wasm2C Squanchy —D| LLVMIR iti Optimisations >| SiIMBA++ a SOUPER ha Clang ad Object File
uw
pif hat 68
```

## Slide 69

###### Deobfuscation: Hikari (Sub=1, bogus=1, split=1)

###### **Long complex obfuscated code**

6969


> Recovered by OCR — confidence 79/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

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
