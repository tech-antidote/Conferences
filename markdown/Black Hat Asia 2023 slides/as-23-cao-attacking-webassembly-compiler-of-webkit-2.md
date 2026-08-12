---
title: "Attacking WebAssembly Compiler of Webkit"
speakers: ["Cao"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Cao-Attacking-WebAssembly-Compiler-of-Webkit.pdf"
pages: 56
sha256: "e4b56d7de3a2a1f5914c98498d1ceff6acdf1cfd4af0163c77f5605232edbc5b"
text_chars: 29786
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
ocr_confidence: 81.3
companion_files: ["AS-23-Cao-Attacking-WebAssembly-Compiler-of-Webkit_tools.txt"]
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T01:35:55Z"
---
# Attacking WebAssembly Compiler of Webkit

**Speakers:** Cao  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Cao-Attacking-WebAssembly-Compiler-of-Webkit.pdf` (56 pages)


## Slide 1

# Attacking the WebAssembly Compiler of WebKit

Zong Cao(@P1umer)     Zheng Wang(@xmzyshypnc)

#BHASIA   @BlackHatEvents

## Slide 2

### Who are we

Zong Cao
(@P1umer)
NeSE of IIE.CAS

**Zheng Wang** (@xmzyshypnc) _Tencent Security Xuanwu Lab_

Yeqi Fu
(@q1iq)
Peking University

Fangming Gu
(@afang5472)
NeSE of IIE.CAS

Bohan Liu
(@p4nda)
Tencent Security
Xuanwu Lab

#BHASIA   @BlackHatEvents

## Slide 3

Why WebAssembly Compiler in WebKit ?

#BHASIA   @BlackHatEvents

## Slide 4

Why WebAssembly Compiler in WebKit ?

#1 #2

#BHASIA   @BlackHatEvents

## Slide 5

### WASM Compiler in WebKit #1

- **New** features from WebAssembly 2.0 specs

   - <u>Wasm 2.0 compatibility roadmap</u>

#BHASIA   @BlackHatEvents

## Slide 6

### WASM Compiler in WebKit #2

- **Shared** security implications

- **Active** on WASM 2.0

Commits
JIT Compiler WASM Compiler
220
214
161
155
135
108
49
13
2020 2021 2022 2023*

**2023*:** 2023.1.1~2023.5.1 **Command** : git log --pretty=oneline --since=202{n}.1.1 --before=202{n}.12.31  -- ./{dir} |wc -l

#BHASIA   @BlackHatEvents

## Slide 7

### WASM Compiler in WebKit #2

• Shared security implications
Commits
• Active  on WASM 2.0
JIT Compiler WASM Compiler
220
214
161
155
135
108
49
13
2020 2021 2022 2023*

 https://www.zerodayinitiative.com/blog/2021/4/2/pwn2own-2021-schedule-and-live-results

#BHASIA   @BlackHatEvents

## Slide 8

**Fuzzing** WebAssembly Compiler in WebKit

#BHASIA   @BlackHatEvents

## Slide 9

### Fuzzing Overview

##### WebAssembly Compiler

LLInt BBQ interpreter Air

LLInt

OMG

B3-O2

- **LLInt** : Low Level Interpreter

- **BBQ:** Build Bytecode Quickly

- **OMG:** Optimized Machine-code Generator

#BHASIA   @BlackHatEvents

## Slide 10

### Fuzzing Overview

**Main challenge** : how to make the fuzzer generate **semi-well-formed** samples

WebAssembly Compiler
LLInt BBQ OMG
interpreter Air B3-O2
Parser

- **LLInt** : Low Level Interpreter

- **BBQ:** Build Bytecode Quickly

- **OMG:** Optimized Machine-code Generator

#BHASIA   @BlackHatEvents

## Slide 11

### Fuzzing Overview

**Main challenge** : how to make the fuzzer generate **semi-well-formed** samples

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR (confidence 76/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Fuzzing Overview
Main challenge: how to make the fuzzer generateGemi-well-formed)samples
ID + Pri> Type + Component + Status > Summary + Labels ~ Owner >
(@lWaSm compile fUzzet: Fatal error in Exception mismatch! Expected:
vr 1427334 2 Bug Blink>JavaScript>WebAssembly Assigned <RangeError: Maximum call stack si
yy 1425320 2 Bug Blink>JavaScript>WebAssembly Verified SSevesr Roompaestizzet: Creh in
Reproducible ClusterFuzz
we 1424671 1 Bug Blink>JavaScript>WebAssembly Duplicate — £. tlively Remove the ability to construct basic types in a TypeBuilder (#5678)
v8_wasm_compile_fuzzer: Fatal erro
yr 1421464 2 Bug Blink>JavaScript>WebAssembly Verified valid module. Run with —-trace-was|
ClusterFuzz
Reproducible ClusterFuzz
fuzzer—-common.cc Reproducible Ch
i : CHECK fe
Reproducible ClusterFuzz
: A WebAssembly test case generator.
1405706 li random.c 0.1
Bug- v8_wasm_compile_fuzzer: DCHECK BD random.h
yy 1404880 1 South Blink>JavaScript>Runtime Duplicate HAS_STRONG_HEAP_OBJECT_TAG|
bu v8_wasm_compile_fuzzer: DCHECK failure in
mY interface.c Reproducible ClusterFuzz allpublic
slike JavaScripts GarbaceCollection v8_wasm_compile_fuzzer: Null-dereference READ in o With cargo fuzz and libfuzzer-sys
o Asa Command Line Tool
Security Reproducible ClusterFuzz allpublic
Bu v8_wasm_compile_fuzzer: DCHECK failure in (address &
yy 1404655 1 sae ” Blink>JavaScript>WebAssembly Duplicate —_::v8internal::kHeapObjectTagMask) == 0 in heap-object.h Reproducible clemensb@chromium.org
ClusterFuzz_allpublic
```

## Slide 12

### Fuzzing Overview

**Main challenge** : how to make the fuzzer generate **semi-well-formed** samples

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR (confidence 77/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Main challenge:
ID + Pri» Type Component ~ Summary + Labels +
(élWasmlcompilelfuzzet: Fatal error in Exception mismatch! Expected:
<RangeError: Maximum call stack si
ClusterFuzz
ye 1427334 2 Buo
v8_wasm_compile_fuzzer: Crash in
Reproducible ClusterFuzz
v@_wasm_compile_fuzzer: Abrt in v8]
Duplicate
Reproducible ClusterFuzz
tlively Remove the ability to construct basic types in a TypeBuilder (#5678)
v8_wasm_compile_fuzzer: Fatal erro
clink>JavaScript>WebAssembly Verified valid module. Run with —-trace-was|
ClusterFuzz
Reproducible ClusterFuzz
fuzzer-common.cc Reproducible Cl
Reproducible ClusterFuzz
yy 1417516 1 Bug Blink>JavaScript>WebAssembly Verited Y8-wasm_compile_fuzzer: DCHECK) = [) __ parameters.h A WebAssembly test case generator.
1405706 li random.c 0.1
Bon v8_wasm_compile_fuzzer: DCHECK 1 random.h
yy 1404880 1 South Blink>JavaScript>Runtime Duplicate HAS_STRONG_HEAP_OBJECT_TAG|
bu v8_wasm_compile_fuzzer: DCHECK failure in
Sony. interface.c Reproducible ClusterFuzz allpublic
slike JavaScripts GarbaceCollection v8_wasm_compile_fuzzer: Null-dereference READ in o With cargo fuzz and libfuzzer-sys
o Asa Command Line Tool
Security Reproducible ClusterFuzz allpublic
bu v8_wasm_compile_fuzzer: DCHECK failure in (address &
yy 1404655 1 sae ” Blink>JavaScript>WebAssembly Duplicate —_::v8internal::kHeapObjectTagMask) == 0 in heap-object.h Reproducible clemensb@chromium.org
```

## Slide 13

### Our Approach: Inspiration

- **_v8_wasm_compile_fuzzer_** : 3 parts with strong binding

- **LibFuzzer Frontend** : Generate random data

- **Wasm Generator:** Convert ramdom data to valid & general wasm module

- **V8 Backend:** Embeded V8 as harness

#BHASIA   @BlackHatEvents

## Slide 14

### Our Approach: Inspiration

- **Original idea** : Port WebKit backend, but there are some issues:

   - **Code complexity**

   - **Integration effort**

#BHASIA   @BlackHatEvents

## Slide 15

### Our Approach: Inspiration

- Use AFL++ for complete WebKit application fuzzing

- Goal shifts: Port WebKit to _wasm_compile_fuzzer_ enable AFL++ with wasm generator

#BHASIA   @BlackHatEvents

## Slide 16

### Our Approach: Inspiration

- **Generator Reuse** : not only between V8 & WebKit

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR (confidence 73/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Our Approach:
* Generator Reuse: not only between V8 & WebKit
|
Type: Libs
>) Random Data CYL valid wasm data Yy Y ;
cc + Frontend |
```

## Slide 17

### Our Approach: Inspiration

- **Generator Reuse** : applicable across peer-applications

#BHASIA   @BlackHatEvents

## Slide 18

### Our Approach: Inspiration

- **Where are Peer Applications?**

   - Different JS engines/compilers

   - Similar libraries & frameworks

   - Different protocol implementations

#BHASIA   @BlackHatEvents

## Slide 19

### Our Approach: AFL++ Extractor

- An AFL++ plugin with:

   - **Concise** code

   - **Easy** usage

   - **Remarkable** results

 **GitHub:** https://github.com/P1umer/AFLplusplus-Extractor/tree/libfuzzer_extractor/utils/aflpp_extractor

#BHASIA   @BlackHatEvents

## Slide 20

### Our Approach: AFL++ Extractor

#### **1.** LibFuzzer divided into Generator and Harness logically

#BHASIA   @BlackHatEvents

## Slide 21

### Our Approach: AFL++ Extractor

**2** .  Remove the invocation of the target functions via patching.

#BHASIA   @BlackHatEvents

## Slide 22

### Our Approach: AFL++ Extractor

- **3** .  Compile libfuzzer into a shared library using **_afl-cc_** modified by AFL++ Extractor

   - Make an AFL++ custom mutator based on this shared library

#BHASIA   @BlackHatEvents

## Slide 23

### Our Approach: AFL++ Extractor

 Apply **AFL++ Extractor** to **_v8_wasm_compile_fuzzer_**

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR (confidence 79/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
ASIA 20253
Our Approach: AFL++ Extractor
v Apply AFL++ Extractor to v8_wasm_compile_fuzzer
Library: $ Original _fuzzer_name).a
piumer@w2lab-server:~/Git/Chromium/src/out/afl git:(HEAD) (0.326
file v8_wasm_compile_fuzzer
v8_wasm_compile_fuzzer: ELF 64-bit (SB shared ones
86-64, version 1 (SYSV), dynamically “tenked.B [
Hash ]=af807f0ad436b346, with debug_info, not stripped
\ J
Feedback
```

## Slide 24

### Our Approach: AFL++ Extractor

 Apply **AFL++ Extractor** to **_v8_wasm_compile_fuzzer_**

 Persistent mode

 Shared memory fuzzing

 Features update

 Different options

#BHASIA   @BlackHatEvents

## Slide 25

### Result

- **13 Security-Related Issues**

- **4 CVEs & Acknowledgements**

- **3 Tiers of Pipeline**

• **2 arch: x64 + arm64**

#BHASIA   @BlackHatEvents

## Slide 26

## Cases Study

#BHASIA   @BlackHatEvents

## Slide 27

### WebKit Wasm Compilers

**1.  LLInt** : Interpreter

**2.  B3 and Air** : Low-level optimizer,  IRGenerator

**3.  BBQ** : Fast in compiling

**4.  OMG** : Fast in executing

#BHASIA   @BlackHatEvents

## Slide 28

### WebKit Wasm Compilers

LLInt/WebAssembly.asm
wasmOp(i32_add, WasmI32Add, macro(ctx)
   mloadi(ctx, m_lhs, t0)
   mloadi(ctx, m_rhs, t1)
(module
   addi t0, t1, t2
 (func (export "add") (param i32 i32) (result i32)
local.get 0    returni(ctx, t2)
local.get 1 end)
i32.add
block (param i32) (result i32)
i32.const 1337
i32.add
end
return
 )
)

 src:  JavaScriptCore/llint/WebAssembly.asm

#BHASIA   @BlackHatEvents

## Slide 29

### WebKit Wasm Compilers

- BBQ omits many optimizations in the B3 compiler

 Ref:  《All About JavaScriptCore’s Many》- Filip Pizlo

#BHASIA   @BlackHatEvents

## Slide 30

### WebKit Wasm Compilers

- OMG uses as many optimizations as possible to generate code that executes quickly.

 Ref:  《All About JavaScriptCore’s Many》- Filip Pizlo

#BHASIA   @BlackHatEvents

## Slide 31

### CVE-2022-32863

#### Vulnerability analysis

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR (confidence 90/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
CVE-2022-32863
Vulnerability analysis
e Vulnerability exists in the BBQ Air.
e Inappropriate implementation in Wasm stackoverflow check
e Type Confusion of JSsWebAssemblyIinstance
```

## Slide 32

[0]

### CVE-2022-32863

#### Vulnerability analysis

AirIRGenerator::AirIRGenerator(...) { // [...] m_prologueGenerator = createSharedTask<B3::Air::PrologueGeneratorFunction>([=, this] (CCallHelpers& jit, B3::Air::Code& code) { // [...] { if (needsOverflowCheck) { // […] jit.addPtr(CCallHelpers::TrustedImm32(-checkSize), GPRInfo::callFrameRegister, scratch); MacroAssembler::JumpList overflow; if (UNLIKELY(needUnderflowCheck)) overflow.append(jit.branchPtr(CCallHelpers::Above, scratch, GPRInfo::callFrameRegister)); overflow.append(jit.branchPtr(CCallHelpers::Below, scratch, CCallHelpers::Address(m_prologueWasmContextGPR, Instance::offsetOfCachedStackLimit()))); jit.addLinkTask([overflow] (LinkBuffer& linkBuffer) { linkBuffer.link(overflow, CodeLocationLabel<JITThunkPtrTag>(Thunks::singleton().stub(throwStackOverflowFromWasmThunkGenerator).code())); }); } // […] if (m_catchEntrypoints.size()) { GPRReg scratch = wasmCallingConvention().prologueScratchGPRs[0]; jit.loadPtr(CCallHelpers::Address(m_prologueWasmContextGPR, Instance::offsetOfOwner()), scratch); jit.store64(scratch, CCallHelpers::Address(GPRInfo::callFrameRegister, CallFrameSlot::thisArgument * sizeof(Register))); } } }); }

[1]

 src: JavaScriptCore/wasm/WasmAirIRGenerator.cpp

#BHASIA   @BlackHatEvents

## Slide 33

### CVE-2022-32863

#### How to trigger

**1.** Exception handler exists in wasm code

**2.** Hit a StackOverflow exception : operationWasmToJSException

->genericUnwind ->Interpreter::unwind

static void visit(CallFrame* startFrame, VM& vm, const Functor& functor)
{
       StackVisitor visitor(startFrame, vm);
if (action == TerminateIfTopEntryFrameIsEmpty && visitor.topEntryFrameIsEmpty())
return;
while (visitor->callFrame()) {
           IterationStatus status = functor(visitor);
if (status != IterationStatus::Continue)
break;
visitor.gotoNextFrame();
       }
}

- ->StackVisitor::visit

 src: JavaScriptCore/interpreter/StackVisitor.h

#BHASIA   @BlackHatEvents

## Slide 34

### CVE-2022-32863

#### Vulnerability analysis

IterationStatus operator()(StackVisitor &visitor) const
{
 // [...]
#if ENABLE(WEBASSEMBLY)
 CalleeBits callee = visitor->callee();
if (callee.isCell())
 {
if (auto *jsToWasmICCallee = jsDynamicCast<JSToWasmICCallee *>(callee.asCell()))
m_vm.wasmContext.store(jsToWasmICCallee->function()->previousInstance(m_callFrame), m_vm.softStackLimit());
 }
if (m_catchableFromWasm && callee.isWasm())
 {
Wasm::Callee *wasmCallee = callee.asWasmCallee();
if (wasmCallee->hasExceptionHandlers())
   {
     JSWebAssemblyInstance *jsInstance = jsCast<JSWebAssemblyInstance *>(m_callFrame->thisValue());
unsigned exceptionHandlerIndex = m_callFrame->callSiteIndex().bits();
     m_handler = {wasmCallee->handlerForIndex(jsInstance->instance(), exceptionHandlerIndex, m_wasmTag), wasmCallee};
if (m_handler.m_valid)
return IterationStatus::Done;
   }
 }
#endif
 // [...]
}

[2]

 src: JavaScriptCore/interpreter/Interpreter.cpp

#BHASIA   @BlackHatEvents

## Slide 35

### CVE-2022-32863

#### Patch

- Setup wasm stack **|this|** first if there is exception handler in wasm

- code

diff --git a/Source/JavaScriptCore/wasm/WasmAirIRGenerator.cpp b/Source/JavaScriptCore/wasm/WasmAirIRGenerator.cpp
index 5255b8d71e21..53ca908b4949 100644
--- a/Source/JavaScriptCore/wasm/WasmAirIRGenerator.cpp
+++ b/Source/JavaScriptCore/wasm/WasmAirIRGenerator.cpp
@@ -1014,14 +1014,21 @@ AirIRGenerator::AirIRGenerator(const ModuleInformation& info, B3::Procedure& pro
            bool needUnderflowCheck = static_cast<unsigned>(checkSize) > Options::reservedZoneSize();
            bool needsOverflowCheck = m_makesCalls || wasmFrameSize >= static_cast<int32_t>(minimumParentCheckSize) ||
needUnderflowCheck;
+            if ((needsOverflowCheck || m_usesInstanceValue) && Context::useFastTLS())
+                jit.loadWasmContextInstance(m_prologueWasmContextGPR);
+
+            // We need to setup JSWebAssemblyInstance in |this| slot before checking stack overflow. Otherwise, we
will fail to get it when unwinding
+            // if we throw an error from the stack overflow check.
+            if (m_catchEntrypoints.size()) {
+                GPRReg scratch = wasmCallingConvention().prologueScratchGPRs[0];
+                jit.loadPtr(CCallHelpers::Address(m_prologueWasmContextGPR, Instance::offsetOfOwner()), scratch);
+                jit.store64(scratch, CCallHelpers::Address(GPRInfo::callFrameRegister, CallFrameSlot::thisArgument *
sizeof(Register)));
+            }
+
            // This allows leaf functions to not do stack checks if their frame size is within
            // certain limits since their caller would have already done the check.
            if (needsOverflowCheck) {
                GPRReg scratch = wasmCallingConvention().prologueScratchGPRs[0];
  // […]
                });
            }
        }
    });

 Fix: e49129f82a16a9b5ef9c951c1743a33057d07d12

#BHASIA   @BlackHatEvents

## Slide 36

### CVE-2022-32885

#BHASIA   @BlackHatEvents

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
CVE-2022-32885
e Vulnerability exists in the LLInt Parser.
e Inappropriate implementation on parsing delegate bytecode
e Break the stack frame balance/StackOverflow
```

## Slide 37

### CVE-2022-32885

#### LLInt Parser Overview

- **Wasm function** : Highly-structured

- **m_expressionStack** : Track the value of expressions

- **m_controlStack** : Stack of expression stacks

- **enclosedExpressionStack** : Store parsed expressions

#BHASIA   @BlackHatEvents

## Slide 38

### CVE-2022-32885

#### Unreachable in Wasm

- The code located behind **Br/Brtable/Return**

(module
 (func (export "add") (param i32 i32) (result i32)
local.get 0
local.get 1
i32.add
block (param i32) (result i32)
i32.const 1337
i32.add
end
return
i32.const 0xdeadbeef
i32.add
return
 )
)

#BHASIA   @BlackHatEvents

## Slide 39

### CVE-2022-32885

#### Delegate in Wasm

- **Delegate(label_x)** :

- handle over exception handling to label_x

(module
try $l0
try
call $foo
delegate $l0 ;; (= delegate 0)
catch
...
catch_all
...
end
)

 Ref: wasm exception-handling

#BHASIA   @BlackHatEvents

## Slide 40

### CVE-2022-32885

#### Vulnerability analysis

- **parseUnreachableExpression** : parse expressions when encountering unreachable blocks

template<typename Context>
auto FunctionParser<Context>::parseUnreachableExpression() -> PartialResult
{
ASSERT(m_unreachableBlocks);
#define CREATE_CASE(name, ...) case OpType::name:
switch (m_currentOpcode) {
     // [...]
case End: {
if (m_unreachableBlocks == 1) {
           ControlEntry data = m_controlStack.takeLast();
if (ControlType::isIf(data.controlData)) {
WASM_TRY_ADD_TO_CONTEXT(addElseToUnreachable(data.controlData));
               m_expressionStack = WTFMove(data.elseBlockStack);
WASM_FAIL_IF_HELPER_FAILS(unify(data.controlData));
WASM_TRY_ADD_TO_CONTEXT(endBlock(data, m_expressionStack));
           } else {
               Stack emptyStack;
WASM_TRY_ADD_TO_CONTEXT(addEndToUnreachable(data, emptyStack));
           }
m_expressionStack.swap(data.enclosedExpressionStack);
       }
       m_unreachableBlocks--;
return { };
   }
   // [...]
   }
}

 <u>src: JavaScriptCore/wasm/WasmFunctionParser.h</u>

#BHASIA   @BlackHatEvents

## Slide 41

### CVE-2022-32885

#### Vulnerability analysis

• Delegate operator should be handled the same way as the End operator : try … end

v.s. try … delegate x

template <typename Context>
auto FunctionParser<Context>::parseUnreachableExpression() -> PartialResult
{
ASSERT(m_unreachableBlocks);
#define CREATE_CASE(name, ...) case OpType::name:
switch (m_currentOpcode)
 {
 // [...]
case Delegate:
 {
WASM_PARSER_FAIL_IF(!Options::useWebAssemblyExceptions(), "wasm exceptions are not enabled");
WASM_PARSER_FAIL_IF(m_controlStack.size() == 1, "can't use delegate at the top-level of a function");
uint32_t target;
WASM_FAIL_IF_HELPER_FAILS(parseBranchTarget(target));
   ControlEntry controlEntry = m_controlStack.takeLast();
WASM_VALIDATOR_FAIL_IF(!ControlType::isTry(controlEntry.controlData), "delegate isn't associated to a
try");
   ControlType &data = m_controlStack[m_controlStack.size() - 1 - target].controlData;
WASM_VALIDATOR_FAIL_IF(!ControlType::isTry(data) && !ControlType::isTopLevel(data), "delegate target is-
n't a try block");
WASM_TRY_ADD_TO_CONTEXT(addDelegateToUnreachable(data, controlEntry.controlData));
   Stack emptyStack;
WASM_TRY_ADD_TO_CONTEXT(addEndToUnreachable(controlEntry, emptyStack));
m_expressionStack.swap(controlEntry.enclosedExpressionStack);
return {};
 }
   // [...]
 }
}

 <u>src: JavaScriptCore/wasm/WasmFunctionParser.h</u>

#BHASIA   @BlackHatEvents

## Slide 42

### CVE-2022-32885

#### POC

• Add a Delegate statement after unreachable code.

[1]
[2]

(module
 (type $t0 (func (param i32 i32 i32) (result i32)))
 (type $t1 (func))
 (func $main (export "main") (type $t0) (param $p0 i32) (param $p1 i32) (param $p2 i32) (result i32)
   (local $l3 f64)
   (try ;; label = @1
     (do
       (try ;; label = @2
         (do
           (try ;; label = @3
             (do
               (drop
                 (call $main
                   (i32.mul
                     (i32.const 0)
                     (i32.const 0))
                   (i32.const 0)
                   (i32.const 0))))
             (catch $e0)
             (catch_all))
           (br 0 (;@2;)))
         (delegate 0)))
     (catch_all))
   (i32.const 0))
 (table $T0 1 2 funcref)
 (memory $M0 16 32)
 (tag $e0 (type $t1))
 (global $g0 (mut i64) (i64.const 0))
 (elem $e0 (i32.const 0) func $main))

#BHASIA   @BlackHatEvents

## Slide 43

### CVE-2022-32885

#### Vulnerability analysis

- parseUnreachableExpression was mistakenly used while parsing the CatchAll operator

template<typename Context>
auto FunctionParser<Context>::parseBody() -> PartialResult
{
m_controlStack.append({ { }, { }, m_context.addTopLevel(&m_signature) });
uint8_t op = 0;
while (m_controlStack.size()) {
       // [...]
if (m_unreachableBlocks)
WASM_FAIL_IF_HELPER_FAILS(parseUnreachableExpression());
else {
WASM_FAIL_IF_HELPER_FAILS(parseExpression());
       }
   }
WASM_FAIL_IF_HELPER_FAILS(m_context.endTopLevel(&m_signature, m_expressionStack));
ASSERT(op == OpType::End);
return { };
}

 <u>src: JavaScriptCore/wasm/WasmFunctionParser.h</u>

#BHASIA   @BlackHatEvents

## Slide 44

### CVE-2022-32885

#### Vulnerability analysis

- In normal case, a pass-jmp instruction

- will be emitted

template <typename Context>
auto FunctionParser<Context>::parseExpression() -> PartialResult
{
switch (m_currentOpcode)
 {
 // [...]
case CatchAll:
 {
   // [...]
   ResultList results;
   Stack preCatchStack;
m_expressionStack.swap(preCatchStack);
WASM_TRY_ADD_TO_CONTEXT(addCatchAll(preCatchStack, controlEntry.con-
trolData));
return {};
 }
   // [...]
 }
}
auto LLIntGenerator::addCatchAll(Stack& expressionStack, ControlType& data) ->
PartialResult
{
finalizePreviousBlockForCatch(data, expressionStack);
WasmJmp::emit(this, data.m_continuation->bind(this));
return addCatchAllToUnreachable(data);
}

 <u>src: JavaScriptCore/wasm/WasmFunctionParser.h</u>

#BHASIA   @BlackHatEvents

## Slide 45

### CVE-2022-32885

#### Vulnerability analysis

- Under the vulnerability, it won’t

- emit such instruction and will fall into CatchAll’s handler code directly

template <typename Context>
auto FunctionParser<Context>::parseUnreachableExpression() -> PartialResult
{
ASSERT(m_unreachableBlocks);
#define CREATE_CASE(name, ...) case OpType::name:
switch (m_currentOpcode)
 {
 // [...]
case CatchAll:
 {
WASM_PARSER_FAIL_IF(!Options::useWebAssemblyExceptions(), "wasm exceptions are not enabled");
if (m_unreachableBlocks > 1)
return {};
   ControlEntry &data = m_controlStack.last();
   m_unreachableBlocks = 0;
   m_expressionStack = {};
WASM_VALIDATOR_FAIL_IF(!isTryOrCatch(data.controlData), "catch block isn't associated to a
try");
WASM_TRY_ADD_TO_CONTEXT(addCatchAllToUnreachable(data.controlData));
return {};
 }
   // [...]
 }
}

 <u>src: JavaScriptCore/wasm/WasmFunctionParser.h</u>

#BHASIA   @BlackHatEvents

## Slide 46

### CVE-2022-32885

#### Patch

- Handle control stack in the same way

- as the End opcode

- Decrement m_unreachableBlocks in the same way as the End opcode

diff --git a/Source/JavaScriptCore/wasm/WasmFunctionParser.h b/Source/JavaScriptCore/wasm/WasmFunctionParser.h
index f74c800c923f..edad1bb01f6b 100644
--- a/Source/JavaScriptCore/wasm/WasmFunctionParser.h
+++ b/Source/JavaScriptCore/wasm/WasmFunctionParser.h
    FunctionParser(Context&, const uint8_t* functionStart, size_t functionLength, const TypeDefinition&, const ModuleInformation& );
@@ -1728,16 +1729,19 @@ auto FunctionParser<Context>::parseUnreachableExpression() -> PartialResult
        uint32_t target;
        WASM_FAIL_IF_HELPER_FAILS(parseBranchTarget(target));
-        ControlEntry controlEntry = m_controlStack.takeLast();
-        WASM_VALIDATOR_FAIL_IF(!ControlType::isTry(controlEntry.controlData), "delegate isn't associated to a try");
+        if (m_unreachableBlocks == 1) {
+            ControlEntry controlEntry = m_controlStack.takeLast();
+            WASM_VALIDATOR_FAIL_IF(!ControlType::isTry(controlEntry.controlData), "delegate isn't associated to a try");
-        ControlType& data = m_controlStack[m_controlStack.size() - 1 - target].controlData;
-        WASM_VALIDATOR_FAIL_IF(!ControlType::isTry(data) && !ControlType::isTopLevel(dat a), "delegate target isn't a try block");
+            ControlType& data = m_controlStack[m_controlStack.size() - 1 - target].controlData;
+            WASM_VALIDATOR_FAIL_IF(!ControlType::isTry(data) && !ControlType::isTopLevel(data), "delegate target isn't a try block");
-        WASM_TRY_ADD_TO_CONTEXT(addDelegateToUnreachable(data, controlEntry.controlData));
-        Stack emptyStack;
-        WASM_TRY_ADD_TO_CONTEXT(addEndToUnreachable(controlEntry, emptyStack));
-        m_expressionStack.swap(controlEntry.enclosedExpressionStack);
+            WASM_TRY_ADD_TO_CONTEXT(addDelegateToUnreachable(data, controlEntry.controlData));
+            Stack emptyStack;
+            WASM_TRY_ADD_TO_CONTEXT(addEndToUnreachable(controlEntry, emptyStack));
+            m_expressionStack.swap(controlEntry.enclosedExpressionStack);
+        }
+        m_unreachableBlocks--;
        return { };
    }

 Fix:  27d302ab3481407e8746f57729f0961058235e33

#BHASIA   @BlackHatEvents

## Slide 47

### CVE-2022-32886

- BBQ & OMG

- Uninitialized value in callSiteIndex

- Wrong exception handler

#BHASIA   @BlackHatEvents

## Slide 48

### CVE-2022-32886

#### Callsite Index

- Used for exception handler

- Store the position of Call/Try/Catch/Throw

- StackMap : keep callsite_index and used_values  key-value pair

#BHASIA   @BlackHatEvents

## Slide 49

### CVE-2022-32886

#### Vulnerability analysis

- The handle is initialized only when the call instruction is enclosed within a try-catch block [1]

PatchpointExceptionHandle B3IRGenerator::preparePatchpointForExceptions(BasicBlock* block, PatchpointValue* patch)
{
   ++m_callSiteIndex;
if (!m_tryCatchDepth)
return { };
   Vector<Value*> liveValues;
   Origin origin = this->origin();
for (Variable* local : m_locals) {
       Value* result = block->appendNew<VariableValue>(m_proc, B3::Get, origin, local);
liveValues.append(result);
   }
for (unsigned controlIndex = 0; controlIndex < m_parser->controlStack().size(); ++controlIndex) {
       ControlData& data = m_parser->controlStack()[controlIndex].controlData;
       Stack& expressionStack = m_parser->controlStack()[controlIndex].enclosedExpressionStack;
for (Variable* value : expressionStack)
liveValues.append(get(block, value));
if (ControlType::isAnyCatch(data))
liveValues.append(get(block, data.exception()));
   }
patch->effects.exitsSideways = true;
patch->appendVectorWithRep(liveValues, ValueRep::LateColdAny);
return PatchpointExceptionHandle { m_callSiteIndex, static_cast<unsigned>(liveValues.size()) };
}

[2]

 src: JavaScriptCore/wasm/WasmB3IRGenerator.cpp

#BHASIA   @BlackHatEvents

## Slide 50

### CVE-2022-32886

#### Vulnerability analysis

- BBQ and OMG will ultimately call the generate function to get the optimized code [3]

[3]

- The generate function omits the storing operation. The callsite index isn’t kept neither in slot nor in stack map

[4]

struct PatchpointExceptionHandle {

template <typename Generator> void generate(CCallHelpers& jit, const B3::StackmapGenerationParams& params, Generator* generator) const {

if (m_callSiteIndex == s_invalidCallSiteIndex) return;

StackMap values(m_numLiveValues); unsigned paramsOffset = params.size() - m_numLiveValues; unsigned childrenOffset = params.value()->numChildren() - m_numLiveValues; for (unsigned i = 0; i < m_numLiveValues; ++i)

values[i] = OSREntryValue(params[i + paramsOffset], params.value()->child(i + childrenOffset)->type());

generator->addStackMap(m_callSiteIndex, WTFMove(values));

jit.store32(CCallHelpers::TrustedImm32(m_callSiteIndex), CCallHelpers::tagFor(CallFrameSlot::argumentCountIncludingThis)); }

static constexpr unsigned s_invalidCallSiteIndex = std::numeric_limits<unsigned>::max();

unsigned m_callSiteIndex { s_invalidCallSiteIndex }; unsigned m_numLiveValues; }

 src: JavaScriptCore/wasm/WasmIRGeneratorHelpers.h

#BHASIA   @BlackHatEvents

## Slide 51

### CVE-2022-32886

#### Vulnerability analysis

- This results in an incorrect handler due to the presence of a dirty value

IterationStatus operator()(StackVisitor &visitor) const
{
 // [...]
#if ENABLE(WEBASSEMBLY)
 CalleeBits callee = visitor->callee();
if (callee.isCell())
 {
if (auto *jsToWasmICCallee = jsDynamicCast<JSToWasmICCallee *>(callee.asCell()))
m_vm.wasmContext.store(jsToWasmICCallee->function()->previousInstance(m_callFrame), m_vm.softStackLimit());
 }
if (m_catchableFromWasm && callee.isWasm())
 {
Wasm::Callee *wasmCallee = callee.asWasmCallee();
if (wasmCallee->hasExceptionHandlers())
   {
     JSWebAssemblyInstance *jsInstance = jsCast<JSWebAssemblyInstance *>(m_callFrame->thisValue());
unsigned exceptionHandlerIndex = m_callFrame->callSiteIndex().bits();
     m_handler = {wasmCallee->handlerForIndex(jsInstance->instance(), exceptionHandlerIndex, m_wasmTag), wasmCallee};
if (m_handler.m_valid)
return IterationStatus::Done;
   }
 }
#endif
 // [...]
}

[5]

 src: JavaScriptCore/interpreter/Interpreter.cpp

#BHASIA   @BlackHatEvents

## Slide 52

### CVE-2022-32886

#### Vulnerability analysis

- Before executing error-handling

- code, the stack map is obtained by calling  the buildEntryBufferForCatch function.

static inline void buildEntryBufferForCatch(Probe::Context& context) { CallFrame* callFrame = context.fp<CallFrame*>(); CallSiteIndex callSiteIndex = callFrame->callSiteIndex(); OptimizingJITCallee* callee = bitwise_cast<OptimizingJITCallee*>(callFrame->callee().asWasmCallee()); const StackMap& stackmap = callee->stackmap(callSiteIndex); VM* vm = context.gpr<VM*>(GPRInfo::regT0); uint64_t* buffer = vm->wasmContext.scratchBufferForSize(stackmap.size() * 8); loadValuesIntoBuffer(context, stackmap, buffer); context.gpr(GPRInfo::argumentGPR0) = bitwise_cast<uintptr_t>(buffer); }

 src: JavaScriptCore/wasm/WasmIRGeneratorHelpers.h

#BHASIA   @BlackHatEvents

## Slide 53

### CVE-2022-32886

#### Vulnerability analysis

- Since the key-value pair was not stored, an assert failure is triggered

const StackMap& OptimizingJITCallee::stackmap(CallSiteIndex callSiteIndex) const
{
auto iter = m_stackmaps.find(callSiteIndex);
if (iter == m_stackmaps.end()) {
for (auto pair : m_stackmaps) {
dataLog(pair.key.bits(), ": ");
for (auto value : pair.value)
dataLog(value, ", ");
dataLogLn("");
       }
   }
RELEASE_ASSERT(iter != m_stackmaps.end());
return iter->value;
}

 src: JavaScriptCore/wasm/WasmCallee.cpp

#BHASIA   @BlackHatEvents

## Slide 54

### CVE-2022-32886

#### Patch

• Store CallSiteIndex for calls in Air and B3 if there are exception handlers<sup>present</sup>

diff --git a/Source/JavaScriptCore/wasm/WasmIRGeneratorHelpers.h b/Source/JavaScriptCore/wasm/WasmIRGeneratorHelpers.h index bfb21da023ad..21d5eda6ed4e 100644 --- a/Source/JavaScriptCore/wasm/WasmIRGeneratorHelpers.h +++ b/Source/JavaScriptCore/wasm/WasmIRGeneratorHelpers.h @@ -40,11 +40,24 @@ namespace JSC { namespace Wasm { struct PatchpointExceptionHandle { template <typename Generator> void generate(CCallHelpers& jit, const B3::StackmapGenerationParams& params, Generator* generator) const { -        if (m_callSiteIndex == s_invalidCallSiteIndex) +        if (m_callSiteIndex == s_invalidCallSiteIndex) { +            if (!m_hasExceptionHandlers || m_hasExceptionHandlers.value()) +                jit.store32(CCallHelpers::TrustedImm32(m_callSiteIndex), CCallHelpers::tagFor(CallFrameSlot::argumentCountIncludingThis)); return; +        }

};

 Fix:  97b340447c9fc3e934a8045e059b3fac71e0ab4d

#BHASIA   @BlackHatEvents

## Slide 55

### Q & A

#BHASIA   @BlackHatEvents

## Slide 56

### Thanks

Feel free to contact us at @P1umer and @xmzyshypnc1 in Twitter

#BHASIA   @BlackHatEvents

## Companion resources

### `AS-23-Cao-Attacking-WebAssembly-Compiler-of-Webkit_tools.txt`

```text
https://github.com/P1umer/AFLplusplus-Extractor/tree/libfuzzer_extractor/utils/aflpp_extractor
```
