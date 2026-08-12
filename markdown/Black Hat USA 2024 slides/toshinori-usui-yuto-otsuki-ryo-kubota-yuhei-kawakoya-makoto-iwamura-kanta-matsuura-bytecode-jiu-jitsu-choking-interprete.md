---
title: "Bytecode Jiu-Jitsu Choking Interpreters to Force Execution of Malicious Bytecode"
speakers: ["Toshinori Usui", "Yuto Otsuki", "Ryo Kubota", "Yuhei Kawakoya", "Makoto Iwamura", "Kanta Matsuura"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Toshinori Usui & Yuto Otsuki & Ryo Kubota & Yuhei Kawakoya & Makoto Iwamura & Kanta Matsuura_Bytecode Jiu-Jitsu Choking Interpreters to Force Execution of Malicious Bytecode.pdf"
pages: 77
sha256: "ad7f0ae2cb23714273d7f51f192460dba8027023e384bcb3c04cca16d72fbd1e"
text_chars: 24737
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:48:32Z"
---
# Bytecode Jiu-Jitsu Choking Interpreters to Force Execution of Malicious Bytecode

**Speakers:** Toshinori Usui, Yuto Otsuki, Ryo Kubota, Yuhei Kawakoya, Makoto Iwamura, Kanta Matsuura  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Toshinori Usui & Yuto Otsuki & Ryo Kubota & Yuhei Kawakoya & Makoto Iwamura & Kanta Matsuura_Bytecode Jiu-Jitsu Choking Interpreters to Force Execution of Malicious Bytecode.pdf` (77 pages)


## Slide 1

Bytecode Jiu-Jitsu Choking Interpreters to Force Execution of Malicious Bytecode

Toshinori Usui<sup>1</sup> , Yuto Otsuki<sup>1</sup> Contributors: Ryo Kubota<sup>1</sup> , Yuhei Kawakoya<sup>1</sup> , Makoto Iwamura<sup>1</sup> , Kanta Matsuura<sup>2</sup>

1 NTT Security Holdings Corporation

2 Institute of Industrial Science, The University of Tokyo

#BHUSA @BlackHatEvents

## Slide 2

###### Toshinori Usui, Ph.D.

- Research scientist, security principal

- Research interests: malware analysis, reverse engineering, and exploit development

- • CTF lover

- Brazilian Jiu-Jitsu enthusiast

Yuto Otsuki, Ph.D.

- Senior researcher

- Research interests: memory analysis, reverse engineering and operating system security

#BHUSA @BlackHatEvents

2

## Slide 3

#### Code Injection Attack

1. Allocate 2. Write a memory region malicious code

3. Execute the code

```
31C0B001...
```

```
31C0B001...
```

#BHUSA @BlackHatEvents

3

## Slide 4

#### Code Injection Attack

1. Allocate 2. Write a memory region malicious code

3. Execute the code

```
31C0B001...
```

```
31C0B001...
```

#BHUSA @BlackHatEvents

4

## Slide 5

#### Code Injection Attack

## 2. Write malicious code

bytecode

```
31C0B001...
```

#BHUSA @BlackHatEvents

5

## Slide 6

Today’s Topic: Bytecode Jiu-Jitsu

Interpreter

Injector
(malware)

#BHUSA @BlackHatEvents

6

## Slide 7

#### Outline

- 入門 Introduction to Code Injection Attack

- 理合 Bytecode Jiu-Jitsu Overview

- 稽古 Interpreter Implementation Basics

- 打込 Interpreter Analysis

- 試合 Bytecode Jiu-Jitsu Attack

- 乱取 Experiments and Evaluations

- 受身 Countermeasures against Bytecode Jiu-Jitsu

- 総括 Takeaways

#BHUSA @BlackHatEvents

7

## Slide 8

##### 入門 Introduction to Code Injection Attack

#BHUSA @BlackHatEvents

8

## Slide 9

#### Code Injection Attack

- Malware tries to conceal their malicious behavior on the target host

- Code injection is a technique to blend malicious behavior with benign one by forcing a benign process to execute malicious code

Injector
(malware)
①Create/Open a
benign process
Injector code Legitimate ④Start a thread to
②Allocate
benign code execute malicious
memory region
code
Malicious code
Malicious code
for injection
③Inject
for injection
malicious code #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

9

## Slide 10

#### Process Hollowing

Injector
(malware) ①Create a suspended
benign process

Create a suspended Benign executable
Legitimate
benign image

Injector code
Malicious image
for injection

IP

#BHUSA @BlackHatEvents

10

## Slide 11

#### Process Hollowing

Injector
(malware) ①Create a suspended Benign executable
benign process
Injector code
②Unmap imageUnmap image
Malicious image

Injector code
②Unmap imageUnmap image
Malicious image
for injection

#BHUSA @BlackHatEvents

11

## Slide 12

#### Process Hollowing

Injector
(malware)

①Create a suspended
benign process

Benign executable **Malicious image** ②Unmap image **for injection**

benign process
Injector code
Malicious image
for injection

③Inject malicious image (replacement)

#BHUSA @BlackHatEvents

12

## Slide 13

#### Process Hollowing

Injector
(malware) ①Create a suspended Benign executable
④Adjust
benign process
Injector code
Malicious image
②Unmap image for injection
Malicious image
for injection
③Inject
malicious image
(replacement)

④Adjust
instruction pointer
IP

#BHUSA @BlackHatEvents

13

## Slide 14

#### Process Hollowing

Injector
(malware) ①Create a suspended Benign executable
④Adjust
benign process
instruction pointer
Injector code
Malicious image
IP
②Unmap image for injection
Malicious image
for injection
③Inject
malicious image
⑤Resume
(replacement)

#BHUSA @BlackHatEvents

14

## Slide 15

#### Process Hollowing

Injector
(malware) ①Create a suspended Benign executable
④Adjust
Not the same
benign process
instruction pointer
Injector code
Malicious image
IP
②Unmap image for injection
Malicious image
for injection
③Inject
malicious image
⑤Resume
(replacement)

#BHUSA @BlackHatEvents

15

## Slide 16

#### Process Hollowing Variants

###### • **Process Doppelgänging**

   1. Start a transaction and writes malicious code to a benign file

   2. Creates an in-memory image from the file

   **3. Rolls the file back**

   4. Creates a process from the image

- **Process Herpaderping**

   1. Writes malicious code to a benign file

   2. Creates an in-memory image from the file

   3. Creates a process from the image

   **4. Overwrites the file to make it benign**

   5. Creates the first thread

   6. Closes the file

#BHUSA @BlackHatEvents

16

## Slide 17

##### 理合 Bytecode Jiu-Jitsu Overview

#BHUSA @BlackHatEvents

17

## Slide 18

#### Our New Technique: Bytecode Jiu-Jitsu

- We introduce a novel technique of a code injection attack ⇒ We call it **_Bytecode Jiu-Jitsu_**

• The attack technique injects malicious **_bytecode_** into an interpreter process (e.g. Python)

**Existing attack Bytecode Jiu-Jitsu techniques** Injection target <u>Arbitrary process Interpreter process</u> Code to be injected Native code Bytecode Behavior blended into <u>Executable Script</u>

#BHUSA @BlackHatEvents

18

## Slide 19

#### Bytecode Jiu-Jitsu Overview

Attacker’s environment
Interpreter
In Malicious bytecode
Malicious put (and data) Embed into
injector
script
Injection
Interpreter
Injector
In Target bytecode
put (and data)
Target
script

Target script
Input Victim’s
environment
Interpreter
Target bytecode
Malicious bytecode(and data)
(and data)

#BHUSA @BlackHatEvents

19

## Slide 20

#### Bytecode Jiu-Jitsu Overview

Preparation phase
Attacker’s environment
Interpreter Extracted as
injection payload Target script
Input Victim’s
In Malicious bytecode environment
Malicious put (and data) Embed into
Interpreter
injector
script
Injection
Benign script
to be replaced Interpreter Target bytecode
Malicious bytecode(and data)
Injector (and data)
In Target bytecode
put (and data)
Target
script Extracted as
signature for
memory scan
20 #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

20

## Slide 21

Bytecode Jiu-Jitsu Overview
Attacker’s environment
Interpreter
Target script script
Scan memory to  Input
In Malicious bytecode
locate bytecode
put (and data) Embed into  by signature
Malicious
injector
script
Injection
Interpreter Target bytecode
Malicious bytecode(and data)(and data)
Injector (and data)
In Target bytecode
put (and data) Infiltrate into
Target victim’s
script environment

Attack phase **Target script script Scan memory to** Input **Victim’s environment locate bytecode Embed into by signature Interpreter injector Injection Target bytecode Malicious bytecode(and data)(and data) Injector (and data) Infiltrate into victim’s environment**

In
put
Malicious
script

#BHUSA @BlackHatEvents

21

## Slide 22

#### How to realize Bytecode Jiu-Jitsu?

- **Problem**

   - Bytecode Jiu-Jitsu requires the internal specifications of target interpreters i.e., **<u>data structures of bytecode and data</u>**

   - However, they are sometimes not publicly available

• **Solution:** Manual reverse engineering…??

#BHUSA @BlackHatEvents

22

## Slide 23

##### 稽古 Interpreter Implementation Basics

#BHUSA @BlackHatEvents

23

## Slide 24

#### Script Execution Mechanism

Analysis Code-gen
Script
phase phase
Virtual Machine
Bytecode cache
Virtual stack/
Virtual Program
Symbol table
virtual register
Counter (VPC)
Decoder/ VM instruction
Fetcher
Dispatcher handler
Execution cycle in interpretation function

#BHUSA @BlackHatEvents

24

## Slide 25

#### Bytecode Cache Implementation

###### Typically implemented with **<u>array of structures</u>**

Bytecode
…
LOAD_CONST 1
STORE_FAST 0
LOAD_FAST 0
LOAD_CONST 2
COMPARE_OP 2
POP_TOP
LOAD_CONST 0
…

###### **Array of structures {Opcode, Operand}**

Opcode Operand
…
LOAD_CONST 1
STORE_FAST 0
LOAD_FAST 0
COMPARE_OP 2
POP_TOP 2
LOAD_CONST 0
…

#BHUSA @BlackHatEvents

25

## Slide 26

#### Bytecode Cache Implementation

###### Typically implemented with **<u>array of structures</u>**

Bytecode
…
LOAD_CONST 1
STORE_FAST 0
LOAD_FAST 0
LOAD_CONST 2
COMPARE_OP 2
POP_TOP
LOAD_CONST 0
…

Array of structures {Opcode, Operand}Index for a symbol table
(Bytecode depends o n symbol
Opcode Operand
tables for data ac cess.)
…
LOAD_CONST 1
STORE_FAST 0
LOAD_FAST 0
COMPARE_OP 2
POP_TOP 2
LOAD_CONST 0
…
#BHUSA

#BHUSA @BlackHatEvents

26

## Slide 27

#### Symbol Table Implementation

**Symbol tables are composed of references between multiple structures and arrays**

###### **Management structure**

###### **Value object**

[1] Type:Int
global consts [2] Val:25
vars
[3](age)
[4]
It manages references to
It contains actual data,
symbol tables
such as integers, strings, etc.
(start node of chains)
(end node)

age = 25

#BHUSA @BlackHatEvents

27

## Slide 28

#### Symbol Table Implementation

Interpretation function

**`interp`** `(` **`script_ctx_info`** `,` **`func_info`** `, …)` **Management structure Arguments include pointers to management structures**

**Management structure Each of management structures has symbol tables for each scope**

###### **Value object**

###### **Value object**

#BHUSA @BlackHatEvents

28

## Slide 29

#### Interpreter Analysis Issues

- These data structures are complicated.

   - Not easy to extract them because bytecode and symbol tables must be kept consistency between them.

- Interpreters share this overall design, but the concrete implementation details differ across interpreters and versions.

- Manual reverse engineering of interpreters requires heavy effort.

- Which means Bytecode Jiu-Jitsu is not practical …?

#BHUSA @BlackHatEvents

29

## Slide 30

#### Interpreter Analysis Issues

- These data structures are complicated.

   - Not easy to extract them because bytecode and symbol tables must be kept consistency between them.

- Interpreters share this overall design, but the concrete implementation details differ across interpreters and versions.

- Manual reverse engineering of interpreters requires heavy effort.

- Which means Bytecode Jiu-Jitsu is not practical …? **→ No, the reverse engineering can be automated!**

#BHUSA @BlackHatEvents

30

## Slide 31

#### How to realize Bytecode Jiu-Jitsu?

- **Problem**

   - Bytecode Jiu-Jitsu requires the internal specifications of target interpreters i.e., **<u>data structures of bytecode and data</u>**

   - However, they are sometimes not publicly available

Too tedious

- **Solution:** ~~Manual reverse engineering…??~~

   - **→ Automated reverse engineering!!**

   - **<u>Dynamic analysis of interpreter binaries by crafted testing scripts</u>** for analyzing implementation details

   - **<u>Tracking pointer dereferences and analyzing memory accesses</u>** to reveal reference relationships and data structures

#BHUSA @BlackHatEvents

31

## Slide 32

##### 打込 Interpreter Analysis: Prepare Bytecode and Symbol Tables to Inject

#BHUSA @BlackHatEvents

32

## Slide 33

Interpreter Analysis Technique
info
Knowledge on
Bytecode and
language specification
Symbol tables
Analyze
Our analysis technique
Manual
In Out
Gen put
put
Test scripts
Injector
Memory access
traces
Observe behavior

Interpreter binary

#BHUSA @BlackHatEvents

33

## Slide 34

#### Technical Overview

**Interpretation function** **`interp`** `(` **`script_ctx_info`** `, …)`

① Find the interpretation function

#BHUSA @BlackHatEvents

34

## Slide 35

#### Technical Overview

###### **Interpretation function**

```
interp(script_ctx_info, …)
```

②Find memory regions accessed during bytecode interpretation

#BHUSA @BlackHatEvents

35

## Slide 36

#### Technical Overview

③ Find a value object

**Interpretation function** **`interp`** `(` **`script_ctx_info`** `, …)`

Value object

12345

#BHUSA @BlackHatEvents

36

## Slide 37

#### Technical Overview

④Find a dereference path
to the object
Value object
12345

**Interpretation function** **`interp`** <u>`(`</u> **`script_ctx_info`** `, …)`

**Management structure**

#BHUSA @BlackHatEvents

37

## Slide 38

#### Technical Overview

**Interpretation function** **`interp`** <u>`(`</u> **`script_ctx_info`** `, …)`

**Management structure**

⑤Find a symbol table,
identify its data structure
Value object
12345

#BHUSA @BlackHatEvents

38

## Slide 39

#### Key Steps of Interpreter Analysis Find the interpretation function Find accessed memory regions Find a value object

Find a dereference path to the object Find a symbol table, identify its data structure Extract bytecode and symbol tables

#BHUSA @BlackHatEvents

39

## Slide 40

Key Steps of Interpreter Analysis Find the interpretation function Find accessed memory regions Find a value object Find a dereference path to the object Find a symbol table, identify its data structure Extract bytecode and symbol tables

#BHUSA @BlackHatEvents

40

## Slide 41

#### What do we need to know first?

Analysis Code-gen
Script
phase phase
Virtual Machine
Bytecode cache
Virtual stack/
Virtual Program
Symbol table
virtual register
Counter (VPC)
Detecting  VPC first is a key Decoder/ VM instruction
Fetcher Detection
Dispatcher handler
Goal
Execution cycle in interpretation function

#BHUSA @BlackHatEvents

41

## Slide 42

#### Key Assumptions for Detection

Analysis Code-gen
② An ins truction in a bytecode cache
Script
phase phase
is always pointed by the  VPC
Virtual Machine
Bytecode cache
Virtual stack/
Virtual Program
Symbol table
virtual register
Counter (VPC)
① The number of memory reads to the VPC is proportional
Decoder/ VM instruction
Fetcher
to the numb er o f statements in the input script
Dis patcher handler
③ The interpretation function has
repeated memory reads to the  VPC

**Execution cycle in interpretation function**

#BHUSA @BlackHatEvents

42

## Slide 43

Detection
Script
Script
Analysis Code-gen
Script Bytecode cache / interpretation function
Script
phase phase
• Detect by using memory accesses to the  VPC
Virtual Machine
Bytecode cache
Virtual stack/
Virtual Program
Symbol table
virtual register
Counter (VPC)
VPC
D ecoder/ VM instruction
Fetcher • Run scripts of  var ious length
Dispatcher handler
• Find a memory region whose # of reads is proportional
Execution cycle in interpretation function #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

43

## Slide 44

Key Steps of Interpreter Analysis Find the interpretation function Find accessed memory regions Find a value object

Find a dereference path to the object Find a symbol table, identify its data structure Extract bytecode and symbol tables

#BHUSA @BlackHatEvents

44

## Slide 45

#### Accessed Memory Region Detection

Pointer tainting
Destination address
Dereference
Pointer
Propagate & Check
Assign a  taint tag

###### **Interpretation function**

interp ( script_ctx_info , …)
② Determine a memory region
with the  tag  as accessed
① Assign a  tag
to the pointer to the
management structure

#BHUSA @BlackHatEvents

45

## Slide 46

#### Accessed Memory Region Detection

Pointer tainting
Destination address
Dereference
Pointer
Propagate & Check
Assign a  taint tag
Interpretation function
The Analyses hereafter will focus only on
interp ( script_ctx_info , …)
② Determine a memory region
the acces sed memory regions
with the  tag  as accessed
① Assign a  tag
to the pointer to the
management structure

#BHUSA @BlackHatEvents

46

## Slide 47

Key Steps of Interpreter Analysis Find the interpretation function Find accessed memory regions Find a value object

Find a dereference path to the object

Find a symbol table, identify its data structure Extract bytecode and symbol tables

#BHUSA @BlackHatEvents

47

## Slide 48

#### Features of Test Script

- We manually craft test scripts to:

   - Run dynamic analysis

   - <u>Control the memory state</u> for the convenience of later analysis

```
global_var= 123456
```

**Feature 2:** Use a characteristic value <u>searchable in memory</u>

**Feature 1:** Has an assignment statement in each scope (this example is for global scope)

#BHUSA @BlackHatEvents

48

## Slide 49

#### Value Object Detection

###### **Test script**

global_var = 123456
Interpretation function
interp ( script_ctx_info , …)

Find a value object by searching memory for a **characteristic value**

Value object
123456

#BHUSA @BlackHatEvents

49

## Slide 50

#### Key Steps of Interpreter Analysis Find the interpretation function Find accessed memory regions

Find a value object

Find a dereference path to the object Find a symbol table, identify its data structure Extract bytecode and symbol tables

#BHUSA @BlackHatEvents

50

## Slide 51

#### Structure/Array Dereference Analysis

- Find structure/array accesses

- Determine base addresses and offsets

###### **Pointer**

dereference

Struct/Array
rbx
+0x10

Struct/Array
Member/Elem

Member/Elem

Member/Elem

```
mov rcx, [ rdx+ 0x40  ]
mov rbx, [ rcx+ rsi*8 ]
mov rax, [ rbx+ 0x10  ]
```

① Find memory accesses
that use the base register

③ Get
② Get base address
offset/index

④ Repeat

#BHUSA @BlackHatEvents

51

## Slide 52

#### Dereference Analysis of Symbol Tables

- Analyze all accessed structures and arrays

- Find **<u>dereference paths from the management structure to value objects</u>**

###### **Interpretation function**

```
interp(script_ctx_info, …)
```

###### **Management structure**

###### **Value object**

#BHUSA @BlackHatEvents

52

## Slide 53

#### Key Steps of Interpreter Analysis Find the interpretation function Find accessed memory regions

Find a value object

Find a dereference path to the object Find a symbol table, identify its data structure Extract bytecode and symbol tables

#BHUSA @BlackHatEvents

53

## Slide 54

#### Structure Analysis of Symbol Tables

- <u>A symbol table containing arbitrary number of variables</u> must be handled

- If references to value objects in the symbol table are managed with **<u>arrays</u>**

   - ⇒ Array length only varies

   - ⇒ Reference structure does not vary

###### **Interpretation function**

interp ( script_ctx_info , …)
Management structure

###### **Value object**

Array
1234
5678
9012
#BHUSA

#BHUSA @BlackHatEvents

54

## Slide 55

#### Key Steps of Interpreter Analysis Find the interpretation function Find accessed memory regions Find a value object

Find a dereference path to the object Find a symbol table, identify its data structure Extract bytecode and symbol tables

#BHUSA @BlackHatEvents

55

## Slide 56

#### Time to Extract!

Preparation phase
Attacker’s environment
Interpreter Extracted as
injection payload Target script
Input Victim’s
In Malicious bytecode environment
Malicious put (and data) Embed into
Interpreter
injector
script
Injection
Benign script
to be replaced Interpreter Target bytecode
Malicious bytecode(and data)
Injector (and data)
In Target bytecode
put (and data)
Target
script Extracted as
signature for
memory scan
56 #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

56

## Slide 57

###### Extraction of Bytecode and Symbol Tables

- ① Execute a malicious script with the behavior to inject

- ② Suspend the execution at the beginning of the interpretation function

- ③ Explore the structures from the management structure to symbol tables based on the obtained structural information

- ④ Read their memory to extract bytecode and symbol tables

#BHUSA @BlackHatEvents

57

## Slide 58

##### 試合 Bytecode Jiu-Jitsu Attack: Determine Place to Inject in Victim’s Environment

#BHUSA @BlackHatEvents

58

## Slide 59

#### Time to Inject!

Attack phase

**Attacker’s environment Interpreter In Malicious bytecode put (and data) Malicious script Interpreter In Target bytecode put (and data) Target script**

**Target script Scan memory to** Input **Victim’s environment locate bytecode Embed into by signature Interpreter injector Injection Target bytecode Malicious bytecode(and data) Injector (and data) Infiltrate into victim’s environment**

#BHUSA @BlackHatEvents

59

## Slide 60

#### Know Your Victim

- **Final step: Locate the proper position to inject to**

   - Memory space layout is randomized

      - The location of bytecode and symbol tables differs across executions

   - It is difficult to reveal the internal memory state of the interpreter in the victim’s environment

      - Should not use debuggers because it’s too suspicious

- **Approach: memory search and exploration**

   - Identify internal state by memory read only

      - Without using debuggers

#BHUSA @BlackHatEvents

60

## Slide 61

###### Recognizing Structure of Target Interpreter

1. Suspend execution and enumerate all stack and heap memory

2. Detect management structures by backtracking from a value object

Management
⑦ Step β ⑤ Step β ③ Step β
Structure A Structure B Array C
Pointer to B
Pointer to C
⑥ Step α
④ Step α
C[i]
Pointer to D
Step α: find the pointer with memory search
Step β: calculate the base address ② Step α

③ Step β
Structure D (Value Object)
1234

① Find a value object by
Pointer to D
searching a value in memory
② Step α

#BHUSA @BlackHatEvents

61

## Slide 62

###### Injection of Bytecode and Symbol Tables

① Traverse memory in the forward direction

② Write bytecode and symbol tables

③ Overwrite the VPC to point to the bytecode entry

④ Resume the execution

#BHUSA @BlackHatEvents

62

## Slide 63

##### 乱取 Experiments and Evaluations

#BHUSA @BlackHatEvents

63

## Slide 64

#### Experimental Setup

Chose open-source interpreters as targets to verify detection points

**Target interpreters Feature** Python Lua Widely used / Attackers frequently use VBScript

**Implementation type**

Open source Both open source and <u>proprietary</u>

#BHUSA @BlackHatEvents

64

## Slide 65

#### Analysis/Injection Test

**Symbol tables Value Bytecode Interp. Interpreters VPC cache function** **Detection object** **Analysis** Python ✓ ✓ ✓ ✓ ✓ ✓ Lua ✓ ✓ ✓ ✓ ✓ ✓ VBScript ✓ ✓ ✓ ✓ ✓ ✓

**Code Interpreters**<sup>**Bytecode, symboltables**</sup> **execution** **Extraction Injection** Python ✓ ✓ ✓ Lua ✓ ✓ ✓ VBScript ✓ ✓ ✓

**All steps of our analysis technique could analyze interpreters correctly**

#BHUSA @BlackHatEvents

65

## Slide 66

#### Detectability of Bytecode Jiu-Jitsu

- We built two types of Bytecode Jiu-Jitsu injectors

   - Inject **infinite loop** : for evaluating detectability of just the <u>injection behavior</u>

   - Inject **downloader malware** : for evaluating detectability of injection + bytecode behavior

- Evaluated whether each security tool can detect them

**Security tools Tools used for the experiment** Anti-virus (AV) 72 AV products Malware analysis sandbox CAPE sandbox Endpoint Detection and System monitoring tool Response (EDR) <u>(frequently used as simple EDR)</u> Memory forensics tools Volatility with hollowfind/imgmalfind/ptemalfind

#BHUSA @BlackHatEvents

66

## Slide 67

Detectability of Bytecode Jiu-Jitsu: Result

**Detection result Security tools** **Infinite loop Downloader** AV 9/72 9/72 Sandbox  ✓ EDR  ✓ Memory forensics   tools

#BHUSA @BlackHatEvents

67

## Slide 68

###### Detectability of Bytecode Jiu-Jitsu: Result

Detection result
Security tools
Infinite loop Downloader
AV 9/72 9/72
Sandbox  ✓
Only 9 AI-based engines flagged it as suspicious
EDR  ✓
Memory forensics
 
tools

#BHUSA @BlackHatEvents

68

## Slide 69

###### Detectability of Bytecode Jiu-Jitsu: Result

Detection result
Security tools
Infinite loop Downloader
AV 9/72 9/72
Sandbox  ✓
EDR  ✓
Memory forensics
 
tools
• Injection requires only memory read/write, which makes it difficult to detect
• Detected the behavior of injected bytecode

#BHUSA @BlackHatEvents

69

## Slide 70

###### Detectability of Bytecode Jiu-Jitsu: Result

**Detection result Security tools** **Infinite loop Downloader** AV 9/72 9/72 • Detection relies executable permission of memory Sandbox  ✓ ~~• Bytecode Jiu-Jitsu does not require it and out of their scope~~ EDR  ✓ Memory forensics   tools

#BHUSA @BlackHatEvents

70

## Slide 71

#### Demo

#BHUSA @BlackHatEvents

71

## Slide 72

##### 受身 Countermeasures against Bytecode Jiu-Jitsu

#BHUSA @BlackHatEvents

72

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
i) h yy fy
" RP
’ /]
i, me
Nl SY
jin no .
\ j
=] " ae,
ee Vii
a r
“ r 4 7 ? ‘ii
ihe %
q #G f Me
ON ll ww
&# Countermeasures against
Bytecode Jiu-Jitsu
a
```

## Slide 73

### Countermeasures with Existing Tools

- **AV**

   - Flag memory read/write APIs as suspicious

- **EDR and sandbox**

   - Detect memory writes to an interpreter process

   - Determine whether the written data is bytecode using signatures, etc.

- **Memory forensics**

   - Analyze an injector binary, detect unnatural parent-child relationships

- **OS security**

   - Protect interpreter processes and restrict memory write accesses

- **Manual analysis**

– Difficult. No bytecode specification, debuggers, or disassemblers

#BHUSA @BlackHatEvents

73

## Slide 74

### Countermeasures in Future Studies

• **<u>Bytecode</u>** / **<u>Malicious bytecode</u> identification**

Identification Input Output Unknown byte Bytecode Bytecode / Not sequence Malicious bytecode Bytecode Malicious / Benign

Applies to

EDRs and sandboxes Memory forensics

   - Learning-based approach may be applicable

- **Manual analysis support**

   - Analyze instruction set of bytecode, build debuggers/disassemblers

#BHUSA @BlackHatEvents

74

## Slide 75

総括 Takeaways

#BHUSA @BlackHatEvents

75

## Slide 76

#### Takeaways

- **<u>Utilizing bytecode for code injection</u>** had not been much discussed before

- • **<u>Our reverse engineering techniques</u>** revealed it to be a **<u>realistic threat</u>** → **Be more careful about bytecode as payload** from now on!

- • **<u>Security researchers should discuss further countermeasures</u>** – We wish our PoC tools will help them

Our PoC tools will be available soon here: https://github.com/ntt-zerolab/Bytecode_Jiu-Jitsu

#BHUSA @BlackHatEvents

76

## Slide 77

# Thank you!

#BHUSA @BlackHatEvents

77

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bisek hat
USA 2024
() NTT Security Holdings
TT
```
