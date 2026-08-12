---
title: "Alice In Kernel Land"
speakers: ["Palmiotti"]
conference: "Black Hat"
conference_full: "Black Hat ASIA 2023"
edition: "ASIA"
year: 2023
source_pdf: "Black Hat Asia 2023 slides/AS-23-Palmiotti-Alice-In-Kernel-Land.pdf"
pages: 47
sha256: "257c643a0711768abf71bfb4b112f7d1d2bce2d2c35068c3d891fe884ebc6e7b"
text_chars: 17359
ocr_pages: 6
has_ocr: true
redacted_secrets: 0
ocr_confidence: 87.2
companion_files: []
extractor: "pymupdf4llm 1.28.2 + tesseract"
converted_at: "2026-08-12T01:51:21Z"
---
# Alice In Kernel Land

**Speakers:** Palmiotti  
**Conference:** Black Hat ASIA 2023  
**Source:** `Black Hat Asia 2023 slides/AS-23-Palmiotti-Alice-In-Kernel-Land.pdf` (47 pages)


## Slide 1

Alice in Kernel Land: Lessons Learned from the eBPF Rabbit Hole

Simon Scannell, Valentina Palmiotti, Juan José López Jaimez

## Slide 2

# About Us, Intro to the Speakers

#### Simon

- Cloud Vulnerability Researcher at Google

- Loves to travel

- Worked on a first version of an eBPF fuzzer in 2020 and found a privilege escalation in the latest Ubuntu version at the time

#### Valentina

- Vulnerability and Exploit Researcher at IBM X-Force Red

- Focused on low-level vulnerabilities, exploit development, and post-exploitation offensive security

- Wored on eBPF exploitation and vuln discovery concurrently to Simon, met and decided to work together in collaboration with new colleague JJ.

#### JJ

- Cloud Vulnerability researcher and Software Developer at Google

- Loves to bake and learn languages

- By pure coincidence: found Simon’s article about the fuzzer and decided to create his own version of it… only to find out Simon was joining his team a few weeks later

## Slide 3

# eBPF - what is it?

Initially created to filter packets (classic Berkley Packet Filtering) eBPF is a technology that allows a user mode application to run code in the kernel without needing to load a kernel module. eBPF programs are used to do all types of things: tracing, instrumentation, hooking system calls, debugging, packet capturing/filtering, and even rootkits ;)

## Slide 4

# eBPF - why?

Developers don’t need to know how to develop kernel code It’s easier than compiling and maintaining a custom modified kernel It’s easy to write eBPF programs

Performance advantages to run directly in the kernel Allows for asynchronous programming style, less context switches from user to kernel, advantageous for modern hardware.

## Slide 5

## eBPF Programs

eBPF programs are written in a high level language (C/Python) Program is compiled into eBPF bytecode using a toolchain.

## Slide 6

## eBPF: How Does it Work?

Usermode application loads byte code into kernel (via eBPF syscall) eBPF verifier performs checks on the bytecode If verifier checks are passed, bytecode is JIT compiled into native instruction set (or instructions are executed by interpreter while running) Application attaches to hook point, event-based execution Application gives input/output with eBPF maps and helper functions

## Slide 7

> Text below was recovered by OCR (confidence 80/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
KERNEL SPACE USER SPACE
BPF_PROG_LOAD i toolchain
—— : iles eBPF
eBPF verifier | € - process | €——— “ort Nes eB
eBPF JIT
compiler
BPF hook
point
eBPF maps
Interpreter
: KEY
led native i
decodes & executes :
eBPF bytecode
```

## Slide 8

## eBPF Privileges

Whether unprivileged can run eBPF programs depends on sysctl knob unprivileged_bpf_disabled

Unprivileged users are limited to where programs can hook (can attach to socket the user owns)

CONFIG_BPF_UNPRIV_DEFAULT_OFF sets the sysctl knob by default. Now set by default in popular distro’s kernels like Ubuntu, beginning in 2022.

CAP_BPF Linux capability can be granted to users or containers to run eBPF programs Fewer restrictions for programs when CAP_BPF is granted

## Slide 9

## eBPF - Applications

eBPF vulnerabilities pose a risk for applications given CAP_BPF capabilities, or running in containers with the the capability, even if unprivileged eBPF is not allowed

May see this in actual environments for:

Untrusted applications that process heavy I/O or networking activity

- Services

- Firewalls

- Security/Telemetry Applications

- Applications that run in containers, ex: Cilium

## Slide 10

# Vulnerabilities

There are 3 main places eBPF vulnerabilities can reside:

- Verifier

- JIT Compiler

- eBPF Kernel Runtime (helper functions)

When building a fuzzer, it’s important to survey the types of vulnerabilities that can occur, where and how they occur, and how to detect them in order to automate corpus generation in a way that makes sense and gain good coverage in relevant parts of the target.

## Slide 11

# Verifier Vulnerabilities - Range Calculation

Verifier keeps track of the **expected range of scalar value registers** used in an eBPF program.

Only scalars can be added to pointers to access the memory of shared maps. Verifier has to ensure these scalar registers stay within the expected range and do not lead to out of bound access of maps.

Errors in how these ranges are calculated result in the ability to manipulate the verifier’s checks allow kernel memory corruption.

## Slide 12

# Verifier Checks Map Access

The verifier must ensure that operations like the one above, don’t result in operating on out of bounds memory

## Slide 13

Range Calculation: CVE-2020-27194

Discovered by the first iteration of the fuzzer we’re presenting today. Caused by miscalculations of 32 bit ranges that are derived from the 64 bit registers. The patch introduced the individual tracking of 32 bit ranges for each register.

## Slide 14

## Verifier Vulnerabilities - Branching Prediction

Verifier must analyze all potential code paths of the program being loaded in order to ensure safe behavior at runtime.

Patches out instructions it believes to be in a branch that will never be reached or does not analyze branches it believes to be in the same state as already visited code paths.

Bugs in the verifier’s branching prediction mechanisms can lead to the ability to manipulate the program state to one unexpected by the verifier

## Slide 15

Branching Prediction - CVE-2023-2163

Discovered by the second iteration of the fuzzer we’re presenting today

## Slide 16

Verifier Vulnerabilities - General Logic Bugs

General logic bugs can occur when traversing and verifying the program. Not directly related to range/bound calculation or branching, but ultimately lead to the verifier generating an incorrect state for the program **CVE-2021-3490 -**

Lead to the failure to update the bounds of a scalar registers after 32 bit AND, OR, and XOR operations. Was not an error in calculating the bounds themselves, though.

## Slide 17

JIT Compiler Vulnerabilities - Code Generation Bugs

The eBPF JIT compiler compiles the eBPF bytecode to assembly of the native architecture of the system

## Slide 18

JIT Compiler Vulnerabilities - Code Generation Bugs Optimization->Branch Miscalculations

**CVE-2021-29154** - Issue with how branch displacements were calculated for some architectures, could lead to arbitrary shellcode execution

Highlights how architectural differences can manifest in this eBPF component

## Slide 19

JIT Compiler Vulnerabilities - Code Generation Bugs

**CVE-2021-38300** - Bug in the way classic eBPF programs were translated and compiled in the JIT compiler Highlights that legacy cBPF program support can create issues once JIT compiled

## Slide 20

# eBPF Runtime Vulnerabilities

eBPF has “helper functions” that can interact with the eBPF program during runtime. The code for these functions reside in the “unsandboxed” area of the kernel, meaning they are just in the normal part of the kernel code base. Vulnerabilities in the eBPF runtime can be triggered by a malicious eBPF program and be used to escalate privileges

## Slide 21

## eBPF Runtime Vulnerabilities

**CVE-2021-38166 -** Integer overflow and out of bounds write in hashmap lookup function

This vulnerability can be triggered if a shared eBPF map is of type hashmap and a helper function is called to retrieve a value stored in the map.

A big portion of the eBPF Runtime code attack surface is related to operating on shared maps (retrieving/storing their values, etc)

## Slide 22

What now? Automated Vulnerability Discovery

With proper context of the target, we began our automated vulnerability discovery process by targeting the eBPF verifier via fuzzing

## Slide 23

## Automating vulnerability discovery - Why?

Verifier code is very complex ( <u>kernel/bpf/verifer.c</u> i has > 17k LoC)

Lots of changes to the source code. **CVE-2020-27194** was introduced as part of a patch for another security issue

eBPF is a standard. If we can automate vulnerability discovery, we can likely do it for more than one implementation

## Slide 24

## Automating vulnerability discovery - Fuzzing?

**Pros** :

- Doesn’t require a very deep technical understanding of the verifier code

- ● The eBPF instruction set is not very large. We can generate all opcodes

- ● The eBPF interface (syscalls etc.) doesn’t change much, meaning a fuzzer can be adapted relatively easy to various versions and implementations

## Slide 25

Fuzzing: Existing solutions considered

At the time, an <u>eBPF fuzzer</u> for the Linux implementation existed. However, it aimed at finding memory corruption in the verifier itself

Syzkaller is a coverage-guided and sophisticated Kernel fuzzer. However:

- Built to trigger and detect memory corruption bugs. We are interested in hard-to-detect logic bugs

- Changing Syzkaller to generate, load, execute and detect errors in eBPF programs requires as much work as writing an eBPF optimized fuzzer from scratch

## Slide 26

## Fuzzing: Tailored strategy

Writing an eBPF optimized fuzzer from scratch allows us to:

- Optimize the fuzzing-input generator and tweak it for experiments

- ● Choose an appropriate architecture for the fuzzer

- ● Implement a strategy for detecting bugs

## Slide 27

## Fuzzing: Input generation

On a very high level a fuzzer just throws random stuff at a program until it crashes The issue with this approach is that in order for our program to crash it has to pass the verifier first

That means a naive bitflipping approach likely won’t generate a long list of opcodes that are:

- Correctly encoded

- Specify a valid operation

- Specify valid registers

- Specify immediates

## Slide 28

## Fuzzing: Input generation

In the first version of the fuzzer, we generated programs by:

- Prepending a static program header that performed all necessary initialization

- Generating a variable length array of opcodes

- ● Each opcode is a correctly encoded ALU operation taking in either a register or an immediate as an operand

- Appending a static program footer that exited the program cleanly

## Slide 29

Fuzzing: Input generation

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
unsigned operation = 0;
// chose a random ALU operation
// for now only support operations which can leave a register in a known state
switch(rg->rand_int_range(@, 7)) {
case 0:
operation = BPF_ADD;
break;
case 1:
operation = BPF_SUB;
break;
operation = BPF_OR;
break;
```

## Slide 30

Fuzzing: Input generation

> Text below was recovered by OCR (confidence 92/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
// now, generate all the instructions
size_t index = this->header_size;
for (size_t i = 0; i < this->num_instr; i++) {
// in most cases do an ALU operation, make sure we don't have a
if (rg->n_out_of(8, 10) || i == this->num_instr - 1) {
alu_instr a;
```

## Slide 31

## Fuzzing: Error detection

We can now generate eBPF programs! Now what?

If a program contains pointer arithmetic and accesses **and** the verifier deems it to be valid then the verifier is confident the memory access is guaranteed to be in bounds

We can test this assumption at runtime by writing a magic value to an eBPF map during eBPF program execution

If the magic value is not in the expected position within the map, the verifier was wrong and we have a security issue!

## Slide 32

Fuzzing: Performance and Scaling

The eBPF verifier runs with a global lock, meaning that the fuzzer won’t scale well

This is bad news because we expect most of our time to be spent within the verifier. Although we have an optimized input generator, most programs will still be invalid

## Slide 33

## Fuzzing: Architecture

At the time, decided to extract the verifier code and compile it in user-space This had several benefits for scalability:

- No context switches

- ● No verifier lock

- Easier to debug where things might go wrong

The downside: Very time consuming and difficult to port to new versions

## Slide 34

Fuzzing: Architecture

> Text below was recovered by OCR (confidence 88/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Fuzzing: Architecture
Userspace (runs fuzzer)
eBPF in userspace triager
Generator creates e Emulates kernel verifier Gets JIT of program
valid eBPF program e Checks program safety —: Tests for bugs
e Resets emulation Catches OOB bugs
Reports bugs
If unsafe If no bug detected
Calls bpi() syscall
to get JIT
```

## Slide 35

## Fuzzing: Performance and Scaling

Pros:

Cons:

- Very scalable and fast due to userspace fuzzing

- ● Optimized eBPF input generation

- ● Easy to debug issues

- Error detection is very naive

- ● eBPF inputs are correctly encoded when generated but still an extremely low rate for valid programs (< 1%)

- ● Hard to adapt to new versions

## Slide 36

# Fuzzing - A New approach

● In our previous strategy the biggest issue was that only a fraction of the generated programs were considered valid. What if we create a new fuzzer that generates a lot of **syntactically** valid programs

- We look for Programs that are **semantically** wrong but the verifier gives them an O.K

## Slide 37

High Level Architecture - Not A fuzzer, a Fuzzing framework

> Text below was recovered by OCR (confidence 93/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
High Level Architecture - Not A fuzzer, a Fuzzing
framework
Control unit
FuzzingStrategy
<Interface>
eBPFGenerationLibrary ExecutionUnit
PointerArithmetic VerifierLogParser Playground
```

## Slide 38

# Fuzzing Strategies - What and Why?

- How do we detect when an error occurs?

- How do we decide how to generate a program?

Answer: Fuzing Strategies - Allow the user of the fuzzer to code their own way to generate eBPF Programs and detect when errors occur

E.G: Verifier Log Parser strategy

## Slide 39

### Verifier Log Parser strategy

- Generation of programs:

   - Random ALU operations

- How does it detect bugs?

   - At verify time: it ingests the verifier log and parses the assumptions the verifier has made about the registers.

   - At run time: The actual values of the registers are stored in a map, then compared with the verifier assumptions

## Slide 40

### Pointer Arithmetic strategy

- Generation of programs:

- Random ALU operations + Random JMP operations (branching)

- ● How does it detect bugs?

   - At the end of the program it generates a _footer_ that:

      - 1) Chooses a random register that received ALU operations

      - 2) Adds the value of that register to a map pointer

      - 3) Attempts to write to the map

   - Then read the value from user-space, if the value is not there: OOB write happened.

This is the strategy that found CVE-2023-2163

## Slide 41

# Program Generation in a nutshell

- Programs get generated in a tree-like structure

- Once the tree generation is complete, each instruction generates its corresponding bpf bytecode (via DFS)

## Slide 42

## Other features - coverage information and statistics

> Text below was recovered by OCR (confidence 76/100) from an image-only slide. Wording is approximate; verify exact values against the source PDF.

```text
Other features - coverage information and
statistics
52711 have been verified, 0 were valid (0.000000 percent were valid) mane os
= vscnprintf(log->kbut, OPF_VERIFIER TMP LOG SIZE, fmt, args):
verifier.c \WAB_ONCE(n >= GPF VERIFIER THP.LOG SIZE - 1,
© full path: /usr/local/google/home/jjlopezjaimez/repos/linux-git/kernel/bpf/verifier.c erifier lop Line truncated - local buffer too short\n"):
© covered lines: 828
© full path: /usr/local/google/home/;jlopezjaimez/repos/linux-git/mm/vmalloc.c
© covered lines: 220 prerr(*BPF: Asks", log->kbuf, newline 2"* : *\n");
© covered lines: 169 1n = min{log->ten total - log->len_used - 1,
© covered lines: 91 nue
syscall.c Log-ubuf = MULL:
© full path: /usr/local/google/home/ijlopezjaimez/repos/linux-git/kernel/bpf/syscall.c >
cone lines: 54 static void bpf_vlog reset(struct bpf_verifier log *log, u32 new pos)
© full path: /usr/local/google/home/jjlopezjaimez/repos/linux-git/kernel/bpf/core.c char zero = 0;
© covered lines: 39
thum.c
© full path: /usr/local/google/homeljjlopezjaimez/repos/linux-git/kernel/bpf/tnum.c
© covered lines: 28 Log->Len_used = new pos;
if (log->Level == BPF_LOG KERNEL) {
return;
/* Yog_level controls verbosity Level of eBPF verifier
+ bpf_verifier log write() is used to dunp the verification trace to the log,
* so the user can figure out what's wrong with the program
”
print#(2, 3) void bpf verifier log write(struct bpf_verifier env *env
const char *fat,
va_list args:
return;
```

## Slide 43

# Some statistics

It can:

- Generate ~35k eBPF Programs per minute

- ● Depending on the strategy, a lot of those programs might be rejected by the verifier, but <u>that’s ok.</u> We are looking for **syntactically valid** programs  that are **semantically wrong** but the verifier thinks are O.K

## Slide 44

# 24 hours after we set it to run for real…

- First Strike! (CVE-2023-2163)

- It was found using the pointer arithmetic strategy

   - We added generation of random JMP operations + random ALU operations and that did the trick…

- TL;DR we discovered that the control flow analysis of the verifier is kinda broken

   - Verifier tries to simulate all possible states of branching to determine if all paths are safe

   - ○ But the verifier is lazy… and if **some** conditions are met… then it prunes the search

   - ○ Welp turns out that the pruning algorithm is broken, it might decide to not traverse certain paths that lead to unsafe conditions

## Slide 45

We turned this into an LPE + Container escape

## Slide 46

# So What now?

- Code of the fuzzing framework (a.k.a _Buzzer_ ) has been made open source at <u>https://github.com/google/buzzer</u>

- There will still be some features to implement

   - Execute bpf programs across multiple vms with different OS versions

      - Better metrics collection

   - Etc.

- We just scratched the surface on how to fuzz ebpf in depth, we can find more complex vulns with more complex fuzzing strategies.

## Slide 47

# Black Hat Sound Bytes

- Granting CAP_BPF should be carefully considered as eBPF remains a complex attack surface

- When building a fuzzer, it’s important to survey the types of vulnerabilities that can occur, where and how they occur and how to detect them in order to automate corpus generation to cover relevant parts of the target

- ● There is a lot of value in contribution between security researchers: the lessons learned in Simon’s original fuzzer paved the way for our new Fuzzer
