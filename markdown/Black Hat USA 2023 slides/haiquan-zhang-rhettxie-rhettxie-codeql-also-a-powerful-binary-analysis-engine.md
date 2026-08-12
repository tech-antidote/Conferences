---
title: "CodeQL Also a Powerful Binary Analysis Engine"
speakers: ["Haiquan Zhang", "Rhettxie Rhettxie"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Haiquan Zhang & Rhettxie Rhettxie_CodeQL Also a Powerful Binary Analysis Engine.pdf"
pages: 41
sha256: "1efec65792765c6b66338fc3426bc6417852b15bd855242be50ccc09b5d6685a"
text_chars: 15991
ocr_pages: 5
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:16:36Z"
---
# CodeQL Also a Powerful Binary Analysis Engine

**Speakers:** Haiquan Zhang, Rhettxie Rhettxie  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Haiquan Zhang & Rhettxie Rhettxie_CodeQL Also a Powerful Binary Analysis Engine.pdf` (41 pages)

## Slide 1

## **CodeQL: Also a Powerful Binary Analysis Engine**

Haiquan Zhang rhettxie

@tencent security yunding lab

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
pifek hat
USA &
CodeQL: Also a Powerful Binary Analysis Engine
Haiquan Zhang
rhettxie
@tencent security yunding lab
#BHUSA @BlackHatEvents
```

## Slide 2

## Outline

- Ø The story begins with static analysis

- Ø CodeQL Introduction(Architecture and Core Engine)

- Ø Exploring the implementation details of CodeQL through the lifecycle of QL statements

- Ø How to extend CodeQL to support binary analysis

- Ø A newly developed dedicated debugger

- Ø Show time

#BHUSA @BlackHatEvents

## Slide 3

### The Story Begins With Static Program Analysis

- Ø Static program analysis is the art of reasoning about the behavior of computer programs without actually running them

- Ø A static program analyzer is a program that reasons about the behavior of other programs

- Ø It’s a hard work last for several decades. Resolved many issues, but still many problems remaining

- Ø Precision and efficiency are the two big problems

#BHUSA @BlackHatEvents

## Slide 4

### Many amazing technologies have been developed

- Ø Type Inference and Abstract Interpretation

- Ø Data Flow & Control Flow & Dependency Analysis

- Ø Pointer Analysis

- Ø Path Sensitive and Context Sensitive Analysis

- Ø Constraint Solving and Symbolic Execution

#BHUSA @BlackHatEvents

## Slide 5

### Also Some Amazing Tools

|Name|Pay or not|Open source|Compiler depend|Tech stack|
|---|---|---|---|---|
|Coverity|commercial|source close|need compile|classic analysis tech|
|Fortify|commercial|source close|need compile|classic analysis tech|
|Symgrep|free use|source open|code scan|pattern matching|
|SVF|free use|source open|need compile
depends on LLVM|classic analysis tech
academic use|
|Clang Static
Analyzer|free use|source open|need compile
clang only|AST travel
symbolic execution|

#BHUSA @BlackHatEvents

## Slide 6

### What is CodeQL

- Ø Founded in 2006, a research project from Oxford University, acquired by Github in 2019

- Ø Partly open source , but the core engine is source closed

- Ø Basically scan code, make database and run query logic, find patterns

- Ø Make code analysis to code property query

#BHUSA @BlackHatEvents

## Slide 7

### Architecture of CodeQL

- Ø The extractor can be regarded as language frontend，so it’s language depends

- Ø Extractor scan code, make extra analysis and store code property to database

- Ø Database store code information, can be shared and reused

- Ø CodeQL introduced a query language, the ql is related with query logic, but not related with code that being analyzed,so it’s language agnostic

- Ø CodeQL has developed a mature and comprehensive library that can perform various data flow analysis, such as the classic taint analysis

- Ø The core engine can be regarded as a database evaluate engine

#BHUSA @BlackHatEvents

## Slide 8

### Engine of CodeQL(extractor)

###### **./codeql database create  -l cpp -j 8 -s /data/codeql/qemu-6.1.0  /data/codeql/qemu.db**

- Ø For compiled languages, the extractor and compiler work in parallel

- Ø Monitor compiler works, if failed, then the process will abort

- Ø Intercept compiler command parameters, and add more

- Ø Extractor has the necessary information to compile a code file

- Ø Extractor scan code, analysis and get code property

#BHUSA @BlackHatEvents

## Slide 9

### Engine of CodeQL(extractor)

###### **How does extractor interrupt a compiler?**

protected void executeSubcommand()

1. Launch preload_tracer process while codeql starts to work

3. GDB shows that codeql/tools/linux64/lib64trace.so injected to LD_PRELOAD

2. Disassembling shows that preload_tracer will inject something into LD_PRELOAD

#BHUSA @BlackHatEvents

## Slide 10

### Engine of CodeQL(extractor) **How does extractor compile code**

- Ø lib64trace.so injected to every process Ø detect whether the host process is a compiler process Ø If so, add parameters from compiler-tracing.spec and launch an extractor process

#BHUSA @BlackHatEvents

## Slide 11

Engine of CodeQL(database) **In fact , codeql generate a trap file firstly then convert the trap to the final database**

**Trap file located at** /data/blackhat/codedb/trap/cpp/tarballs/data/blackhat/co de/test_c/source/data/blackhat/code/test_c

dbscheme is a guidance document for the content extraction, extractor extracts information according to that file

#BHUSA @BlackHatEvents

## Slide 12

### Engine of CodeQL(database)

###### **Let’s map these files together, and see an example**

Ø Extractor scan code, extracts information described in dbscheme

Ø All the code information extracted out will be placed at trap files

Ø Trap is a text file，it’s not convenient for further process It will be converted to structed db file

#BHUSA @BlackHatEvents

## Slide 13

### Engine of CodeQL(database)

**Let’s explore the dbscheme file**

###### **Take functions as an example**

- Ø functions is the collection of all functions

- Ø It’s unique lable is @function, can be referenced by this name

- Ø It has two field, name & kind， name is string and kind is an int Ø kind 1 means normal function, 2 means constructor

locations_stmt( /** The location of a statement. */ unique int id: @location_stmt, int container: @container ref, int startLine: int ref, int startColumn: int ref, int endLine: int ref, int endColumn: int ref );

Stmts is complicated Is has recursion type

#BHUSA @BlackHatEvents

## Slide 14

### Engine of CodeQL(database)

###### **Let’s explore the trap file**

simple example

complicated example

In trap file xopen is a function, named “xopen”, and it kind is 1(normal)

It’s a statement Kind 6 means a stmt_return Location is at  startLine 16, startColumn 3 Endline is 16 and endColumn is 11

#BHUSA @BlackHatEvents

## Slide 15

### Engine of CodeQL(database)

###### **trap to database**

xopen string encoded to 5336

xopen function in trap file

- a function declaration converted to an int tuple and write to db file

- Ø The int values in tuple can be regarded as index to the actual resources

- Ø It’s a complex and tedious process, and we will not go into further details here

0x59cb=22987  0x14d8=5336

the rel file is db file, tuples data are stored simply and directly in database file

#BHUSA @BlackHatEvents

## Slide 16

### The Query Language

- Ø Declarative Logic Programming

- Ø With class and OOP support

Ø Target language independent Ø Built-in with many libraries, such as the most common data flow analysis, taint analysis

#BHUSA @BlackHatEvents

## Slide 17

### QL to DIL

###### **The first lowing phase**

Ø It’s a lowing process

Ø High level user friendly language to machine friendly language Ø From where select, high level logic to child query operation Ø Table query and bool calculus

#BHUSA @BlackHatEvents

## Slide 18

### DIL to RA

###### **The second lowing phase**

- Ø Continue lowing

- Ø Data logic to relation algebra operations

Ø RA operations are classic JOIN UNION and BOOL calculus

Ø R1 R2, they are not registers

#BHUSA @BlackHatEvents

## Slide 19

### Evaluate Engine

###### **RA code and query tree**

- Ø RA expr is a query tree Ø A query tree is a set of logic related together, and can not be separated Ø The engine will consume a tree at a time Ø Evaluate from bottom to up Ø Support recursion evaluation

#BHUSA @BlackHatEvents

## Slide 20

### Summary

- Ø CodeQL has several language frontend, as extractor

- Ø Extractor extracts code information, do analysis, and store information to database

- Ø CodeQL implemented a datalog query language to query code property

- Ø CodeQL stores code property as database, and regard code analysis as database query

#BHUSA @BlackHatEvents

## Slide 21

### The Advance of CodeQL

- Ø The architecture design is very elegant, highly modular, and separates the front-end and back-end

- Ø CodeQL is a faithful implementer of database technology, convert code analysis to data query

- Ø Well designed query language, focus on code pattern or semantic matching. One query language to handle many other code language

- Ø Thanks to a unified query language, the same logic for different analysis tasks can be reused on a large scale

#BHUSA @BlackHatEvents

## Slide 22

### Extending CodeQL to binary

Ø new dbscheme for binary Ø new extractor for binary Ø new QL library for binary

##### **Architecture**

#BHUSA @BlackHatEvents

## Slide 23

## Design of binary dbshceme

- Ø Store the file, architecture, string, and function information of the binary.

- Ø Store the information of instructions, registers, and basic blocks inside the function.

- Ø Store the use and def information of registers inside the function.

- Ø Store the information of global variables and pointers.

- Ø Store memory layout information.(address ,section etc)

#BHUSA @BlackHatEvents

## Slide 24

### New Dbscheme For Binary

###### Basic information

Instruction and register information

###### Control flow information

#BHUSA @BlackHatEvents

## Slide 25

## New Extractor For Binary

The extractor needs to extract information according to the tables defined by the dbscheme. The main challenge here is how to efficiently save the relationships between the tables.

Extracting all strings from binary

Extracting imported function information from binary

Extracting usage information of instructions and registers from binary.

#BHUSA @BlackHatEvents

## Slide 26

### Configure a new workflow

Ø The above has completed the creation of the two most important key components for creating a database.Now, they need to be integrated into the CodeQL data creation workflow. Below is how we supplemented the configuration files needed for the workflow through dynamic debugging.

###### Register a new language option

###### Configure the compiler

###### Generate asm.dbscheme.stats file

#BHUSA @BlackHatEvents

## Slide 27

### Autobuild.sh For Binary

###### database create

Different from the data workflow for creating source code, we separate the extractor process, and autobuild.sh is just for packaging the trap files and copying them to a specific directory in the database.

#BHUSA @BlackHatEvents

## Slide 28

### QL library For Binary

Ø The QL library can help us use the QL language, and with this flexible language, we can accomplish even more powerful tasks.

- l Export functions l Functions

- l Registers, instructions

- l Import functions

- l Strings

**Done In Development** Support basic table Supports SSA IR, dataflow, queries and taint analysis

**Future** Supporting more architectures (arm, risc-v)

#BHUSA @BlackHatEvents

## Slide 29

### Simple example

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Simple example
CodeQL Query Results
export_func.ql X
1 10 export_func.ql on demo_db - finished in 0 seconds (1985 results) Open
« 110 » —[7/6/2023, 4:35:59 PM] export_func.ql
ql > src > examples > export_func.ql > {} export_func
. #select v 1985 results
1 import asm # [0]
unsetenv
putenv
from ExportFunc func ee
select func.getFuncName() group_member
__bss_start
mB WN
the_replace_len
sigwinch_sighandler
sh_modcase
parse_shellopts
BSE MPNOOKR WN
parse_string
12 protected_mode
13 rl_show_char
14 rl_byte_oriented
15 __libc_csu_fini
16 rl_filename_quoting_desired
17 search_for_command
00
rl eof char
```

## Slide 30

### Complex example

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Complex example
q
expr.qi M X
1
2
ou RW
N
foe}
10 }
11
12
13 }
14
15
16
17
18
19
20
> src > examples >
expr.ql > {} expr > @ dumpStr
import asm
predicate hasGNU(StrLit s ){
s.getStringLiteral().matches("%GNU GPL%"')
}
query string dumpStr(StrLit s) {
result = s.getStringLiteral()
i
query string dumpFunc(FunctionType f)
{
result = f.getFuncName()
+
from StrLit s,ImportFunc importFunc,FunctionType func,Callinsn callinsn
where hasGNU(s) and importFunc.getFuncName().matches("exec%")
and func.getFuncName()= "save_input_line_state"
and callinsn.getInsnFunction()=func
select s.getStringLiteral(), func.getFuncName(),callinsn, importFunc.getFuncName( )
>
CodeQL Query Results X
« 1 11» expr.ql on demo_db - finished in 0 seconds (1 results) [7/6/2023, 4:40:46 PM] Open expr.q|
#select v 1
# [0] i] callinsn [3]
License GPLv3+: GNU GPL version 3 or later . . call
<http://gnu.org/licenses/gpI.html> « save_input_line_state xmalloc execve@@GLIBC_
result
2.2.5
```

## Slide 31

### QL language Debugger At RA-level

- Ø The current version of the debugger supports breakpoints, execution, single-stepping, viewing relations, and tracing.

**Architecture**

#BHUSA @BlackHatEvents

## Slide 32

#### com.semmle.inmemory.eval.Evaluate.evaluate

Ø It is the starting point for RA's interpreted execution, where we can use CountingPrinter.print(expr) to print out the decompiled text of RA

- Ø Decompiled text

#BHUSA @BlackHatEvents

## Slide 33

### RA To Pipeline

###### 13 types of operation pipelines

RA operation Pipeline operation
ApplyTupleOperation TupleOperationPipeline
StreamDedup StreamDedupPipeline
SelectionByTest SelectionByTestPipeline
Literal AbstractRelationPipeline
EmptySet EmptySetPipeline
Union UnionPipeline
InvokeHigherOrderRelation InvokeHigherOrderRelationPipeline
Join JoinPipeline
… …

#BHUSA @BlackHatEvents

## Slide 34

### Pipeline Run

- Ø Each type of pipeline will eventually call its own runinternal method to perform operations such as reading and writing tables. Tables in the database are saved and used in memory in the form of page relations.

Get data corresponding to the page relation

Running pipeline

#BHUSA @BlackHatEvents

## Slide 35

##### com.semmle.inmemory.caching.RelationManager.addRelation

Ø CodeQL will save the page relations mentioned earlier here. Each table also has a different storage type, and we have implemented reading for each type in the debugger.

###### Entry point

Page relation data

Page information

The storage format of a relation

#BHUSA @BlackHatEvents

## Slide 36

### codeql-debug Agent

- Ø We discovered a hidden performance tuning parameter 'semmle.profiler.verbosity' during dynamic debugging, which can save the engine's execution state to a file. This way, we don't have to implement a trace function through jdb, we just need to add this parameter to the startup parameters.

###### Undisclosed system tuning parameters

Added launch parameters

#BHUSA @BlackHatEvents

## Slide 37

## Demo

#BHUSA @BlackHatEvents

## Slide 38

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black ha
USA 20253
EXPLORER oo debug.ql x > oO
> OPEN EDITORS iIpacks > codeq! > cpp-queries > 0.5.1 > Summary jebug.c
 CoDEQL 1 import cpp —
2 import semmle. code. cpp. security. Security
> Best Practices 3 import semmle. code. cpp. security. TaintTracking =
> codeql-suites 4 import TaintedwithPath
> Critical 5
>D tics :
iagnostics 6 | predicate isProcessOperationExplanation(Expr arg, string processOperation) {
> Documentation
7 exists(int processOperationArg, FunctionCall call |
> experimental 8 isProcessOperationArgument (processOperation, processOperationArg) and
> external 9 call.getTarget().getName() = processOperation and
> filters 10 call.getArgument(processOperationArg) = arg
> Header Cleanup is }
> JPL_C 13 T
> ist 14 class Configuration extends TaintTrackingConfiguration {
> Likely Bugs 15 override predicate isSink(Element arg) { isProcessOperationExplanation(arg, _) }
> Metrics 16}
> Microsoft 7
> PointsTo 18
> Power of 10 a eee processOperation, Expr arg, Expr source, PathNode sourceNode, PathNode sinkNode
> areas) 21 isProcessOperationExplanation(arg, processOperation) and
© Summary 22 taintedWithPath(source, arg, sourceNode, sinkNode)
debug.ql 23 select arg, sourceNode, sinkNode,
LinesofCode.al 24 "The value of this argument fiay come from $@ and is being passed “ + processQperation, source,
LinesOfCode.qix 7 source. toString()
LinesOfUserCode.ql 27
LinesOfUserCode.qlx
AlertSuppression.ql
pecieea cpanel PRC ourPu CON TERMINAL shty OB A x
CHANGELOG.md pani
! codeqi-pack.lock.yml zhangsan@HUNTAZHANG-MBO codeql % ff
default.qll
definitions.ql
definitions.qlx
objc.qll
! qlpack.yml
> esharp-all
> esharp-examples
> esharp-queries
> go-all
> go-examples
> OUTLINE I
> TIMELINE
Ln 24,Col34 Spaces:2 UTF-8 LF QL CodeQLCLIv2.12.1 (Canary) @Prettier & O
```

## Slide 39

## OPEN SOURCE

https://github.com/YunDingLab/codeql-binary

#BHUSA @BlackHatEvents

## Slide 40

# Q&A

huntazhang@tencent.com jitxie@tencent.com

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
USA 20253
Q&A
huntazhang@tencent.com Oo ANSenascee
jitxie@tencent.com TENCENT SECURITY YUNDING LAB
```

## Slide 41

## Thanks

#BHUSA @BlackHatEvents
