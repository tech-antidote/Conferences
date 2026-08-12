---
title: "Control Flow Intergrity on IBM i"
speakers: ["Bálint Varga-Perke"]
conference: "REcon"
conference_full: "REcon 2024"
edition: ""
year: 2024
source_pdf: "Recon 2024_Slides/Bálint Varga-Perke_Control Flow Intergrity on IBM i.pdf"
pages: 76
sha256: "99f761f5696ba47ca6f3eaa4fbd6b968b88dc8e1284ec2be2b5dc2e61d6b2968"
text_chars: 25835
ocr_pages: 9
has_ocr: true
redacted_secrets: 0
ocr_confidence: 79.9
ocr_unreliable_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 6
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:09:30Z"
---
# Control Flow Intergrity on IBM i

**Speakers:** Bálint Varga-Perke  
**Conference:** REcon 2024  
**Source:** `Recon 2024_Slides/Bálint Varga-Perke_Control Flow Intergrity on IBM i.pdf` (76 pages)


## Slide 1

## **`CONTROL FLOW INTEGRITY ON IBM I`**

\```
REcon 2024
\```

1

## Slide 2

### **`WHOAMI`**

\```
Bálint Varga-Perke (@buherator)
Silent Signal co-founder
IBM i focused research (2022.)
Senior Security Expert
\```

2

## Slide 3

### **`PRIOR WORK`**

\```
Architecture
Leif Svalgaard
Hugo Landau
Hacking
Shalom Carmel - Hacking iSeries
Matthew Carpenter blogposts
Bart Kulach - Hacking the Legacy
Not many others?
\```

3

## Slide 4

# **`IBM I`**

4

## Slide 5

# **`IBM I`**

\```
Midrange: more than a microcomputer, less than a
mainframe
Vertically integrated platform (think iPhone)
POWER CPU (think PowerPC)
2021: POWER 10
Object-Oriented OS (think ???)
Unix subsystem (PASE) is out of scope now
\```

5

## Slide 6

### **`OOP OS`**

##### `Usual OS`

##### `IBM i`

- `Files, processes, databases, ...`

- `File system and Memory`

- `Serialization for persistence`

- `Everything is an object`

- `Single-Level Store (Disk+Memory)`

- `Transparent caching/persistence, object encapsulation`

6

## Slide 7

### **`SINGLE-LEVEL STORE`**

\```
Disk+Memory -> single 64-bit address space
[40 bit segment ID] || [24 bit offset]
Object encapsulation hides caching/persistence
System-wide address space!
Separated program segments on SL50
\```

7

## Slide 8

### **`OOP OS - *PGM EXAMPLE`**

\```
No loading phase
Except for stack/heap
Stored thing === Executed thing
Edited data === Stored data
No such thing as .read() on a Program Object
It's a program not a file
Not a continuous byte stream!
\```

8

## Slide 9

### **`MACHINE INTERFACE (MI)`**

\```
Backwards compatibility is a major selling point
Object-oriented bytecode
Midrange SW runs "without modification" across
different architectures
\```

9

## Slide 10

# **`SECURITY`**

10

## Slide 11

### **`THE MYTH, THE LEGEND`**

\```
"The Only Operating System That has Never been infected by
Virus, Trojan, Worm, or Malware." - LinkedIn
"The IBM i itself can’t be contaminated by viruses created for
computers, but its files are considered excellent 'carriers'"
- Fortra
\```

\```
"The architecture of the IBM i system makes it highly unlikely
that a virus could be written to attack it" - IBM
\```

\```
External interfaces (e.g. IFS) and configuration are
known ITW targets!
\```

11

## Slide 12

### **`PZ TAKES A LOOK`**

\```
CVE-2023-30990: Pre-Auth RCE (pcrappyfuzzerftw)
Several LPE's
Core components (vs. external interfaces)
Logical bugs, analogous to Wintel systems
See our TROOPERS'24 talk and blog
\```

12

## Slide 13

## **`MEMORY CORRUPTION?`**

13

## Slide 14

### **`SPATIAL SAFETY`**

\```
intmain(){
char buf[4];
int num;
scanf("%x %s", &num, buf);
// Out-of-bounds read in both directions
for (int i=-2; i < 8; i++){
printf(" %02x ", buf[i]);
    }
printf("\n%x\n", num);
return 0;
}
\```

14

## Slide 15

### **`SPATIAL SAFETY`**

15


> Recovered by OCR — confidence 87/100 on the text kept, 76/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
40
Press
SPATIAL SAFETY
to end term nal
00 13
15
```

## Slide 16

### **`EXPLOITATION?`**

\```
OOB access -> privilege escalation
SLS -> Single address space
Even "artificial" corruptions work!
Below Security Level 50
Memory corruptions do occur ItW
Search for MCH3601, MCH0601
\```

16

## Slide 17

# **`REVERSE`**

17

## Slide 18

### **`MI VS NATIVE`**

\```
Every language is first compiled to an intermediate
representation
OPM -> U-Code -> MI
ILE -> W-Code-> (N)MI
Think JVM/.NET bytecode
MI code is embedded in *PGM's
\```

\```
The translator generates native code from MI
MI is independent from HW, so you can "recompile"
to new architectures
\```

18

## Slide 19

### **`STATIC ANALYSIS`**

\```
Program objects are not bitstreams!
Programs still need to be transferred to other
systems etc.
\```

\```
Save Files (*SAVF): ~Universal object serialization
format
\```

\```
*PGM -> *FILE -> SCP/FTP
\```

19

## Slide 20

\```
SAVE FILES (*SAVF)
Undocumented format
Free, closed-source reader: jSAVF
\```

20

## Slide 21

### **`SERIALIZED *PGM`**

\```
SAVF's can contain multiple objects
PGM: Undocumented format
Let's write a parser...
\```

21

## Slide 22

\```
DYNAMIC ANALYSIS
System Service Tools (SST)
Low-level debugging features for admins
R/W memory dump
No breakpoints, tracing, etc.
Partially masked register state
"scanf() debugging"
\```

22

## Slide 23

### **`BASE STRUCTURE`**

23


> Recovered by OCR — confidence 73/100 on the text kept, 54/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
BASE STRUCTURE
Hex editor
Display For
DI SPLAY/ ALTER/ DUMP
Wi PROGRAM SUBTYPE:
PROGRAM ATTRS S31lILlGOOGOO81LlOOB OG 4
516 TBL PTR LES7FOHEB0A1 ooS05 6
```

## Slide 24

\```
KAITAI <3 GHIDRA
Kaitai Struct allows declarative, multi-language
parser creation
Debug in Python/JS/... REPL
Hexeditor integration (Hobbit, VSCode)
Reusable Java code for Ghidra
Adding XCOFF support to Ghidra with Kaitai Struct
\```

24

## Slide 25

- `1` **`public class GhidraPGM400Loader extends AbstractProgramWrapperLoader`** `{`

- `2 @Override`

- `3` **`protected void load`** `(ByteProvider provider /*...*/ ){`

- `4` **`ByteBufferKaitaiStream`** `stream =`

- `5` **`new ByteBufferKaitaiStream`** `(provider.readBytes(0, provider.length()))`

- `6 // Instantiate strcture with Kaitai`

- `7` **`Savf`** `kaitai =` **`new Savf`** `(stream);`

- `8 // Object-oriented access to structure`

- `9 Savf.` **`ProgramHeaderBase`** `programBaseHeader =`

- `10 kaitai.mainSegment().pgmHeader().programHeader();`

- `11 // ...`

- `12 }`

- `13 // ... 14 }`

25

## Slide 26

- **`1 public class GhidraPGM400Loader extends AbstractProgramWrapperLoader { 2 @Override`**

- **`3 protected void load (ByteProvider provider /*...*/ ){ 4 ByteBufferKaitaiStream stream =`**

- **`5 new ByteBufferKaitaiStream (provider.readBytes(0, provider.length()))`**

- **`6 // Instantiate strcture with Kaitai`**

- **`7 Savf kaitai = new Savf (stream);`**

- **`8 // Object-oriented access to structure`**

- **`9 Savf. ProgramHeaderBase programBaseHeader =`**

- **`10 kaitai.mainSegment().pgmHeader().programHeader();`**

- **`11 // ... 12 } 13 // ... 14 }`**

25.1

## Slide 27

public class GhidraPGM400Loader extends AbstractProgramWrapperLoader {
  @Override
  protected void load(ByteProvider provider /*...*/ ){
    ByteBufferKaitaiStream stream =
      new ByteBufferKaitaiStream(provider.readBytes(0, provider.length()))
    // Instantiate strcture with Kaitai
    Savf kaitai = new Savf(stream);
    // Object-oriented access to structure
    Savf.ProgramHeaderBase programBaseHeader =
      kaitai.mainSegment().pgmHeader().programHeader();
    // ...
  }
  // ...
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
    ByteBufferKaitaiStream stream =
      new ByteBufferKaitaiStream(provider.readBytes(0, provider.length()))
public class GhidraPGM400Loader extends AbstractProgramWrapperLoader {
1
  @Override
2
  protected void load(ByteProvider provider /*...*/ ){
3
4
5
    // Instantiate strcture with Kaitai
6
    Savf kaitai = new Savf(stream);
7
    // Object-oriented access to structure
8
    Savf.ProgramHeaderBase programBaseHeader =
9
      kaitai.mainSegment().pgmHeader().programHeader();
10
    // ...
11
  }
12
  // ...
13
}
14
    // Instantiate strcture with Kaitai
    Savf kaitai = new Savf(stream);
public class GhidraPGM400Loader extends AbstractProgramWrapperLoader {
1
  @Override
2
  protected void load(ByteProvider provider /*...*/ ){
3
    ByteBufferKaitaiStream stream =
4
      new ByteBufferKaitaiStream(provider.readBytes(0, provider.length()))
5
6
7
    // Object-oriented access to structure
8
    Savf.ProgramHeaderBase programBaseHeader =
9
      kaitai.mainSegment().pgmHeader().programHeader();
10
    // ...
11
  }
12
  // ...
13
}
14
25.2

## Slide 28

public class GhidraPGM400Loader extends AbstractProgramWrapperLoader {
  @Override
  protected void load(ByteProvider provider /*...*/ ){
    ByteBufferKaitaiStream stream =
      new ByteBufferKaitaiStream(provider.readBytes(0, provider.length()))
    // Instantiate strcture with Kaitai
    Savf kaitai = new Savf(stream);
    // Object-oriented access to structure
    Savf.ProgramHeaderBase programBaseHeader =
      kaitai.mainSegment().pgmHeader().programHeader();
    // ...
  }
  // ...
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
    ByteBufferKaitaiStream stream =
      new ByteBufferKaitaiStream(provider.readBytes(0, provider.length()))
public class GhidraPGM400Loader extends AbstractProgramWrapperLoader {
1
  @Override
2
  protected void load(ByteProvider provider /*...*/ ){
3
4
5
    // Instantiate strcture with Kaitai
6
    Savf kaitai = new Savf(stream);
7
    // Object-oriented access to structure
8
    Savf.ProgramHeaderBase programBaseHeader =
9
      kaitai.mainSegment().pgmHeader().programHeader();
10
    // ...
11
  }
12
  // ...
13
}
14
    // Instantiate strcture with Kaitai
    Savf kaitai = new Savf(stream);
public class GhidraPGM400Loader extends AbstractProgramWrapperLoader {
1
  @Override
2
  protected void load(ByteProvider provider /*...*/ ){
3
    ByteBufferKaitaiStream stream =
4
      new ByteBufferKaitaiStream(provider.readBytes(0, provider.length()))
5
6
7
    // Object-oriented access to structure
8
    Savf.ProgramHeaderBase programBaseHeader =
9
      kaitai.mainSegment().pgmHeader().programHeader();
10
    // ...
11
  }
12
  // ...
13
}
14
    // Object-oriented access to structure
    Savf.ProgramHeaderBase programBaseHeader =
      kaitai.mainSegment().pgmHeader().programHeader();
public class GhidraPGM400Loader extends AbstractProgramWrapperLoader {
1
  @Override
2
  protected void load(ByteProvider provider /*...*/ ){
3
    ByteBufferKaitaiStream stream =
4
      new ByteBufferKaitaiStream(provider.readBytes(0, provider.length()))
5
    // Instantiate strcture with Kaitai
6
    Savf kaitai = new Savf(stream);
7
8
9
10
    // ...
11
  }
12
  // ...
13
}
14
25.3

## Slide 29

### **`KAITAI VS. PGM`**

26


> Recovered by OCR — confidence 85/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
T signal
KAITAI VS. PGM
‘eh tables
29 p
rocedure extension table
object tree
dHdrPtr [Addr
yrocStartPtr [A
rmPtr [Ad
mvPtr [A
cbSize = 0x160
stringId = 6x16
yrocDictId = OxA
iodNumber = Oxl1
26
```

## Slide 30

\```
Private ISA extensions: POWER-AS
\```

27


> Recovered by OCR — confidence 79/100 on the text kept, 57/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
undefined
1e57Ge6da1003084
1e57Ge6da1 063096
1e57Ge6dal 063094
Private ISA extensions:
38
Ad
fe
ris
ris
20
11 rs, 0x8
fF 26h
POWER-AS
27
```

## Slide 31

28


> Recovered by OCR — confidence 80/100 on the text kept, 70/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
000030!
000030: ??
00003061 00 li
00003064 c6 ridicr , 76, 0x38,
00003068 ? e tch from 7c O1
00003069
0000306a
0000306b
0000306c
00003070,
00003074
00003075
Search Memory
Search Value: 61850000
00003077
00003075
0000307c
Hex Sequence: |61 85 00 00
Display Formatted Data
Page/Line. .. 52 / 41
2A9EE6911E 002074 0000A4 F88A0032 STQ 4,0X30(10) |=
2A9EE6911E 002078 0000A8 61430000 ORI 3,10,0 IBM can :;)
2A9EE6911E 00207C 0000Ac 48000155 BL 0X154
28
```

## Slide 32

### **`POWER-AS FOR GHIDRA`**

\```
We have a Processor Module!
\```

29


> Recovered by OCR — confidence 72/100 on the text kept, 63/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
POWER-AS FOR GHIDRA
We have a Processor Module!
Program Trees §&| Listing: S2DBG.pgm
v fey S2DBG.pgm
increment
3692b 02d 25002194 60 28 std rO, Ox28(r1)
3692b 02d 250021a4 80 03 bgtla cr7,SuUB_fffftffffffffsoo0
3692b02d250021a8 00 30 std r4,0x30(r3)
3692b02d250021b8 50 88 td Oxld,r9,r16
3692b 02d 250021be 60 80 1 r7, 0x80
3692b02d250021c0 cl c6 rldicr r7.r7, 0x38, Ox?
3692b02d250021¢4 03 e6 settag
3692b02d250021cc 06 60 ori rs, Pg, 0x0
3692b02d250021d0 oo 12 stq r4, Oxl0(r3)
3692b 02d 250021d4 oo 04 b LAB_3692b02d250021d8
Segment 1
Segment 2
ExceptionSpace
StackSpace
an S¥Mbol Tree y ei me X
> fi, Imports
> fim Exports
~~ Eel Functions
LAB_3692b02d250021d8
FUN_3692b02d25002200
increment
main
00 28 ld rQ, 0x28(r1)
03 a6 mtspr LR, ro
```

## Slide 33

### **`POWER-AS FOR GHIDRA`**

30


> Recovered by OCR — confidence 72/100 on the text kept, 60/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
POWER-AS FOR GHIDRA
=|
6) longlong 1lVarl;
7) byte in_er?;
16) *(undefineds *)(in_rl + Ox28) = in_LR;
13) if ((bool)(in_er? == 2461)) {
15) }
16) *(undefinedS *)(param_1 + @x30) = param_2;
17) 1WWarl = *(longlong *)(param_1 + Ox28) + *(longlong *)(param_1 + Ox30);
19 settag():
21) *(longlong *)(param_l + Ox18) =
Sic 25 return:
30
```

## Slide 34

\```
POWER-AS FOR GHIDRA
Some findings
\```

\```
Register usage
Calling convention
Registers + thick pointers on stack
Function arguments and locals use different stack
pointers
\```

\```
How to handle that in Ghidra?!
Local stack grows up...
Return addresses are on a different stack
\```

31

## Slide 35

# **`ATTACK!`**

32

## Slide 36

33


> Recovered by OCR — confidence 85/100 on the text kept, 58/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
=
settag
orl
orl
stq
r4,r/, 0x0
33
```

## Slide 37

### **`MEMORY TAGGING`**

\```
1-bit of extra information can be encoded for every
aligned 128-bit QWORD
HW assisted (ECC?), can't be leaked/forged
SETTAG + store instruction
Loads check tags
LQ sets bits in XER, then TXER traps
LTPTR loads NULL if untagged
\```

34

## Slide 38

### **`MEMORY TAGGING`**

\```
7c 01 03 e6     settag
f8 88 00 22     stq        r4,0x20(r8)
e1 1f ff d1     lq         r8,-0x30(r31)
7c 00 05 48     txer       0x0,0x0,0xa
\```

35

## Slide 39

### **`MEMORY TAGGING`**

\```
"Was this pointer created in an
approved way?"
\```

36

## Slide 40

### **`MEMORY TAGGING`**

\```
Consequence:
\```

\```
Corrupted pointers can't be dereferenced
\```

37

## Slide 41

#### `Idea #0`

\```
Write shellcode and jump to it
\```

38

## Slide 42

### **`TYPED POINTERS`**

\```
printf("[%llx %llx + %d]", buf, offset);
[8000000000000000 ab4dc0ffee002000 + 1337]
\```

\```
First 64-bits of a 128-bit ptr contains the type
\```

39

## Slide 43

### **`TYPED POINTERS`**

\```
"The instruction is also extended
with a third operand (in bits 28:31
inclusive), an immediate, which
appears to mask the loaded value in
some way." - The PowerPC AS Tagged
Memory Extensions
\```

40

## Slide 44

### **`FUNCTION POINTER CALL`**

|`1`|`lq`|`r8,-50(r31),0x01`|`; Pointer from stack in R8||R9`|
|---|---|---|---|
|`2`|||`; Last four reserved bits are: 0b0001`|
|`3`
`4`
`5`
`6`
`7`
`8`|`txer`
**`ori`**
**`ori`**
**`ori`**
**`ld`**
`;`|`0x0,0x0,0xa`
 `r10,r9,0x0`
 `r12,r8,0x0`
 `r3,r7,0x0`
 `r11,0x0(r10)`|`; Type check`
`; Function address -> R10`
`; Funcptr type -> R12`
`; Setting callee parameter stack`
`; Dereference function address to R11`|
|`9`
`10`
`11`
`12`|`...`
**`ld`**
`mtspr`
**`ld`**
`bctrl`|`r4,0x8(r11)`
`CTR,r4`
 `r2,0x0(r11)`
|`; Another deref from R11 to R4`
`; Set program counter from R4`
`; Branch to CTR`|

41

## Slide 45

### **`FUNCTION POINTER CALL`**

|**`lq`**

**`1`**
**`2`**|**`r8,-50(r31),0x01`**
|**`; Pointer from stack in R8||R9`**
**`Last four reserved bits are: 0b0001`**|
|---|---|---|
|
**`txer`**

**`3`**|
**`0x0,0x0,0xa`**|
**`; Type check`**|
|**`ori`**
**`4`**|**`r10,r9,0x0`**|**`; Function address -> R10`**|
|**`ori`**
**`5`**
**`ori`**
**`6`**|**`r12,r8,0x0`**
 **`r3,r7,0x0`**|**`; Funcptr type -> R12`**
**`; Setting callee parameter stack`**|
|**`ld`**
**`7`**
**`;`**
**`8`**|
 **`r11,0x0(r10)`**|
**`; Dereference function address to R11`**|
|**`...`**

**`ld`**
**`9`**
**`mtspr`**
**`10`**
**`ld`**
**`11`**
**`bctrl`**
**`12`**|**`r4,0x8(r11)`**
**`CTR,r4`**
 **`r2,0x0(r11)`**
|**`; Another deref from R11 to R4`**
**`; Set program counter from R4`**
**`; Branch to CTR`**|

41.1

## Slide 46

FUNCTION POINTER CALL
lq         r8,-50(r31),0x01  ; Pointer from stack in R8||R9
                             ; Last four reserved bits are: 0b0001
txer       0x0,0x0,0xa       ; Type check
1
2
3
ori        r10,r9,0x0        ; Function address -> R10
4
ori        r12,r8,0x0        ; Funcptr type -> R12
5
ori        r3,r7,0x0         ; Setting callee parameter stack
6
ld         r11,0x0(r10)      ; Dereference function address to R11
7
; ...
8
ld         r4,0x8(r11)       ; Another deref from R11 to R4
9
mtspr      CTR,r4            ; Set program counter from R4
10
ld         r2,0x0(r11)
11
bctrl                        ; Branch to CTR
12
ori        r10,r9,0x0        ; Function address -> R10
ori        r12,r8,0x0        ; Funcptr type -> R12
ld         r11,0x0(r10)      ; Dereference function address to R11
ld         r4,0x8(r11)       ; Another deref from R11 to R4
lq         r8,-50(r31),0x01  ; Pointer from stack in R8||R9
1
                             ; Last four reserved bits are: 0b0001
2
txer       0x0,0x0,0xa       ; Type check
3
4
5
ori        r3,r7,0x0         ; Setting callee parameter stack
6
7
; ...
8
9
mtspr      CTR,r4            ; Set program counter from R4
10
ld         r2,0x0(r11)
11
bctrl                        ; Branch to CTR
12
mtspr      CTR,r4            ; Set program counter from R4
bctrl                        ; Branch to CTR
lq         r8,-50(r31),0x01  ; Pointer from stack in R8||R9
1
                             ; Last four reserved bits are: 0b0001
2
txer       0x0,0x0,0xa       ; Type check
3
ori        r10,r9,0x0        ; Function address -> R10
4
ori        r12,r8,0x0        ; Funcptr type -> R12
5
ori        r3,r7,0x0         ; Setting callee parameter stack
6
ld         r11,0x0(r10)      ; Dereference function address to R11
7
; ...
8
ld         r4,0x8(r11)       ; Another deref from R11 to R4
9
10
ld         r2,0x0(r11)
11
12
41.2

## Slide 47

### **`TYPED POINTERS`**

\```
LQ-TXER mask pairs (lq_stats.py)
\```

\```
LQ mask: 0x1 with TXER mask 0xA - 1 instances
LQ mask: 0xF with TXER mask 0x3 - 3 instances
\```

\```
LQ mask: 0x2 with TXER mask 0x3 - 9 instances
LQ mask: 0xF with TXER mask 0x3 - 21 instances
\```

42

## Slide 48

\```
Type ByteLQ MaskTXER Mask
0x800xF0x3
0xA10x10xA
0xA20x20x3
\```

43

## Slide 49

### **`TYPED POINTERS`**

\```
Consequence:
\```

\```
Can't transfer control to data via pointers
\```

44

## Slide 50

#### `Idea #1`

\```
Just use a large enough overflow!
\```

45

## Slide 51

### **`SEGMENT BOUNDARY CHECKING`**

###### `putchar(str[i]);`

- `1 ltptr      r8,0x2(r29),0x2  ; Load address from typed pointer to R8 2` **`add`** `r7,r8,r12 ; Add offset (R12) to address, result in R7 3 td         0x1d,r7,r8 ; Trap conditionally 4 lbz        r6,0x0(r7)       ; Load byte from R7`

46

## Slide 52

### **`SEGMENT BOUNDARY CHECKING`**

###### `putchar(str[i]);`

- **`1 ltptr      r8,0x2(r29),0x2  ; Load address from typed pointer to R8 2 add r7,r8,r12 ; Add offset (R12) to address, result in R7 3 td         0x1d,r7,r8 ; Trap conditionally 4 lbz        r6,0x0(r7)       ; Load byte from R7`**

46.1

## Slide 53

### **`SEGMENT BOUNDARY CHECKING`**

\```
The 0x1d (0b11101) mask doesn't make sense!
\```

47


> Recovered by OCR — confidence 87/100 on the text kept, 80/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
SEGMENT BOUNDARY CHECKING
The 0x1ld (0611101) mask doesn't make sense!
Trap Doubleword
td TO,RA,RB
TO RA
11
if « b) & TO, then TRAP
if > b) & TO, then TRAP
if D) & TO, then TRAP
b) & TO, then TRAP
b) & TO, then TRAP
<
```

## Slide 54

### **`SEGMENT BOUNDARY CHECKING`**

\```
td_masks.py> Running...
TD Mask: 0b11100 - 44 instances found
TD Mask: 0b11101 - 4 instances found
td_masks.py> Finished!
\```

\```
Checking if top 40 bits of src and dst registers
match.
\```

48

## Slide 55

### **`SEGMENT BOUNDARY CHECKING`** <u>`DEMO`</u>

49

## Slide 56

### **`SEGMENT BOUNDARY CHECKING`**

\```
Consequence:
\```

\```
Can't move pointers outside their original segments
\```

50

## Slide 57

#### `Idea #2`

#### `Return address overwrite?`

51

## Slide 58

### **`RETURN ADDRESS OVERWRITE`**

\```
Tag/type not checked on function return!
Return addresses are stored in a separate segment
\```

52

## Slide 59

\```
RETURN ADDRESS OVERWRITE
Consequence:
\```

\```
User code can't corrupt return addresses
\```

53

## Slide 60

#### `Idea #3`

#### `Out-of-context call?`

54

## Slide 61

### **`OUT-OF-CONTEXT FPTR CALL`**

- `1` **`void`** `(*adminCmd)(` **`char`** `*); 2 Command commands[2]; 3 4 commands[1].name="lower"; commands[1].exec=lower; 5 commands[0].name="upper"; commands[0].exec=upper; 6 adminCmd = my_system; 7 8 adminCmd("SNDPGMMSG MSG(CRACKMEX) MSGTYPE(*INFO)"); 9 // ...`

- `10` **`while`** `(cmd != 99){ 11 // ... 12 Command *tmpCmd = &(commands[cmd]); 13 printf("%llx %llx %llx %llx\n", *tmpCmd); 14 printf("Invoking %s(%s)\n", tmpCmd->name, param); 15 tmpCmd->exec(param); 16 }`

}

55

## Slide 62

### **`OUT-OF-CONTEXT FPTR CALL`**

- **`1 void (*adminCmd)( char *);`**

- **`2 Command commands[2];`**

- **`3`**

- **`4 commands[1].name="lower"; commands[1].exec=lower;`**

- **`5 commands[0].name="upper"; commands[0].exec=upper;`**

- **`6 adminCmd = my_system;`**

- **`7`**

- **`8 adminCmd("SNDPGMMSG MSG(CRACKMEX) MSGTYPE(*INFO)");`**

- **`9 // ...`**

- **`10 while (cmd != 99){ 11 // ... 12 Command *tmpCmd = &(commands[cmd]);`**

- **`13 printf("%llx %llx %llx %llx\n", *tmpCmd);`**

- **`14 printf("Invoking %s(%s)\n", tmpCmd->name, param);`**

- **`15 tmpCmd->exec(param);`**

- **`16 }`**

55.1

## Slide 63

OUT-OF-CONTEXT FPTR CALL
void (*adminCmd)(char*);
Command commands[2];

commands[1].name="lower"; commands[1].exec=lower;
commands[0].name="upper"; commands[0].exec=upper;
adminCmd = my_system;

adminCmd("SNDPGMMSG MSG(CRACKMEX) MSGTYPE(*INFO)");
// ...
while(cmd != 99){
    // ...
    Command *tmpCmd = &(commands[cmd]);
    printf("%llx %llx %llx %llx\n", *tmpCmd);
    printf("Invoking %s(%s)\n", tmpCmd->name, param);
    tmpCmd->exec(param);
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
}
16
Command commands[2];

commands[1].name="lower"; commands[1].exec=lower;
commands[0].name="upper"; commands[0].exec=upper;
void (*adminCmd)(char*);
1
2
3
4
5
adminCmd = my_system;
6

7
adminCmd("SNDPGMMSG MSG(CRACKMEX) MSGTYPE(*INFO)");
8
// ...
9
while(cmd != 99){
10
    // ...
11
    Command *tmpCmd = &(commands[cmd]);
12
    printf("%llx %llx %llx %llx\n", *tmpCmd);
13
    printf("Invoking %s(%s)\n", tmpCmd->name, param);
14
    tmpCmd->exec(param);
15
}
16
void (*adminCmd)(char*);
adminCmd = my_system;
adminCmd("SNDPGMMSG MSG(CRACKMEX) MSGTYPE(*INFO)");
1
Command commands[2];
2

3
commands[1].name="lower"; commands[1].exec=lower;
4
commands[0].name="upper"; commands[0].exec=upper;
5
6

7
8
// ...
9
while(cmd != 99){
10
    // ...
11
    Command *tmpCmd = &(commands[cmd]);
12
    printf("%llx %llx %llx %llx\n", *tmpCmd);
13
    printf("Invoking %s(%s)\n", tmpCmd->name, param);
14
    tmpCmd->exec(param);
15
}
16
55.2

## Slide 64

OUT-OF-CONTEXT FPTR CALL
void (*adminCmd)(char*);
Command commands[2];

commands[1].name="lower"; commands[1].exec=lower;
commands[0].name="upper"; commands[0].exec=upper;
adminCmd = my_system;

adminCmd("SNDPGMMSG MSG(CRACKMEX) MSGTYPE(*INFO)");
// ...
while(cmd != 99){
    // ...
    Command *tmpCmd = &(commands[cmd]);
    printf("%llx %llx %llx %llx\n", *tmpCmd);
    printf("Invoking %s(%s)\n", tmpCmd->name, param);
    tmpCmd->exec(param);
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
}
16
Command commands[2];

commands[1].name="lower"; commands[1].exec=lower;
commands[0].name="upper"; commands[0].exec=upper;
void (*adminCmd)(char*);
1
2
3
4
5
adminCmd = my_system;
6

7
adminCmd("SNDPGMMSG MSG(CRACKMEX) MSGTYPE(*INFO)");
8
// ...
9
while(cmd != 99){
10
    // ...
11
    Command *tmpCmd = &(commands[cmd]);
12
    printf("%llx %llx %llx %llx\n", *tmpCmd);
13
    printf("Invoking %s(%s)\n", tmpCmd->name, param);
14
    tmpCmd->exec(param);
15
}
16
void (*adminCmd)(char*);
adminCmd = my_system;
adminCmd("SNDPGMMSG MSG(CRACKMEX) MSGTYPE(*INFO)");
1
Command commands[2];
2

3
commands[1].name="lower"; commands[1].exec=lower;
4
commands[0].name="upper"; commands[0].exec=upper;
5
6

7
8
// ...
9
while(cmd != 99){
10
    // ...
11
    Command *tmpCmd = &(commands[cmd]);
12
    printf("%llx %llx %llx %llx\n", *tmpCmd);
13
    printf("Invoking %s(%s)\n", tmpCmd->name, param);
14
    tmpCmd->exec(param);
15
}
16
    Command *tmpCmd = &(commands[cmd]);
    tmpCmd->exec(param);
void (*adminCmd)(char*);
1
Command commands[2];
2

3
commands[1].name="lower"; commands[1].exec=lower;
4
commands[0].name="upper"; commands[0].exec=upper;
5
adminCmd = my_system;
6

7
adminCmd("SNDPGMMSG MSG(CRACKMEX) MSGTYPE(*INFO)");
8
// ...
9
while(cmd != 99){
10
    // ...
11
12
    printf("%llx %llx %llx %llx\n", *tmpCmd);
13
    printf("Invoking %s(%s)\n", tmpCmd->name, param);
14
15
}
16
55.3

## Slide 65

### **`CRACKMEX`** <u>`DEMO`</u>

56

## Slide 66

### **`FAILS / FUTURE WORK`**

\```
Misaligned loads / Type confusion
How do I get useful pointers?
TOCTOU
\```

\```
No tags on regs!
Did't look
Translator bugs
Microarchitecture
\```

57

## Slide 67

### **`TEMPORAL SAFETY`**

- `1` **`for`** `(` **`int`** `i=0; i < BUFS_COUNT; i++){`

- `2 bufs[i]=(` **`char`** `*)malloc(0xffe000);`

- `3 memset(bufs[i], 0x41, 0xffe000); 4 }`

- `5` **`for`** `(` **`int`** `i=0;i<BUFS_COUNT;i++){`

- `6 free(bufs[i]);`

- `7`

   - `}`

- `8`

- `9` **`for`** `(` **`int`** `j=0; j < 10; j++){`

- `10` **`for`** `(` **`int`** `i=0; i<BUFS_COUNT; i++){ 11` **`for`** `(` **`int`** `k=0; k<0xffe000; k++){ 12` **`if`** `(bufs[i][k] != 0x41){ 13 printf("%02x ", bufs[i][k]); 14 } 15 } 16 } 17 }`

17 }

58

## Slide 68

### **`TEMPORAL SAFETY`**

- **`1 for ( int i=0; i < BUFS_COUNT; i++){`**

- **`2 bufs[i]=( char *)malloc(0xffe000);`**

- **`3 memset(bufs[i], 0x41, 0xffe000); 4 }`**

- **`5 for ( int i=0;i<BUFS_COUNT;i++){`**

- **`6 free(bufs[i]);`**

- **`7`**

   - **`}`**

- **`8`**

- **`9 for ( int j=0; j < 10; j++){`**

- **`10 for ( int i=0; i<BUFS_COUNT; i++){`**

- **`11 for ( int k=0; k<0xffe000; k++){`**

- **`12 if (bufs[i][k] != 0x41){ 13 printf("%02x ", bufs[i][k]); 14 }`**

- **`15 }`**

- **`16 } 17 }`**

58.1

## Slide 69

TEMPORAL SAFETY
for (int i=0; i < BUFS_COUNT; i++){
  bufs[i]=(char*)malloc(0xffe000);
  memset(bufs[i], 0x41, 0xffe000);
}
1
2
3
4
for (int i=0;i<BUFS_COUNT;i++){
5
  free(bufs[i]);
6
}
7

8
for (int j=0; j < 10; j++){
9
  for (int i=0; i<BUFS_COUNT; i++){
10
      for (int k=0; k<0xffe000; k++){
11
          if (bufs[i][k] != 0x41){
12
              printf("%02x ", bufs[i][k]);
13
          }
14
      }
15
  }
16
}
17
for (int i=0;i<BUFS_COUNT;i++){
  free(bufs[i]);
}
for (int i=0; i < BUFS_COUNT; i++){
1
  bufs[i]=(char*)malloc(0xffe000);
2
  memset(bufs[i], 0x41, 0xffe000);
3
}
4
5
6
7

8
for (int j=0; j < 10; j++){
9
  for (int i=0; i<BUFS_COUNT; i++){
10
      for (int k=0; k<0xffe000; k++){
11
          if (bufs[i][k] != 0x41){
12
              printf("%02x ", bufs[i][k]);
13
          }
14
      }
15
  }
16
}
17
for (int j=0; j < 10; j++){
  for (int i=0; i<BUFS_COUNT; i++){
      for (int k=0; k<0xffe000; k++){
          if (bufs[i][k] != 0x41){
              printf("%02x ", bufs[i][k]);
          }
      }
  }
}
for (int i=0; i < BUFS_COUNT; i++){
1
  bufs[i]=(char*)malloc(0xffe000);
2
  memset(bufs[i], 0x41, 0xffe000);
3
}
4
for (int i=0;i<BUFS_COUNT;i++){
5
  free(bufs[i]);
6
}
7

8
9
10
11
12
13
14
15
16
17
58.2

## Slide 70

### **`TEMPORAL SAFETY`**

59

## Slide 71

# **`IDEAS?`**

60

## Slide 72

# **`ENDPGM`**

61

## Slide 73

### **`SUMMARY`**

\```
Memory corruption is possible on IBM i
CFI makes exploitation hard
Logical bugs are more appealing
Even Data-oriented exploitationis harder on
segmented memory
Accepting objects from untrusted systems is
Achilles' Heel of the platform
Now we have tools to attack it
\```

62

## Slide 74

### **`RABBIT HOLE`**

\```
IBM i cloud instances - pub400.com
Custom IBM POWER hardware - raptorcs.com
\```

63

## Slide 75

### **`THANK YOU!`**

#### **<u>`Writeup`</u>**

\```
Ghidra ext.
\```

#### **<u>`Kaitai defs`</u>**

\```
greetz: depth, hl, s2, alligators,
hipsters
\```

64

## Slide 76
