---
title: "Endoscope Unpacking Android Apps with VM-Based Obfuscation"
speakers: ["Fan Wu", "Xuankai Zhang"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Fan Wu & Xuankai Zhang_Endoscope Unpacking Android Apps with VM-Based Obfuscation.pdf"
pages: 43
sha256: "5881607f7e91d983db979203407b937b7881c2e4f12b902b77871b172c3fd25c"
text_chars: 21297
ocr_pages: 3
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:15:49Z"
---
# Endoscope Unpacking Android Apps with VM-Based Obfuscation

**Speakers:** Fan Wu, Xuankai Zhang  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Fan Wu & Xuankai Zhang_Endoscope Unpacking Android Apps with VM-Based Obfuscation.pdf` (43 pages)


## Slide 1

# Endoscope: Unpacking Android Apps with VM-based Obfuscation

Speaker: Fan Wu Contributor: Xuankai Zhang

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
USA &
AUGUST 9-10, ©0253
BRIEFINGS
Endoscope: Unpacking Android Apps
with VM-based Obfuscation
Speaker: Fan Wu
Contributor: Xuankai Zhang
```

## Slide 2

## About us

- Fan Wu: Expert Security Engineer at Meituan; previously with Alibaba Cloud.

- Speaker of multiple security conferences (BCS, CIS, etc.) • Xuankai Zhang: Graduate student of ShangHai Jiaotong University and intern at Meituan.

- His area of interest is software reverse engineering and code analysis.

#BHUSA @BlackHatEvents

## Slide 3

## Agenda

- Intro & Background Story

- The Rhino Bytecode Case and its Reversing

- More General Scenario of VM-Packed Programs

- Unpacking under General Scenario

- Insights & Conclusion

#BHUSA @BlackHatEvents

## Slide 4

## VM-Based Obfuscation

Compiling code into bytecode comprising of a specific set of custom instruction, and running it on a custom-built Virtual Machine.

The tools used to carry out the obfuscation is referred to as a packer. VM-Based obfuscation has long been used for benign and evil purposes

- Anti-plagiarism

- Intellectual property protection

- Hiding malicious payload

#BHUSA @BlackHatEvents

## Slide 5

## VM-Based Obfuscation on Android

- Recent years has seen increasing numbers of VM-protected Android apps

- Android has a multiple-layer architecture. Cross-layer invocations, especially those through Java Native Interface(JNI) are commonly used by Android VM-based packers, while those for PC programs have no such characteristic.

Applications Android Framework Android Runtime & Libraries Hardware Abstraction Layer Linux Kernel

#BHUSA @BlackHatEvents

## Slide 6

## Background Story

- Months ago, when analyzing an Android malware, we found that it executes js bytecode on Mozilla Rhino engine, with the bytecode’s source deliberately removed

- • We studied the Rhino engine and managed to reverse and recover some of the malware’s semantics

#BHUSA @BlackHatEvents

## Slide 7

## Background Story

- Later, we encountered other in-the-wild malwares that are obfuscated with different virtualization techniques

- The exact method we used to reverse previous malware cannot be reused in these cases

- So we figured out a method that is  more general

Interpreter

Custom Virtual Machine

#BHUSA @BlackHatEvents

## Slide 8

## Agenda

- Intro & Background Story

- The Rhino Bytecode Case and its Reversing

- More General Scenario of VM-Packed Programs

- Unpacking under General Scenario

- Insights & Conclusion

#BHUSA @BlackHatEvents

## Slide 9

## The Rhino Bytecode Malware Case

onCreate() of Entry Activity

handleIntent()

doExecution()

decrypt()

- This InterpretedFunction object only stores Rhino bytecode, not the source.

- • Each byte of bytecode is interpreted in a large switch-case statement.

executeScriptWith Continuations()

- Unlike the situation of Dalvik bytecode, there is no existing tool to translate Rhino bytecode back to source. And the encodedSource field of InterpreterData object is set to empty string.

#BHUSA @BlackHatEvents

## Slide 10

## Generation of Bytecode and its Reverse

Source code in  Parse Abstract syntax  CodeGen Interpret
Bytecode
Javascript tree (AST)
root Icode_LINE
Icode_REG_STR_C0
-42
ExpressionStatement STRING
-16 Icode_REG_STR_C1
-43 Icode_PROP_AND_THIS
FunctionCall
41 Icode_REG_STR_C2
STRING
-33
PropertyGet StringLiteral Icode_REG_IND_C1
"tahkcalb".split("").reverse().join(""); 38
CALL
FunctionCall Name “” -44 Icode_REG_STR_C3
-16 Icode_PROP_AND_THIS
-32 Icode_REG_IND_C0
PropertyGet “join” CALL
38
Icode_REG_STR1
-45
FunctionCall Name Icode_PROP_AND_THIS
-16
Icode_REG_STR1
-45 STRING
PropertyGet StringLiteral “reverse” 41 Icode_REG_IND_C1
-33 CALL
“”
StringLiteral Name Icode_POP_RESULT
RETURN_RESULT
“tahkcalb” “split”
#BHUSA
……
……

#BHUSA @BlackHatEvents

## Slide 11

## Reconstruct AST and Source

root
ExpressionStatement
FunctionCall
PropertyGet StringLiteral
PropertyGet FunctionCall Name “”
PropertyGet “join”
StringLiteral Name FunctionCall Name
PropertyGet StringLiteral “reverse”
“tahkcalb” “split” StringLiteral Name “”
“tahkcalb” “split”

-42 -16 Icode_LINE -43 Icode_REG_STR_C0 -42 **STRING** -16 Icode_REG_STR_C1 -43 **Icode_PROP_AND_THIS** 41 Icode_REG_STR_C2 -33 STRING Icode_REG_IND_C1 38 CALL -44 Icode_REG_STR_C3 -16 Icode_PROP_AND_THIS -32 Icode_REG_IND_C0 38 CALL -45 Icode_REG_STR1 Icode_PROP_AND_THIS -16 Icode_REG_STR1 -45 STRING 41 Icode_REG_IND_C1 -33 CALL -42 Icode_POP_RESULT RETURN_RESULT -16 -43

StringLiteral “tahkcalb” stack stack Key reverse logic itsStringTable 0 ”tahkcalb” 1 ”split” 2 ””

stack

Rhino provides a toSource() method that transform an AST back into source code recursively J

……

"tahkcalb".split("").reverse().join("");

#BHUSA @BlackHatEvents

## Slide 12

## Agenda

- Intro & Background Story

- The Rhino Bytecode Case and its Reversing

- More General Scenario of VM-Packed Programs

- Unpacking under General Scenario

- Insights & Conclusion

#BHUSA @BlackHatEvents

## Slide 13

## A more General VM-Packer Scenario

### In-the-wild Samples protected by VM-based obfuscators on Android usually

- Close source

- Implement virtual machine in a native library (JNI)

- • Adopt app-specific Randomization

- Difficulty levels up!

#BHUSA @BlackHatEvents

## Slide 14

## Key Components: VM Entry / Exit

VM Entry:  Switch to virtual context
                  Copy registers, etc
Dispatcher
Handlers
…
Loop / VM Exit: Switch back to original context

#BHUSA @BlackHatEvents

## Slide 15

## Key Components: Dispatcher & Handlers

### Dispatcher loop:

VM Entry
Dispatcher
…
Handlers
Loop / VM Exit

- Fetch and decode a virtual instruction

- • Look up in the handler table

- • Invoke the handler

&add_handler
&sub_handler
Fetch and
&mul_handler
Decode Loop Lookup
&div_handler
&xor_handler
…

Handler table

#BHUSA @BlackHatEvents

## Slide 16

## Challenges in Reversing

- We only have binaries for in-the-wild, not source code/original Dalvik bytecode.

- • Lack of information about virtualized instructions and VM’s mechanism

- Control flow is very complex, so static and dynamic analysis are both timeconsuming

#BHUSA @BlackHatEvents

## Slide 17

## One more Challenge

- Many VM-protected programs use randomized, app-specific encryption parameters and order of handler pointers in handler table

- As a result, the result of manually analyzing a VM-packed program A, is not reusable to another program B which is packed with same packer

Multiple runs
One app + one obfuscator Different obfuscated program
\x10 &add_handler
Obfuscated  Virtualized  \xea Handler  &sub_handler
instructions1
program 1 \x05 Table 1 &mul_handler
\xe5 &div_handler
… …
\x30 &if_eq_handler
App VM-based  Obfuscated  Virtualized  \xb1 Handler  &get_handler
obfuscator
program 2 instructions2 \x2d Table 2 &put_handler
\xaf &invoke_handler
… …

#BHUSA @BlackHatEvents

## Slide 18

## Agenda

- Intro & Background Story

- The Rhino Bytecode Case and its Reversing

- More General Scenario of VM-Packed Programs

- Unpacking under General Scenario

- Insights & Conclusion

#BHUSA @BlackHatEvents

## Slide 19

## Assumptions and Prerequisites

- Our method of unpacking only works properly when the following assumptions are met

- The packer we are going to reverse is accessible and we can use it to obfuscate any custom app

- The obfuscator follow the typical pattern of “transform Dalvik bytecode into native functions”

- Provided that Dalvik bytecode can be easily transferred back to Java with existing tools, our goal under this scenario is to recover Dalvik bytecode from obfuscated program

#BHUSA @BlackHatEvents

## Slide 20

## The Obfuscated Program

return handler
……………………………….. ……………
……………………………….. ……………
\x10 ……………………………….. ……………
&nop_handler ……………………………….. ……………
\x50 \xea
&mov_handler
\xb1 \x05
&return_handler
mul handler
Instruction
\x08 Virtualized  \xe5 Handler  ……………………………….. ……………
Obfuscation &const_handler Sequence for
……………………………….. ……………
Original dalvik bytecode \x01\x8e instructions \x04\x00 Table &add_handler&sub_handler each Handler ……………………………….. …………………………………………….. ……………
Reverse
\x53 \xa9 &mul_handler
\x00 \x7f &div_handler mov handler
… …
……………………………….. ……………
\xc0
… ……………………………….. ……………
……………………………….. ……………
……………………………….. ……………
…

#BHUSA @BlackHatEvents

## Slide 21

## The Execution Process

return handler ……………………………….. …………… ……………………………….. …………… ……………………………….. ……………

……………………………….. ……………
\x10 &nop_handler Instruction  ……………………………….. ……………
\x50
\xea &mov_handler Sequence for
\xb1 each Handlers
\x05 &return_handler mul handler
\x08 Virtualized  \xe5 Fetch and  Handler  &const_handler ……………………………….. ……………
……………………………….. ……………
Original dalvik bytecode \x8e instructions \x00 Decode Loop Table &add_handler ……………………………….. ……………
\x01 ……………………………….. ……………
\x04 &sub_handler
\x53
\xa9 &mul_handler
\x00
\x7f &div_handler mov handler
… … ……………………………….. ……………
\xc0
… ……………………………….. ……………

……………………………….. ……………
……………………………….. ……………

#BHUSA @BlackHatEvents

## Slide 22

## The Execution Process Cont.

return handler
……………………………….. ……………
……………………………….. ……………
……………………………….. ……………
\x10 &nop_handler Instruction  ……………………………….. ……………
\x50
\xea &mov_handler Sequence for
\xb1 each Handlers
\x05 &return_handler mul handler
\x08 Virtualized  \xe5 Fetch and  Handler  &const_handler ……………………………….. ……………
……………………………….. ……………
Original dalvik bytecode \x8e instructions \x00 Decode Loop Table &add_handler ……………………………….. ……………
\x01 ……………………………….. ……………
\x04 &sub_handler
\x53
\xa9 &mul_handler
\x00
\x7f &div_handler mov handler
… … ……………………………….. ……………
\xc0
… ……………………………….. ……………
……………………………….. ……………
……………………………….. ……………

#BHUSA @BlackHatEvents

## Slide 23

## The Reverse Process

? handler
……………………………….. ……………
……………………………….. ……………
……………………………….. ……………
\x10 ? Instruction  ……………………………….. ……………
?
\xea ? Sequence for
? \x05 ? each Handlers ? handler
? Virtualized  \xe5 Fetch and  Handler  ? ……………………………….. ……………
……………………………….. ……………
Original dalvik bytecode ? instructions \x00 Decode Loop Table ? ……………………………….. ……………
? \x04 ? ……………………………….. ……………
Reverse
? \xa9 ?
? \x7f ? ? handler
… … ……………………………….. ……………
?
… ……………………………….. ……………
App-specific Encryption parameters Random order of handlers ……………………………….. ……………
……………………………….. ……………

#BHUSA @BlackHatEvents

## Slide 24

## Intuition

- To keep the obfuscated program’s semantics identical to that of original one, each handler of the VM is initially translated from a set of simple operations in original Dalvik bytecode

- Although the intermediates are app-specific, the relationship between the original Dalvik bytecode and the handler content is fixed (Diagram on next page)

- • Also, the obfuscated functions generally pass parameters in the same way as original program.

#BHUSA @BlackHatEvents

## Slide 25

## Intuition Cont.

•
Whenever there is a mov instruction in the original Dalvik code, during execution of the obfuscated program
the instruction sequence for mov handler must execute once, and vice versa.
return handler
……………………………….. ……………
……………………………….. ……………
……………………………….. ……………
\x10 &nop_handlernop_handler Instruction  ……………………………….. ……………
? \xea &mov_handlermov_handler Sequence for
? \x05 &return_handlerreturn_handler each Handlers mul handler
mov Virtualized  \xe5 Fetch and  Handler  &const_handlerconst_handler ……………………………….. ……………
……………………………….. ……………
Original dalvik  ? instructions Decode Loop Table
bytecode \x00 &add_handleradd_handler ……………………………….. ……………
mul \x04 &sub_handlersub_handler ……………………………….. ……………
? \xa9 &mul_handlermul_handler
?
\x7f &div_handlerdiv_handler mov handler
… … ……………………………….. ……………
?
… ……………………………….. ……………
……………………………….. ……………
App-specific and random
……………………………….. ……………

… #BHUSA @BlackHatEvents

## Slide 26

## Learn the Mapping Relations

- Provided the above intuition, we can construct apps, obfuscate them and execute obfuscated programs, to learn the mapping relations between original Dalvik bytecode and executed handlers

- • Then we can apply the learned rules to transform back executed handler information of other apps

\x13 h_13 \x10 h_50 \x50
\x8f h_8f \xea h_b1 \xb1
\x70 h_70 \x05 h_08 Look up the  \x08
\x53 h_53 \xe5 h_8e learnt mapping  \x8e
relations
\x30 … h_30 \x00 … h_01 \x01
\x28 h_28 \x04 h_53 \x53
Obfuscate  Execute
\x30 h_30 \xa9 h_00 \x00
& Execute
\x68 h_68 \x7f h_c0 \xc0
… … … … …
Constructed  Executed  Virtualized  Executed  Recovered
app handlers instructions handlers Dalvik bytecode
…

Learn mapping relations

Apply learnt mapping relation to unpack apps

#BHUSA @BlackHatEvents

## Slide 27

## Questions to Solve During the Learning Phase

1. Determine virtualized instructions for each function

2. Figure out relationship between virtualized instruction and handler address

3. Identify handlers by their content, so as to recognize each handler when executing in-the-wild apps

\x13
h_13
\x8f
h_8f
\x70
h_70
\x53 h_53
\x30 … h_30
\x28 h_28
Obfuscate
\x30 h_30
& Execute
\x68 h_68
… …
Constructed  Executed
app handlers
…

Learn mapping relations

#BHUSA @BlackHatEvents

## Slide 28

## Proposed Solution

1. Determine virtualized instructions for each function

- Hook and trace the register function

2. Figure out mapping relations between virtualized instruction and handler address • Instrumentation to collect Dynamic Trace + analyze trace log to construct mapping

3. Identify handlers by their content, so as to recognize them in trace of other apps • Generate Genetic Signature to identify each handler

#BHUSA @BlackHatEvents

## Slide 29

## 1.Virtualization of Functions

Before obfuscation

After obfuscation

Virtualized instructions

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pisek hat
USA 20253
6
000014f8: |6f20 0100 5400
>onCreate(Landroid/os/Bundle
000014fe: |0740
00001500: |1f00 0400
type@eee4
Q0001504: |6201 0cdd
ComposableSingletons$MainActi
field@dedc
20001508: |6e10 2b00 0100
ComposableSingletons$MainActi
0000150e: 10c1
protected onCreate(Landroid/os/Bundle; )V
pl, “savedInstanceState":Landroid/os/Bundle;
20
000: invoke-super
)V # method@gee1
21
0003: move-object
004: check-cast
{p@, p1}, Landroidx/activity/ComponentActivity;-
v0, pd
v@, Landroidx/activity/ComponentActivity; #
0006: sget-object v1, Lcom/example/myapplication/
vityKt ; ->INSTANCE: Lcom/example/myapplication/ComposableSingletons$MainActivityKt; #
0008: invoke-virtual {v1}, Lcom/example/myapplication/
vityKt;->getLambda-3$app_debug()Lkotlin/jvm/functions/Function2; # method@002b
000b: move-result-obiect v1
public void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState) ;
ComponentActivityKt.setContent$default(this, null, ComposableSingletons$MainActivityKt. INSTANCE.
m4078getLambda3$app_debug(), 1, null);
id *v3; //
int v4; // 8h 8
__int128 *v5; // 1]
int *v6; //
oid *v73 //
int v8; //
int16 v9; // 44
_int128 v10[2]; // 4
Las Ty: 5
7 4 v12; //
__int64 v13; //
= *(_QWORD
= 61;
@LL;
3
=_256
memse 10, 0, sizeof( Ds
8;
5
&v85
& 5
return vminterpret| » &V3, &off_10720);
)(_ReadStatusReg(ARM64_SYSREG(3, 3, 13, @, 2)) + 40);
Before obfuscation
public native void onCreate(Bundle bundle);
After obfuscation
data:
8 E6 08 46 08 08 828 O5 eB
38 00 6F 08 6B GO DO E1
°8 20 @2 67 27 D3 30 1B 01
8 OF 10 1E 01 08 G8 O5 O1
Q000000000886D42 O62
Q@1 01 06 @@ E6 10 47 00
@1 @0+word_6CC8 DCW
2D @0+
1@ @2+DCW Ox11E, 2,
Al @2+DCW @xE1, 1, 4
@2 @@+DCW @x54D3, @
unk_6D42 DCB
Virtualized instructions
```

## Slide 30

## 1.Determine Virtualized Instructions for each Function

- Hook and trace the arguments passed to env->RegisterNatives(), to get signature of function and address of virtualized instructions

Hook

|**Name**|**Signature**|**Virtualized instructions**|
|---|---|---|
|onCreate|(Landroid/os/Bundle;)V|\x12\x20\x00\x00T\x00D@\xd0\x00…|
|invoke|(Landroidx/compose/ru
ntime/Composer;I)V|\x01\x00\x04\x00\xa7\x20\r\x00\x05\x00]\
x00\x06…|
|…|…|…|
||Dumped Vir|tualized instructions|

#BHUSA @BlackHatEvents

## Slide 31

2. Mapping Relations between Virtualized Instruction and Handler Address

• There is need to observe execution flow [inside] function, so merely hook the entrance and exit of function is not enough

- Debugging is the first thing comes to mind, but it requires much tedious manual work, and coping with anti-debug mechanisms

- So we use Instrumentation + Trace way to construct the mapping

\x10 ?
\xea ?
\x05 ?
Virtualized  \xe5 Fetch and  Handler  ?
instructions \x00 Decode Loop Table ?
\x04 ?
\xa9 &mul_handler
\x7f ?
… …

#BHUSA @BlackHatEvents

## Slide 32

## 2. Tools and Frameworks for Instructionlevel Instrumentation

- DBI : Valgrind, DynamoRIO, QBDI, Intel Pin…

- • Emulator: Unicorn, Unidbg…

- • Frida-Stalker

### Considerations

- Android support: exclude Intel Pin and Valgrind

- Environment supplement: necessary when using a simulator

QBDI or other instruction-level instrumentation frameworks can serve our purpose

#BHUSA @BlackHatEvents

## Slide 33

## 2. Locating Dispatcher and Handler Table

- Dispatcher firstly loads an address(of handler) to a register, and then uses “br” to jump to that address

- The address points to code segment, but itself is stored in data segment, or more precisely, the handler table

- The target of the jump is a handler, and after that the content, or instruction sequence of that handler is executed

Part of dispatcher

A handler address from handler table

Handler content

#BHUSA @BlackHatEvents

## Slide 34

## 2. Mapping Virtualized Instruction and Handler Address

- Each run of the above function builds a mapping between a virtualized instruction and a handler

#### Dumped Virtualized instructions

handler table

#BHUSA @BlackHatEvents

## Slide 35

## 3. Need to Identify Each Handler

- When unpacking in-the-wild apps that original dex file is unavailable, the order of handlers is random, which means handler address only cannot identify a handler

- • As a result, during the learning phase, we need to create ”identity” with handler’s content for each handler.

Handler content

\x10 h_? ?
\xea h_? ?
\x05 h_? Look up the  ?
\xe5 h_? learnt mapping  ?
relations
\x00 … h_? ?
\x04 h_? ?
Execute
\xa9 h_? ?
How do we
\x7f h_? ?
know this is
h_50?  Virtualized … Executed … Recovered …
instructions handlers Dalvik bytecode

Apply learnt mapping relation to unpack apps

#BHUSA @BlackHatEvents

## Slide 36

## 3. Genetic Signature of Handler

We generally use “hash(hex(instruction sequence))” as genetic signature of a handler, but this signature needs to undergo the following processing steps:

- Truncate the sequence to only include the part before the 'br' instruction.

- Replace instructions that have different corresponding machine codes across different programs with a fixed sequence. This kind of instructions include jump instructions(e.g. b, bl, cbz) and PC-register-relative instructions(e.g. adrp), etc.

h_50

Instruction sequence of a handler

Hexed sequence

Genetic signature

#BHUSA @BlackHatEvents

## Slide 37

## Put it Together: Reversing In-the-wild Obfuscated App

- Execute in-the-wild apps to get genetic signatures corresponding to executed virtualized instructions, and then just apply learnt mapping relations to recover them into Dalvik bytecodes

Identify with
genetic signatures
\x10 h_50 \x50
\xea h_b1 \xb1
\x05 h_08 Look up the  \x08
\xe5 h_8e learnt mapping  \x8e
relations
\x00 … h_01 \x01
\x04 h_53 \x53
Execute
\xa9 h_00 \x00
\x7f h_c0 \xc0
… … …
Virtualized  Executed  Recovered
instructions handlers Dalvik bytecode

Apply learnt mapping relation to unpack apps

#BHUSA @BlackHatEvents

## Slide 38

## Agenda

- Intro & Background Story

- The Rhino Bytecode Case and its Reversing

- More General Scenario of VM-Packed Programs

- Unpacking under General Scenario

- Insights & Conclusion

#BHUSA @BlackHatEvents

## Slide 39

## Usage of Inexpensive Packer in Obfuscation of Android Malware

- We have noticed a tendency of malwares using inexpensive VM-based packers

- • One of the most famous commercial packers charge ¥18000 (about $2516) per year, while some inexpensive packers only charge About $4 per year.

- This seems to attract price-sensitive malware authors. A significant portion of recently seen VMprotected malware samples are obfuscated with inexpensive packers

#BHUSA @BlackHatEvents

## Slide 40

## Another Common Obfuscation Technique on Android

- Hiding the Dex data and dynamically releasing it into memory during execution is another widely-used obfuscation technique.

- For this kind of obfuscation, existing unpacking tools search for and extract the Dex data from the memory.

- However, these tools are unable to unpack apps that are protected by VM obfuscation, as the original Dalvik bytecode is never placed into the memory.

#BHUSA @BlackHatEvents

## Slide 41

## Conclusion and Takeaways

In conclusion, we propose a two-fold methodology for Unpacking Android apps with VM-based obfuscation:

- For specific type of obfuscation with Rhino bytecode, since it is open-source, we analyze the VM and reconstruct AST to recover source from bytecode

- For more general scenario, we introduce a method through gathering execution trace and using genetic signatures to learn mapping relationship between original bytecode and handler. The learnt relations are then applied to recover semantics of in-the-wild VM-obfuscated apps.

#BHUSA @BlackHatEvents

## Slide 42

## Reference

- <u>https://web.archive.org/web/20230531155247/https://blog.autojs.org/2022/08/24/ encryption/</u>

- <u>https://swarm.ptsecurity.com/how-we-bypassed-bytenode-and-decompiled-node-jsbytecode-in-ghidra/</u>

- <u>https://github.com/QBDI/QBDI</u>

- <u>https://www4.comp.polyu.edu.hk/~csxluo/Parema.pdf</u>

#BHUSA @BlackHatEvents

## Slide 43

# Thanks!

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
piekhat
USA &
Thanks!
#BHUSA @BlackHatEvents
```
