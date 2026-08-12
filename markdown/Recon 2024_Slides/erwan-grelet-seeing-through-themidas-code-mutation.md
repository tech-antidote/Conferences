---
title: "Seeing Through Themida's Code Mutation"
speakers: ["Erwan Grelet"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Erwan Grelet_Seeing Through Themida's Code Mutation .pdf"
pages: 61
sha256: "155007984f1027cd2f35f67b2aa404790d254cbcb6815474e2afa08592e0ea53"
text_chars: 15186
ocr_pages: 12
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:29:11Z"
---
# Seeing Through Themida's Code Mutation

**Speakers:** Erwan Grelet  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Erwan Grelet_Seeing Through Themida's Code Mutation .pdf` (61 pages)

## Slide 1

# **Seeing Through Themida’s Code Mutation**

Erwan Grelet June 29th, 2024

REcon 2024

1

## Slide 2

## **About Me**

Security researcher at Ubisoft Interests:

Contacts

   - @ergrelet

   - @ergrelet@mastodon.social

- Reverse Engineering

- Vulnerability Research

- Software Development

- Software Obfuscation

- 0Disclaimer: this is the result of a personal research project and is not linked to my employer.

REcon 2024

2

## Slide 3

## **Themida**

- Commercial **software protector**

- Developed by Oreans Technologies<sup>1</sup>

- **Binary-to-binary** workflow

- Supports **x86 and .NET Windows executables** (EXEs and DLLs)

- 1https://www.oreans.com/

REcon 2024

3

## Slide 4

## **SecureEngine**

- Code protection engine used by Themida

- Shared with other Oreans products<sup>2</sup>

- Contains the code mutation engine

- 2Code Virtualizer and WinLicense

REcon 2024

4

## Slide 5

## **Mutation-based Code Obfuscation**

In commercial protectors code mutation generally means:

- **No** interpreter or **virtual machine** (VM) involved

REcon 2024

5

## Slide 6

## **Mutation-based Code Obfuscation**

In commercial protectors code mutation generally means:

- **No** interpreter or **virtual machine** (VM) involved

- **Light obfuscation** of the code

REcon 2024

5

## Slide 7

## **Mutation-based Code Obfuscation**

In commercial protectors code mutation generally means:

- **No** interpreter or **virtual machine** (VM) involved

- **Light obfuscation** of the code

- Adds and **modifies machine code** , preserves original behavior

REcon 2024

5

## Slide 8

## **Mutation-based Code Obfuscation**

In commercial protectors code mutation generally means:

- **No** interpreter or **virtual machine** (VM) involved

- **Light obfuscation** of the code

- Adds and **modifies machine code** , preserves original behavior

- Can modify the **control flow graph**

REcon 2024

5

## Slide 9

## **Initial Motivation**

### The goal

- Develop a deobfuscator for the mutation engine

REcon 2024

6

## Slide 10

## **Initial Plan of Action**

### The plan

- Fully understand the features of Themida’s mutation engine

- Find potential weaknesses we can leverage to deobfuscate the code

REcon 2024

7

## Slide 11

## **Obtaining Themida**

Research done on the demo version of Themida (v3.1.1)

- Available on Oreans’s web site<sup>3</sup>

- Contains the same mutation engine as the paid version

- We can use the demo as a black box to infer features and behaviors

- 3https://www.oreans.com/download.php

REcon 2024

8

## Slide 12

## **What Mutation Looks Like**

**Figure 1:** Original CFG ( **6** basic blocks)

**Figure 2:** CFG after mutation ( **74** basic blocks)

REcon 2024

9

## Slide 13

## **What Mutation Looks Like**

**Figure 3:** Original code ( **71** instructions)

**Figure 4:** Code after mutation ( **2160** instructions)

REcon 2024

10

## Slide 14

## **Initial Approach**

REcon 2024

11

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Initial Approach
Compare |
Mutated machine
code
Machine code —_> Themida
REcon 2024 11
```

## Slide 15

**uops.info**

### _uops.info_<sup>_a_</sup> to the rescue!

- Provides descriptions of all(?) x86 instructions

   - Contained in a single XML “database”

- Provides a script to generate assembly code

- _a_ https://uops.info/xml.html

**Figure 5:** Assembly file generated from uops.info’s database

REcon 2024

12

## Slide 16

**Input Generation**

**Figure 6:** Input generation pipeline

REcon 2024

13

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Input Generation
a
uops.info XML Python Script Assembly File Es En
Figure 6: Input generation pipeline
REcon 2024 13
```

## Slide 17

**Difficulties**

Ended up testing the _SecureEngine_ ’s instruction handling logic as well:

**Figure 7:** Crash while protecting a function with Themida

**Figure 8:** Stack corruption viewed in WinDbg

(Haven’t tried to root cause these)

REcon 2024

14

## Slide 18

**Difficulties**

**Figure 9:** Infinite loop while protecting a function with Themida

REcon 2024

15

## Slide 19

## **Features**

_SecureEngine_ ’s code mutation engine features:

- Opaque function/code entry

- Junk code insertion

- Instruction substitution

   - Constant unfolding

   - Register-to-stack spilling

REcon 2024

16

## Slide 20

## **Opaque Code Entry**

- Original code is **redirected to a trampoline**

- Trampoline is used to hinder static analysis

   - Equivalent to obfuscated `push ADDR; ret`

   - Redirects to the actual obfuscated code

REcon 2024

17

## Slide 21

## **Opaque Code Entry**

**Figure 10:** Entry of a protected function

REcon 2024

18

## Slide 22

**Opaque Code Entry**

**Figure 11:** CFG of trampolines generated by Themida to wrap code

REcon 2024

19

## Slide 23

**Opaque Code Entry**

**Figure 12:** Part of the CFG which computes the obfuscated code’s address

REcon 2024

20

## Slide 24

## **Junk Code Insertion**

- Junk code insertion is triggered randomly, for **75% of all instructions**

- Junk code can be **inserted before** original instructions **or after or both**

- Junk code **cancels itself** out **within a single basic block**

REcon 2024

21

## Slide 25

## **Junk Code Insertion**

Example of MOV instruction with junk code inserted around:
1 push eax
2 add ax  , 42
3 shl eax  , 12
4 mov ebx  , ecx ; O r i g i n a l i n s t r u c t i o n
5 pop eax

REcon 2024

22

## Slide 26

**Instruction Substitution**

The _SecureEngine_ ’s code mutation engine can substitute the **14** following x86 instruction classes<sup>4</sup> :

**AND** , **DEC** , **INC** , **JMP** , **MOV** , **MOVZX** , **NEG** , **NOT** , **OR** , **POP** , **PUSH** , **SUB** , **XCHG** , **XOR**

The instruction substitution pass is **always** applied to supported instructions.

> 4In XED, an instruction class is “what is typically thought of as the instruction mnemonic.”

REcon 2024

23

## Slide 27

**Instruction Substitution**

Example of `XCHG` instruction substitution:

**Figure 13:** Original instruction

**Figure 14:** Mutated instruction

REcon 2024

24

## Slide 28

## **Constant Unfolding**

Example of constant unfolding on `MOV` :

**Figure 15:** Original instruction

**Figure 16:** Mutated instruction

REcon 2024

25

## Slide 29

## **FLAGS Register**

To preserve FLAGS register, the engine disables code mutation locally when needed:

**Figure 17:** “Mutated” intructions when FLAGS are used

REcon 2024

26

## Slide 30

## **Broken Instructions**

Interestingly, some instructions can be **randomly** transformed into broken machine code. Example of a broken `FCMOVNB` instruction:

**Figure 18:** Original instruction

**Figure 19:** “Mutated” instruction

REcon 2024

27

## Slide 31

## **Broken Semantics**

But also, semantics can be broken sometimes:

**Figure 20:** Original instruction ( `NOP` )

**Figure 21:** Mutated instruction ( `MOV DH, 0` )

REcon 2024

28

## Slide 32

## **Weaknesses**

The obfuscation is annoying enough, but there are some weaknesses:

- **Each basic block** is created from **one original instruction**

- **Each basic block** is **mutated independently**

- The original function’s **CFG is preserved**

This means we can **deobfuscate each basic block individually** to recover original instructions.

REcon 2024

29

## Slide 33

## **Simplifying The Code**

To simplify the code, a couple of ideas came to mind too, but both involve an IR:

- Code Optimization

- Program Synthesis

REcon 2024

30

## Slide 34

## **Simplifying The Code**

To simplify the code, a couple of ideas came to mind too, but both involve an IR:

- Code Optimization

- Program Synthesis

   - Symbolic Execution

REcon 2024

30

## Slide 35

**The Big Picture**

**Figure 22:** Deobfuscation process, the big picture

REcon 2024

31

## Slide 36

**The Big Picture**

**Figure 23:** Deobfuscation process, the big picture

REcon 2024

31

## Slide 37

## **Defeating Trampolines**

To defeat opaque code entry, we can **symbolically execute trampolines**

- Trampolines contains 2 conditional branches

- Trampoline **logic is always the same**

REcon 2024

32

## Slide 38

## **Defeating Trampolines**

**Figure 24:** Symbolic Execution Path

REcon 2024

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Defeating Trampolines
<- Start symbolic execution
REcon 2024 Figure 24: Symbolic Execution Path 33
```

## Slide 39

## **Defeating Trampolines**

**Figure 25:** Symbolic Execution Path

REcon 2024

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Defeating Trampolines
<- Redirect execution to
the right branch
REcon 2024 Figure 25: Symbolic Execution Path 33
```

## Slide 40

## **Defeating Trampolines**

**Figure 26:** Symbolic Execution Path

REcon 2024

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Defeating Trampolines
<- Redirect execution to
the left branch
REcon 2024 Figure 26: Symbolic Execution Path 33
```

## Slide 41

## **Defeating Trampolines**

**Figure 27:** Symbolic Execution Path

REcon 2024

33

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Defeating Trampolines
<- Extract mutated code's start address
REcon 2024 Figure 27: Symbolic Execution Path 33
```

## Slide 42

**Instruction Synthesis**

We can differentiate 3 cases for the instruction synthesis process.

REcon 2024

34

## Slide 43

**Instruction Synthesis (case #1)**

**Figure 28:** Case #1 ( **no junk code** , no substitution)

REcon 2024

35

## Slide 44

**Instruction Synthesis (case #2)**

**Figure 29:** Case #2 ( **junk code inserted** , no substitution)

REcon 2024

36

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Instruction Synthesis (case #2)
14007ed67 add rdx, 8x8
14807ed6b add rdx, 8x8
14007ed72 xor rdx, qword [rsp]
14007ed76 xor qword [rsp], rdx
140@7ed7a xor rdx, qword [rsp]
14007ed7e pop rsp
14007ed7Ff movups xmmword [rdi+@x20], xmm@
14007ed83 push Ox7fFF59c1
14007ed88 mov qword [rsp], r1@
14007ed8c push rsp
14007ed8d pop r1e
14007ed8f add r10, @x8
14007ed93 sub r1@, 8x8
14007ed9a xchg qword [rsp], r1@
Figure 29: Case #2 (junk code inserted, no substitution)
REcon 2024
```

## Slide 45

**Instruction Synthesis (case #2)**

**Figure 30:** Basic block’s symbolic execution

**Figure 31:** MOVUPS instruction’s symbolic execution

REcon 2024

37

## Slide 46

**Instruction Synthesis (case #2)**

**Figure 32:** Basic block’s symbolic execution (FLAGS removed)

**Figure 33:** MOVUPS instruction’s symbolic execution

REcon 2024

37

## Slide 47

**Instruction Synthesis (case #2)**

**Figure 34:** Basic block’s symbolic execution (FLAGS removed)

**Figure 35:** MOVUPS instruction’s symbolic execution

REcon 2024

37

## Slide 48

**Instruction Synthesis (case #3)**

For instructions which the mutation **engine can substitute** :

- We only have to manually synthesize **14 instruction classes**

- Development effort is thus **symmetric between attack and defense**

- We can use **pattern matching**

REcon 2024

38

## Slide 49

**Instruction Synthesis (case #3)**

**Figure 36:** Basic block’s symbolic execution

REcon 2024

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Instruction Synthesis (case #3)
Exprid : Ex ‘==', ExpriId('RSP', 64), ExprInt(@x®, 64)),
Exprid( ‘af g prSlice(ExprOp('*', ExprId('RSP', 64), ExprOp('+'
Exprid('pf' 3 . y', ExprOp('&', ExprId('RSP', 64), Exp
Exprid : ExprSlice "&', ExprOp('*', ExprId('RSP', 64
ExpriId( ‘R13 : ExpriId “5
ExprId(‘n 1): ExprSlice(ExprId('R! » 64), 63, 64),
Exprid F : ExprSlice(ExprOp('*', ExprId('RSP', 64), ExprOp(‘&'
Exprid *, 64): ExprInt(@x12e, 64)
Figure 36: Basic block's symbolic execution
REcon 2024 38
```

## Slide 50

**Instruction Synthesis (case #3)**

**Figure 37:** Basic block’s symbolic execution (FLAGS removed)

REcon 2024

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Instruction Synthesis (case #3)
>» LApI Luu oag, oF
RSF, Ge), Cap opy
Figure 37: Basic block’s symbolic execution (FLAGS removed)
REcon 2024 38
```

## Slide 51

**Instruction Synthesis (case #3)**

**Figure 38:** Instruction “synthesized” via pattern matching

REcon 2024

38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Instruction Synthesis (case #3)
Exprid( ‘R13
Figure 38: Instruction “synthesized” via pattern matching
REcon 2024 38
```

## Slide 52

## **Result**

**Figure 39:** Simplified binaries can be run

REcon 2024

39

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Result
$ ./sha256_test_protected.exe
SHA-256 tests: SUCCEEDED
$ themida-unmutate ./sha256_test_protected.exe -a ©x1400011d0 0x140001000 0x140001200 0x140001270
-o sha256_test_simplified.exe
INFO - Resolving mutated's functions' addresses...
INFO Function at 0x1400011d0 jumps to 0x14031f24a
INFO Function at 0x140001000 jumps to 0x140028532
INFO Function at 0x140001200 jumps to 0x140211875
INFO Function at 0x140001270 jumps to 0x1400760b7
INFO Deobfuscating mutated functions...
INFO - Simplifying function at @x14031f2Ua...
INFO - Simplifying function at 0x140028532...
INFO - Simplifying function at @x140211875
INFO - Simplifying function at @x1400760b7...
INFO - Rebuilding binary file..
INFO Done! You can find your deobfuscated binary at 'sha256_test_simplified.exe'
$ ./sha256_test_simplified.exe
SHA-256 tests: SUCCEEDED
$|
Figure 39: Simplified binaries can be run
REcon 2024
```

## Slide 53

## **Result**

**Figure 40:** Original ( **6** BBs) **Figure 41:** Obfuscated **Figure 42:** Deobfuscated ( **74** BBs) ( **7** BBs) REcon 2024

40

## Slide 54

## **Result**

**Figure 43:** Original (71 instructions)

**Figure 44:** Deobfuscated (74 instructions)

REcon 2024

41

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
Result
1400011b 57 push 15 {__saved_r15}
400011b2 4156 push 14 {__saved_r14}
1490011b4 4155 push 13. {__saved_r13}
400011b6 push 12. {__saved_r12}
1b8 push —rsi_{__saved_rsi}
11b9 push di. {__saved_rdi}
40001 1ba push —rbp {__saved_rbp}
1400011bb push —rbx {
49001 1bc sub rsp, x48
4000 xor eax, eax {0x0}
1400011¢2 f6c test dl, ox
149001105 @f85cceeeee0 jne @x14000129
|
40011cb 48c1eaa4 shr rdx, x4
400011cf 801000000 mov eax, Ox!
Figure 43: Original (71
REcon 2024
instructions)
e94bec6601 jmp data
14067000
140670000 push 15 {__saved_r15}
148678002 push 14 {__saved_ri4}
149670004 push 13 {__saved_r13}
148678006 push 12 {__saved_r12}
140670008 push si {__saved_rsi}
149678009 push di {__saved_rdi}
149670008 push bp {__saved_rbp}
14967000b push bx {__saved_rbx}
14967000 add rsp, oxfffffrrrftttftos
140678010 xor eax, eax {8x8}
140670012 test dl, oxt
149678016 of 85deeee000 jne _@x1406700F2
—_—_——
14067881¢ 48c1¢a04 shr rdx, @x4 |
149670028 b8e1800000 mov eax. @x
Figure 44: Deobfuscated (74 instructions)
41
```

## Slide 55

## **Recap**

To recap:

- A few **weaknesses** facilitated the work

REcon 2024

42

## Slide 56

## **Recap**

To recap:

- A few **weaknesses** facilitated the work

- Static **symbolic execution** was very **effective**

REcon 2024

42

## Slide 57

## **Recap**

To recap:

- A few **weaknesses** facilitated the work

- Static **symbolic execution** was very **effective**

- The attack **scales and works seemlessly on complex functions**

   - Time complexity is roughly linear to the number of basic blocks

   - It can be parallelized

REcon 2024

42

## Slide 58

## **Recap**

To recap:

- A few **weaknesses** facilitated the work

- Static **symbolic execution** was very **effective**

- The attack **scales and works seemlessly on complex functions**

   - Time complexity is roughly linear to the number of basic blocks

   - It can be parallelized

- We’re able to recover very **close-to-original machine code**

REcon 2024

42

## Slide 59

## **Recap**

To recap:

- A few **weaknesses** facilitated the work

- Static **symbolic execution** was very **effective**

- The attack **scales and works seemlessly on complex functions**

   - Time complexity is roughly linear to the number of basic blocks

   - It can be parallelized

- We’re able to recover very **close-to-original machine code**

- **Binaries can be patched** to run on the deobfuscated code

REcon 2024

42

## Slide 60

## **Recap**

To recap:

- A few **weaknesses** facilitated the work

- Static **symbolic execution** was very **effective**

- The attack **scales and works seemlessly on complex functions**

   - Time complexity is roughly linear to the number of basic blocks

   - It can be parallelized

- We’re able to recover very **close-to-original machine code**

- **Binaries can be patched** to run on the deobfuscated code

- A blog series will be published soon with more details, stay tuned!

REcon 2024

42

## Slide 61

**Questions?**

Code is available here (GPL-3.0): https://github.com/ergrelet/themida-unmutate

**Figure 45:** QR Code for the link above

REcon 2024

43
