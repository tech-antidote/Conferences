---
title: "HODOR Reducing Attack Surface on Node.js via System Call Limitation"
speakers: ["Wenya Wang", "Xingwei Lin", "Jingyi Wang", "Wang Gao", "Dawu Gu"]
conference: "Black Hat"
conference_full: "Black Hat Europe 2023"
edition: "Europe"
year: 2023
source_pdf: "Black Hat Europe 2023 slides/Wenya Wang, Xingwei Lin, Jingyi Wang, Wang Gao, Dawu Gu _ HODOR Reducing Attack Surface on Node.js via System Call Limitation.pdf"
pages: 34
sha256: "cffbe905089a0883b85c3268e06f4cf66d560acd53a804650e293c40768ee1ae"
text_chars: 12842
ocr_pages: 3
has_ocr: true
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-11T21:13:13Z"
---
# HODOR Reducing Attack Surface on Node.js via System Call Limitation

**Speakers:** Wenya Wang, Xingwei Lin, Jingyi Wang, Wang Gao, Dawu Gu  
**Conference:** Black Hat Europe 2023  
**Source:** `Black Hat Europe 2023 slides/Wenya Wang, Xingwei Lin, Jingyi Wang, Wang Gao, Dawu Gu _ HODOR Reducing Attack Surface on Node.js via System Call Limitation.pdf` (34 pages)

## Slide 1

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
bidekhat —
DECEMBER 4-7
EXCEL LONDON / UK
#BHEU @BlackHatEvents
```

## Slide 2

HODOR: Reducing Attack Surface on Node.js via System Call Limitation

Speakers: Wenya Wang, Xingwei Lin

**Contributors** : Wenya Wang, Xingwei Lin, Jingyi Wang, Wang Gao, Dawu GuM

#BHEU @BlackHatEvents

## Slide 3

##### Agenda

- **_<u>Introduction</u>_**

- **Previous work & Remaining challenges**

- **HODOR: system call level protection system for Node.js applications**

- • **Evaluation**

- **Conclusion & Takeaways**

#BHEU @BlackHatEvents

3

Information Classification: General

## Slide 4

## Node.js

Node.js is an **open-source, cross-platform JavaScript runtime** environment.

✓ Asynchronous and Event-Driven ✓ Single-Threaded ✓ Cross-Platform ✓ NPM (Node Package Manager) ✓ JavaScript Everywhere

Ebay LinkedIn
Paypal Microsoft
Netflix Uber Walmart Yahoo

#BHEU @BlackHatEvents

4

Information Classification: General

## Slide 5

#### Node.js architecture

- ✓ Node.js Applications (JS)

- ✓ Built-in Module Layer (JS)

- ✓ Binding Module Layer (C++)

- ✓ Dependency Module Layer (C)

#BHEU @BlackHatEvents

5

Information Classification: General

## Slide 6

## Motivation

- ➢ NPM is a package manager with over 1 million packages →The key to the success of Node.js

- ➢ 19.63% of packages in the NPM ecosystem depend on vulnerable packages, such as gadget chain attacks, inject-related attacks, and supply chain attacks. →Most of them may lead to ACE attacks.

- ➢ Arbitrary Command/Code Execution: the attackers can perform arbitrary dangerous critical operations

- mail `cat / etc /passwd`

- • mail `nc −l −e /bin/bash 8001`

###### **Growl Application (v1.8.0)**

- mail `su root`

- …

#BHEU @BlackHatEvents

6

Information Classification: General

## Slide 7

##### Agenda

- **Introduction**

- **_<u>Previous work & Remaining challenges</u>_**

- **HODOR: system call level protection system for Node.js applications**

- • **Evaluation**

- **Conclusion & Takeaways**

#BHEU @BlackHatEvents

7

Information Classification: General

## Slide 8

How to reduce the attack surface of ACE attacks for Node.js applications?

#BHEU @BlackHatEvents

8

Information Classification: General

## Slide 9

How to reduce the attack surface of ACE attacks for Node.js applications?

###### **_<u>Threat Model</u>_**

- ✓ Consider an attacker with _<u>ACE ability</u>_

- ✓ Not considered: preventing ACE, code vulnerabilities in binding layer/dependency layer, race condition, DOS attack, etc

#BHEU @BlackHatEvents

9

Information Classification: General

## Slide 10

### Existing Works: Software Debloating

- Use program analysis to cut the **_<u>useless code</u>_**

   - ✓ (USENIX Sec’19) RAZOR: A Framework for Post-deployment Software Debloating

   - ✓ (USENIX Sec’19) Less is More: Quantifying the Security Benefits of Debloating Web Applications ✓ (Usenix Sec’20) Slimium: Debloating the Chromium Browser with Feature Subsetting

✓ (RAID’20) Mininode: Reducing the Attack Surface of Node.js Application

<u>What is software debloating? (educative.io)</u>

#BHEU @BlackHatEvents

10

Information Classification: General

## Slide 11

### Existing Works: System Call Limitation

- Restrict the system calls that can be used by the application

   - ✓ (USENIX Sec’20) Temporal System Call Specialization for Attack Surface Reduction

   - ✓ (RAID’20) Confine: Automated System Call Policy Generation for Container Attack Surface Reduction ✓ (RAID’20) sysfilter: Automated System Call Filtering for Commodity Software

   - ✓ (PLDI’20) BlankIt Library Debloating Getting What You Want Instead of Cutting What You Don’t ✓ (USENIX Sec’21) Saphire: Sandboxing PHP Applications with Tailored System Call Allowlists

#BHEU @BlackHatEvents

11

Information Classification: General

## Slide 12

Remaining Challenges **1. Cross-language mapping requirement** ✓ JS code layer & C/C++ code layer

**2. Integration with Node.js framework**

✓ Node.js runs in a single process that creates two kinds of threads.

https://medium.com/preezma/node-js-event-loop-architecture-godeeper-node-core-c96b4cec7aa4

#BHEU @BlackHatEvents

12

Information Classification: General

## Slide 13

## Problem Formulation

- The number of all system calls provided by the system:

- The number of system calls in the whitelist:

- The degree of attack surface reduction in the system call level:

**_Goal_** _: minimize the attack surface in the system call level to prevent malicious critical operations, while not affecting the application’s normal execution_

#BHEU @BlackHatEvents

13

Information Classification: General

## Slide 14

##### Agenda

- **Introduction**

- **Previous work & Remaining challenges**

- • **_<u>HODOR: system call level protection system for Node.js applications</u>_**

- **Evaluation**

- **Conclusion & Takeaways**

#BHEU @BlackHatEvents

14

Information Classification: General

## Slide 15

##### Our approach: Hodor

A lightweight runtime protection system.

#BHEU @BlackHatEvents

15

Information Classification: General

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
plaekhat
Our approach: Hodor
A lightweight runtime protection system.
as Node.js D
Application 5
5 SO Native | aoe
Modules Source Code
Modules SZ Call Graph Mappings
— Constructor Builder
(Ss) |
Node.js
Code
Bo! Dependencies bite
Itcode
® @
15
Information Classification: General
Ee,
System Call
Recorder
@
&
Main- Thread-
Thread- _Pool-
Excuted Excuted
Whitelist Whitelist
>
Kernel
Restriction Profile Installation
®
```

## Slide 16

##### Step 1: Call Graph Construction

- ➢ **JS > complement missing nodes/edges/syscall** ✓ **Code features of built-in methods**

- [1,2,3].map( **x => x * 2** );

   - fs.readFile(filename, **CallbackFunc** );

- ✓ **Dynamic Analysis Refiner**

   - let sum = new Function(’a’,’b’,’return a+b’);

   - eval(“sum()”);

- ✓ **Dynamic Command Execution**

   - child_process.exec(“touch new file”);

#BHEU @BlackHatEvents

16

Information Classification: General

## Slide 17

##### Step 1: Call Graph Construction

- ➢ **JS > complement missing nodes/edges/syscall** ✓ **Code features of built-in methods**

      - [1,2,3].map(x => x * 2);

      - fs.readFile(filename, CallbackFunc);

   - ✓ **Dynamic Analysis Refiner**

      - let sum = new Function(’a’,’b’,’return a+b’);

      - eval(“ **sum()** ”);

   - ✓ **Dynamic Command Execution**

      - child_process.exec(“touch new file”);

#BHEU @BlackHatEvents

17

Information Classification: General

## Slide 18

##### Step 1: Call Graph Construction

- ➢ **JS > complement missing nodes/edges/syscall**

   - ✓ **Code features of built-in methods**

      - [1,2,3].map(x => x * 2);

      - fs.readFile(filename, callbackFunc);

   - ✓ **Dynamic Analysis Refiner**

      - let sum = new Function(’a’,’b’,’return a+b’);

      - eval(“sum()”);

   - ✓ **Dynamic Command Execution**

      - child_process.exec(“ **touch new file** ”);

#BHEU @BlackHatEvents

18

Information Classification: General

## Slide 19

##### Step 1: Call Graph Construction

- ➢ **JS > complement missing nodes/edges/syscall**

   - ✓ **Code features of built-in methods**

      - [1,2,3].map(x => x * 2);

      - fs.readFile(filename, callbackFunc);

   - ✓ **Dynamic Analysis Refiner**

      - let sum = new Function(’a’,’b’,’return a+b’);

      - eval(“sum()”);

   - ✓ **Dynamic Command Execution**

      - child_process.exec(“touch new file”);

- ➢ **Implementation**

   - ✓ Reimplement **JAM** and add in proposed optimizations

      - ISSTA’21 Modular call graph construction for security scanning of node.js applications

   - ✓ Combine dynamic call graph tool **Nodeprof** and Linux **strace** utility

#BHEU @BlackHatEvents

19

Information Classification: General

## Slide 20

##### Step 1: Call Graph Construction

- ➢ **C/C++ call graph > eliminate non-existing nodes/edges**

   - ✓ Partial context-aware analysis for **<u>switch-case statement</u>** & function pointer parameter

#BHEU @BlackHatEvents

20

Information Classification: General

## Slide 21

##### Step 1: Call Graph Construction

- ➢ **C/C++ call graph > eliminate non-existing nodes/edges**

   - ✓ Partial context-aware analysis for switch-case statement & **<u>function pointer parameter</u>**

#BHEU @BlackHatEvents

21

Information Classification: General

## Slide 22

##### Step 1: Call Graph Construction

- ➢ **C/C++ call graph > eliminate non-existing nodes/edges**

   - ✓ Partial context-aware analysis for switch-case statement & function pointer parameter

- ➢ **Implementation**

   - ✓ clang with wllvm > llvm link > **SVF ++**

#BHEU @BlackHatEvents

22

Information Classification: General

## Slide 23

##### Step 2: Mapping Builder

- ➢ We build **<u>call graph traversal</u>** for call graphs of the Node.js application layer, Binding Module layer, and Dependency layer.

- ➢ We build **<u>LLVM Pass</u>** for the Built-in Module layer.

- ➢ We get mappings of different layers.

#BHEU @BlackHatEvents

23

Information Classification: General

## Slide 24

##### Step 3: System Call Recorder

- ➢ Based on mappings, we calculate the **<u>system call whitelists</u>** for the Node.js application.

- ➢ We **<u>divide</u>** the system call list into the system call list of **main thread** and the system call list of **the thread pool** .

#BHEU @BlackHatEvents

24

Information Classification: General

## Slide 25

##### Step 4: Hodor Installation

- ➢ **Seccomp Implementation**

   - ✓ For **<u>thread pool required applications</u>** , we **<u>first</u>** install the filter for the thread pool thread and **<u>then</u>** install the filter for the main thread to prevent the thread pool thread from inheriting the main thread filter.

   - ✓ For thread pool dis-required applications, we **<u>only</u>** load the main thread filter.

- ➢ **Read/write Permission Restrictions.**

   - ✓ **<u>Read</u>** and **<u>write system calls</u>** are widely used by Node.js engine.

   - ✓ **<u>Chroot</u>** mechanism and Switch the ownership.

#BHEU @BlackHatEvents

25

Information Classification: General

## Slide 26

##### Agenda

- **Introduction**

- **Previous work & Remaining challenges**

- **HODOR: system call level protection system for Node.js applications**

- • **_<u>Evaluation</u>_**

- **Conclusion & Takeaways**

#BHEU @BlackHatEvents

26

Information Classification: General

## Slide 27

##### Evaluation

- ➢ **Dataset**

   - ✓ 169 packages suffered from ACE attacks

   - ✓ Three large-scale real-world applications (koa, express and json-server).

   - ✓ Node.js core tests and 4 well-known web frameworks (koa, fastify, express, and connect).

- ➢ **Total Result**

   - .

   - ✓ HODOR can **reduce the attack surface** of Node.js applications to <u>19.42%</u>

#BHEU @BlackHatEvents

27

Information Classification: General

## Slide 28

###### Evaluation - Call Graph Construction and Resulting Protection

- ✓ The **optimization of JS call graph** construction helps identify hidden required system calls for **23.21%** packages.

- ✓ The **optimization of C/C++ call graph** construction further reduces the system call permissions by **71.02%** .

- ✓ HODOR **reduces the attack surface** for the **main thread** to **19.20%** , for the **thread pool thread** to **7.73%** , while **_not affecting_** the application’s normal operation.

#BHEU @BlackHatEvents

28

Information Classification: General

## Slide 29

###### Evaluation - Exploit Mitigation

✓ We construct **different advanced attack payloads** to simulate various dangerous behaviors of attackers, where a variety of critical system calls can be invoked.

- ✓ HODOR could effectively mitigate the execution of **73.59%** exploits.

#BHEU @BlackHatEvents

29

Information Classification: General

## Slide 30

###### Evaluation - Comparison with Other Techniques

###### ✓ HODOR can defend against **a wider spectrum of attacks** (additionally covering arbitrary command execution) **with less runtime overhead** .

#BHEU @BlackHatEvents

30

Information Classification: General

## Slide 31

###### Evaluation - Runtime Overhead

- ✓ The runtime overhead of HODOR is **0.61%** for **Node.js core tests** , **2.80%** for the **web framework** , and **0.39%** for all **168 packages** .

#BHEU @BlackHatEvents

31

Information Classification: General

## Slide 32

##### Agenda

- **Introduction**

- **Previous work & Remaining challenges**

- **HODOR: system call level protection system for Node.js applications**

- • **Evaluation**

- **_<u>Conclusion & Takeaways</u>_**

#BHEU @BlackHatEvents

32

Information Classification: General

## Slide 33

- Conclusion & Takeaways 1. Attendees will learn a new call graph building methods for JavaScript code and C/C++ code.

2. Attendees will gain knowledge of a novel protection mechanism for Node.js applications, focusing on thread-level and system call-level security.

3. Attendees will develop an understanding of the hazards associated with vulnerabilities in the Node.js application ecosystem, with a particular emphasis on system call-level vulnerabilities.

#BHEU @BlackHatEvents

33

Information Classification: General

## Slide 34

# Thanks & Questions?

Wenya Wang,  Xingwei Lin      @xwlin_roy

#BHEU @BlackHatEvents

> Text below was recovered by OCR from an image-only slide; treat wording as approximate.

```text
blackhat
Thanks & Questions?
Wenya Wang, Xingwei Lin ¥ @xwlin_roy
#BHEU @BlackHatEvents
```
