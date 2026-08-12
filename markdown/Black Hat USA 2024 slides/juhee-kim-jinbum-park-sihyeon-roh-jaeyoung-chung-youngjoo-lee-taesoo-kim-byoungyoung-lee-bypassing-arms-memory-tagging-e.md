---
title: "Bypassing ARM's Memory Tagging Extension with a Side-Channel Attack"
speakers: ["Juhee Kim", "Jinbum Park", "Sihyeon Roh", "Jaeyoung Chung", "Youngjoo Lee", "Taesoo Kim", "Byoungyoung Lee"]
conference: "Black Hat"
conference_full: "Black Hat USA 2024"
edition: "USA"
year: 2024
source_pdf: "Black Hat USA 2024 slides/Juhee Kim & Jinbum Park & Sihyeon Roh & Jaeyoung Chung & Youngjoo Lee & Taesoo Kim & Byoungyoung Lee_Bypassing ARM's Memory Tagging Extension with a Side-Channel Attack.pdf"
pages: 68
sha256: "525043b1fd082cd504fc966142f53ab70bcbe17eb17d63a2569a62d374988fa3"
text_chars: 17857
ocr_pages: 3
has_ocr: true
redacted_secrets: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T00:47:57Z"
---
# Bypassing ARM's Memory Tagging Extension with a Side-Channel Attack

**Speakers:** Juhee Kim, Jinbum Park, Sihyeon Roh, Jaeyoung Chung, Youngjoo Lee, Taesoo Kim, Byoungyoung Lee  
**Conference:** Black Hat USA 2024  
**Source:** `Black Hat USA 2024 slides/Juhee Kim & Jinbum Park & Sihyeon Roh & Jaeyoung Chung & Youngjoo Lee & Taesoo Kim & Byoungyoung Lee_Bypassing ARM's Memory Tagging Extension with a Side-Channel Attack.pdf` (68 pages)

## Slide 1

Bypassing ARM's Memory Tagging Extension with a Side-Channel Attack

Speaker: Juhee Kim

#BHUSA @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
| 4a
blackhat os
USA 2024
AUGUST 7-8, 2024
Bypassing ARM's Memory Tagging
Extension with a Side-Channel Attack
Speaker: Juhee Kim
```

## Slide 2

#### Whoami

###### Juhee Kim

Ph.D Student  at CompSec Lab, Seoul National University <u>kimjuhi96@snu.ac.kr</u>

###### Focuses on

- Software and Systems security - Bug finding, Attack mitigation

- Linux kernel, Web browser, GPU/ML systems

2

## Slide 3

#### Contributors

###### Jinbum Park

- Security researcher at Samsung Research

- System security, Confidential Computing

- Published in USENIX Security and ASPLOS

###### Sihyeon Roh

- Ph.D Student at CompSec Lab

- Hardware side-channels

###### Jaeyoung Chung

- Ph.D Student at CompSec Lab

- System Security

- CTF player

###### Youngjoo Lee

- Ph.D Student at CompSec Lab

- • Fuzzing, Browser security, Bug gounty

- CTF player

###### Taesoo Kim

- Vice president of Samsung Research Professor of Georgia Tech

• Won several best paper awards from USENIX Security, EuroSys

###### Byoungyoung Lee

- Professor of Seoul National University

- Leads CompSec Lab

- System security, Confidential computing

- • Previous CTF player

- Spoken at Black Hat

3

## Slide 4

#### Roadmap

ARM Memory
Tagging Extension

Real-world
MTE Bypass Attack
MTE
JS

Cache  Speculative
Side-Channel Execution
Cache if (cond)
True False
MTE Tag Leakage
Side-Channel
MTE

4

## Slide 5

#### Roadmap

ARM Memory
Tagging Extension

Cache  Speculative
Side-Channel Execution
Cache if (cond)
True False

Real-world MTE Bypass Attack

MTE
JS

MTE Tag Leakage Side-Channel

MTE

5

## Slide 6

Memory corruption attacks have been the most pervasive and dangerous security threats Heartbleed (2014) Bad Binder (2019) OpenSSL information leak

reggreSSHion (2024)

BLASTPASS (2023)

6

## Slide 7

#### What is Memory Corruption?

Invalid Access
Valid Access
(Out-of-bounds)
Pointer Memory Pointer Memory
&obj1 &obj2
obj1 obj1
obj2

7

## Slide 8

#### What is Memory Corruption?

Invalid Access
Valid Access
(Use-after-free)
Pointer Memory Pointer Memory
&obj1 &obj1
obj1 Freed

8

## Slide 9

#### Attack and Defense Techniques

70s-80s 90s 2000s 2010s 2020s
DOP
ROP/JOP
Stack  Heap
Overflow Overflow
JIT spraying Spectre
ARM PAC
DEP/NX CFI
Stack Canaries
ARM MTE
StackGuard
Intel MPK
ASLR
9

## Slide 10

Google Pixel 8 / 8 pro — First MTE hardware released in Sep. 2023

- _“_ **_MTE_** _being one_ **_key_** _feature that is delivering_ **_secure mobile experiences_** _”_

- _Arm (Feb 2023)_

- _“_ **_MTE_** _is still by far the most promising path forward for improving C/C++ software security” - Google Project Zero (Aug 2023)_

- _“_ **_Memory tagging_** _has the potential to provide good value both for_ **_discovering vulnerabilities_** _and as_ **_a mitigation for vulnerabilities_** _” - Microsoft (Mar 2020)_

10

## Slide 11

## Why is MTE so Special? Hardware-based Memory Corruption Detection Fast and Compatible

11

## Slide 12

#### ARM Memory Tagging Extensions

Memory
Pointer
Valid
Address
obj1
Memory
Invalid
Pointer Tag
Tag
obj2
(Key)
(Lock)
obj3

12

## Slide 13

#### (1) Memory Tag

###### **Dedicated memory region stores a 4-bit tag per 16-byte data**

Memory Tag
(Lock)
Data Tag
obj1
obj2
obj3

13

## Slide 14

#### (2) Pointer Tag

**Pointer** Address **Pointer Tag (Key)**

**A pointer stores a 4-bit tag in its unused space**

14

## Slide 15

#### (3) Tag Allocation

**New instructions to create a random tag and load/store memory tags**

Pointer Data Tag
&obj1
obj1
&obj2
obj2
&obj2
obj3
…

15

## Slide 16

(4) Tag Check
Transparently done by hardware
Valid memory access Invalid memory access
Pointer
Data
Tag Pointer
Data Tag
&obj1
&obj2
obj1
obj1
obj2
Tag check
Tag check
No Fault
Tag Check Fault
Crash

16

## Slide 17

#### How to Bypass MTE?

**(1) Tag Collision (16 possible tags) Wait until the pointer tag matches the target memory tag**

Pointer Data Tag
&obj2
obj1
obj2
Tag check
Match

17

## Slide 18

#### How to Bypass MTE?

###### **(2) Pointer Tag Corruption Corrupt the pointer tag to the target memory tag**

Pointer Data Tag
&obj 21
obj1
obj2
Tag check
Match

18

## Slide 19

#### Challenge: Random Tags

Pointer Data Tag
ptr &obj2
obj1
obj2
Tag check
Match  ⇒ Attack Succeeds 1/16 (6%)
Mismatch
⇒ Attack Fails 15/16 (94%)
Crash

19

## Slide 20

# MTE Bypass Requirement **A Reliable way to leak MTE tag of any address**

20

## Slide 21

# Approach

- **Leak tag check result from Cache Side-channel** - **Exploit Speculative Execution to avoid crash**

21

## Slide 22

#### Roadmap

###### ARM Memory Tagging Extension

###### Real-world MTE Bypass Attack

MTE
JS

Cache  Speculative
Side-Channel Execution
Cache if (cond)
True False
MTE Tag Leakage
Side-Channel
MTE

22

## Slide 23

#### What is Cache?

CPU
Cache
Memory

23

## Slide 24

#### What is Cache?

First Access : Slow Second Access : Fast
CPU CPU
Load(ptr); ptr &obj ptr &obj
val obj val obj
Fast
Cache Cache
Cached Cached
obj obj
Slow
Memory
obj

24

## Slide 25

#### Cache Side-Channel

CPU
Q. Has obj been accessed?
ptr &obj
obj
Load(ptr); Fast
Cache
Cached ?
obj

###### **A. ptr has been accessed!**

25

## Slide 26

#### What is Cache Side-Channel?

CPU

Q. Has obj been accessed?
ptr &obj
obj
Load(ptr); Slow
Cache
Not
?
obj
Cached
A. ptr has NOT been  Memory
accessed!
obj

26

## Slide 27

#### Exploit cache side-channel è Leak whether an address is accessed

27

## Slide 28

#### Roadmap

###### ARM Memory Tagging Extension

###### Real-world MTE Bypass Attack

MTE
JS

Cache  Speculative
Side-Channel Execution
Cache if (cond)
False
MTE Tag Leakage
Side-Channel
MTE

28

## Slide 29

#### What is Speculative Execution?

CPU
ptr &obj
… ≈
if (cond) {
v = Load(ptr);
…
Cache
}

29

## Slide 30

#### What is Speculative Execution?

CPU
ptr &obj
… cond Unknown≈
if (cond) {
Waiting until  cond  is ready
v = Load(ptr);
Huge resource waste!
…
Cache
}

30

## Slide 31

#### What is Speculative Execution?

CPU
Evaluated Speculated
ptr &obj
…
cond Not ready True
if (cond) {
Speculate cond
v = Load(ptr);
…
Cache
}

31

## Slide 32

#### What is Speculative Execution?

CPU
Evaluated Speculated
ptr &obj
…
cond Not ready True
if (cond) {
Tag
Check
v = Load(ptr); Match
…
Cache
}
obj

32

## Slide 33

#### What is Speculative Execution?

###### CPU

Evaluated Speculated
ptr &obj
…
cond Not ready True
if (cond) {
v obj
v = Load(ptr);
…
Cache
}
obj

33

## Slide 34

#### What is Speculative Execution?

###### CPU

Evaluated Speculated
ptr &obj
…
cond True True Confirm True
if (cond) {
v
obj Changesobj
Correct Speculation
v = Load(ptr);
…
Cache
Continue
}
Execution
obj

34

## Slide 35

#### What is Speculative Execution?

CPU
Evaluated Speculated
ptr &obj
…
Revert
cond False True
if (cond) { Discard
Execution
v
Changes
obj
Wrong Speculation
v = Load(ptr);
…
Cache
Revert
}
Execution
obj
Does not Revert Cache

35

## Slide 36

#### Tag check fault on Speculative Execution?

CPU
Evaluated Speculated
… ptr &obj
if (cond) {
cond Not ready False True
Wrong Speculation Tag
Tag Check Faultv = Load(ptr);Discard Fault Check
…
Cache
}
obj
Tag check fault does not crash the
program in the speculative execution!

36

## Slide 37

Exploit cache side-channel è Leak whether an address is accessed Exploit speculative execution è Avoid crash on tag check fault

37

## Slide 38

#### Roadmap

###### ARM Memory Tagging Extension

Real-world
MTE Bypass Attack
MTE
JS

Cache  Speculative
Side-Channel Execution
Cache if (cond)
True False
MTE Tag Leakage
Side-Channel
MTE

38

## Slide 39

#### MTE Side-channel attack

###### **Goal: Leak the memory tag given a pointer**

Pointer Memory
check_ptr &check check ?

39

## Slide 40

#### MTE Side-channel attack

**Two test cases:**

Access(check_ptr);

###### **A. Valid tag in check_ptr**

###### **B. Invalid tag in check_ptr**

check_ptr &check check &check check
Tag Check Tag Check
Cache Cache
No Cache Cache
check check
DifDifferenceerence?

40

## Slide 41

#### MTE Side-channel attack

**Two test cases:**

Access(check_ptr); Access(test_ptr);

###### **A. Valid tag in check_ptr**

###### **B. Invalid tag in check_ptr**

check_ptr &check check &check check
test_ptr &test test &test test
Cache
Difference?

41

## Slide 42

A. Valid tag in check_ptr
CPU
Tag Leakage Gadget
Evaluated Speculated
check_ptr &check
if (cond) { test_ptr &test
cond Not ready False True
// Check
Tag
Access(check_ptr);  Tag
Check
Check MatchMatch
…
Cache
// Test
Access(test_ptr); check
Cache contains both
check and test
test
}

42

## Slide 43

B. Invalid tag in check_ptr CPU Tag Leakage Gadget Evaluated Speculated check_ptr &check if (cond) { test_ptr &test cond Not ready **False** True // Check Access(check_ptr); **Tag** Tag Check Fault **Check** … **Mismatch** Cache // Test **No reason to continue speculative execution** Access(test_ptr);Not Accessed check Correct specà (synchronous) tag check fault Wrong spec à Revert execution **Cache only contains** } **check, not test**

43

## Slide 44

#### Leak by Cache Side-Channel

A. Valid tag in check_ptr B. Invalid tag in check_ptr
&check check &check check
Cache Cache
check check
test
Fast Slow
Load(test_ptr); Load(test_ptr);
Leak whether the tag is Valid/Invalid by
test_ptr access latency!

44

## Slide 45

#### Do new MTE chips contain the tag leakage side-channels?

**PACMAN – ISCA 2022, DEF CON 30**

- Discovered a Pointer Authentication Code (PAC) side-channel

- **MTE as Tested – Google Project Zero, POC 2023**

   - **if (cond) { // Check**

- Attempted to find a MTE tag side-channel à **Failed**

**val = *check_ptr; Our work** test_ptr |= val; // val=0 • **Found 2 Tag Leakage Gadgets + Susepected Root Causes** // ???test_ptr |= val; • Gadget poc: **<u>https://github.com/compsec-snu/tiktag</u>** … • Detailed analysis in our paper: **<u>https://arxiv.org/abs/2406.08719 // Test</u>**

**StickyTags – VUSec, IEEE S&P 2024**

- Orthogonally found one of our tag leakage gadets

**Access(test_ptr);**

**}**

45

## Slide 46

#### Gadget 1: Multiple Loads

###### Suspected root cause

if (cond) {

…

// Check: 2+ load

*check_ptr;  Tag Check Fault
*check_ptr; Tag Check Fault
…
// Test: load/store

No Access *test_ptr; }

- On **_multiple faults_ ,** the CPU **_re-speculates that the speculation was wrong_** => **stop/reduce speculations** in branch speculation and memory prefetcher

Gadget Requirements

- Check: 2+ Loads with check_ptr

- Test: Any Load/Store with test_ptr

**_The wrong path event_** _… provides a hint that the processor pipeline may have fetched one or more_ **_instructions that do not require execution_** _. … some examples are_ **_invalid memory accesses_** _, …_

46

## Slide 47

#### Gadget 2: Store-to-Load Forwarding

Suspected root cause

if (cond) {

// Check: store-to-load

*check_ptr = **val** ; Tag Check Fault **val** = *check_ptr; Tag Check Fault // Test: dependent load/store No Access *(test_ptr+ **val** ); }

•
On  tag check fault , the CPU blocks
store-to-load forwarding
Store Buffer
Load Buffer
Address Data Address Data
0x1 …1000 val 0x1 …1000 val
0x1 …1000 val 0x2 …1000 ?
0x2 …1000 val 0x1 …1000 ?
0x2 …1000 val 0x2 …1000 ?
0x1 : correct tag
0x2 : wrong tag

47

## Slide 48

#### Roadmap

###### ARM Memory Tagging Extension

Cache  Speculative
Side-Channel Execution
Cache if (cond)
True False

Real-world
MTE Bypass Attack

MTE
JS

###### MTE Tag Leakage Side-Channel **MTE**

48

## Slide 49

### Real-world MTE-Enabled Software

- MTE became recently available

- • Software systems that provide (optional) MTE support

Google  Linux
Chrome
Kernel

###### **Secure OSes**

GrapheneOS Unikraft

OPTEE

• More software systems are likely to adopt MTE in the near future

49

## Slide 50

Real-world Gadgets & Attacks When MTE is enabled

**1. Google Chrome V8 Engine** Constructed exploitable Gadget 2 from JavaScript →Leak MTE tag of the renderer memory

**2. Linux kernel** Found potential Gadget 1 in snd_timer() → Leak MTE tag of the kernel memory from user space

Refer to our paper for the details: https://arxiv.org/abs/2406.08719

50

## Slide 51

Google Chrome Threat Model
Chrome Renderer process
Potential
Memory
V8 JavaScript  Blink Rendering
Corruption
Engine
Engine
HTML CSS
Attacker-
JavaScript
provided
Protected
V8 Sandbox Third-party libraries

51

## Slide 52

#### Google Chrome Threat Model

Chrome Renderer process
MTE Potential
Memory
V8 JavaScript  Blink Rendering
Corruption
Engine
Engine
HTML CSS
Attacker-
JavaScript
JavaScript
provided
Tag Leakage
MTE
Protected
V8 Sandbox Third-party libraries

52

## Slide 53

#### Gadget 2 from JavaScript

if (cond) {
idx : out-of-bounds index (64-bit)
check[ idx ]  = val;
check[idx]  : check_ptr
val =   check[ idx ]  ;
x =  test[val]  ;
test[val]  : test_ptr
} Speculative Execution

53

## Slide 54

#### Gadget 2 in Google V8 (JavaScript)

TagLeak(target) {
for (let tag=0; tag < 16; ++tag) {  ⃪ Iterate all tag values
check[idx]
idx = AddrToIdx(tag, target);  ⃪ out-of-bounds index
Valid tag Invalid tag
if (cond) {
No fault
Tag Check Fault
check[ idx ]  = val; Tag Leakage
No fault
val =  check[ idx ]; Gadget Tag Check Fault
x =   test[val]  ;
Access No Access
}
Fast Slow
time[tag] = Measure( test[val]  );
}
return time.indexOf(min(time)); Tag Leaked!
}

54

## Slide 55

#### Chrome MTE Bypass Attack

Trigger memory corruption if
tag match is expected
Chrome
vuln_ptr
? &vuln vuln ?
target ?
Leak tag of
memory objects TagLeak(addr)

55

## Slide 56

#### 1. Leak MTE Tag of vulnerable object

vuln.tag =

Chrome
vuln_ptr
? &vuln vuln ?
TagLeak(&vuln)

56

## Slide 57

#### 2. Leak MTE Tag of target object

Chrome
vuln_ptr
vuln.tag =
&vuln vuln
target ?
target.tag =
TagLeak(&target)

57

## Slide 58

#### 3. Reallocate target on tag mismatch

vuln.tag =
target.tag =
vuln.tag != target.tag

Chrome
vuln_ptr
&vuln vuln
target

58

## Slide 59

#### 3. Reallocate target on tag mismatch

vuln.tag =
Free(target);

Chrome
vuln_ptr
&vuln vuln
Freed

59

## Slide 60

#### 3. Reallocate target on tag mismatch

Chrome
vuln_ptr
vuln.tag =
&vuln vuln
Free(target); target ?
Alloc(target);
TagLeak(&target)

60

## Slide 61

#### 4. Trigger vulnerability on tag match

Trigger out-of-bounds access
Chrome
vuln_ptr
vuln.tag =
&target&vuln vuln
target.tag = target
Tag check
vuln.tag == target.tag
Match

61

## Slide 62

##### CVE-2023-5217 Chrome libvpx heap overlfow **Original Memory Corruption** à **Attack Fail**

62

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2023-5217 Chrome libvpx heap overlfow
Original Memory Corruption > Attack Fail
‘— £0 | Elements Console Sources Network >>
DH O\tpry|o@ Default levels ¥ | No Issues git:( ) x ./out/pixel/bin/chrome_public_apk logcat -d 38151FDJHO00VB
@7- 21:45:33.867 26749 26749
@7- 21:45:33.869 1746
>| PI Zygote : Forked child process 26765
07-20 21:45:33.873 26765 26765 fj cessServiced:16: Using CollectorTypeCMC GC
07-20 21:45:33.890 26765 26765 fj CompatibilityChangeReporter: Compat change id reported: 171979766; UID 98024; state: ENABLE
D
07-20 21:45:33.896 26765 26765 O
D
07-20 21:45:33.893 26765 26765 1D} ApplicationLoaders: Returning zygote-cached class loader: /system_ext/framework/androidx.wi
ndow. extensions. jar
67-20 21:45:33.895 26765 26765 o nativeloader: Configuring clns-7 for other apk /data/app/~~Wq5RFIknKZXtEjRSzjS3rg==/org.chr
omium. chrome-URbKRdB7K3uFbj JgnLiqUA==/base.apk. target_sdk_version=34, uses libraries=, library_path=/data/app/~-WqSRFIknKZX
jRS2jS3rg==/org. chromium. chrome-URbKRdB7K3uFbj JgnLiqUA==/1ib/arm64: /data/app/~-Wq5RFIknKZXtEjRSzj$3rg==/org. chromium. chrom
e-URbKRdB7K3uFbj JgnLiqUA==/base.apk!/1ib/arm64-v8a, permitted _path=/data: /mnt/expand: /data/user/@/org. chromium. chrome
67-20 21:45:33.902 26765 26765 i cr_SplitCompatApp: version=125.0.6422.231 (642223104) minSdkVersion=26 isBundle=false proce
ssName=org. chromium. chrome: sandboxed_process@:org. chromium. content .app.SandboxedProcessService:16 isIsolatedProcess=true
CompatibilityChangeReporter: Compat change id reported: 242716250; UID 90024; state: ENABLE
07 45:33.906 26765 26765 fi cr_ChildProcessService: Creating new ChildProcessService pid=26765
all la Ize 07 45:33.915 26765 26781 fi cr_LibraryLoader: Successfully loaded native Library
07 45:33.916 26765 26781 ff cr_CachingUmaRecorder: Flushed 2 samples from 2 histograms, @ samples were dropped
07 45:33.918 26765 26781 f} SystemServiceRegistry: No service published for: uimode
07 45:33.921 26765 26781 fi Libc : SetHeapTaggingLevel: tag level set to 3
67-20 21:45:33.972 14168 14168 ff cr_E2E_ControllerImpl: E2E_Up Tab ‘New tab’
07 245:33.982 3876 tivit : 4 ‘
@7 :45:33.996 26749 26749 fj Zygote =: Process 26544 exited cleanly (0)
2 git: ( ) x node ./server.js
; Listening on 0.6.0.6:8000
&767G 40% 08% §46.0°C 0/0 MB/s 0 47% G © balanced Sat 20Jul21
```

## Slide 63

CVE-2023-5217 Chrome libvpx heap overlfow **With MTE Tag Leakage** à **Attack Success**

63

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
CVE-2023-5217 Chrome libvpx heap overlfow
With MTE Tag Leakage >
x £0 Elements Console Sources Network >> 1 £83 3 Terminal - tmux
GD O|tpry|@ [Filte Default levels ¥ | NolIssues | £3 ) x ./out/pixel/bin/chrome_public_apk logcat -d 38151FDJHOOOVB
@ Not allowed to load local resource: newtab/:1
chrome-native: //newtab/
Navigated to
Initialize
Initialize
» chromium-oob2 git: ( ) x node ./server.js
j Listening on 6.0.0.0:8000
$ Console
ad 8767G 241% 07% 047.0°C #0/0 MB/s 49 47% && \ balanced Sat 20 Jul2
```

## Slide 64

#### Vendor Responses

###### **ARM**

- Acknowledged the MTE tag side-channel in multiple ARM cores

- • MTE Tags are not a secret

- à Tag leakage is not a security vulnerability

- • Expected the cost of the hardware fix to be low and recommended the fix.

ARM MTE Security Updates: <u>https://developer.arm.com/Arm%20Security%20Center/Arm%20Memory%20Tagging%20Extension</u>

64

## Slide 65

#### Vendor Responses

###### **Google Android Security Team**

- MTE tag leakage are **hardware flaw** of Pixel 8 & Pixel 8 pro

- **Still, MTE is a strong mitigation against limited-shot exploits: -** Minimal attack surface (e.g., Messaging app)

   - Physically remote attack (e.g., Bluetooth, NFC, Wi-Fi, …)

   - Process isolation, IPC attack (e.g., Android, Chrome browser)

65

## Slide 66

#### Vendor Responses

###### **Google Chrome V8 Security Team**

• **data confidentiality** (including MTE tag’s confidentiality) is out of scope of the V8 Sandbox

- Currently doesn’t plan to adopt MTE on renderer due to **potential side-channel issues**

66

## Slide 67

#### Takeaway

● **ARM MTE** is a promising security feature to defend against **memory corruption attacks**

● However, current MTE hardware contains **tag leakage side-channel issues**

● MTE-based security can be improved by **software and hardware enhancement** in the future

67

## Slide 68

## Questions?

68
