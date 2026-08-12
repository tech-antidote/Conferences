---
title: "The V8 Heap Sandbox"
speakers: ["Samuel Groß"]
conference: "OffensiveCon"
conference_full: "OffensiveCon 2024"
edition: ""
year: 2024
source_pdf: "OffensiveCon24 slides/Samuel Groß_The V8 Heap Sandbox.pdf"
pages: 41
sha256: "1c606be44ad2528b06556d3138b1bb0851afd495ac55995768bb13c3df96e682"
text_chars: 7538
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T23:21:46Z"
---
# The V8 Heap Sandbox

**Speakers:** Samuel Groß  
**Conference:** OffensiveCon 2024  
**Source:** `OffensiveCon24 slides/Samuel Groß_The V8 Heap Sandbox.pdf` (41 pages)


## Slide 1

# The V8 Heap Sandbox OffensiveCon 2024

Samuel Groß - Google V8 Security

## Slide 2

Typical Exploit Flow
Arbitrary  Code
Memory
V8 Bug Memory Execution
Corruption
Read & Write (in Renderer)
Code
Chrome
Execution …
Sandbox Bug
(Unsandboxed)

## Typical Exploit Flow

## Slide 3

Typical Exploit Flow
Arbitrary  Code
Memory
V8 Bug Memory Execution
Corruption
Read & Write (in Renderer)
V8 Sandbox
Code
Chrome
Execution …
Sandbox Bug
(Unsandboxed)

## Typical Exploit Flow

## Slide 4

## Why JavaScript Engine Security is hard

“Typical” Application
Attacker controlled
Data
Code
Compiler + Runtime Memory safety (can be) guaranteed here
Hardware

## Slide 5

## Why JavaScript Engine Security is hard

JavaScript Engine
Attacker controlled Data
Code
Compiler + Runtime
This is direct attack surface
=> Cannot guarantee memory safety here
Hardware

## Slide 6

## Why JavaScript Engine Security is hard

- Compiler-based memory safety doesn’t work if compiler is attack surface

   - => Any logic bug can potentially turn into memory corruption

- Disabling optional compilers solves only a part of the problem

   - Plenty of bugs elsewhere (e.g. runtime) …

   - … and it is very slow :(

- => Writing a high-performance, memory-safe JS engine is **hard**

## Slide 7

High-performance, memory-safe JavaScript engine?

**Write Bug Free Code**

Big, hard problem

## Slide 8

## A different approach…

Idea:

- Accept that bugs will happen and that memory will be Can corrupt

- corrupted memory here

- ● Limit which memory can be corrupted

“Privileged” Address Space

V8 Sandbox

- Make that a security boundary

- => Result: an in-process sandbox

“Privileged” Address Space

## Slide 9

Higher Addresses 0xa48000000000

**V8 Sandbox (1TB)**

0xa38000000000

Lower Addresses

## Slide 10

Higher Addresses 0xa48000000000

**V8 Sandbox (1TB)** HeapObj1 HeapObj2

0xa38000000000

Lower Addresses

## Slide 11

Higher
Addresses
V8 Sandbox (1TB)
HeapObj1
HeapObj2 Raw pointer
Lower
Addresses

Higher Addresses 0xa48000000000

0xa38000000000

Lower Addresses

## Slide 12

V8 Sandbox (1TB)
HeapObj1
HeapObj2 Offset from sandbox base

Higher Addresses 0xa48000000000

0xa38000000000

Lower Addresses

## Slide 13

V8 Sandbox (1TB)
HeapObj1
HeapObj2 Offset from sandbox base
External
Object

Higher Addresses 0xa48000000000

0xa38000000000

Lower Addresses

## Slide 14

V8 Sandbox (1TB)
HeapObj1
HeapObj2 Offset from sandbox base
External
Object

Higher Addresses 0xa48000000000

0xa38000000000

Lower Addresses

## Slide 15

Higher
Addresses
0xa48000000000
V8 Sandbox (1TB)
HeapObj1
HeapObj2 Offset from sandbox base
Index
0xa38000000000
External Ptr Table
External
0 Type + Pointer
Object
Lower
1 Type + Pointer Addresses

## Slide 16

Higher
Addresses
0xa48000000000
V8 Sandbox (1TB)
HeapObj1
HeapObj2 Offset from sandbox base
Index
0xa38000000000
External Ptr Table
External
0 Type + Pointer
Object
Lower
1 Type + Pointer Addresses
Basically: ban all raw pointers!

## Slide 17

## Sandbox with Hardware Support?

- In the future, may be possible to “drop privileges” when executing JS or Wasm code

- Would be very similar to userspace/kernel split

- Ideally: want to be able to run untrusted _machine code_

## Slide 18

High-performance, memory-safe JavaScript engine! (with a sandbox)

Lots of smaller, simpler problems

## Slide 19

Performance

## Slide 20

## Performance

- Sandbox building blocks are fundamentally cheap

   - Offsets require just an additional add or shift+add instruction

   - Pointer table requires one additional memory load for external references

- => Benefit over other memory safety technologies

- Today: overhead of sandbox is only around 1% on popular benchmarks

   - => Can be (and is already) enabled by default!

Sandboxification (x28 always contains the sandbox base) ldr x3, [x0, #7] ldr x3, [x0, #7] add x3, x28, x3, lsr #24

## Slide 21

Untrusted Indices

## Slide 22

## Untrusted Indices

Tagged<MyHeapObject> obj = ...; int idx = obj->get_the_index(); int val = obj->get_the_value(); some_global_array[idx] = val;

## Slide 23

## Untrusted Indices

Tagged<MyHeapObject> obj = ...; **uint** idx = obj->get_the_index(); int val = obj->get_the_value(); **SBXCHECK(idx < some_global_array_size);** some_global_array[idx] = val;

## Slide 24

Broken Invariants

## Slide 25

## Broken Invariants

std::vector<std::string> JSObject::GetPropertyNames() { int num_properties = TotalNumberOfProperties(); std::vector<std::string> properties(num_properties); for (int i = 0; i < NumberOfInObjectProperties(); i++) { properties[i] = GetNameOfInObjectProperty(i); }

// Deal with the other types of properties // ...

## Slide 26

## Broken Invariants

std::vector<std::string> JSObject::GetPropertyNames() { int num_properties = TotalNumberOfProperties(); std::vector<std::string> properties(num_properties); for (int i = 0; i < NumberOfInObjectProperties(); i++) { **SBXCHECK(i < properties.size());** properties[i] = GetNameOfInObjectProperty(i); }

// Deal with the other types of properties // ...

## Slide 27

Sandbox CFI

## Slide 28

## Sandbox CFI

- Obvious: machine code cannot be inside the sandbox

   - => Move out of the sandbox

## Slide 29

## Sandbox CFI

- Obvious: machine code cannot be inside the sandbox

   - => Move out of the sandbox

- Obvious: cannot have raw pointers to machine code inside the sandbox

   - => Use code pointer table indirection (essentially a form of CFI)

## Slide 30

## Sandbox CFI

- Obvious: machine code cannot be inside the sandbox

   - => Move out of the sandbox

- Obvious: cannot have raw pointers to machine code inside the sandbox

   - => Use code pointer table indirection (essentially a form of CFI)

- Less obvious: code metadata cannot be inside the sandbox

   - Can e.g. lead to code corruption when manipulated

   - => Move out of the sandbox

## Slide 31

## Sandbox CFI

- Obvious: machine code cannot be inside the sandbox

   - => Move out of the sandbox

- Obvious: cannot have raw pointers to machine code inside the sandbox

   - => Use code pointer table indirection (essentially a form of CFI)

- Less obvious: code metadata cannot be inside the sandbox

   - Can e.g. lead to code corruption when manipulated

   - => Move out of the sandbox

- Less obvious: interpreter bytecode cannot be in the sandbox

   - Causes stack corruption if manipulated

   - => Move out of sandbox and also reference via a pointer table

## Slide 32

0xa48000000000
V8 Sandbox (e.g. 1TB)
HeapObj1
HeapObj3
HeapObj2
0xa38000000000
External Ptr Table Code Ptr Table
Trusted Ptr Table
0 Type + Pointer 0 Pointer
0 Type + Pointer
1 Type + Pointer 1 Pointer
1 Type + Pointer
V8 Code Space
JIT Code
Code  V8 Trusted Space Bytecode
Metadata
Pointer
Blink Heap Offset
Blink Object Index

## Slide 33

Wasm
Func

## Sandbox CFI

Func
JS
Callsite
JS
Func

And more subtle issues in this area:

   - Calling convention/signature mismatch

   - ● Deoptimization and tier-up

   - ● Desynchronized code references

   - …

- => Still work to do in this area

## Slide 34

Testing

## Slide 35

## Testing

- Sandbox is _testable_

   - Clear attacker model + tools to develop and validate sandbox bypasses

- This enables:

   - automatic fuzzing

   - ability to write regression tests

   - inclusion in Chrome’s bug bounty program (active since March 2024)

let memory = new Sandbox.MemoryView(0, kSize); let dv = new DataView(memory);

// Full read+write to sandbox address space dv.setUint8(0x41414141, 0x42);

## Slide 36

Demo

## Slide 37

## Slide 38

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
v8/v8 lain) fout/*64,sbxtst/d6 Sancbox-testing poc.js §
```

## Slide 39

## Conclusion

Sandbox increases length of (typical) V8-based Chrome exploit chain

V8 Chrome
V8
Bug Sandbox Bug Sandbox Bug

Key question: how hard is this new attack surface?

… Only one way to find out: build it, then see what happens :)

## Slide 40

## Resources

- Blog post: <u>v8.dev/blog/sandbox</u>

- README: <u>src/sandbox/README.md</u>

- Past sandbox bugs: <u>v8-sandbox buganizer hotlist</u>

- Sandbox VRP rules: <u>g.co/chrome/vrp/#v8-sandbox-bypass-rewards</u>

## Slide 41

Questions?
